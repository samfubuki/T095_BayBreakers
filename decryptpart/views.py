from django.shortcuts import render

# Create your views here.
def enterform(request):
    return render(request, 'decryptpart/enterform.html')

def output(request):
    var1 = request.POST["key"]
    print(var1)
    var2 = request.POST["message"]
    print(var2)
    var3=var1+var2
    return render(request, "decryptpart/outputform.html",  {'output':var3}) 