function radioClickCancelEvent(ele){
    $(ele).on('click', function($e){
        if ($(this).prop('checked')){
            $(this).prop('checked', false)
        }
    });
}
$(function(){
    radioClickCancelEvent('#id_category_id input:radio')
});