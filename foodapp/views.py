from django.shortcuts import render, redirect, HttpResponse
from foodapp.models import categorydb, productdb,contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate


# Create your views here.
def home(req):
    return render(req, "index.html")





def new(req):
    return render(req, "addcategory.html")


def savedata(req):
    if req.method == "POST":
        na = req.POST.get('cname')
        dn = req.POST.get('description')
        img = req.FILES['image']
        obj = categorydb(Category_name=na, Description=dn, Image=img)
        obj.save()
    return redirect(new)


def display(req):
    data = categorydb.objects.all()
    return render(req, "displaycategory.html", {"data": data})


def editdata(req, dataid):
    data = categorydb.objects.get(id=dataid)
    print(data)
    return render(req, "editcategory.html", {"data": data})


def updatecategory(req, dataid):
    if req.method == "POST":
        cn = req.POST.get('cname')
        pl = req.POST.get('description')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=dataid).Image
        categorydb.objects.filter(id=dataid).update(Category_name=cn, Description=pl, Image=file)
        return redirect(display)


def deletedata(req, dataid):
    data = categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(display)


def product(req):
    data = categorydb.objects.all()
    return render(req, "addproduct.html", {"data": data})


def savepro(req):
    if req.method == "POST":
        pn = req.POST.get('pname')
        ds = req.POST.get('description')
        img = req.FILES['image']
        pri = req.POST.get('price')
        ct = req.POST.get('category')
        obj = productdb(Product_name=pn, Image=img, Description=ds, Price=pri, Category=ct)
        obj.save()
        return redirect(product)


def displaypro(req):
    data = productdb.objects.all()
    return render(req, "displayproduct.html", {"data": data})


def editpro(req, dataid):
    data = productdb.objects.get(id=dataid)
    category_data = categorydb.objects.all()
    return render(req, "editproducts.html", {"data": data, "category_data": category_data})


def updatepro(req, dataid):
    if req.method == "POST":
        pn = req.POST.get('pname')
        dn = req.POST.get('description')
        pri = req.POST.get('price')
        ct = req.POST.get('category')

        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).Image
        productdb.objects.filter(id=dataid).update(Product_name=pn, Description=dn, Price=pri, Category=ct, Image=file)
        return redirect(displaypro)


def deletepro(req, dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaypro)


def loginn(request):
    return render(request, "adminlogin.html")

def adminloginn(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pswrd = request.POST.get('password')
        print(uname,pswrd)
        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname, password=pswrd)
            if user is not None:
                login(request, user)
                request.session['username'] = uname
                request.session['password'] = pswrd
                return redirect(home)
            else:
                return redirect(loginn)
        else:
            return redirect(loginn)


def adminlogout(req):
    del req.session['username']
    del req.session['password']
    return redirect(loginn)

def displaycontact(req):
    data = contactdb.objects.all()
    return render(req, "display_contact.html", {"data": data})

def deletecontact(req, dataid):
    data = contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycontact)