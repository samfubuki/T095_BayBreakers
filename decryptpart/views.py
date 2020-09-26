from django.shortcuts import render

# Create your views here.
def enterform(request):
    return render(request, 'decryptpart/enterform.html')