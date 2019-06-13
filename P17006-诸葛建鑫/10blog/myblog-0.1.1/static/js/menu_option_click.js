$(function(){
   menuTitleClickBind();
});

function menuTitleClickBind(){
    $('.menu-item-title').on('click', function($e){
        let $this = $(this);
        let $i = $this.children('i');
        if ($this.hasClass('active')){
            $this.removeClass('active');
            $i.removeClass("fa-caret-down").addClass("fa-caret-right");
        }else{
            let $sib = $(this).parent().siblings().children('.menu-item-title');
            $this.addClass('active');
            $i.removeClass("fa-caret-right").addClass("fa-caret-down");
            // $sib.removeClass('active');
            // $sib.children('i').removeClass("fa-caret-down").addClass("fa-caret-right");
        }
    })
}