from rest_framework import serializers
from .models import Dj_Product

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dj_Product
        fields = '__all__' # 모델안의 모든 field를 가져옴