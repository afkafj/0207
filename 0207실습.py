# 큐
# def isQueueFull():
#     global SIZE, queue, front, rear
#     if (rear == SIZE-1) : 
#         return True
#     else :
#         return False
    
# def isQueueEmpty() :
#     global SIZE, queue, front, rear
#     if (front == rear) :
#         return True
#     else :
#         return False
    
# def enQueue(data) :
#     global SIZE, queue, front, rear
#     if (isQueueFull()) :
#         print("큐가 꽉 참")
#         return
#     rear += 1
#     queue[rear] = data

# def deQueue() :
#     global SIZE, queue, front, rear
#     if (isQueueEmpty()) :
#         print("큐가 빔")
#         return None
#     front += 1
#     data = queue[front]
#     queue[front] = None

#     for i in range(front+1, rear+1) :
#         queue[i-1]=queue[i]
#         queue[i]=None
#     front = -1
#     rear -= 1

#     return data


# def peek() :
#     global SIZE, queue, front, rear
#     if (isQueueEmpty()) :
#         print("큐가 빔")
#         return None
#     return queue[front+1]


# SIZE = 5
# queue = [None for _ in range(SIZE)]
# front = rear = -1


# if __name__ =="main" :
#     enQueue('정국') 
#     enQueue('뷔') 
#     enQueue('지민') 
#     enQueue('진') 
#     enQueue('슈가')
#     print("대기 줄 상태")

#     for _ in range(rear+1) :
#         print(deQueue(), '님 식당으로 들어감')
#         print("대기 줄 상태 :", queue)

#     print("식당 영업종료") 



# 이진 트리
# import random

# class TreeNode() :
#     def __init__ (self) :
#         self.left = None
#         self.data = None
#         self.right = None

# memory = []
# root = None
# dataAry = ['바나나맛 우유', '레쓰비', '츄파춥스', '도시락', '삼다수', '콜라', '삼각김밥']
# sellAry = [random.choice(dataAry) for _ in range(20)]

# print('오늘 판매된 물건(중복0) -->', sellAry)

# node = TreeNode()
# node.data = sellAry[0]
# root = node
# memory.append(node)

# for name in sellAry[1:] :

#     node = TreeNode()
#     node.data = name

#     current = root
#     while True :
#         if name == current.data :
#             if current.left == None :
#                 current.left = node
#                 memory.append(node)
#                 break
#             current = current.left
#         else :
#             if current.right == None :
#                 current.right == node
#                 memory.append(node)
#                 break
#             current = current.right

# print("이진 탐색 트리 구성 완료")

# def preorder(node) :
#     if node == None :
#         return
#     print(node.data, end = ' ')
#     preorder(node.left)
#     preorder(node.right)

# print('오늘 판매된 종류(중복X)-->', end = '  ')
# preorder(root)


