from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class InicioView(ListView):
    template_name = 'blog/inicio.html'
    queryset = Post.objects.all()
    paginate_by = 2
    
class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    
def about(request):
    
    return render(request, "blog/about.html")
