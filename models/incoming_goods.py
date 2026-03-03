from django.db import models
from django.contrib.auth.models import User

from erp.models import Product, Warehouse


class IncomingGoods(models.Model):
    quantity = models.SmallIntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='incomingGoods')
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='incomingGoods')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT, related_name='incomingGoods')

    class Meta:
        db_table = "erp_incoming_goods"

    def __str__(self):
        return '{} {}'.format(self.product.number, self.warehouse.code)
