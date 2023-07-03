import pytest

from blog.factories import PostFactory

# fixture tem diversos objetivos, e neste caso é podermos reutilizarmos o teste 
@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')

@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'