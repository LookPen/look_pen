from django.conf.urls import url
import blog.views as blog

urlpatterns = [
    url(r'^$', blog.HomeView.as_view(), name='home'),
    url(r'^sub$', blog.SubCategoryView.as_view(), name='sub')
]
