from django.shortcuts import render
from django.views import generic
import blog.control as c_blog


class HomeView(generic.ListView):
    def get(self, request, *args, **kwargs):
        """
        导航信息
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pid = request.GET.get('pid', 1)
        sub_id = request.GET.get('sub_id', None)

        # 1、获取导航、标签
        mains = c_blog.get_main_category()
        subs = c_blog.get_sub_category(pid)
        tags = c_blog.get_tags()

        # 如果传了sub_id 则以请求为准
        sub_id = sub_id if sub_id else subs[0].id

        # 2、获取内容列表
        articles = c_blog.get_articles_by_category(sub_id)

        return render(request, 'index.html', context={'mains': mains, 'subs': subs, 'tags': tags, 'articles': articles})
