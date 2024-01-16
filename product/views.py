from django.shortcuts import render
from . import models

# Create your views here.


def index(request):
    list_product1=models.data.objects.all()
    list_product2=models.ability.objects.all()
    list_product3 = models.tahsil.objects.all()
    list_product4 = models.my_work_img.objects.all()
    list_product6 = models.work_place.objects.all()
    list_product7 = models.tajrobeh.objects.all()
    return render(request,'product/base.html',{"list_product1":list_product1,
                                                                    "list_product2":list_product2,
                                                                    "list_product3":list_product3,
                                                                    "list_product4": list_product4,
                                                                    'list_product6':list_product6,
                                                                    "list_product7":list_product7,
                                                                    })






