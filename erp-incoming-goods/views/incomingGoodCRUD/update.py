from django.shortcuts import get_object_or_404, render, redirect
from erp.models import WarehouseStock

from erp.models.incoming_goods import IncomingGoods


def update_entry(request, entry_id):
    entry = get_object_or_404(IncomingGoods, pk=entry_id)

    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity'))
        entry.warehouse_code = request.POST.get('warehouse')

        quantity_difference = new_quantity - entry.quantity
        entry.quantity = new_quantity
        entry.save()

        warehouse_stock_entry = WarehouseStock.objects.get(
            warehouse=entry.warehouse,
            product=entry.product
        )

        warehouse_stock_entry.stock += quantity_difference
        warehouse_stock_entry.save()

        return redirect('incoming_goods')

    return render(
        request,
        'update.html',
        {
            "entry": entry,
            "ean": entry.product.gtin,
            "product_name": entry.product.name,
            "product_number": entry.product.number
        }
    )
