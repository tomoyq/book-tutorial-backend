from rest_framework import views, status
from rest_framework.response import Response

from .models import *
from .serializers import *

class ProductView(views.APIView):
    """
    商品操作に関する関数
    """

    def get(self, request, format=None):
        """
        商品の一覧を取得する
        """

        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)