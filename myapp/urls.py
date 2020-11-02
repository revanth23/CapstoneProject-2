from django.urls import path
from articles.views import ArticleListView
from myapp.views import ArticleDayArchiveView


urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    # Example: /2012/nov/10/
    path('<int:year>/<str:month>/<int:day>/',ArticleDayArchiveView.as_view(),name="archive_day"),
]
