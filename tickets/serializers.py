from rest_framework import fields, serializers
from .models import *


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'

class ReversationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reversation
        fields='__all__'

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Guest
        fields=['pk','reversation','name','mobile']



