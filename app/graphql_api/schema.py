import graphene
from .blog import queries, mutations
# from api.schema import (
#     query as api_query,
#     mutation as api_mutation
# )


class Query(queries.Query, graphene.ObjectType):#api_query.Query
    pass


class Mutation(mutations.Mutation, graphene.ObjectType):#api_mutation.Mutation,
    pass


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)