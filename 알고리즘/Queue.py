def enQ(a):
    global rear
    if rear == N - 1:
        print("Queue_Full")
    else:
        rear += 1
        q[rear] = a
def deQ():
    global front
    if front == rear:
        print("Queue_Empty")
    else:
        front += 1
        return q[front]
def Qpeek():  # front 다음 원소를 알 수 있게한다
    if front == rear:
        print("Queue_Empty")
    else:
        return q[front + 1]

N = 10
q = [0] * N  # 큐생성
front = rear = -1

for _ in range(3):
    n=int(input())
    rear+=1
    q[rear]=n
while front!=rear:
    front+=1
    print(q[front])