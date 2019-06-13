function ajaxLogoutBind(){
    let $logout = $(".account-logout");
    $logout.on('click', function($e){
        let url = $logout.attr('url');
        $.ajax({
            url: url,
            type: 'get',
            success: function(args){
                let {status} = args;
                if (status === 699){            // 对当前页面的账户区域进行替换
                    let {msg:{replace, delCookies}} = args;
                    if (replace){
                        let {old, rep, ap} = replace;
                        $(old).remove();
                        $(ap).append($(rep));
                    }
                    if (delCookies){
                        delCookies.forEach(function(val, ind){
                            $.cookie(val, '', {expires: -1});
                        });
                    }
                }
                if (status === 399) {           // 重定向到新的网页
                    let {msg:{delCookies, dst}} = args;
                    if (delCookies){
                        delCookies.forEach(function(val, ind){
                            $.cookie(val, '', {expires: -1});
                        });
                    }
                    if (dst){
                        window.location.href = dst;
                    }
                }
            }
        });
    });
}
$(function(){
    ajaxLogoutBind();
});