from django.shortcuts import render
from django.utils.timezone import datetime
from customer.models import OrderModel
from django.views import View
# Create your views here.


class Dashboard(View):
    def get(self, request, *args, **kwargs):
        # get the current date
        today = datetime.today()
        
        orders = OrderModel.objects.filter(created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)

        # loop through the orders and add price value, check if order is not shipped

        unshipped_orders = []
        total_revenue = 0
        for order in orders:
            total_revenue += order.price
            
            if not order.is_shipped:
                unshipped_orders.append(order)
        # pass total number of order and total revenue to template
        context = {
            'orders': unshipped_orders,
            'total_revenue': total_revenue,
            'total_orders': len(orders)
        }
        return render(request, "dashboard.html", context)

class OrderDetails(View):
    def get(self,request,pk,*args,**kwargs):
        order = OrderModel.objects.get(pk=pk)
        context = {
            'order' :order
        }
        
        return render(request,'order_details.html', context )
    def post(self,request,pk,*args,**kwargs):
        order = OrderModel.objects.get(pk=pk)
        order.is_shipped = True
        order.save()
        
        context = {
            'order':order
        }
        
        
        return render(request, 'order_details.html', context)
    