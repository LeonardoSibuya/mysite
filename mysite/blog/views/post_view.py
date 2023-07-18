from django.views import generic

from blog.models import Post

# Aqui estamos renderizando o index.html e usando o listview para listar e filtrar os posts com status 1, dentro do index.html
class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"

# Aqui estamos renderizando o post_detail.html
class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"