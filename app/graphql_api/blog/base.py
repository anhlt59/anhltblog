import graphene
from django.contrib.auth.models import User
from graphene import relay
from graphene_django.types import DjangoObjectType
from blog.models import Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post

class UserType(DjangoObjectType):
    class Meta:
        model = User


# just for relay implementation
class PostNode(DjangoObjectType):
    class Meta:
        model = Post
        filter_fields = {
            'author': ['exact',],
            'title': ['exact', 'icontains', 'istartswith',],
            'status': ['exact',]
        }
        interfaces = (relay.Node,)


# class MovieType(DjangoObjectType):
#     class Meta:
#         model = Movie
#     movie_age = graphene.String()
#     def resolve_movie_age(self, info):
#         return "Old movie" if self.year < 2000 else "New movie"