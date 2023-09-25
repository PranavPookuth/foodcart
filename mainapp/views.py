from django.shortcuts import render,redirect
from foodapp.models import contactdb,categorydb,productdb
from mainapp.models import cartdb,checkoutdb,userdb
from django.db.models import Sum
from django.contrib import messages
# Create your views here.
def homepage(req):
    category_data = categorydb.objects.all()
    context={
        'category_data':category_data
    }
    return render(req,"home.html",context)

def aboutpage(req):
    category_data = categorydb.objects.all()
    return render(req,"about.html",{"category_data":category_data})

def contactpage(req):
    category_data = categorydb.objects.all()
    return render(req,"contact.html",{"category_data":category_data})

def savecontact(req):
    if req.method=="POST":
        na = req.POST.get('name')
        em = req.POST.get('email')
        msg = req.POST.get('message')
        obj=contactdb(Name=na, Email=em, Message=msg)
        obj.save()
        return redirect(contactpage)


def shoppage(req,products):
    category_data = categorydb.objects.all()
    product_data = productdb.objects.filter(Category=products)
    context = {
        'category_data' : category_data,
        'product_data' : product_data
    }
    return render(req,"shop.html",context)

def cartpage(req):
    cart=cartdb.objects.filter(username=req.session['username'])
    data = categorydb.objects.all()
    grandtotal= cart.aggregate(Sum("totalprice"))["totalprice__sum"]
    return render(req,"cart.html",{'data':data,"cart":cart,"grandtotal":grandtotal} )


def savecart(req):
    if req.method == "POST":
        pn = req.POST.get('productname')
        un = req.POST.get('username')
        pid = req.POST.get("pid")
        file = productdb.objects.get(id=pid)
        img=file.Image
        pp = req.POST.get('productprice')
        pq = req.POST.get('productquanatity')
        tp = req.POST.get('totalprice')
        obj = cartdb(productname = pn,price = pp,quantity=pq,totalprice = tp,image=img,username=un)
        obj.save()
        return redirect(cartpage)

def deletecart(req,dataid):
    data=cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(cartpage)






def checkpage(req):
    cart = cartdb.objects.all()
    grandtotal = cart.aggregate(Sum("totalprice"))["totalprice__sum"]
    return render(req,"check.html",{"cart":cart,"grandtotal":grandtotal})


def savecheckout(req):
    if req.method=="POST":
        na=req.POST.get('Name')
        em =req.POST.get('Email')
        ad = req.POST.get('Address')
        ph =req.POST.get('Phone')
        cy =req.POST.get('city')
        pin = req.POST.get('pincode')
        obj= checkoutdb(name =na,email = em,address=ad,phone=ph,city=cy,pincode=pin )
        obj.save()
        return redirect(homepage)
def singlepage(req,dataid):
    data = categorydb.objects.all()
    product = productdb.objects.get(id=dataid)
    return render(req,"singleproduct.html",{'data':data,'product':product})

def userpage(req):
    return render(req,"login.html")

def usersavedata(request):
    if request.method=="POST":
        user_r=request.POST.get('usernamel')
        gmail_r = request.POST.get('email')
        password_r=request.POST.get('passwordl')
        c_password=request.POST.get('conformpasswordl')
        obj=userdb(username=user_r,email=gmail_r,password=password_r,confirmpassword=c_password)
        obj.save()
        messages.success(request, "Congratulations..! Account created successfully...!")

        return redirect(userpage)

def userloginpage(request):
        if request.method == "POST":
            username_R = request.POST.get("username")
            password_R = request.POST.get("password")
            if userdb.objects.filter(username=username_R, password=password_R).exists():
                data = userdb.objects.filter(username=username_R, password=password_R).values('email', 'id').first()

                request.session['username'] = username_R

                request.session['password'] = password_R

                return redirect(homepage)

            else:
                return redirect(userpage)
        else:
            return redirect(userpage)


def userlogout(request):
    request.session.clear()
    return redirect(userloginpage)
def gateway(req):
    cart=cartdb.objects.all()
    grandtotal = cart.aggregate(Sum("totalprice"))["totalprice__sum"]
    return render(req,"paymentgateway.html",{"cart":cart,"grandtotal":grandtotal})