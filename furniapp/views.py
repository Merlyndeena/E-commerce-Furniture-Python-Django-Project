from django.shortcuts import render,redirect
from furniapp.models import category_db,product_db
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from  django.contrib.auth import authenticate,login
from django.contrib import messages
from datetime import date
from webapp.models import contactdb
def index(req):
    cat=category_db.objects.all()
    no=cat.count()
    pro=product_db.objects.all()
    pro=pro.count()
    return render(req,"index.html",{'no':no,'pro':pro})
def add_cat(req):
    category=category_db.objects.all()
    return render(req,"add_cat.html",{'category':category})

def view_cat(req):
    cat=category_db.objects.all()
    return render(req,"view_cat.html",{'cat':cat})

def save_cat(req):
    if req.method=="POST":
        a=req.POST.get('cname')
        b=req.FILES['cimg']
        c=req.POST.get('cdesc')
        obj=category_db(C_Name=a,C_Image=b,C_Desc=c)
        obj.save()
        messages.success(req,"Category Saved...!")
        return redirect(add_cat)
def edit_cat(req,c_id):
    cate=category_db.objects.get(id=c_id)
    return render(req,"edit_cat.html",{'cate':cate})

def update_cat(req,ct_id):
    if req.method=="POST":
        a=req.POST.get('cname')
        c=req.POST.get('cdesc')
    try:
        b = req.FILES['cimg']
        fs=FileSystemStorage()
        file=fs.save(b.name,b)
    except MultiValueDictKeyError:
        file=category_db.objects.get(id=ct_id).C_Image
    category_db.objects.filter(id=ct_id).update(C_Name=a,C_Image=file,C_Desc=c)
    messages.success(req,"Category Updated")
    return redirect(view_cat)
def delete_cat(req,cate_id):
    x=category_db.objects.filter(id=cate_id)
    x.delete()
    messages.error(req,"Category Deleted...!")
    return redirect(view_cat)
def add_pro(req):
    category=category_db.objects.all()
    return render(req,"add_pro.html",{'category':category})
def view_pro(req):
    pro=product_db.objects.all()
    return render(req,"view_pro.html",{'pro':pro})
def save_pro(req):
    if req.method=="POST":
        a=req.POST.get('cname')
        b=req.POST.get('pname')
        c=req.POST.get('quantity')
        d=req.POST.get('amt')
        e=req.POST.get('pdesc')
        f=req.POST.get('pcoo')
        g=req.POST.get('manu')
        h=req.FILES['cimg1']
        i=req.FILES['cimg2']
        j=req.FILES['cimg3']
        obj=product_db(cat_name=a,p_name=b,p_quan=c,p_mrp=d,p_desc=e,p_coo=f,p_manu=g,p_img1=h,p_img2=i,p_img3=j)
        obj.save()
        messages.success(req,"Product Saved...!")
        return redirect(add_pro)
def edit_pro(req,p_id):
    category=category_db.objects.all()
    pro=product_db.objects.get(id=p_id)
    return render(req,"edit.html",{'pro':pro,'category':category})
def update_pro(req,p_id):
    if req.method == "POST":
        a = req.POST.get('cname')
        b = req.POST.get('pname')
        c = req.POST.get('quantity')
        d = req.POST.get('amt')
        e = req.POST.get('pdesc')
        f = req.POST.get('pcoo')
        g = req.POST.get('manu')
        try:
            h = req.FILES['cimg1']
            fs=FileSystemStorage()
            file=fs.save(h.name,h)
        except MultiValueDictKeyError:
            file=product_db.objects.get(id=p_id).p_img1
        try:
            i = req.FILES['cimg2']
            fs=FileSystemStorage()
            file1=fs.save(i.name,i)
        except MultiValueDictKeyError:
            file1=product_db.objects.get(id=p_id).p_img2
        try:
            j = req.FILES['cimg3']
            fs=FileSystemStorage()
            file2=fs.save(j.name,j)
        except MultiValueDictKeyError:
            file2=product_db.objects.get(id=p_id).p_img3
        product_db.objects.filter(id=p_id).update(cat_name=a,p_name=b,p_quan=c,p_mrp=d,p_desc=e,p_coo=f,p_manu=g,p_img1=file,p_img2=file1,p_img3=file2)
        messages.success(req, "Product Updated")
        return redirect(view_pro)
def delete_pro(req,p_id):
    x=product_db.objects.filter(id=p_id)
    x.delete()
    messages.error(req,"Product Deleted...!")
    return redirect(view_pro)
def admin_login(req):
    return render(req,"admin_log.html")
def login_page(request):
    if request.method=="POST":
        un=request.POST.get('user')
        pa=request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            user=authenticate(username=un,password=pa)
            if user is not None:
                login(request,user)
                request.session['username']=un
                request.session['password']=pa
                messages.success(request,"Login Successfully..!")
                return redirect(index)
            else:
                messages.warning(request,"Please check your password..!")
                return redirect(admin_login)
        else:
            messages.warning(request,"Invalid Username ..!")
            return redirect(admin_login)
def logout(req):
    del req.session['username']
    del req.session['password']
    return redirect(admin_login)
def contact_data(req):
    con=contactdb.objects.all()
    return render(req,"contact_data.html",{'con':con})
def delete_contact(req,p_id):
    x=contactdb.objects.filter(id=p_id)
    x.delete()
    return redirect(contact_data)
