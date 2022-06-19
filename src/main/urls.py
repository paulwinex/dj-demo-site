from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from apps.blog.views import IndexView, ArticleView, ArticleCreateView, ArticleUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('article/<int:pk>/', ArticleView.as_view(), name='details'),
    path('add/', ArticleCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='edit'),
    path('admin/', admin.site.urls),
]
