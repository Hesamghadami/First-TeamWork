from rest_framework import serializers
from ...models import *


# class CourseApiSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=200)
#     price = serializers.IntegerField()


class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portofolio
        fields = ["id", "title", "price", "category", "image1", "image2", "image3"]




class PortfolioDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portofolio
        fields = ["id", "title", "price", "category", "image1", "image2", "image3", "client_url", "client", "content", "status"]