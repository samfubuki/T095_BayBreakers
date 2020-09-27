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


if __name__ == "__main__":
    main()
