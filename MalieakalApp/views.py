from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import uuid
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib.auth import update_session_auth_hash
from .forms import *
import random
import string
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime,date, timedelta
import pywhatkit
######################################################################### <<<<<<<<<< LANDING MODULE >>>>>>>>>>>>>>
def index(request):
    return render(request, 'index/index.html')



def user_type(request):
  
    return render(request, 'index/user_type.html')

def login_main(request):
    if request.method == 'POST':
        username  = request.POST['username']
        password = request.POST['password']
        print(username)
        user = authenticate(username=username, password=password)
        
        
        if User_Registration.objects.filter(username=request.POST['username'], password=request.POST['password'],role="user1").exists():

            member = User_Registration.objects.get(username=request.POST['username'],password=request.POST['password'])
            
            request.session['userid'] = member.id
            if Profile_User.objects.filter(user_id=member.id).exists():
                return redirect('staff_home')
            else:
                return redirect('profile_staff_creation')
            
            
        elif User_Registration.objects.filter(username=request.POST['username'], password=request.POST['password'],role="user2").exists():
            member = User_Registration.objects.get(username=request.POST['username'],password=request.POST['password'])
            request.session['userid'] = member.id
            if Profile_User.objects.filter(user_id=member.id).exists():
                return redirect('home')
            else:
                return redirect('profile_user_creation')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request,'index/login.html')

def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if  User_Registration.objects.filter(email=email).exists():
            user =  User_Registration.objects.get(email=email)

        

            current_site = get_current_site(request)
            mail_subject = "Reset your password"
            message = render_to_string('index/forget-password/reset_password_email.html',{
                'user':user,
                'domain' :current_site,
                'user_id' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : default_token_generator.make_token(user),
            }) 

            to_email = email
            send_email = EmailMessage(mail_subject,message,to = [to_email])
            send_email.send()

            messages.success(request,"Password reset email has been sent your email address.")
            return redirect('login_main')
        else:
            messages.error(request,"This account does not exists !")
            return redirect('forgotPassword')
    return render(request,'index/forget-password/forgotPassword.html')


def resetpassword_validate(request,uidb64,token):
    try:
        user_id = urlsafe_base64_decode(uidb64).decode()
        user =  User_Registration._default_manager.get(pk=user_id)  
    except(TypeError,ValueError,OverflowError, User_Registration.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user,token):
        request.session['user_id'] = user_id 
        messages.success(request,"Please reset your password.")
        return redirect('resetPassword')
    else:
        messages.error(request,"The link has been expired !")
        return redirect('login_main')
    
def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('user_id') 
            user =  User_Registration.objects.get(pk=uid)
            user.password = password
            user.save()
            messages.success(request,"Password reset successfull.")
            return redirect('login_main')

        else:
            messages.error(request,"Password do not match")
            return redirect('resetPassword')
    else:
        return render(request,'index/forget-password/resetPassword.html')

def logout(request):
    if 'userid' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')
############################################################# <<<<<<<<<< STAFF MODULE >>>>>>>>>>>>>>
def staff_base(request):
    ids=request.session['userid']
    usr=Profile_User.objects.get(user=ids)
    lk=category.objects.get(id=1)
 
    context={
        'user':usr,
        "lk":lk
    }
    return render(request, 'staff/staff_base.html',context)

def staff_home(request):
    ids=request.session['userid']
    usr=Profile_User.objects.get(user=ids)
    items = item.objects.all()
    return render(request, 'staff/staff_home.html',{'items':items,'user':usr,})

def new_module(request):

    item_categories = category.objects.all()
    under_choices = (
    ("Home Appliance", "Home Appliance"),
    ("Electronics", "Electronics"),
    ("Furniture", "Furniture"),
    )
    if request.method == 'POST':
        form_data = request.POST.dict()

        title = form_data.get('title', None)
        price = form_data.get('price', None)
     
        offer_price = form_data.get('offer_price', None)
        image = request.FILES.get('image', None)
        category_id = form_data.get('categories', None)
        under_category = form_data.get('under_category', None)
        title_description = form_data.get('title_description', None)
        description = form_data.get('description', None)

        categorys = get_object_or_404(category, pk=category_id)
      

        new_item = item(
            category = categorys,
            name = title,
            price = price,
            buying_count = 0,
            offer = offer_price,
            image = image,
            under_category = under_category,
            title_description = title_description,
            description = description
        )
        new_item.save()
        return redirect('staff_home')
    context={
        'item_categories':item_categories,
        'under_choices':under_choices,
    }

    return render(request,'staff/new_item_add.html',context)

# <<<<<<<<<< for Editing item >>>>>>>>>>>>>>

