from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'blog_posts'

urlpatterns = [
    path('', views.PostList.as_view()),
    path('post/<int:pk>/', views.PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
