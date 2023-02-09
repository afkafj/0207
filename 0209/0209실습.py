# 11장
# def scoreSort(ary) :
#     n = len(ary)
#     for end in range(1, n) :
#         for cur in range(end, 0, -1) :
#             if (ary[cur-1][1]>ary[cur][1]) :
#                 ary[cur-1], ary[cur]=ary[cur], ary[cur-1]
#     return ary

# scoreAry = [['선미', 88],['초아',99], ['화사', 71], ['영탁', 78], ['영웅', 67], ['민호', 92]]

# print('정렬 전-->', scoreAry)
# scoreAry = scoreSort(scoreAry)
# print('정렬 후 -->', scoreAry)

# print('##성적별 조 편성표##')
# for i in range(len(scoreAry)//2) :
#     print(scoreAry[i][0], ':', scoreAry[len(scoreAry)-1-i][0])

# 12장
# import random
# import time

# def selectionSort(ary) :
#     n = len(ary)
#     for i in range(0, n-1) :
#         minIdx = i
#         for k in range(i+1, n) :
#             if (ary[minIdx] > ary[k]) :
#                 minIdx = k
#         tmp = ary[i]
#         ary[i] = ary[minIdx]
#         ary[minIdx] = tmp

#     return ary

# def qSort(arr, start, end) :
#     if end <= start :
#         return
    
#     low = start
#     high = end

#     pivot = arr[(low + high) //2]
#     while low <= high :
#         while arr[low] < pivot :
#             low += 1
#         while arr[high] > pivot :
#             high -= 1
#         if low <= high :
#             arr[low], arr[high] = arr[high], arr[low]
#             low, high = low + 1, high - 1

#     mid = low

#     qSort(arr, start, mid-1)
#     qSort(arr, mid, end)

# def quickSort(ary) :
#     qSort(ary, 0, len(ary)-1)

# countAry = [1000, 10000, 12000, 15000]

# for count in countAry :
#     tempAry = [random.randint(10000,99999) for _ in range(count)]
#     selectAry = tempAry[:]
#     quickAry = tempAry[:]

#     print("##데이터 수 : ", count, "개")
#     start = time.time()
#     selectionSort(selectAry)
#     end = time.time()
#     print(" 선택 정렬 --> %10.3f 초" % (end-start))
#     start = time.time()
#     quickSort(selectAry)
#     end = time.time()
#     print(" 퀵 정렬 --> %10.3f초" % (end-start))
#     print()

#     count *=5


