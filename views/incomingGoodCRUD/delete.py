from django.http import JsonResponse

from erp.models import WarehouseStock
from erp.models.incoming_goods import IncomingGoods


def delete_entry(request, entry_id):
    try:
        entry = IncomingGoods.objects.get(pk=entry_id)
        warehouse_stock_entry = WarehouseStock.objects.filter(
            warehouse=entry.warehouse,
            product=entry.product
        ).first()

        if warehouse_stock_entry:
            warehouse_stock_entry.stock -= entry.quantity
            warehouse_stock_entry.save()

        entry.delete()
        return JsonResponse({'success': True})
    except IncomingGoods.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Entry not found'})
