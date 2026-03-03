from rest_framework.response import Response
from rest_framework.views import APIView

from erp.api.api import ProductSerializer
from erp.models import Product


class ProductsByEanView(APIView):
    def get(self, request, ean):
        products = Product.objects.filter(
            gtin__icontains=ean
        )

        json_products = ProductSerializer(products, many=True).data

        return Response(
            {
                'data': json_products,
                'meta': {
                    'count': 0
                }
            }
        )