def new_module_edit(request, item_id):
    item_instance = get_object_or_404(item, pk=item_id)
    item_categories = category.objects.all()
    under_choices = (
        ("Home Appliance", "Home Appliance"),
        ("Electronics", "Electronics"),
        ("Furniture", "Furniture"),
    )

    context = {
        'item_instance': item_instance,
        'item_categories': item_categories,
        'under_choices': under_choices,
    }
    if request.method == 'POST':
        form_data = request.POST.dict()
        item_instance.name = form_data.get('title', '')
        item_instance.price = form_data.get('price', '')
        item_instance.offer = form_data.get('offer_price', '')
        item_instance.image = request.FILES.get('image', item_instance.image)
        category_id = form_data.get('categories', None)
        if category_id:
            category_instance = get_object_or_404(category, pk=category_id)
            item_instance.category = category_instance
        item_instance.under_category = form_data.get('under_category', '')
        item_instance.title_description = form_data.get('title_description', '')
        item_instance.description = form_data.get('description', '')

        item_instance.save()
        return redirect('staff_home')

    return render(request, 'staff/new_item_edit.html', context)
#################################
def delete_item(request,id):
    d1=item.objects.get(id=id)
    d1.delete()
    return redirect('/staff_home/')

def profile_staff_creation(request):
    if request.session.has_key('userid'):
        pass
    else:
        return redirect('/')
    ids=request.session['userid']
    usr=User_Registration.objects.get(id=ids)
    if request.method =="POST":
        
        firstname = request.POST.get('firstname',None)
        lastname = request.POST.get('lastname',None)
        phonenumber = request.POST.get('phonenumber',None)
        email = request.POST.get('email',None)
        gender = request.POST.get('gender',None)
        address = request.POST.get('address',None)
        date_of_birth= request.POST.get('date_of_birth',None)
        pro_pics = request.FILES.get('propic',None)
        secondnumb = request.POST.get('secondnumb',None)
        profile_artist = Profile_User(
            firstname=firstname,
            lastname=lastname,
            phonenumber=phonenumber,
            email=email,
            gender=gender,
            date_of_birth=date_of_birth,
            address=address,
            pro_pic=pro_pics,
            user=usr,
            secondnumber=secondnumb
        )
        profile_artist.save()


        return redirect('staff_home')
    context={
        'user':usr
    }
    return render(request,'index\index_staff\profile_staff_creation.html', context)

#######################################logout################### <<<<<<<<<< USER MODULE >>>>>>>>>>>>>>>>

def user_base(request):
    ids=request.session['userid']
    usr=Profile_User.objects.get(user=ids)
    lk=category.objects.get(id=1)
 
    context={
        'user':usr,
        "lk":lk
    }
    return render(request, 'user/user_base.html',context)



def user_registration(request):

    if request.method =='POST':
        form = User_RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User_Registration.objects.filter(email=email).exists():
                messages.error(request, 'Email Id already exists')
                return redirect('creator_registration')
            else:
                user_model=form.save()
            user_id = user_model.pk
            return redirect('index_user_confirmation',user_id=user_id)
    else:
        form = User_RegistrationForm()
        form.initial['role'] = 'user2'
    return render(request,'index\index_user\index_user_registraion.html',{'form':form})


def index_user_confirmation(request,user_id):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            print("success")
            if User_Registration.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('index_user_confirmation', user_id=user_id)
            else:
                artist_object = get_object_or_404(User_Registration, pk=user_id)
                artist_object.username=username
                artist_object.password = password
                artist_object.save()
                messages.success(request, 'Thank you for registering with us.')
                return redirect('login_main')
        else:
            messages.error(request, ' Password and Confirm Password are not matching. Please verify it.')
            return redirect('index_user_confirmation', user_id=user_id)

    return render(request,'index\index_user\index_user_confirmation.html',{'user_id':user_id})

def profile_user_creation(request):
    if request.session.has_key('userid'):
        pass
    else:
        return redirect('/')
    ids=request.session['userid']
    usr=User_Registration.objects.get(id=ids)
    if request.method =="POST":
        
        firstname = request.POST.get('firstname',None)
        lastname = request.POST.get('lastname',None)
        phonenumber = request.POST.get('phonenumber',None)
        email = request.POST.get('email',None)
        gender = request.POST.get('gender',None)
        address = request.POST.get('address',None)
        date_of_birth= request.POST.get('date_of_birth',None)
        pro_pics = request.FILES.get('propic',None)
        secondnumb = request.POST.get('secondnumb',None)
        profile_artist = Profile_User(
            firstname=firstname,
            lastname=lastname,
            phonenumber=phonenumber,
            email=email,
            gender=gender,
            date_of_birth=date_of_birth,
            address=address,
            pro_pic=pro_pics,
            user=usr,
            secondnumber=secondnumb
        )
        profile_artist.save()


        return redirect('user_home')
    context={
        'user':usr
    }
    return render(request,'index\index_user\profile_user_creation.html', context)


