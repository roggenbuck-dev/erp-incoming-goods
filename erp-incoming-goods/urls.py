from django.urls import path

from erp.views.incomingGoodCRUD import delete, update
from erp.views.incomingGoodCRUD.create import new_goods
from erp.views.incomingGoodCRUD.read import incoming_goods
from erp.views.products.products_by_ean import ProductsByEanView
from erp.views.products.products_by_name import ProductsByNameView
from erp.views.products.products_by_number import ProductsByNumberView

urlpatterns = [
    path('incoming-goods/', incoming_goods, name='incoming_goods'),
    path('incoming-goods/create/', new_goods, name='new_goods'),
    path('incoming-goods/delete/<int:entry_id>/', delete.delete_entry, name='delete'),
    path('incoming-goods/update/<int:entry_id>/', update.update_entry, name='update'),
    path('products/products-by-ean/<ean>', ProductsByEanView.as_view(), name='products_by_ean'),
    path('products/products-by-name/<n>', ProductsByNameView.as_view(), name='products_by_name'),
    path('products/products-by-number/<number>', ProductsByNumberView.as_view(), name='products_by_number'),
]
