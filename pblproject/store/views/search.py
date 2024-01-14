from django.shortcuts import render
from .models import Product

def search_view(request):
    query = request.GET.get('query')
    results = Product.objects.filter(title__icontains=query)
    context = {'results': results}
    return render(request, 'search_results.html', context)