def home(request):
    if request.session.has_key('userid'):
        pass
    else:
        return redirect('/')
    ids=request.session['userid']
    usr=Profile_User.objects.get(user=ids)

    cat1="Home Appliance"
    cat2="Electronics"
    cat3="Furniture"
    all_images = bannerads.objects.all().last()
    cat_images = category.objects.all()
    item_det = item.objects.all().order_by('-buying_count')[:6]
    
    
    return render(request, 'user\home.html', {'image': all_images,'cat':cat_images,'user':usr,"cat1":cat1,"cat2":cat2,"cat3":cat3})

def user_home(request):
    if request.session.has_key('userid'):
        pass
    else:
        return redirect('/')
    ids=request.session['userid']
    usr=Profile_User.objects.get(user=ids)
    context={
        'user':usr
    }
    return render(request, 'user/user_home.html',context)

def category_items(request, category):
    if request.session.has_key('userid'):
        pass
    else:
        return redirect('/')
    ids=request.session['userid']
    usr=Profile_User.objects.get(user=ids)
    items=item.objects.filter(category_id=category)
    
    context={
        'user':usr,
        "items":items,
        
    }
    return render(request, 'user/category_items.html',context)

def under_items(request, category):
    print(category)
    if request.session.has_key('userid'):
        pass
    else:
        return redirect('/')
    ids=request.session['userid']
    usr=Profile_User.objects.get(user=ids)
    
    items=item.objects.filter(under_category=category)
    print(items)
    context={
        'user':usr,
        "items":items,
        "category":category
    }
    return render(request, 'user/uder_items.html',context)

def under_category_items_add_cart(request, id, categorys):
    if request.session.has_key('userid'):
        pass
    else:
        return redirect('/')
    ids=request.session['userid']
    usr=User_Registration.objects.get(id=ids)
    
    items=item.objects.get(id=id)
    cat=category.objects.get(id=categorys)
    if cart.objects.filter(user=usr,item=items).exists():
        messages.error(request, 'This item is already in cart')
        items=item.objects.filter(category_id=categorys)
        usrd=Profile_User.objects.get(user=ids)
        context={
        'user':usrd,
        "items":items
        }
   
    else:
        crt=cart()
        crt.user=usr
        crt.item=items
        crt.save()
        messages.error(request, 'This item is add to cart')
        items=item.objects.filter(category_id=categorys)
        usrd=Profile_User.objects.get(user=ids)
        context={
            'user':usrd,
            "items":items
        }
    return redirect("under_items",cat.category_name)

def all_items(request):

    if request.session.has_key('userid'):
        pass
    else:
        return redirect('/')
    ids=request.session['userid']
    usr=Profile_User.objects.get(user=ids)
    
    items=item.objects.all()

    context={
        'user':usr,
        "items":items,
 
    }
    return render(request, 'user/all_item.html',context)

def all_items_add_cart(request, id, category):
    if request.session.has_key('userid'):
        pass
    else:
        return redirect('/')
    ids=request.session['userid']
    usr=User_Registration.objects.get(id=ids)
    
    items=item.objects.get(id=id)
    print(items.name)
    if cart.objects.filter(user=usr,item=items).exists():
        messages.error(request, 'This item is already in cart')
        items=item.objects.filter(category_id=category)
        usrd=Profile_User.objects.get(user=ids)
        context={
        'user':usrd,
        "items":items
        }
   
    else:
        crt=cart()
        crt.user=usr
        crt.item=items
        crt.save()
        messages.error(request, 'This item is add to cart')
        items=item.objects.filter(category_id=category)
        usrd=Profile_User.objects.get(user=ids)
        context={
            'user':usrd,
            "items":items
        }
    return redirect("all_items")

def add_cart(request, id, category):
    if request.session.has_key('userid'):
        pass
    else:
        return redirect('/')
    ids=request.session['userid']
    usr=User_Registration.objects.get(id=ids)
    
    items=item.objects.get(id=id)
    print(items.name)
    if cart.objects.filter(user=usr,item=items).exists():
        messages.error(request, 'This item is already in cart')
        items=item.objects.filter(category_id=category)
        usrd=Profile_User.objects.get(user=ids)
        context={
        'user':usrd,
        "items":items
        }
   
    else:
        crt=cart()
        crt.user=usr
        crt.item=items
        crt.save()
        messages.error(request, 'This item is add to cart')
        items=item.objects.filter(category_id=category)
        usrd=Profile_User.objects.get(user=ids)
        context={
            'user':usrd,
            "items":items
        }
    return render(request, 'user/category_items.html',context)
    
