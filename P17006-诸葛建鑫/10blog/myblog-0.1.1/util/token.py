# ------------------ pip install pyjwt ------------------ #
import jwt
from myBlog.settings import SECRET_KEY      # 使用时，注意django提供的key的位置
from functools import wraps
from web import models as web_models
from django.shortcuts import redirect, reverse
# from django.http import HttpRequest
# import datetime
# import base64
# import time
#
#
# def fix(src):
#     rem = len(src) % 4
#     return src+b'='*rem


def gen_token(nid: int, expire: int):
    payload = {
        "nid": nid,
        "exp": expire
    }
    ret = jwt.encode(payload, SECRET_KEY, "HS256")
    # hd, pld, sig = ret.split(b".")
    # print(base64.urlsafe_b64decode(fix(hd)))
    # print(base64.urlsafe_b64decode(fix(pld)))
    # print(base64.urlsafe_b64decode(fix(sig)))
    return ret.decode(encoding="utf-8")     # ret是一个bytes序列，需要装换为字符串，作为set-cookie: token='......'


def validate_token(token: str):
    """
    验证token:
        如果token有效，返回payload
        如果token过期，会抛出jwt.exceptions.ExpiredSignatureError
        如果token无效，会抛出jwt.exceptions.InvalidSignatureError
        如果token有效，返回payload
    """
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])


# ---------------- 测试代码 ------------------ #
# a = gen_token(1, int(datetime.datetime.now().timestamp()+6))
# print(validate_token(a))
# time.sleep(7)
# print(datetime.datetime.now().timestamp())
# print(validate_token(a))        # token超时


def logged_add_payload(fn):
    @wraps(fn)
    def _wrap(request, *args, **kwargs):
        token = request.COOKIES.get("jwt_token", None)
        payload = {}
        if token is not None:
            try:
                payload = validate_token(token)
            except:
                payload = {}
        request.payload = payload
        return fn(request, *args, **kwargs)
    return _wrap


def logged_add_blog(fn):
    @wraps(fn)
    def _wrap(request, *args, **kwargs):
        token = request.COOKIES.get("jwt_token", None)
        payload = {}
        if token is not None:                           # 如果cookie中没有token键值对，说明没有登录
            try:
                pld = validate_token(token)             # 验证cookie中的token是否有效，无效或过期都会抛出异常
                logged_in_blog = web_models.Blog.objects.filter(user_id=pld['nid']).select_related('user').first()
                payload["logged_in_blog"] = logged_in_blog
            except:
                payload = {}
        request.payload = payload
        return fn(request, *args, **kwargs)
    return _wrap


def logged_redirect_to_index(fn):
    @wraps(fn)
    def _wrap(request, *args, **kwargs):
        token = request.COOKIES.get("jwt_token", None)
        if token is None:
            return fn(request, *args, **kwargs)
        try:
            payload = validate_token(token)
            logged_in_blog = web_models.Blog.objects.filter(user_id=payload['nid']).first()
            return redirect(reverse("user-web:home_article_list", args=(logged_in_blog.site,)))
        except:
            return fn(request, *args, **kwargs)
    return _wrap


def no_logged_redirect_to_login(fn):
    @wraps(fn)
    def _wrap(request, *args, **kwargs):
        token = request.COOKIES.get("jwt_token", None)
        if token is None:
            return redirect('user-web:login')
        else:
            try:
                payload = validate_token(token)
                request.payload = payload
                return fn(request, *args, **kwargs)
            except:
                return redirect('user-web:login')
    return _wrap

