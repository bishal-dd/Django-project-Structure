import graphene
from .models.receipts.queries import ProfileQuery
from .models.Invoices.queries import ServiceQuery


class RootQuery(ProfileQuery, ServiceQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=RootQuery)
