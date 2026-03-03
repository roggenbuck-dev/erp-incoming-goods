from django.db import models


class Warehouse(models.Model):
    code = models.CharField(max_length=4, blank=False, default='', unique=True)

    class Meta:
        db_table = "erp_warehouse"

    def __str__(self):
        return self.code
