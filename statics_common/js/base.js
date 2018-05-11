$(function () {
    // 是否隐藏返回到顶部
    $(window).scroll(function () {
        if ($(this).scrollTop() != 0) {
            $('#to-top').fadeIn();
        } else {
            $('#to-top').fadeOut();
        }
    });

    //返回到顶部
    $('#to-top').click(function () {
        $('body,html').animate({scrollTop: 0}, 500);
    });

});