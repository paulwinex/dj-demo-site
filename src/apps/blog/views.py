from django.views.generic import TemplateView, ListView, DetailView
from apps.blog.models import Article


class IndexView(ListView):
    template_name = 'blog/index.html'
    # model = Article
    queryset = Article.objects.filter(published=True)
    context_object_name = 'articles'


class ArticleView(DetailView):
    template_name = 'blog/article.html'
    model = Article
    context_object_name = 'article'
