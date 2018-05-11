from django.shortcuts import render
from django.views import generic
import blog.control as c_blog


class HomeView(generic.DetailView):
    def get(self, request, *args, **kwargs):
        """
        导航信息
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pid = request.GET.get('pid', 1)

        # 获取导航、标签
        mains = c_blog.get_main_category()
        subs = c_blog.get_sub_category(pid)
        tags = c_blog.get_tags()

        return render(request, 'index.html', context={'mains': mains, 'subs': subs, 'tags': tags})


class ArticleView(generic.ListView):
    def get(self, request, *args, **kwargs):
        """
        文章列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        sub_id = request.GET.get('sub_id', None)

        if sub_id:
            articles = c_blog.get_articles_by_category(sub_id)
        else:
            articles = []

        return render(request, 'sub/article_list.html', context={'articles': articles})
