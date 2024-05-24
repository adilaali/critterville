from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from . forms import AdminLoginForm,CategoryForm,AdminUpdateBuyerForm,AdminUpdatePetForm,UpdateCategoryForm
from .models import Login,Category
from costomer.models import SignUp
from seller.models import PetDetails
from django.contrib import messages
from django.contrib.auth import logout as logouts


# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')


def adminlogin(request):
    if request.method=='POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['UserName']
            password=form.cleaned_data['Password']
            try:
                user=Login.objects.get(UserName=username)
                if username!="critterville":
                    messages.warning(request,"Enter a valid Username")
                    return redirect('/adminlogin')
                
                elif password!="crittervil":
                    messages.warning(request,"Incorrect Password")
                    return redirect('/adminlogin')
                
                else:
                    messages.success(request,"")
                    return redirect('/dashboard')
            except:
              messages.warning(request,"Username or Password Incorrect")
    else:
        form=AdminLoginForm()
    return render(request,'adminlogin.html', {'form':form})

def category(request):
    if request.method=='POST':
        form = CategoryForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
    
    else:
        form = CategoryForm()
    return render(request,'category.html', {'form':form})

def viewcategories(request):
    user=Category.objects.all()
    return render(request,'viewcategories.html',{'user':user})

def updatecategory(request,id):
    user=Category.objects.get(id=id)
    if request.method=='POST':
        form=UpdateCategoryForm(request.POST or None,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,"updated")
            return redirect('/viewcategories')
    else:
        form=UpdateCategoryForm(instance=user)
    return render(request,'updatecategory.html',{'user':user,'form':form})

def deletecategory(request,id):
    user=Category.objects.get(id=id)
    user.delete()
    messages.success(request,"Deleted")
    return redirect('/viewcategories')

def showusers(request):
    user=SignUp.objects.all()
    return render(request,'showusers.html',{'user':user})



def adminupdatebuyer(request,id):
    user=SignUp.objects.get(id=id)
    form=AdminUpdateBuyerForm(request.POST or None,instance=user)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            messages.success(request," ")
            return redirect('/showusers')
    else:
        form=AdminUpdateBuyerForm(instance=user)
    return render(request,'adminupdatebuyer.html',{'form':form})

def admindeleteuser(request,id):
    user=SignUp.objects.get(id=id)
    user.delete()
    messages.success(request," ")
    return redirect('/showusers')


def showpets(request):
    pet=PetDetails.objects.all()
    return render(request,'showpets.html',{'pet':pet})


def admin_updatepet(request,id):
    pet=PetDetails.objects.get(id=id)
    form=AdminUpdatePetForm(request.POST or None,request.FILES or None,instance=pet)
    if form.is_valid():
        form.save()
        messages.success(request," ")
        return redirect('/showpets')
    else:
        form=AdminUpdatePetForm(instance=pet)
    return render(request,'adminupdatepet.html',{'form':form})

def admin_deletepet(request,id):
    pet=PetDetails.objects.get(id=id)
    pet.delete()
    messages.success(request," ")
    return redirect('/showpets')

def adminlogout(request):
    logouts(request)
    messages.success(request,"")
    return redirect('/')







    

