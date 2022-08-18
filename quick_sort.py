def quick_sort(arr):
    length=len(arr)
    if length<=1:
        return arr
    else:
        pivot = arr.pop()


    smaller_items=[]
    greater_items=[]

    for item in arr:
        if item<pivot:
            smaller_items.append(item)

        else:
            greater_items.append(item)

    return quick_sort(smaller_items) + [pivot] + quick_sort(greater_items)

print(quick_sort([60,40,20,10,50,30,0,12,11]))

