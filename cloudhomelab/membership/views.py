import json
import stripe
from .forms import  *
from .models import *
from cmd import IDENTCHARS
from requests import request  
from itertools import product
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import View
from django.views import View , generic
from xmlrpc.client import FastMarshaller
from django.contrib import auth , messages
from django.http import HttpResponse, JsonResponse
from distutils.sysconfig import customize_compiler
from django.contrib.auth import authenticate, login 
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group , User, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, DetailView, TemplateView, DeleteView


stripe.api_key = 'sk_test_51KqHH8SIeyPpwH6UXIU6JXkww9X4NkNqJsgypvtpbgWFPud2v4S3os3WcjgE3lARykc8vVSfkr9mj4TW458VYYV30094N3JEMN'



STRIPE_PUBLISHABLE_KEY='pk_test_51KqHH8SIeyPpwH6U9sammw0PglKR5v5RNymdmNU5RgdjmUAtteTaToqCX5xcTlmQsxnx3GJnp1lBGPnEE5WPL95W00sHDJ3szs'
STRIPE_SECRET_KEY='sk_test_51KqHH8SIeyPpwH6UXIU6JXkww9X4NkNqJsgypvtpbgWFPud2v4S3os3WcjgE3lARykc8vVSfkr9mj4TW458VYYV30094N3JEMN'



# @login_required
# class Home(TemplateView):
#     template_name =  'homepage.html'


# This class will show the product details in customer index page
class Customer_index(ListView):
    context_object_name  = 'textile'
    queryset = Textiles.objects.all()
    template_name  = "products/customer/customer_index.html"


class contactus(TemplateView):

    template_name = 'contactus.html'


# This class will register the customer
class Registration(View):
    def get(self, request):
        return render(request,'products/registration/registration.html')
    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username is already exist')
                return redirect('products/registration/registration')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                user.save()
                messages.info(request, 'customer registered')
                return redirect("products/registration/login")
        else:
            messages.info(request,'password is not matching')
            return redirect('products/registration/registration')





# run

class SignUp(generic.CreateView):
    form_class = CustomSignupForm
    success_url = reverse_lazy('')
    template_name = 'signup.html'

    def form_valid(self, form):
        valid = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid




@login_required
class Index(TemplateView):
    template_name = 'products/index.html'



# This class is login for admin and customer
class Login(View):
    def get(self, request):
        return render(request,'products/registration/login.html')
    def post(self, request):
        if request.method=='POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if username == 'manager' and password == 'manager':
                auth.login(request, user)
                return redirect('products/productshop_owner/owner_index')
            elif user is not None:
                auth.login(request, user)
                return redirect("products/customer/customer_index")
            else:
                messages.info(request,'Invalid Credentials......')
                return redirect("products/registration/login")
        
# The logout class
class Logout(View):
    def get(self, request):
        auth.logout(request)
        return redirect('/')


    

# This class will show the product details in admin index page
class Owner_index(ListView):
    context_object_name  = 'textile'
    queryset = Textiles.objects.all()
    template_name = "products/productshop_owner/owner_index.html"

# This class will add the product details
class Add_product(View):
    form_class = TextilesForm
    def get(self, request):
        TextilesForm = self.form_class()
        return render(request, "products/productshop_owner/add_product.html", {'form': TextilesForm})
    def post(self, request):
        if request.method == 'POST':
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('products/productshop_owner/owner_index')
            else:
                return redirect('products/productshop_owner/add_product')
      

# This class will delete the product details
class Delete_product(View):
    def get(self, request, id):
        textile = Textiles.objects.get(id=id)
        textile.delete()
        return redirect("products/productshop_owner/owner_index")


# This class will edit/update the product details
class Edit_product(View):
    def get(self, request, id):
        textile = Textiles.objects.get(id=id) 
        form = TextilesForm(instance=textile)
        return render(request, 'products/productshop_owner/edit_product.html', {'form':form})
    def post(self, request, id):
        if request.method == 'POST':
            textile = Textiles.objects.get(id=id)
            form = TextilesForm(request.POST,request.FILES, instance=textile)
            print(form)
            if form.is_valid():
                form.save()
                return redirect("products/productshop_owner/owner_index")

# This class will display the product booked message
class Book_product(TemplateView):
    template_name = "products/customer/book_product.html"



class productDetailView(DetailView):
   
    model = Textiles
    template_name = "products/customer/product_detail.html"
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(productDetailView, self).get_context_data(**kwargs)
        context['stripe_publishable_key'] = STRIPE_PUBLISHABLE_KEY
        return context 




class PaymentFailedView(TemplateView):
    template_name = "cancel.html"

class PaymentSuccessView(TemplateView):
    template_name = "success.html"     


def success(request):
    if request.method == 'GET' and 'session_id' in request.GET:
        session = stripe.checkout.Session.retrieve(request.GET['session_id'],)
        customer = Customer()
        customer.user = request.user
        customer.stripeid = session.customer
        customer.membership = True
        customer.cancel_at_period_end = False
        customer.stripe_subscription_id = session.subscription
        customer.save()
    return render(request, 'success.html')




