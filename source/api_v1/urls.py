from django.urls import path

from api_v1.views import get_token_view, ArticleListView, ArticleCreateView, DetailView, \
    UpdateView, DeleteView

app_name = 'api_v1'

urlpatterns = [
    path('get_token/', get_token_view, name='get_token'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('article/create/', ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/', DetailView.as_view(), name='article_view'),
    path('article/<int:pk>/update/', UpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', DeleteView.as_view(), name='article_delete')
]
