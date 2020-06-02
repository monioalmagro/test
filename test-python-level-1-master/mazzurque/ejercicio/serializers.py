from rest_framework import serializers
from .models import Fisica , Juridica 


class FisicaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Fisica
        fields = "__all__"
       

class JuridicaSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Juridica
        fields = "__all__"


