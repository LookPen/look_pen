from django.shortcuts import render
from django.views import generic
import blog.control as c_blog


class HomeView(generic.DetailView):
    def get(self, request, *args, **kwargs):
        """
        获取导航、标签
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        mains = c_blog.get_main_category()
        tags = c_blog.get_tags()

        return render(request, 'index.html', context={'mains': mains, 'tags': tags})


class ArticleView(generic.ListView):
    def get(self, request, *args, **kwargs):
        """
        文章列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        sub_id = request.GET.get('sid', None)

        if sub_id:
            articles = c_blog.get_articles_by_category(sub_id)
        else:
            articles = []

        return render(request, 'sub/article_list.html', context={'articles': articles})


class SubCategoryView(generic.ListView):
    def get(self, request, *args, **kwargs):
        """
        获取子分类
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pid = request.GET.get('pid', 1)
        subs = c_blog.get_sub_category(pid)

        return render(request, 'sub/sub_category.html', context={'subs': subs})
