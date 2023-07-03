from django.db import models
from django.contrib.auth.models import User

#aqui seria o status dos posts do blog, onde podemos criar um rascunho e podemos postar o post
STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

#Aqui criamos uma função que será a estrutura da tabela de post, utilizamos o models.model sendo um pacote do django que já facilita esta criação dos campos.
class Post(models.Model):

    # campo de titulo do post
    title = models.CharField(max_length=200, unique=True)

    # campo de identificação do post
    slug = models.SlugField(max_length=200, unique=True)

    # campo do autor do post, e utilizamos o USER pacote que pegamos do django, onde facilita a criação de usuários, para que não precisemos criar tabelas para a criação dos usuarios do blog
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    # campo de quando foi atualizado o post
    update_on = models.DateTimeField(auto_now=True)

    # campo de conteudo do post
    content = models.TextField()

    # campo de quando foi criado o post
    created_on = models.DateTimeField(auto_now_add=True)

    # campo de status dos posts do blog, onde podemos criar um rascunho e podemos postar o post
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        # aqui é onde ordenamos os posts, pela data de criação
        ordering = ['-created_on']

        #aqui estamos sobreescrevendo o __str__(self) para ele retornar o titulo do post
        def __str__(self):
            return self.title