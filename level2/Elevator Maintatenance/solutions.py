def solution(l):
    # sort with rules
    # we will use merge sort here
    def compare(l, i1, i2):
        # return the index with smaller value
        l1 = l[i1]
        l2 = l[i2]
        def extract(s):
            res = ""
            while (s!=""):
                res += s[0]
                s = s[1:]
                if(s==""):
                    return int(res) if res!="" else -1,s
                elif(s[0]=="."):
                    s = s[1:]
                    return int(res) if res!="" else -1 ,s
            #s==""
            return -1, s

        counter = 0
        while (True):
            while (counter == 4):
                return
            v1,l1 = extract(l1)
            v2,l2 = extract(l2)

            if (v1 == -1):
                return i1
            if (v2 == -1):
                return i2

            if (v1 < v2):
                return i1
            if (v2 < v1):
                return i2

    def merge(l, low, high):
        # high is the not included
        if (high - low <= 1):
            return

        mid = (low + high) // 2
        merge(l, low, mid)
        merge(l, mid, high)

        merge_sort(l, low, mid, high)

    def merge_sort(l, low, mid, high):
        ind = low
        i = low
        j = mid
        aux = []
        for e in l:
            aux.append(e)

        while (i < mid or j < high):
            if (i == mid):
                l[ind] = aux[j]
                j += 1
            elif (j == high):
                l[ind] = aux[i]
                i += 1
            elif (compare(aux, i, j) == i):
                l[ind] = aux[i]
                i += 1
            else:
                l[ind] = aux[j]
                j += 1

            ind += 1

    merge(l,0,len(l))

    return l