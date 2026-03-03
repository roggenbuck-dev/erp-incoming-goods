from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from erp.models import Product, Warehouse, WarehouseStock
from erp.models.incoming_goods import IncomingGoods


@login_required
def new_goods(request):
    if request.method == 'POST':
        user = request.user
        ean = request.POST.get('ean')
        product_name = request.POST.get('product_name')
        product_number = request.POST.get('product_number')
        quantity = int(request.POST.get('quantity'))
        warehouse_code = request.POST.get('warehouse')

        # get a product based on the information in ProductDatabase
        product = Product.objects.get(
            number=product_number,
        )

        # get a warehouse based on the provided code
        warehouse = Warehouse.objects.get(
            code=warehouse_code
        )

        # Create a new IncomingGoods object and save it to the database
        incoming_goods_obj = IncomingGoods.objects.create(
            created_by=user,
            quantity=quantity,
            product=product,
            warehouse=warehouse,
        )
        # Update the warehouse stock with the incoming quantity
        warehouse_stock, created = WarehouseStock.objects.get_or_create(
            warehouse=warehouse,
            product=product,
            defaults={'stock': 0}
        )
        warehouse_stock.stock = quantity + warehouse_stock.stock
        warehouse_stock.save()

        return redirect('incoming_goods')

    return render(request, 'create.html')
