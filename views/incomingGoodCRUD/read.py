from erp.models.incoming_goods import IncomingGoods
from django.shortcuts import render


def incoming_goods(request):
    return render(
        request,
        'incomingGoods.html',
        {
            'incomingGoods': IncomingGoods.objects.all()
        }
    )
