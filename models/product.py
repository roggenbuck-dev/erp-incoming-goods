from django.db import models


class Product(models.Model):
    number             = models.CharField(max_length=20, blank=False, default='', unique=True)
    gtin               = models.CharField(max_length=20, blank=False, default='', unique=True)
    name               = models.CharField(max_length=255, blank=False, default='')
    unit               = models.CharField(max_length=3, blank=False, default='')
    tax_rate           = models.ForeignKey('TaxRate', on_delete=models.PROTECT, default='', related_name='%(class)s_requests_name')
    brand              = models.ForeignKey('Brand', on_delete=models.PROTECT, default='', related_name='%(class)s_requests_name')
    brand_number       = models.CharField(max_length=50, blank=True, default='')
    srp                = models.DecimalField(max_digits=15, decimal_places=5, default=0)
    active             = models.BooleanField(default=True)
    imported           = models.BooleanField(default=False)
    use_stock          = models.BooleanField(default=False)
    is_virtual         = models.BooleanField(default=False)
    sales_unit         = models.ForeignKey('SalesUnit', on_delete=models.PROTECT, default='', related_name='%(class)s_requests_unit')
    length_mm          = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    width_mm           = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    height_mm          = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    product_weight_kg  = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    shipping_weight_kg = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sales_channels     = models.ManyToManyField('SalesChannel')

    class Meta:
        db_table = "erp_product"

    def __str__(self):
        return self.number
