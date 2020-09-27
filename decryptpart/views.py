from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.

def enterform(request):
    return render(request, 'decryptpart/enterform.html')

def loginpage(request):
    return render(request, 'decryptpart/login.html')    

def login(request):
    if request.method=='POST':
        #check if a user exists
        #check if password exists
        username=request.POST['username']
        password = request.POST['password']
        print(username)
        if username=="General@123" and  password=="INDIA":
           # messages.success(request, "You have been able to login successfully")
            return render(request, "decryptpart/enterform.html")
           
        else:
            messages.error(request,'username or password not correct')
            return redirect(request,'decryptpart/login.html')   
           


def output(request):
    key = request.POST["key"]
    s = request.POST["message"]
    s = s.strip()
    key = key.strip()

    # print(s,key)
    #def decode(s,key):
    n = len(s)
    m = len(key)
    t = key
    n //=m
    mat = [["0"]*(m+1) for i in range(n+1)]

    cnt = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if ord(s[cnt])==32:
                mat[j][i] = "0"
            else:
                mat[j][i] = s[cnt]
            cnt+=1
    key = sorted(list(key))
    cnt = 0
    for i in range(1,m+1):
        mat[0][i] = key[cnt]
        cnt+=1
    key = t
    # print(mat)
    matrix = [[0]*(m+1) for i in range(n+1)]
    cnt = 1
    for i in range(m):
        for j in range(1,m+1):
            if key[i]==mat[0][j]:
                for k in range(1,n+1):
                    matrix[k][cnt]=mat[k][j]
                cnt+=1
    v = []

    cnt = 0
    a = ""
    for i in range(1,n+1):
        for j in range(1,m+1):
            if matrix[i][j]=="0" or matrix[i][j]=="_":
                v.append(a)
                a = ""
                continue
            a+=matrix[i][j]
    print(v)        
    mp = {}
    mp["Khardung"]=1
    mp["Lachulung"]=1
    mp["Gyong"]=1
    mp["Sasser"]=1
    mp["Zoji"]=1
    mp["Sia"]=1
    mp["Indira"]=1
    mp["Rezang"]=1
    mp["Tanglang"]=1
    mp["Pensi"]=1
    mp["Marsimik"]=1
    flag = 0
    for i in range(len(v)):
        if v[i] in ["not", "Not"]:
            flag = 1
    for i in range(len(v)):
        if v[i] in mp:
            mp[v[i]] = 0
    res = []
    # print(mp)
    if flag ==1:
        for key in sorted(mp.keys()):
            if mp[key] ==1:
                res.append(key)
    else:
        for key in sorted(mp.keys()):
            if mp[key]==0:
                res.append(key)
    x = " ".join(res) 
    print(x)
    v = " ".join(v)
    #x = decode(s,key)         

    return render(request, "decryptpart/outputform.html",  {'output':x,'message':v}) 