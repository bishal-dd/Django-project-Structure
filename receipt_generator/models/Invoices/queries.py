import graphene
from .type import ServiceType
from .models import Service


class ServiceQuery(graphene.ObjectType):
    all_services = graphene.List(ServiceType)

    def resolve_all_services(root, info):
        return Service.objects.all()