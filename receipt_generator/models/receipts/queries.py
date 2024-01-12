import graphene
from .type import ProfileType
from .models import Profile


class ProfileQuery(graphene.ObjectType):
    all_profiles = graphene.List(ProfileType)

    def resolve_all_profiles(root, info):
        return Profile.objects.all()