from django.urls import path, re_path
from . import views
# from .views import MainPageView, NewsView, NewsArticleView
from news.views import news_list_view, news_detail_view, create_news_view


app_name = 'news'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', news_list_view, name="news_list"),
    # path('news/', NewsView.as_view()),
    path('<int:link>/', news_detail_view, name="news_list_view"),
    path('create/', create_news_view, name="create"),
    #re_path('/(?P<link>[^/]*)/?', NewsView.as_view()),

]

# urlpatterns = [
#     # path('', views.index, name='index'),
#     path('', views.index, name='index'),
#     path('news/', MainPageView.as_view()),
#     # path('news/', NewsView.as_view()),
#     path('<int:link>/', NewsArticleView.as_view()),
#     #re_path('/(?P<link>[^/]*)/?', NewsView.as_view()),
#
# ]