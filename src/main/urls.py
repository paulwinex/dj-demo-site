from django.contrib import admin
from django.urls import path
from apps.blog.views import IndexView, ArticleView, ArticleCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('article/<int:pk>', ArticleView.as_view(), name='details'),
    path('add/', ArticleCreateView.as_view(), name='add'),
    path('admin/', admin.site.urls),
]
