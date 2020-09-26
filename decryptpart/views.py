from django.shortcuts import render

# Create your views here.

def enterform(request):
    return render(request, 'decryptpart/enterform.html')

def loginpage(request):
    return render(request, 'decryptpart/login.html')    

def login(request):
    if request.method=='POST':
        #check if a user exists
        #check if password exists
        uname=request.POST['username']
        pwd = request.POST['password']
        if uname=="General@123" and  pwd=="INDIA":
            return render(request, "decrypt/enterform.html")
        else:
            ret    


def output(request):
    s = request.POST["key"]
    key = request.POST["message"]
    s = input().strip()
    key = input().strip()
    def decode(s,key):
        s
        n = len(s)
        m = len(key)
        t = key
        n //=m
        mat = [[0]*(m+1) for i in range(n+1)]

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
                a+=matrix[i][j]
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
            if v[i]=="not" or v[i]=="not":
                flag = 1
        for i in range(len(v)):
            if v[i] in mp:
                mp[v[i]] = 0
        res = []
        if flag ==1:
            for key,val in mp:
                if val==1:
                    res.append(key)
        else:
            for key,val in mp.items():
                if val==0:
                    res.append(key)
    decode(s,key)

    ##return render(request, "decryptpart/outputform.html",  {'output':}) 