from rest_framework.response import Response
from rest_framework.views import APIView

from erp.api.api import ProductSerializer
from erp.models import Product


class ProductsByNumberView(APIView):

    def get(self, request, number):
        products = Product.objects.filter(
            number__icontains=number
        )

        json_products = ProductSerializer(products, many=True).data

        return Response(
            {
                'data': json_products
            }
        )
