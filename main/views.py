from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Products, Orders
from django.http import HttpRequest, HttpResponse
from .forms import UserForm
from django.contrib.auth import authenticate, login

# Create your views here.


class HomeView(ListView):
    model = Products
    template_name = 'Home.html'


class ProductView(DetailView):
    pass


def productDetails(request, pk):

    prod = Products.objects.filter(id=pk)

    context = {
        'product': prod

    }
    cnt = Orders.objects.filter(user=request.user, status=False).count()

    context['count'] = cnt

    return render(request, 'product.html', context)
    # return HttpResponse(f'product details of{pk}')


def loginpage(request):

    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        print(uname)
        print(pwd)
        valid = authenticate(request, username=uname, password=pwd)

        if valid is not None:
            login(request, valid)
            return redirect('Home')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):

    if request.method == 'POST':
        user = UserForm(request.POST)

        if user.is_valid():
            user.save()

            return redirect('login')
        else:
            return HttpResponse('Invalid details')
    else:
        uForm = UserForm()
        context = {'form': uForm}
        return render(request, 'register.html', context)


def cart(request, name):
    print(name)
    print('Cart called')
    context = {}

    products = Products.objects.all()

    context['object_list'] = products

    cnt = Orders.objects.filter(user=request.user, status=False).count()

    context['count'] = cnt

    if request.method == 'POST':

        valid_prd = Products.objects.filter(name=name)

        if valid_prd is not None:
            ord = Orders()
            ord.user = request.user
            ord.order_id = 1
            ord.item = Products.objects.get(name=name)
            ord.status = False

            #Orders.objects.create(request.user, 1, name, False)
            ord.save()

    return render(request, 'Home.html', context)

    def order_cnt(request):

        return Orders.objects.filter(user=request.user, status=False).count()
