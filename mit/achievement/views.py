from django.shortcuts import render

# Create your views here.
def achievement(request):
    
    return render(request, 'achievement/achievement.html')