def subscription(request):
    try:
        if request.user.customer:
            return redirect('settings')
    except Customer.DoesNotExist:
        pass

    if request.method == 'POST':
        pass
    else:
        membership = 'monthly'
        final_inr = 199
        membership_id = 'price_1L014WSIeyPpwH6UCSmu151M'
        if request.method == 'GET' and 'membership' in request.GET:
            if request.GET['membership'] == 'yearly':
                membership = 'yearly'
                membership_id = 'price_1L014XSIeyPpwH6Uq2pNfJve'
                final_inr = 1999

        # Create Strip Checkout
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            customer_email = request.user.email,
            line_items=[{
                'price': membership_id,
                'quantity': 1,
            }],
            mode='subscription',
            allow_promotion_codes=True,
            success_url='http://127.0.0.1:8000/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='http://127.0.0.1:8000/cancel',
        )

        return render(request, 'subscription.html', {'final_inr': final_inr, 'session_id': session.id})




@login_required
def premium(request):
    return render( request , 'premium.html')

@login_required
def settings(request):
    membership = False
    cancel_at_period_end = False
    if request.method == 'POST':
        subscription = stripe.Subscription.retrieve(request.user.customer.stripe_subscription_id)
        subscription.cancel_at_period_end = True
        request.user.customer.cancel_at_period_end = True
        cancel_at_period_end = True
        subscription.save()
        request.user.customer.save()
    else:
        try:
            if request.user.customer.membership:
                membership = True
            if request.user.customer.cancel_at_period_end:
                cancel_at_period_end = True
        except Customer.DoesNotExist:
            membership = False
    return render(request, 'settings.html', {'membership':membership,
    'cancel_at_period_end':cancel_at_period_end})



def index(request):
    return render(request, 'indexpage.html')







def delete(request):
  stripe.Subscription.delete(stripe.Subscription.retrieve(request.user.customer.stripe_subscription_id))
  return HttpResponse("Cancelled succeffully")

#use this working updartion view
def modify(request):
 if request.method == 'GET' :
    subscription =  stripe.Subscription.retrieve(request.user.customer.stripe_subscription_id)

    stripe.Subscription.modify(
    subscription.id,
    cancel_at_period_end=False,
    proration_behavior='create_prorations',
    items=[{
        'id': subscription['items']['data'][0].id,
    
        'price': 'price_1L014XSIeyPpwH6Uq2pNfJve',
    
    }]
    )
    return render(request,'exit.html')
            
def downgrade(request):
 if request.method == 'GET' :
    subscription =  stripe.Subscription.retrieve(request.user.customer.stripe_subscription_id)

    stripe.Subscription.modify(
    subscription.id,
    cancel_at_period_end=False,
    proration_behavior='create_prorations',
    items=[{
        'id': subscription['items']['data'][0].id,
    
        'price': 'price_1L014WSIeyPpwH6UCSmu151M',
    
    }]
    )
    return render(request,'exit.html')








def pausepayments(request):
    customer_id= stripe.Subscription.retrieve(request.user.customer.stripe_subscription_id),
    stripe.Subscription.modify(
    request.user.customer.stripe_subscription_id,
    pause_collection={
        'behavior': 'mark_uncollectible',
   
    },
    )
    return HttpResponse("Successfully Paused")

def unpause(request):

        stripe.Subscription.modify(
        request.user.customer.stripe_subscription_id,
        pause_collection='',
        )
        return render(request,  "exit.html")


@login_required
def home(request):
    return render(request, 'customer_index.html')



def cancel(request):
    return render(request, 'cancel.html')



# @user_passes_test(lambda u: u.is_superuser)
def updateaccounts(request):
    customers = Customer.objects.all()
    for customer in customers:
        subscription = stripe.Subscription.retrieve(customer.stripe_subscription_id)
        if subscription.status != 'active':
            customer.membership = False
        else:
            customer.membership = True
        customer.cancel_at_period_end = subscription.cancel_at_period_end
        customer.save()
    return HttpResponse('completed')




@csrf_exempt
def create_checkout_session(request, id, ):

 premium = 'price_1L014XSIeyPpwH6Uq2pNfJve'
 basic = 'price_1L014WSIeyPpwH6UCSmu151M'
 if request.method == 'GET' :
    subscription =  stripe.Subscription.retrieve(request.user.customer.stripe_subscription_id)

    if subscription ==  request.user.customer.stripe_subscription_id :
        
        request_data = json.loads(request.body)
        product = get_object_or_404(Textiles, pk=id)

        stripe.api_key = STRIPE_SECRET_KEY
        checkout_session = stripe.checkout.Session.create(
            # Customer Email is optional,
            # It is not safe to accept email directly from the client side
            customer_email = request_data['email'],
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'inr',
                        'product_data': {
                        'name': product.product_model,
                        },
                        'unit_amount': int(product.price * 100),
                    },
                    'quantity': 1,
                }
            ],
            mode='payment',
            success_url='http://127.0.0.1:8000/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='http://127.0.0.1:8000/cancel',
            )
        # return JsonResponse({'data': checkout_session})
    return JsonResponse({'sessionId': checkout_session.id}) 