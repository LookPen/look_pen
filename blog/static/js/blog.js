// 渲染子菜单
function get_sub_category(pid) {
    $('.navbar .active').each(function (k, v) {
        $(v).removeClass('active')
    })
    $('#' + pid).addClass('active')

    $('#sub_category').empty()
    $('#sub_category').append('<div class="loading"></div>')

    $('#dropdown-toggle').te


    $.ajax({
        url: '/sub?pid=' + pid,
        type: 'GET',
        success: function (data) {
            $('.loading').hide()

            $('#sub_category').append(data)
        }
    })

}

// 渲染文章列表
function get_article_list(sid) {
    $("#sub_category .menu-item").each(function (k, v) {
        $(v).removeClass('active')
    })
    $('#' + sid).addClass('active')

    $('#article_list').empty()
    $('#article_list').append('<div class="loading"></div>')

    $.ajax({
        url: '/article?sid=' + sid,
        type: 'GET',
        success: function (data) {
            $('.loading').hide()

            $('#article_list').append(data)
        }
    })
}