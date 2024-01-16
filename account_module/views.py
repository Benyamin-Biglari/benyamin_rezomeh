from django.shortcuts import render
from . import form
from . import models
import datetime
from django.views import View
from django.shortcuts import redirect

class register(View):
    def get(self,request):
        form_reg=form.registerform()
        img=models.call_img.objects.all()
        return render(request,'call/contact.html',context={"form":form_reg,
                                                           "img":img})
    

    def post(self,request):
        form_reg=form.registerform(request.POST)
        if form_reg.is_valid():
            new_message=models.register_model()
            new_message.username =form_reg.cleaned_data['username']
            new_message.email = form_reg.cleaned_data['email']
            new_message.desc = form_reg.cleaned_data['desc']
            new_message.date = datetime.datetime.now()
            new_message.is_active=False
            new_message.is_superuser=False
            new_message.save()
            return redirect('/')
