from django.shortcuts import render, redirect
from django.contrib import messages
from queue import PriorityQueue
mp = {}
um = {}
arr = []
v = []


def dijkstra(src, end):
    d = {}
    for i in range(11):
        if arr[i] != src:
            d[arr[i]] = "1e9"
        else:
            d[arr[i]] = 0

    q = PriorityQueue()
    q.put(src)

    while q.qsize():
        k = q.get()
        for i in range(len(um[k])):
            z = um[k][i]
            w = mp[(k, z)]
            if (d[k]+w) < d[z]:
                d[z] = d[k]+w
                q.put(z)
    return d[end]


def main():
    arr.append("Khardung")
    arr.append("Lachulung")
    arr.append("Gyong")
    arr.append("Sasser")
    arr.append("Sia")
    arr.append("Zoji")
    arr.append("Indira")
    arr.append("Rezang")
    arr.append("Pensi")
    arr.append("Marsimik")
    arr.append("Tanglang")

    um["Khardung"] = "Lachulung"
    um["Khardung"] = "Gyong"
    um["Khardung"] = "Sasser"
    um["Lachulung"] = "Sia"
    um["Lachulung"] = "Khardung"
    um["Gyong"] = "Khardung"
    um["Gyong"] = "Zoji"
    um["Gyong"] = "Indira"
    um["Sasser"] = "Khardung"
    um["Sasser"] = "Zoji"
    um["Sasser"] = "Sia"
    um["Zoji"] = "Gyong"
    um["Zoji"] = "Sasser"
    um["Sia"] = "Lachulung"
    um["Sia"] = "Sasser"
    um["Sia"] = "Rezang"
    um["Indira"] = "Gyong"
    um["Indira"] = "Rezang"
    um["Rezang"] = "Sia"
    um["Rezang"] = "Indira"
    um["Rezang"] = "Tanglang"
    um["Rezang"] = "Pensi"
    um["Tanglang"] = "Rezang"
    um["Tanglang"] = "Marsimik"
    um["Pensi"] = "Rezang"
    um["Pensi"] = "Marsimik"
    um["Marsimik"] = "Tanglang"
    um["Marsimik"] = "Pensi"

    mp[("Khardung", "Lachulung")] = 1
    mp[("Lachulung", "Khardung")] = 1
    mp[("Khardung", "Sasser")] = 1
    mp[("Sasser", "Khardung")] = 1
    mp[("Khardung", "Gyong")] = 1
    mp[("Gyong", "Khardung")] = 1
    mp[("Lachulung", "Sia")] = 1
    mp[("Sia", "Lachulung")] = 1
    mp[("Gyong", "Indira")] = 1
    mp[("Indira", "Gyong")] = 1
    mp[("Gyong", "Zoji")] = 1
    mp[("Zoji", "Gyong")] = 1
    mp[("Sasser", "Sia")] = 1
    mp[("Sia", "Sasser")] = 1
    mp[("Sasser", "Zoji")] = 1
    mp[("Zoji", "Sasser")] = 1
    mp[("Sia", "Rezang")] = 1
    mp[("Rezang", "Sia")] = 1
    mp[("Indira", "Rezang")] = 1
    mp[("Rezang", "Indira")] = 1
    mp[("Rezang", "Tanglang")] = 1
    mp[("Tanglang", "Rezang")] = 1
    mp[("Rezang", "Pensi")] = 1
    mp[("Pensi", "Rezang")] = 1
    mp[("Tanglang", "Marsimik")] = 1
    mp[("Marsimik", "Tanglang")] = 1
    mp[("Pensi", "Marsimik")] = 1
    mp[("Marsimik", "Pensi")] = 1

    vans = []

    m = dict()

    for i in range(len(v)):
        m[v[i]] = 1
    mini = 10000
    ans1 = " "
    for i in range(11):
        if m.get(arr[i]) != None:
            continue

        sum = 0
        for j in range(len(v)):
            ans = dijkstra(arr[i], v[j])
            sum += ans
        if sum < mini:
            mini = sum
            vans.clear()
            vans.append(arr[i])
        elif sum == mini:
            vans.append(arr[i])
    for i in range(len(vans)):
        print(vans[i], end=" ")

# Create your views here.


def enterform(request):
    return render(request, 'decryptpart/enterform.html')


def loginpage(request):
    return render(request, 'decryptpart/login.html')


def login(request):
    if request.method == 'POST':
        # check if a user exists
        # check if password exists
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        if username == "General@123" and password == "INDIA":
           # messages.success(request, "You have been able to login successfully")
            return render(request, "decryptpart/enterform.html")

        else:
            messages.error(request, 'username or password not correct')
            return redirect(request, 'decryptpart/login.html')


def output(request):
    key = request.POST["key"]
    s = request.POST["message"]
    s = s.strip()
    key = key.strip()

    # print(s,key)
    # def decode(s,key):
    n = len(s)
    m = len(key)
    t = key
    n //= m
    mat = [["0"]*(m+1) for i in range(n+1)]

    cnt = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if ord(s[cnt]) == 32:
                mat[j][i] = "0"
            else:
                mat[j][i] = s[cnt]
            cnt += 1
    key = sorted(list(key))
    cnt = 0
    for i in range(1, m+1):
        mat[0][i] = key[cnt]
        cnt += 1
    key = t
    # print(mat)
    matrix = [[0]*(m+1) for i in range(n+1)]
    cnt = 1
    for i in range(m):
        for j in range(1, m+1):
            if key[i] == mat[0][j]:
                for k in range(1, n+1):
                    matrix[k][cnt] = mat[k][j]
                cnt += 1
    v = []

    cnt = 0
    a = ""
    for i in range(1, n+1):
        for j in range(1, m+1):
            if matrix[i][j] == "0" or matrix[i][j] == "_":
                v.append(a)
                a = ""
                continue
            a += matrix[i][j]
    print(v)
    mp = {}
    mp["Khardung"] = 1
    mp["Lachulung"] = 1
    mp["Gyong"] = 1
    mp["Sasser"] = 1
    mp["Zoji"] = 1
    mp["Sia"] = 1
    mp["Indira"] = 1
    mp["Rezang"] = 1
    mp["Tanglang"] = 1
    mp["Pensi"] = 1
    mp["Marsimik"] = 1
    flag = 0
    for i in range(len(v)):
        if v[i] in ["not", "Not"]:
            flag = 1
    for i in range(len(v)):
        if v[i] in mp:
            mp[v[i]] = 0
    res = []
    # print(mp)
    if flag == 1:
        for key in sorted(mp.keys()):
            if mp[key] == 1:
                res.append(key)
    else:
        for key in sorted(mp.keys()):
            if mp[key] == 0:
                res.append(key)
    x = " ".join(res)
    print(x)
    v = " ".join(v)
    
    #x = decode(s,key)
    dijkstra_vals = ['Gyong'] 
   
    #for i in range(len(res)-1):
        #dijkstra_vals.append(dijkstra(res[i], res[i+1]))    
      
    return render(request, "decryptpart/outputform.html",  {'output': x, 'message': v, 'dijkstra':dijkstra_vals})