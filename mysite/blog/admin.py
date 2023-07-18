from django.contrib import admin

# Register your models here.
# Assim importamos o Post.py que criamos no models
from .models import Post

# Serve para mudarmos as estruturas do django admin, acrescentando novos filtros e preenchimentos.
class PostAdmin(admin.ModelAdmin):
    # o list_display irá exibir uma lista com todos os posts que foram criados.
    list_display = ("title", "slug", "status", "created_on")
    # list_filter é usado para filtrar, neste caso filtrar os posts pelo status.
    list_filter = ("status",)
    # search_fields usado para definir os campos que podemos realizar buscas
    search_fields = ("title", "content")
    # é usado para definir campos que serão preenchidos automaticamente com base em outros campos. quando preencher o campo "title" ao criar uma nova postagem no painel de administração, o campo "slug" será preenchido automaticamente com uma versão amigável do título, com espaços substituídos por hífens e caracteres especiais removidos.
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)