function InputCheck() {
    this.map = {
        "user": {
            "tip": ".jsTipUser",
            "regex": /[a-zA-Z0-9]{6,18}/,
            "empty": "用户名不能为空",
            "err": "用户名6~18个字符"
        },
        "email": {
            "tip": ".jsTipEmail",
            "regex": /^[_a-z0-9-]+(\.[_a-z0-9-]+)*@([a-z0-9-]+\.)+(com|net|cn|org|me|cc|biz)$/,
            "empty": "邮箱不能为空",
            "err": "邮箱格式不正确"
        },
        "pwd": {
            "tip": ".jsTipPwd",
            "regex": /^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[~!@#$%^&*?+\-\/=_])[0-9a-zA-Z~!@#$%^&*?+\-\/=_]{8,32}$/,
            "empty": "密码不能为空",
            "err": "8~32个字符，须含数字，字母，特殊字符"
        },
        "confirm_pwd": {
            "tip": ".jsTipConfirm",
        },
        "check_code": {
            "tip": ".jsTipCode",
        },
    };
    this.validated = {};

    this.inputFocusClear = function (that) {
        function fn($e) {
            let obj = that.map[$(this).prop("name")];
            $(obj.tip).text("");
        }
        return fn
    }(this);

    this.regexpBlurCheck = function (that) {
        function fn($e) {
            let $ele = $(this);
            let name = $ele.prop('name');
            let val = $ele.val();
            let obj = that.map[name];
            if (!val.trim()) {
                $(obj.tip).text(obj.empty);
                that.validated[name] = 0;
            } else if (obj.regex.test(val)) {
                that.validated[name] = 1;
            } else {
                $(obj.tip).text(obj.err);
                that.validated[name] = 0;
            }
        }
        return fn
    }(this);

    this.confirmBlurCheck = function (that) {
        function fn($e) {
            let $ele = $(this);
            let $pwds = $(":password");
            let name = $ele.prop("name");
            let obj = that.map[name];
            if (!$ele.val().trim()) {
                $(obj.tip).text("确认密码不能为空");
                that.validated[name] = 0;
            } else if ($pwds.eq(0).val() === $pwds.eq(1).val()) {
                that.validated[name] = 1;
            } else {
                $(obj.tip).text("两次输入密码不一致");
                that.validated[name] = 0;
            }
        }
        return fn
    }(this);

    this.codeBlurCheck = function (that) {
        function fn($e) {
            let $ele = $(this);
            let name = $ele.prop("name");
            let obj = that.map[name];
            if ($ele.val().trim().length !== 4) {
                $(obj.tip).text("验证码应为4位");
                that.validated[name] = 0;
            } else {
                that.validated[name] = 1;
            }
        }
        return fn
    }(this);
}

function AccountValidate(lst){
    this.lst = lst;
    this.ic = new InputCheck();
    this.EventBind = function(){
        let that=this;
        this.lst.forEach(function (val, ind){
            $(val).on("focus", that.ic.inputFocusClear);
            if (val === ".regValidate"){
                $(val).on("blur", that.ic.regexpBlurCheck);
            }else if (val === ".confirm_pwd"){
                $(val).on("blur", that.ic.confirmBlurCheck);
            }else if (val === ".check_code"){
                $(val).on("blur", that.ic.codeBlurCheck);
                $(".jsCodeImg").on("click", function($e){          // 验证码
                    this.src = this.src+"?";
                });
            }
        });

    };
    this.submitEvent = function(){
        let that=this;
        $(".jsSubmit").on("click", function () {
            let flag = true;
            $(".account-fm input").blur();
            for (let k of Object.keys(that.ic.validated)){
                if (that.ic.validated[k] === 0){flag=false; break;}
            }
            if (flag){
                let $fm = $(".account-fm");
                $.ajax({
                    url: $fm.prop('action'),
                    type: 'POST',
                    data: $fm.serialize(),
                    success: function(arg) {
                        console.log(arg);       // TODO
                        if (arg.status === 399){
                            let {setCookies, dst} = arg.msg;
                            if (setCookies) {
                                for (let info of setCookies) {
                                    $.cookie(...info);
                                }
                            }
                            if (dst){
                                window.location.href = dst;
                            }
                        }else {
                            if (that.lst.indexOf(".check_code") !== -1){
                                $(".jsCodeImg").click();           // 每次数据检测通过后提交，都需更新验证码，即触发图片的点击事件
                            }
                            let len = $(".fm-item").length;
                            arg.msg.forEach(function(val, ind){
                                if (val && ind < len){
                                    $(".fm-item").eq(ind).find("span").text(val);
                                }else if (ind === len) {
                                    $(".account-err-tip span").text(val);
                                }
                            });
                        }
                    }
                });
            }
        });
    };
}
