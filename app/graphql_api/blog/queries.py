import graphene
from graphene import relay
from django.contrib.auth.models import User
import graphql_jwt
from graphql_jwt.decorators import login_required
from graphene_django.filter import DjangoFilterConnectionField

from .base import PostType, PostNode


class Query(graphene.ObjectType):

    # all_movies = graphene.List(MovieType)
    # movie = graphene.Field(MovieType, id=graphene.Int(), title=graphene.String())
    all_post = DjangoFilterConnectionField(PostNode)
    post = relay.Node.Field(PostNode)
    # all_directors = graphene.List(PostType)

    # @login_required
    # def resolve_all_movies(self, info, **kwargs):
    #     # user = info.context.user
    #     # if not user.is_authenticated:
    #     #     raise Exception("Auth credentials were not provided")
    #     return Movie.objects.all()

    # def resolve_all_user(self, info, **kwargs):
    #     return User.objects.all()