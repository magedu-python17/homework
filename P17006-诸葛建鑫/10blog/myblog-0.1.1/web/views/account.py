from django.shortcuts import render, reverse, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseRedirect
from django.db.models import Q
from web.customForm.accountForm import RegisterForm, LoginForm
from util.check_code import gen_check_code
from util.token import gen_token, logged_redirect_to_index, no_logged_redirect_to_login
from .. import models as web_models
from io import BytesIO
import bcrypt
import json
import datetime


@logged_redirect_to_index
def ajax_reg(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'reg.html')
    else:
        return JsonResponse({
            'status': 399,
            'msg': {"dst": "/"}
        })


# @logged_redirect_to_index
# def ajax_reg(request: HttpRequest):
#     if request.method == 'GET':
#         return render(request, 'reg.html')
#     elif request.method == 'POST':
#         rfm = RegisterForm(request, request.POST)
#         if rfm.is_valid():   # 验证通过，写入注册信息，写cookie，并跳转
#             try:
#                 data = rfm.cleaned_data
#                 name, email, pwd = data["user"], data["email"], data["pwd"]
#                 # 注意： 已经在accountForm中验证用户，邮箱不存在
#                 pwd = bcrypt.hashpw(pwd.encode(encoding='utf-8'), bcrypt.gensalt()).decode(encoding='utf-8')
#                 u = web_models.User.objects.create(name=name, email=email, pwd=pwd)
#                 user_id = u.nid
#                 web_models.Blog.objects.create(user_id=user_id, site=name)
#                 jwt_token = gen_token(user_id, int(datetime.datetime.now().timestamp()+3600*24*30))
#                 return JsonResponse({
#                     "status": 399,
#                     'msg': {
#                         "setCookies": [["jwt_token", jwt_token, {"expires": 30}]],
#                         "dst": "/"}
#                 })
#             except Exception as e:
#                 return JsonResponse({"status": 599, "msg": str(e)})
#         else:
#             err = json.loads(rfm.errors.as_json())
#             keys = ["user", "email", "pwd", "confirm_pwd", "check_code"]
#             err_v = [err.get(key, [{}])[0].get("message", "") for key in keys]
#             if err.get('__all__'):
#                 err_v[3] = err['__all__'][0].get("message", "")
#             return JsonResponse({"status": 499, "msg": err_v})


def check_code(request):
    if request.method == 'GET':
        stream = BytesIO()
        img, c = gen_check_code()
        img.save(stream, 'png')
        request.session["check_code"] = c.upper()
        return HttpResponse(stream.getvalue())
    return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")


@logged_redirect_to_index
def ajax_login(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == "POST":
        lfm = LoginForm(request, request.POST)
        if lfm.is_valid():
            try:
                data = lfm.cleaned_data
                name = data.get("user")
                u = web_models.User.objects.filter(name=name).first()
                user_id = u.nid
                jwt_token = gen_token(user_id, int(datetime.datetime.now().timestamp()+3600*24*30))
                return JsonResponse({
                    "status": 399,
                    "msg": {
                        "setCookies": [["jwt_token", jwt_token, {"expires": 30}]],
                        "dst": "/"}
                })
            except Exception as e:
                return JsonResponse({"status": 599, "msg": str(e)})
        else:
            err = json.loads(lfm.errors.as_json())
            ec = err.get("check_code", [{}])[0].get("message", "")
            ea = err.get("__all__", [{}])[0].get("message", "")
            err_v = ["", "", ec, ea]
            return JsonResponse({"status": 499, "msg": err_v})
    return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")


@no_logged_redirect_to_login
def ajax_logout(request):
    if request.method == 'GET':
        request.session.clear()
        ele_str = """<div class="nav-item"><a href="{}">登录</a></div><div class="nav-item"><a href="{}">注册</a></div>"""\
            .format(reverse("user-web:login"), reverse('user-web:reg'))
        return JsonResponse({'status': 699, "msg": {
            "replace": {"old": ".logged-account", "rep": ele_str, "ap": ".nav-right"},
            "delCookies": ["jwt_token"]
        }})
    return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")
