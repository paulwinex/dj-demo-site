from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.blog.models import Article
from .form import ArticleForm, ArticleEditForm


class IndexView(ListView):
    template_name = 'blog/index.html'
    queryset = Article.objects.filter(published=True)
    context_object_name = 'articles'


class ArticleView(DetailView):
    template_name = 'blog/article.html'
    model = Article
    context_object_name = 'article'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'blog/create_edit.html'
    form_class = ArticleForm


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'blog/create_edit.html'
    model = Article
    form_class = ArticleEditForm
