import json
from django.shortcuts import render
from django.views import View
from django.db.models import Q
from django.core.mail import send_mail
from .models import MenuItem, category, OrderModel

# Create your views here.


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')


class Order(View):
    def get(self, request, *args, **kwargs):
        appetizers = MenuItem.objects.filter(category__name__contains='Appetizer')
        entres = MenuItem.objects.filter(category__name__contains='Entre')
        desserts = MenuItem.objects.filter(category__name__contains='Dessert')
        drinks = MenuItem.objects.filter(category__name__contains='Drink')

        context = {
            'appetizers': appetizers,
            'entres': entres,
            'desserts': desserts,
            'drinks': drinks,
        }

        return render(request, 'order.html', context)

    def post(self, request, *args, **kwargs):
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        
            
        order_items = {
            'items': []
        }
        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)

            price = 0
            item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(price = price, name = name, email = email, street = street, city = city, state = state, zip_code = zip_code)
           
        #order.save()
        order.items.add(*item_ids)
        
        body = ('Thank You for your order! your food is being made and will be deliver soon!\n'
            f'your total price:{price}\n'
            'Thank you again for your order')
        
        send_mail(
            'Thank you for your order!',
            body,
            'example@example.com',
            [email],
            fail_silently=False
        )
                

        context = {
            'items': order_items['items'],
            'price': price
        }

        return render(request, 'order_confirmation.html', context)


class Menu(View):
    def get(self,request,*args,**kwargs):
        menu_items= MenuItem.objects.all()
        
        context = {
            'menu_items':menu_items
        }
        
        return render(request,'menu.html',context)
    
class MenuSearch(View):
    def get(self,request,*args,**kwargs):
        query = self.request.GET.get("q")
        menu_items = MenuItem.objects.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query) |
            Q(description__icontains=query)
        )

        context = {
            'menu_items' : menu_items
        }
        
        return render(request,'menu.html', context)