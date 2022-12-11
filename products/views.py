from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.db.models.functions import Lower
from .models import Product, Category

# Create your views here.

def products(request):
    products = Product.objects.all()
    categories = None
    sort = None
    direction = None
    
    
    if request.GET:
        
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            
            if sortkey == 'name': #alphabetical name sort
                sortkey == 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
                                             
            if sortkey == 'category': #alphabetical category sort
                sortkey = 'category__name'
                
            if 'direction' in request.GET: #direction sort
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
                    
        
        if 'category' in request.GET: #category filtering
            categories = request.GET['category'].split(',') 
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
    current_sorting = f'{sort}_{direction}'
    
    context={
        'products':products,
        'selected_categories':categories,
        'current_sorting':current_sorting,
        
    }
    print(categories)
    
    return render(request,'products.html',context)




def productInfo(request,product_id):
    product = get_object_or_404(Product, pk = product_id)
    
    context={
        'product':product
    }
    print(product.category.name)
    
    return render(request,'productInfo.html',context)