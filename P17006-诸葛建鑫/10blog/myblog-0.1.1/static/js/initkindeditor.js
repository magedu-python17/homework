function initKindEditor() {
    // KindEditor.create第一个参数时如果找到该标签， 第二个是KindEditor的初始化参数。
    let fm = $('form').serialize();
    let regex = /^.*csrfmiddlewaretoken=([^&]*).*$/;
    let token = regex.exec(fm)[1];
    KindEditor.create(
        '.kind-editor',
        {
            width: '100%',
            resizeType: 2,
            allowPreviewEmoticons: true,
            allowImageUpload: true,
            items:
                [
                    'source', '|', 'undo', 'redo', '|', 'preview', 'print', 'template', 'code', 'cut', 'copy', 'paste',
                    'plainpaste', 'wordpaste', '|', 'justifyleft', 'justifycenter', 'justifyright',
                    'justifyfull', 'insertorderedlist', 'insertunorderedlist', 'indent', 'outdent', 'subscript',
                    'superscript', 'clearhtml', 'quickformat', 'selectall', '|', 'fullscreen', '/',
                    'formatblock', 'fontname', 'fontsize', '|', 'forecolor', 'hilitecolor', 'bold',
                    'italic', 'underline', 'strikethrough', 'lineheight', 'removeformat', '|', 'image', 'multiimage',
                    'flash', 'media', 'insertfile', 'table', 'hr', 'emoticons', 'baidumap', 'pagebreak',
                    'anchor', 'link', 'unlink', '|', 'about'
                ],
            uploadJson: '/backend/article-pic',
            extraFileUploadParams: {'csrfmiddlewaretoken': token},
            afterBlur: function(){
                KindEditor.sync('.kind-editor');
            },
        }
        );
}
function ajaxSubmitBind(){
    $('.jsSubmit').on('click', function($e){
        let $fm = $('form');
        let data = $fm.serialize();
        let url = $fm.prop('action');
        console.log(1, url);
        $.ajax({
            url: url,
            type: 'post',
            data: data,
            success: function (args) {
                console.log(args, args.status, args.msg);
                if (args.status === 399){
                    window.location.href = args.msg;}
                else if (args.status === 499){
                    $('form>li>label+span').remove();
                    let $e = $('form>li>label');
                    let len = $e.length;
                    args.msg.forEach(function(val, ind){
                        if (ind<len){
                            let $ele = $("<span>");
                            $ele.text(val);
                            $e.eq(ind).after($ele);
                        }
                    });
                }
            }
        });
    });
}
$(function() {
    initKindEditor();
    ajaxSubmitBind();
});