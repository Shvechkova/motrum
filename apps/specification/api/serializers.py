from rest_framework import serializers

from apps.product.api.serializers import ProductSerializer, ProductSpesifSerializer, StockSerializer
from apps.product.models import Stock
from apps.specification.models import ProductSpecification, Specification

        
class SpecificationSerializer(serializers.ModelSerializer):
    # date = serializers.DateField(format="%Y-%m-%d")
    # date_update = serializers.DateField(format="%Y-%m-%d")
    # date_stop = serializers.DateField(format="%Y-%m-%d")
    class Meta:
        model = Specification
        fields = "__all__"
        
class ProductSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecification
        fields = "__all__"  
        
class ListProductSpecificationSerializer(serializers.ModelSerializer):
    
  
    product_name = serializers.CharField(source='product.name')
    product_id = serializers.CharField(source='product.id')
    lot = serializers.SerializerMethodField()
    class Meta:
        model = ProductSpecification
        fields = (
            "id",
            "product_name",
            "product_id",
            "quantity",
            "lot",
          
            
            
        )  
    def get_lot(self, obj):
            stock_item = Stock.objects.get(
                prod_id=obj.product_id)
            print(stock_item)
            serializer = StockSerializer(stock_item, many=False)

            return serializer.data            

class ListsProductSpecificationSerializer(serializers.ModelSerializer):
    productspecification_set = ListProductSpecificationSerializer(read_only=False, many=True)
    class Meta:
        model = Specification
        fields = (
            "id",
            "file",
            "date",
            "date_stop",
            "total_amount",
            "productspecification_set",
            
        )
    def to_representation(self, instance):
        representation = super(ListsProductSpecificationSerializer, self).to_representation(instance)
        representation['date'] = instance.date.strftime('%d.%m.%Y')
        representation['date_stop'] = instance.date_stop.strftime('%d.%m.%Y')
        return representation                       
       