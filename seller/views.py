from django.shortcuts import render,redirect
from .forms import PetDetailsForm,UpdateSellerForm
from .models import PetDetails
from costomer . models import SignUp
from django.contrib import messages
from django.contrib.auth import logout as logouts

# Create your views here.
def sellerhome(request,id):
    user=SignUp.objects.get(id=id)
    if request.method=='POST':
        form = PetDetailsForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            username=form.cleaned_data['Username']
            name=form.cleaned_data['Name']
            category=form.cleaned_data['Category']
            breed=form.cleaned_data['Breed']
            gender=form.cleaned_data['Gender']
            age=form.cleaned_data['Age']
            size=form.cleaned_data['Size']
            weight=form.cleaned_data['Weight']
            health=form.cleaned_data['Health']
            location=form.cleaned_data['Location']
            photo1=form.cleaned_data['Photo1']
            photo2=form.cleaned_data['Photo2']
            contactno=form.cleaned_data['Contact_No']
            description=form.cleaned_data['Description']
            price=form.cleaned_data['Price']
            
            tab = PetDetails(Username=username,Name=name,Category=category,Breed=breed,
                                 Gender=gender,Age=age,Size=size,Weight=weight,
                                 Health=health,Location=location,Photo1=photo1,Photo2=photo2,
                                 Contact_No=contactno,Description=description,Price=price)
            tab.save()
            messages.success(request,"")
            return redirect('/listed_products/%s' % user.id)
    else:
        form = PetDetailsForm()
    return render(request,'sellerhome.html', {'form':form,'user':user})



def updatepetdetail(request,uid,pid):
    user=SignUp.objects.get(id=uid)
    pet=PetDetails.objects.get(id=pid)
    form=UpdateSellerForm(request.POST or None,request.FILES or None,instance=pet)
    if form.is_valid():
        form.save()
        messages.success(request,"")
        return redirect('/viewpetdetails/%s/%s' % (user.id,pet.id))
    else:
        form=UpdateSellerForm(instance=pet)
    return render(request,'updatepetdetail.html',{'form':form,'user':user,'pet':pet})


def listed_products(request,id):
    user=SignUp.objects.get(id=id)
    pet=PetDetails.objects.filter(Username=id)
    return render(request,'listed_products.html',{'pet':pet,'user':user})

def viewpetdetails(request,uid,id):
    user=SignUp.objects.get(id=uid)
    pet=PetDetails.objects.get(id=id)
    return render(request,'viewpetdetails.html',{'pet':pet,'user':user})

def sellerlogout(request):
    logouts(request)
    messages.success(request,"")
    return redirect('/')

def deletepet(request,uid,pid):
    user=SignUp.objects.get(id=uid)
    pet=PetDetails.objects.filter(id=pid)
    pet.delete()
    messages.success(request,"")
    return redirect('/sellerhome/%s' % user.id)



