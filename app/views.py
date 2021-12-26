from django.shortcuts import redirect, render
from .forms import MobileForm
from .models import Mobile
def index(request):
    mobiles=Mobile.objects.all()
    return render(request,'app/home.html',{'mobiles':mobiles})

def create_mobile(request,id=None):
    if id is None:
        form=MobileForm()
        if request.method == 'POST':
            form=MobileForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
        return render(request,'app/create_mobile.html',{'form':form})
    else:
        mobile=Mobile.objects.get(id=id)
        form=MobileForm(instance=mobile)
        if request.method == 'POST':
            form=MobileForm(request.POST or None,request.FILES or None,instance=mobile)
            if form.is_valid():
                form.save()
                return redirect('home')
        return render(request,'app/create_mobile.html',{'form':form,'mobile':mobile})

def delete_mobile(request,id):
    mobile=Mobile.objects.get(id=id)
    mobile.delete()
    return redirect('home')
