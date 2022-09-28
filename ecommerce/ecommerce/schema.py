
import graphene
import store.schema

class Query(store.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)