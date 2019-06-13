from django.forms import Form, fields
from django.core.exceptions import ValidationError
from django.http import HttpRequest
from ..models import User
import bcrypt


class BaseForm(object):
    def __init__(self, request: HttpRequest, *args, **kwargs):
        self.request = request
        super(BaseForm, self).__init__(*args, **kwargs)


class RegisterForm(BaseForm, Form):
    USER_REG = r'[a-zA-Z0-9]{6,18}'
    EMAIL_REG = r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@([a-z0-9-]+\.)+(com|net|cn|org|me|cc|biz)$"
    PWD_REG = r'^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[~!@#$%^&*?+\-\/=_])[0-9a-zA-Z~!@#$%^&*?+\-\/=_]{8,32}$'

    user = fields.RegexField(USER_REG, error_messages={'invalid': '用户名6~18个字符'})
    email = fields.RegexField(EMAIL_REG, error_messages={'invalid': '邮箱格式不正确'})
    pwd = fields.RegexField(PWD_REG, error_messages={'invalid': '8~32个字符，须含数字，字母，特殊字符'})
    confirm_pwd = fields.CharField(required=True, error_messages={'required': '确认密码不能为空'})
    check_code = fields.CharField(required=True, error_messages={'required': '验证码不能为空'})

    def clean_user(self):
        data = self.cleaned_data.get("user")
        if User.objects.filter(name=data).count():
            raise ValidationError("该用户名已被注册")
        else:
            return data

    def clean_email(self):
        data = self.cleaned_data.get("email")
        if User.objects.filter(email=data).count():
            raise ValidationError("该邮箱已被注册")
        else:
            return data

    def clean_check_code(self):
        data = self.cleaned_data.get("check_code", '').upper()
        code = self.request.session.get("check_code", '')       # session本来就保存的是upper数据
        if code != data:
            raise ValidationError("验证码错误")
        else:
            return data

    def clean(self):
        data = self.cleaned_data
        pwd = data.get('pwd', False)    # 如果前面密码都没有验证通过，那么clean_data中就没有pwd键值对,此时也不要要验证密码是否一致
        if (not pwd) or pwd == data.get('confirm_pwd'):
            return data
        else:
            raise ValidationError('两次输入密码不一致')


class LoginForm(BaseForm, Form):
    USER_REG = r'[a-zA-Z0-9]{6,18}'
    PWD_REG = r'^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[~!@#$%^&*?+\-\/=_])[0-9a-zA-Z~!@#$%^&*?+\-\/=_]{8,32}$'
    user = fields.RegexField(USER_REG, error_messages={'invalid': '用户名6~18个字符'})
    pwd = fields.RegexField(PWD_REG, error_messages={'invalid': '8~32个字符，须含数字，字母，特殊字符'})
    check_code = fields.CharField(required=True, error_messages={'required': '验证码不能为空'})

    def clean_check_code(self):
        data = self.cleaned_data.get("check_code", '').upper()
        code = self.request.session.get("check_code", '')       # session本来就保存的是upper数据
        if code != data:
            raise ValidationError("验证码错误")
        else:
            return data

    def clean(self):
        data = self.cleaned_data
        name = data.get("user")
        pwd = data.get("pwd")
        u = User.objects.filter(name=name).first()
        if u and bcrypt.checkpw(pwd.encode(encoding='utf-8'), u.pwd.encode(encoding='utf-8')):   # 用户存在且密码 验证通过
            return data
        else:
            raise ValidationError("用户名或密码错误")










