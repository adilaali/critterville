from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserSignUpForm,UserLoginForm,UpdateBuyerForm,BuyerChangePasswordForm
from .models import SignUp
from seller.models import PetDetails
from adminapp.models import Category
from django.contrib import messages
from django.contrib.auth import logout as logouts
from critterville import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,'index.html')


def usersignup(request):
    if request.method=='POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            firstname=form.cleaned_data['FirstName']
            lastname=form.cleaned_data['LastName']
            phonenumber=form.cleaned_data['Phone_Number']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Pass_word']
            confirmpassword=form.cleaned_data['ConfirmPassword']

            user=SignUp.objects.filter(Email=email).exists()

            if user:
                messages.warning(request,"Already Exist")
                return redirect('/usersignup')
            elif password!=confirmpassword:
                messages.warning(request,"Mismatch")
                return redirect('/usersignup')
            else:
                tab = SignUp(FirstName=firstname, LastName=lastname, Phone_Number=phonenumber, Email=email, Pass_word=password)
                tab.save()
                messages.success(request,"")
                return redirect('/userlogin')
    else:
        form = UserSignUpForm()   
    return render(request,'usersignup.html', {'form':form})

def userlogin(request):
    if request.method=='POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Pass_word']
            try:
                user=SignUp.objects.get(Email=email)
                if not user:
                    messages.warning(request,"Enter a valid Email")
                    return redirect('/userlogin')
                elif password!=user.Pass_word:
                    messages.warning(request,"Incorrect Password")
                    return redirect('/userlogin')
                else:
                    messages.success(request,"")
                    return redirect('/userhome/%s' % user.id)
            except:
                messages.warning(request,"Username or Password Incorrect")
                return redirect('/userlogin')
    
    else:
        form=UserLoginForm()
    return render(request,'userlogin.html', {'form':form})



def userhome(request,id):
    user=SignUp.objects.get(id=id)
    return render(request,'userhome.html',{'user':user})


def buyerhome(request,id):
    user=SignUp.objects.get(id=id)
    category=Category.objects.all()
    return render(request,'buyerhome.html',{'user':user,'category':category})

def updatebuyer(request,id):
    user=SignUp.objects.get(id=id)
    if request.method=='POST':
        form=UpdateBuyerForm(request.POST or None,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,"")
            return redirect('/viewprofile/%s' % user.id)
    else:
        form=UpdateBuyerForm(instance=user)
    return render(request,'updatebuyer.html',{'user':user,'form':form})

def changepasswordbuyer(request,id):
    user=SignUp.objects.get(id=id)
    if request.method=='POST':
        form=BuyerChangePasswordForm(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            confirmpassword=form.cleaned_data['ConfirmPassword']
            if oldpassword!=user.Pass_word:
                messages.warning(request,"Incorrect")
                return redirect('/changepasswordbuyer/%s' % user.id)
            elif oldpassword==newpassword:
                messages.warning(request,"Similar")
                return redirect('/changepasswordbuyer/%s' % user.id)
            elif newpassword!=confirmpassword:
                messages.warning(request,"Mismatch")
                return redirect('/changepasswordbuyer/%s' % user.id)
            else:
                user.Pass_word=newpassword
                user.save()
                messages.success(request,"Success")
                return redirect('/buyerhome/%s' % user.id)
    else:
        form=BuyerChangePasswordForm()
    return render(request,'changepasswordbuyer.html',{'form':form,'user':user})

def buyerlogout(request):
    logouts(request)
    messages.success(request,"")
    return redirect('/')

def readcategory(request,id,uid):
    user=SignUp.objects.get(id=uid)
    category=Category.objects.all()
    cats=Category.objects.get(id=id)
    pro=PetDetails.objects.filter(Category=cats)
    return render(request,'readcategory.html',{'user':user,'cats':cats,'pro':pro,'category':category})

def viewpetdetails2(request,id):
    pet=PetDetails.objects.get(id=id)
    return render(request,'viewpetdetails2.html',{'pet':pet})

def viewprofile(request,id):
    user=SignUp.objects.get(id=id)
    return render(request,'viewprofile.html',{'user':user})

def deleteuser(request,id):
    user=SignUp.objects.get(id=id)
    user.delete()
    messages.success(request,"")
    return redirect('/')

def mail(request):
    if request.method=='POST':
        cname=request.POST.get('contact_name')
        cemail=request.POST.get('contact_email') 
        cmessage=request.POST.get('contact_message') 
        toemail="critterville123@gmail.com"  
        res=send_mail(cname,cmessage,settings.EMAIL_HOST_USER,[toemail],fail_silently=False)
        if(res==1):
            msg="Mail Sent Successfully"
        else:
            msg="Mail could not sent"
        return HttpResponse(msg)
    else:
        return render(request,'mail.html')
    



