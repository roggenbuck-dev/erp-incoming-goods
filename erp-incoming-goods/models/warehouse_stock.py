from django.db import models

from erp.models import Product, Warehouse


class WarehouseStock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, default='', related_name='%(class)s_requests_number')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT, default='', related_name='%(class)s_requests_code')
    stock = models.IntegerField(default=0)

    class Meta:
        db_table = "erp_warehouse_stock"

    def __str__(self):
        return self.product.number
