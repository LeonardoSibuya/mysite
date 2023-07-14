from django.db import models
from django.contrib.auth.models import User

#aqui seria o status dos posts do blog, onde podemos criar um rascunho e podemos postar o post
STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

#Aqui criamos uma função que será a estrutura da tabela de post, utilizamos o models.model sendo um pacote do django que já facilita esta criação dos campos.
class Post(models.Model):

    # Isso define um campo de caractere para o título do post, com no máximo 200 caracteres e garantindo que seja único.
    title = models.CharField(max_length=200, unique=True)

    # Isso define um campo de caractere para o slug do post, que é uma versão amigável para URL do título. Também tem um limite de 200 caracteres e deve ser único.
    slug = models.SlugField(max_length=200, unique=True)

    # campo do autor do post, e utilizamos o USER pacote que pegamos do django, onde facilita a criação de usuários, para que não precisemos criar tabelas para a criação dos usuarios do blog. Cada post terá um autor associado.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    # Isso define um campo de data e hora para registrar a última atualização do post. Ele é atualizado automaticamente sempre que o post é modificado.
    update_on = models.DateTimeField(auto_now=True)

    # campo de conteudo do post
    content = models.TextField()

    # Isso define um campo de data e hora para registrar a data e hora de criação do post. Ele é definido automaticamente com a data e hora atuais no momento da criação do post.
    created_on = models.DateTimeField(auto_now_add=True)

    #  Isso define um campo inteiro para representar o status do post. Ele usa as opções definidas em STATUS para permitir que o post seja marcado como rascunho ou publicado. O valor padrão é 0, indicando um rascunho.
    status = models.IntegerField(choices=STATUS, default=0)

    # Aqui, estamos definindo uma classe interna chamada Meta, que contém metadados da classe Post.
    class Meta:
        # Isso especifica que os posts devem ser ordenados pela data de criação em ordem decrescente, ou seja, do mais recente para o mais antigo.
        ordering = ['-created_on']

        # Aqui, estamos definindo o método especial __str__() para a classe Post. Esse método é chamado quando precisamos representar um objeto Post como uma string. Nesse caso, estamos retornando o título do post como a representação em string do objeto Post
        def __str__(self):
            return self.title