def cart_view(request):
   
    if request.session.has_key('userid'):
        pass
    else:
        return redirect('/')
    ids=request.session['userid']
    usr=Profile_User.objects.get(user=ids)
    carts=cart.objects.filter(user=ids)
  
    context={
        "cart":carts,
        'user':usr,
        
    }
    return render(request, 'user/cart_display.html',context)

def product_view(request, item_id):
    if request.session.has_key('userid'):
        pass
    else:
        return redirect('/')
    ids=request.session['userid']
    usr=Profile_User.objects.get(user=ids)
    try:
        item_instance = item.objects.get(id=item_id)
        oprice = item_instance.price

        if item_instance.offer:
            off = item_instance.offer
            rp = oprice - (oprice * (off / 100))
        else:
            rp = oprice

        return render(request, 'user/productview.html', {'item': item_instance, 'rp': rp,'user':usr,})

    except item.DoesNotExist:
        # Handle the case where the item does not exist
        return HttpResponse("Item not found", status=404)

def add_cart_pr_view(request, id, category):
    if request.session.has_key('userid'):
        pass
    else:
        return redirect('/')
    ids=request.session['userid']
    usr=User_Registration.objects.get(id=ids)
    
    items=item.objects.get(id=id)
    print(items.name)
    if cart.objects.filter(user=usr,item=items).exists():
        messages.error(request, 'This item is already in cart')
        items=item.objects.filter(category_id=category)
        usrd=Profile_User.objects.get(user=ids)
        
   
    else:
        crt=cart()
        crt.user=usr
        crt.item=items
        crt.save()
        messages.error(request, 'This item is add to cart')
        items=item.objects.filter(category_id=category)
        usrd=Profile_User.objects.get(user=ids)
        
    return redirect("product_view",id)

def cart_checkout(request):
    if request.session.has_key('userid'):
        pass
    else:
        return redirect('/')
    ids=request.session['userid']
    usr=Profile_User.objects.get(user=ids)
    carts=cart.objects.filter(user=ids)
  
    context={
        "cart":carts,
        'user':usr,
        
    }
    return render(request, 'user/cart_checkout.html',context)
    
# send reciept
def send_receipt(request):
    ids=request.session['userid']
    usr=User_Registration.objects.get(id=ids)
    pro=Profile_User.objects.get(user=ids)
    if request.method =="POST":
        total_amount = request.POST.get('total_amount')
       
        item_id =request.POST.getlist('item_id[]') 
        qty =request.POST.getlist('qty[]') 

        if len(item_id)==len(qty):
            mapped2 = zip(item_id,qty)
            mapped2=list(mapped2)
         
            for ele in mapped2:
                itm=item.objects.get(id=ele[0])
                itm.buying_count=int(itm.buying_count+1)
                itm.save()
                created = checkout.objects.create(user=usr,item=itm,qty=ele[1],item_total=int(ele[1])*int(itm.price),item_name=itm.name,item_price=itm.price,date=date.today())

        chk_item=checkout.objects.filter(date=date.today()).order_by('-id')[:len(item_id)]
      
        lst=""
        for i in chk_item:
            rcp="\n\nItem : "+str(i.item_name)+'\nAmount : '+str(i.item_price)+' * '+str(i.qty)+' = '+str(i.item_total)
            lst+=rcp
     
        tot="\n\nTotal Amount : "+str(total_amount)
        subject = 'Greetings from Malieakal'
        message = 'Greetings from Malieakal\n\nReciept,\n\nName :'+str(usr.name)+str(usr.lastname)+'\nAddress :'+str(pro.address)+'\n\n'+str(lst)+str(tot)
        email_from = settings.EMAIL_HOST_USER
        
        recipient_list = [usr.email]
        send_mail(subject,message , email_from, recipient_list, fail_silently=True)

        # pywhatkit.sendwhatmsg("+918848937577",
        #                         ""+str(message),21,59)

        pywhatkit.sendwhatmsg_instantly(
            phone_no="+918848937577", 
            message=""+str(message),
        )
        print("Successfully Sent!")
        
        
        messages.error(request, 'Purchase Success Full')
        
        for i in item_id:
            print(i)
            ckt=cart.objects.get(user=usr,item_id=i).delete()
        
          
    
        return redirect("cart_checkout")
    return redirect("cart_checkout")

def delete_cart(request,id):
    ids=request.session['userid']
    usr=User_Registration.objects.get(id=ids)
    ckt=cart.objects.get(user=usr,id=id).delete()
    return redirect("cart_checkout")
  