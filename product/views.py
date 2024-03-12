from django.shortcuts import get_object_or_404
from .models import Product, Category
from django.views.generic import ListView, DetailView
from django.http import HttpResponse,JsonResponse
from .cart import Cart

def cart_summary(request):
    return HttpResponse("hi there")
# def cart_add(request):
#     cart=Cart(request)
#     print(request.POST)
#     if request.POST.get('action') == 'post':
#         product_id = int(request.Post.get('product_id'))
#         print(product_id)
    
#         return JsonResponse({"product_id":product_id})
#     return HttpResponse("hi there")
def cart_add(request):
    cart=Cart(request)
    if request.POST.get('action')=='post':
        product_id=int(request.POST.get('product_id'))
        product=get_object_or_404(Product,id=product_id)

        cart.add(product=product)

        return JsonResponse({"product_id":str(product_id)})


    return HttpResponse('salom')



def cart_delete(request):
    return HttpResponse("hi there")
def cart_update(request):
    return HttpResponse("hi there")



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

