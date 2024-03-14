from django.shortcuts import get_object_or_404,render
from .models import Product, Category
from django.views.generic import ListView, DetailView
from django.http import HttpResponse,JsonResponse
from .cart import Cart

def cart_summary(request):
    cart = Cart(request)
    products = cart.get_products()
    quantity = cart.get_quantity()
    total = cart.get_total_price()
    
    data = {
        "products":products,
        "quantities":quantity,
    }


    return render(request, 'product/cart_summary.html',context=data)

def cart_add(request):
    cart = Cart(request)

    

    if request.method == 'POST' and request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('product_quantity', 1))    
        
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=quantity)

        return JsonResponse({"product_id": product_id})

    return HttpResponse('Invalid Request')


def cart_delete(request):
    return HttpResponse("hi there")
def cart_update(request):
    return HttpResponse("hi there")

def about(request):
    return render(request, 'product/about.html')



class ProductListView(ListView):
    model = Product
    template_name = 'product/index.html'
    context_object_name = 'products'


class CategoryProductsList(DetailView):
    model = Category
    template_name = 'product/index.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context['products'] = category.products.all()
        return context
    


class  ProductDetailView(DetailView):
    model=Product
    template_name='product/detail.html'
    context_object_name='product'


