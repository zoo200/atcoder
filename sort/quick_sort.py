def quick_sort(array):
    if len(array) <= 1:
        print('ccc',array)
        return array

    # ピボット
    p = array[len(array)//2]
    l = 0
    r = len(array) -1

    while (l < r):
        print('aaa',array,array[l],array[r],l,r,p)
        # ピボットより小さい値を左、大きい値を右に移動する
        while array[l] < p:
            print('bbb',array,array[l],array[r],l,r,p)
            l += 1
        while p < array[r]:
            print('ccc',array,array[l],array[r],l,r,p)
            r -= 1
        if (l >= r):
            print('ddd',array,array[l],array[r],l,r,p)
            break

        # 見つかった要素を交換
        print('eee',array,array[l],array[r],l,r,p)
        array[l],array[r] = array[r],array[l]
        print('fff' ,array)

    # 左右に分けた部分を再帰的にクイックソート
    print('ggg',array[:l])
    array[:l] = quick_sort(array[:l])
    print('hhh',array[l:])
    array[l:] = quick_sort(array[l:])

    return array

a = [3,2,1,4,5,9,6,8,7]
print(a)
j= quick_sort(a)
print(j)
