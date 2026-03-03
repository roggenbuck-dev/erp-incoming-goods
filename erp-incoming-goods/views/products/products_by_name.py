from rest_framework.response import Response
from rest_framework.views import APIView

from erp.api.api import ProductSerializer
from erp.models import Product


class ProductsByNameView(APIView):

    def get(self, request, name):
        products = Product.objects.filter(
            name__icontains=name
        )

        json_products = ProductSerializer(products, many=True).data

        return Response(
            {
                'data': json_products
            }
        )
