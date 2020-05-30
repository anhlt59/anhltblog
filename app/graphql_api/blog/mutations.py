import graphene
from graphene import relay
import graphql_jwt
from graphql_relay import from_global_id

from blog.models import Post
from .base import PostType, PostNode


class PostCreateMutation(graphene.Mutation):

    class Arguments:
        author = graphene.String(required=True)
        title = graphene.String(required=True)
        body = graphene.String(required=True)
        status = graphene.String(required=True)

    post = graphene.Field(PostType)

    def mutate(self, info, **kwargs):
        """two way to pass arguments
        1. title, year,...
        2. **kwargs
        """
        if (author := kwargs.get("author", None)) \
                and (title := kwargs.get("title", None))\
                and (body := kwargs.get("body", None)) \
                and (status := kwargs.get("status", None)):
            post = Post.objects.create(
                author=author,
                title=title,
                body=body,
                status=status
            )
            mutation = PostCreateMutation(post=post)
        else:
            mutation = None

        return mutation


# class MovieUpdateMutation(graphene.Mutation):
#     class Arguments:
#         title = graphene.String()
#         year = graphene.Int()
#         id = graphene.ID(required=True)
#
#     movie = graphene.Field(MovieType)
#
#     def mutate(self, info, **kwargs):
#         if id := kwargs.get('id', None):
#             movie = Movie.objects.get(pk=id)
#
#             if title := kwargs.get('title', None):
#                 movie.title = title
#             if year := kwargs.get('year', None):
#                 movie.year = year
#             if director := kwargs.get('director', None):
#                 movie.director = director
#             movie.save()
#         else:
#             movie = None
#
#         return MovieUpdateMutation(movie=movie)
#
#
# class MovieUpdateMutationRelay(relay.ClientIDMutation):
#     class Input:
#         title = graphene.String()
#         id = graphene.ID(required=True)
#
#     movie = graphene.Field(MovieType)
#
#     @classmethod
#     def mutate_and_get_payload(cls, root, info, **kwargs):
#         if id := kwargs.get('id', None):
#             data = {}
#             if title := kwargs.get('title', None):
#                 data['title'] = title
#             if year := kwargs.get('year', None):
#                 data['year'] = year
#             if director := kwargs.get('director', None):
#                 data['director'] = director
#             Movie.objects.get(pk=from_global_id(id)[1]).update(**data)
#             status = True
#         else:
#             status = False
#
#         return MovieUpdateMutationRelay(status=status)

class Mutation:
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    # revoke_token = graphql_jwt.Revoke.Field()

    create_post = PostCreateMutation.Field()
    # update_movie = MovieUpdateMutation.Field()
    # update_movie_relay = MovieUpdateMutationRelay.Field()
    # delete_movie = MovieDeleteMutation.Field()