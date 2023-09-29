from django.shortcuts import render
from item.models import Category,Item

# Create your views here.
def index(request):
    items = Item.objects.filter(isSold = False)[:6] # Get the newest 6 items from the items
    categories = Category.objects.all() # Get all the avaliable categories
    return render(request, 'core/index.html',
                  {'categories': categories,
                      'items' : items,})
                  #These names point to above variables. They must be referenced for using in template

def contact(request):
    return render(request, 'core/contact.html')

