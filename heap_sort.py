def max_heapify(array, n, i):
  # ルート array[i]
  # とりあえずルートが最大
  largest = i
  l  = 2 * i
  r = 2*  i + 1
  
  # 左側の子がルートより大きい場合
  if l < n and array[i] < array[l]:
    print("lll" ,l,array[i],array[l])
    largest = l
  
  # 右側の子がルートよりも左側よりも大きい場合
  if r < n and array[largest] < array[r]:
    print("rrr" ,r,array[largest] , array[r])
    largest = r
  
  # ルート以外がルートより大きい場合は入れ替え
  if largest != i:
    array[i], array[largest] = array[largest], array[i]
    # 入れ替えのあったsubtreeでmax-heapを満たすようにheapifyを行う
    print("kkk",array, n, largest)
    max_heapify(array, n, largest)

def heap_sort(array):
  n = len(array)
  # max-heapを作る
  for i in range(n//2, -1, -1):
    print ("xxx",array,n,i)
    max_heapify(array, n, i)
  
  print ("yyy",array,n,i)

  for i in range(n-1, 0, -1):
    print ("sss",array,n,i)
    array[i], array[0] = array[0], array[i]
    print ("ppp",array,n,i)
    max_heapify(array, i, 0)

  print ("zzz",array,n,i)

if __name__ == '__main__':
  array = [2, 5, 4, 3, 1,9, 6, 8, 7]
  print(array)
  heap_sort(array)
  print(array) 
