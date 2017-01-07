from rest_framework import serializers
from todo.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all())

    class Meta:
        model = Category
        fields = ('name', )


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.FileField(max_length=None, use_url=True)
    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'image',
                  'category',
                  'price',
                  'attributes', )

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Product.objects.create(**validated_data)
