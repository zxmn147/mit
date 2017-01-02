from django.shortcuts import render

# Create your views here.
def international(request):
    
    return render(request, 'international/international.html')