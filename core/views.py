from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import Ad
from .forms import SignUpForm,AddAdForm

@login_required(login_url='login')
def my_ad(request):
    print('hi viw ad list')
    ads=Ad.objects.filter(user=request.user).order_by('-created_at')
    return render(request,'core/ad_list.html',{'ads':ads})

@login_required(login_url='login')
def delete_ad(request,id):
     ad=get_object_or_404(Ad,id=id)
     if request.user != ad.user:
          return redirect('ad_list')
     if request.method == 'POST':
          ad.delete()
          messages.error(request,'پست کاربر با موفقیت حذف شد')
          return redirect('my_ad')
     return redirect('ad_detail',id=id)

@login_required(login_url='login')
def edite_ad(request,id):
     ad=get_object_or_404(Ad,id=id)
     if request.user != ad.user:
          return redirect('ad_list')
     if request.method =='POST':
          form=AddAdForm(request.POST,request.FILES,instance=ad)
          if form.is_valid:
              form.save()
              messages.success(request,'پست کاربر با موفقیت ویرایش شد')
              return redirect('ad_detail',id=ad.id)
     else:
           form=AddAdForm(instance=ad)
     return render(request,'core/add_ad.html',{'form':form})

def ad_list(request):
    print('hi viw ad list')
    ads=Ad.objects.all().order_by('-created_at')
    return render(request,'core/ad_list.html',{'ads':ads})

def ad_detail(request,id):
    ad=get_object_or_404(Ad,id=id)
    return render(request,'core/ad_detail.html',{'ad':ad})

@login_required(login_url='login')
def add_ad(request):
     if request.method == 'POST':
          form=AddAdForm(request.POST,request.FILES)
          if form.is_valid():
               ad=form.save(commit=False)
               ad.user=request.user
               ad.save()
               messages.success(request,'آگهی شما با موفقیت ثبت شد')
               return redirect('ad_list')
     else:
          form=AddAdForm()
     return render(request,'core/add_ad.html',{'form':form})

def signup(request):
    if request.method =='POST': 
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('ad_list')
    else:
            form=SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

def about(request):
     return render(request,'core/about.html')


# Create your views here.
