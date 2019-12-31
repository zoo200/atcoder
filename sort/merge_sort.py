def merge_sort(arr):
    if len(arr) <= 1:
        print("zzz",arr)
        return arr

    mid = len(arr) // 2
    # ここで分割を行う
    left = arr[:mid]
    right = arr[mid:]

    # 再帰的に分割を行う
    print("aaa",arr,left,right)
    left = merge_sort(left)
    print("bbb",arr,left,right)
    right = merge_sort(right)
    print("ccc",arr,left,right)

    # returnが返ってきたら、結合を行い、結合したものを次に渡す
    return merge(left, right)

def merge(left, right):
    merged = []
    l_i, r_i = 0, 0

    # ソート済み配列をマージするため、それぞれ左から見ていくだけで良い
    while l_i < len(left) and r_i < len(right):
        # ここで=をつけることで安定性を保っている
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    # 上のwhile文のどちらかがFalseになった場合終了するため、あまりをextendする
    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
    return merged

if __name__ == '__main__':
  array = [2, 5, 4, 3, 1,9, 6, 8, 7]
  print(array)
  merge_sort(array)
  print(merge_sort(array)) 
