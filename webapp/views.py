from django.shortcuts import render,redirect
from furniapp.models import product_db,category_db
from webapp.models import contactdb,signup_db,cartdb,orderdb
from django.contrib import messages
import razorpay

# Create your views here.
def homePage(request):
    cat=category_db.objects.all()
    carts = cartdb.objects.filter(username=request.session['s_name'])
    no=carts.count()
    return render(request,"home.html",{'cat':cat,'no':no})
def product_page(req):
    product=product_db.objects.all()
    cat = category_db.objects.all()
    return render(req,"product.html",{'product':product,'cat':cat})
def about(req):
    cat = category_db.objects.all()
    return render(req,"about.html",{'cat':cat})
def contact(req):
    cat = category_db.objects.all()
    return render(req,"contact.html",{'cat':cat})
def save_contact(req):
    if req.method=="POST":
        a=req.POST.get('fname')
        b=req.POST.get('lname')
        c=req.POST.get('email')
        d=req.POST.get('msg')
        obj=contactdb(f_name=a,l_name=b,email=c,msg=d)
        obj.save()
        return redirect(contact)
def product_filter(req,cate_name):
    data=product_db.objects.filter(cat_name=cate_name)
    return render(req,"product_filter.html",{'data':data})
def single_products(req,pro_id):
    data=product_db.objects.get(id=pro_id)
    return render(req,"single_product.html",{'data':data})
def signup(req):
    return render(req,"signup.html")
def signin(req):
    return render(req,"signin.html")
def save_signup(req):
    if req.method=="POST":
        a=req.POST.get('name')
        b=req.POST.get('email')
        c=req.POST.get('phn')
        d=req.POST.get('pass')
        e=req.POST.get('repass')
        obj=signup_db(s_name=a,s_email=b,s_mob=c,s_pass=d,s_newpass=e)
        if signup_db.objects.filter(s_name=a).exists():
            messages.warning(req,"Name already exists..!")
            return redirect(signup)
        elif signup_db.objects.filter(s_email=b).exists():
            messages.warning(req,"Email already exists..!")
            return redirect(signup)
        obj.save()
        messages.success(req,"Signed Up Successfully..!")
        return redirect(signup)
def signin_page(request):
    if request.method=="POST":
        un=request.POST.get('user')
        pa=request.POST.get('pass')
        if signup_db.objects.filter(s_name=un,s_pass=pa).exists():
            request.session['s_name']=un
            request.session['s_pass']=pa
            messages.success(request,"Login Successfully..!")
            return redirect(homePage)
        else:
            messages.warning(request,"Please enter correct Password")
            return redirect(signin)
    else:
        messages.warning(request,"invalid username")
        return redirect(signin)

def logout_page(req):
    del req.session['s_name']
    del req.session['s_pass']
    messages.success(req,"Logged Out Successfully")
    return redirect(signin_page)
def save_cart(req):
    if req.method=="POST":
        a=req.POST.get('user')
        b=req.POST.get('pname')
        c=req.POST.get('quan')
        d=req.POST.get('price')
        e=req.POST.get('tp')
        try:
            x=product_db.objects.get(p_name=b)
            img=x.p_img1
        except product_db.DoesNotExist:
            img = None
        obj=cartdb(username=a,prod_name=b,quan=c,price=d,tprice=e,cart_img=img)
        obj.save()
        return redirect(homePage)
def cart(request):
    carts = cartdb.objects.filter(username=request.session['s_name'])
    subtotal=0
    shipping_amt=0
    total_amt=0
    for i in carts:
        subtotal=subtotal+i.tprice
        if subtotal>50000:
            shipping_amt=100
        else:
            shipping_amt=250
        total_amt=subtotal+shipping_amt
    return render(request,"cart.html",{'carts':carts,'subtotal':subtotal,'shipping_amt':shipping_amt,'total_amt':total_amt})
def delete_cart(req,p_id):
    x=cartdb.objects.filter(id=p_id)
    x.delete()
    return redirect(cart)
def checkout(request):
    carts = cartdb.objects.filter(username=request.session['s_name'])
    subtotal = 0
    shipping_amt = 0
    total_amt = 0
    for i in carts:
        subtotal = subtotal + i.tprice
        if subtotal > 50000:
            shipping_amt = 100
        else:
            shipping_amt = 250
        total_amt = subtotal + shipping_amt
    return render(request,"checkout.html",{'carts':carts,'subtotal':subtotal,'shipping_amt':shipping_amt,'total_amt':total_amt})
def save_order(req):
    if req.method=="POST":
        a=req.POST.get('name')
        b=req.POST.get('address')
        c=req.POST.get('place')
        d=req.POST.get('email')
        e=req.POST.get('phone')
        f=req.POST.get('tp')
        g=req.POST.get('notes')
        obj=orderdb(name=a,address=b,place=c,email=d,phn=e,tprice=f,desc=g)
        obj.save()
        return redirect(checkout)
def payment(req):
    customer=orderdb.objects.order_by('-id').first()
    pays=customer.tprice
    amount=int(pays*100)
    pay_str=str(amount)
    for i in pay_str:
        print(i)
    if req.method=="POST":
        order_currency='INR'
        client=razorpay.Client(auth=('rzp_test_QzIn7XrT0zJ9If','9jM71BiWU9CXbvXJd0IZSuTl'))
        payyment=client.order.create({'amount':amount,'currency':order_currency})
    return render(req,"payment.html",{'customer':customer,'pay_str':pay_str})