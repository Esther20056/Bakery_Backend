from rest_framework import serializers 
from .models import  Newbakes

class ItemsSerializer(serializers.ModelSerializer):
   class Meta:
      model = Newbakes
      fields = '__all__' 

# class PopularSerializer(serializers.ModelSerializer):
#    class Meta:
#       model = Popular
#       fields = '__all__' 

# class sortSerializer(serializers.ModelSerializer):
#    class Meta:
#       model =ItemSort 
#       fields = '__all__'

# class RecieverSerializer(serializers.ModelSerializer):
#    class Meta:
#       model =Reciever
#       fields ='__all__'

