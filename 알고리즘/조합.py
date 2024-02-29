# arr=['A','B','C','D','E']
# n = 3
# for a in range(5):
#     start1 = a+1
#     for b in range(start1,5):
#         start2 = b+1
#         for c in range(start2,5):
#             print(arr[a],arr[b],arr[c])

#######################################
# path = []
# def fff(lev,start):
#     if lev == n:
#         print(path)
#         return
#     for i in range(start, 5):
#         path.append(arr[i])
#         fff(lev+1,i+1)
#         path.pop()
# fff(0,0)
#########################################
'''
주사위 세개
'''
arr=[i for i in range(1,7)]
n = 3

path = []
def fff(lev):
    if lev == n:
        print(*path)
        return
    for i in range(6):
        path.append(arr[i])
        fff(lev+1)
        path.pop()
    print()
fff(0)
############################################