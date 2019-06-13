function ajaxDeleteEvent(ele) {
    $(ele).each(function(ind, val){
        let attr1 = $(this).prop('href');
        $(this).attr('url', attr1).prop('href', 'javascript: void(0)');
    });
    $(ele).on('click', function($e){
        let that=this;
        let attr1 = $(this).attr('url');
        $.ajax({
            url: attr1,
            type: 'GET',
            success: function(args){
                let {status, msg} = args;
                if (status === 299){
                    $(that).parent().parent().html(msg)
                }
            }
        });
    });
}
function ajaxModalEditEvent(ele, ele_modal, err_modal){
    $(ele).each(function(ind, val){
        let attr1 = $(this).prop('href');
        $(this).attr('url', attr1).prop('href', 'javascript: void(0)');
    });
    $(ele).on('click', function($e){
        let v = $(this).parent().siblings(".option-title").text().trim();
        let $tr = $(this).parent().parent();
        let nid = $tr.attr("nid");
        let ind = $tr.index();
        $(ele_modal).find(".modal-option-title").val(v).attr('old', v).attr('ind', ind);
        $(ele_modal).find(".modal-option-nid").val(nid);
        $(ele_modal).modal("show");
    });
    $(ele_modal).find(".modal-option-title").on('focus', function($e){
        $(err_modal).empty();
    });
    $(ele_modal).find(".ajaxModalSubmit").on("click", function($e){
        let $err = $(err_modal);
        $err.empty();
        let $fm = $(ele_modal).find("form");
        let $title = $(ele_modal).find(".modal-option-title");
        let v = $title.attr('old');
        let new_v = $title.val();
        let ind = $title.attr('ind');
        if (new_v === v){
            $err.text("检测到类名未修改")
        }else{
            $.ajax({
                url: $fm.prop('action'),
                type: "POST",
                data: $fm.serialize(),
                success: function(args){
                    let {status, msg} = args;
                    if (status === 299){
                        $(ele).eq(ind).parent().siblings(".option-title").children("a").text(new_v);
                        $(ele_modal).modal("hide");
                    }else if (status === 499) {
                        $err.text(msg);
                    }
                }
            });
        }
    });
}
function ajaxFormSubmitEvent(fm, btn){
    let $fm = $(fm);
    let url = $fm.prop("action");
    $fm.find(btn).on('click', function($e){
        $.ajax({
            url: url,
            type: "POST",
            data: $fm.serialize(),
            success: function(args){
                console.log(args);
                let {status, msg} = args;
                if (status === 399){
                    let {redirect} = msg;
                    if (redirect){
                        window.location.href = redirect;
                    }
                }
                if (status === 499){
                    let {tip} = msg;
                    if (tip){
                        let {remove, after, content} = tip;    // after选中多个label元素，依次将错误信息添加到label元素后。
                        $(remove).remove();
                        $(after).each(function(ind, val){
                            $(this).after(content[ind]);
                        });
                    }
                }
            }
        });
    })
}
