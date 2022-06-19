from django.views.generic import TemplateView, ListView, DetailView, CreateView
from apps.blog.models import Article
from .form import ArticleForm


class IndexView(ListView):
    template_name = 'blog/index.html'
    # model = Article
    queryset = Article.objects.filter(published=True)
    context_object_name = 'articles'


class ArticleView(DetailView):
    template_name = 'blog/article.html'
    model = Article
    context_object_name = 'article'


class ArticleCreateView(CreateView):
    template_name = 'blog/create_edit.html'
    form_class = ArticleForm



