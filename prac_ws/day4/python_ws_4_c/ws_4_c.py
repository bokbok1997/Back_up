matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
# 아래애 코드를 작성하시오.
matrix_len = 0
temporary_len = 0

for cnt in matrix:
    matrix_len+=1

print (matrix_len)

for cnt1 in range(matrix_len):
    temporary_len = 0
    for cnt2 in matrix[cnt1]:
        temporary_len+=1
    if temporary_len <= 4:
        print(f'{matrix[cnt1]}리스트는 {temporary_len}개 만큼 요소를 가지고 있습니다.')

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        print(f'\'matrix\'의 {x},{y}번째 요소의 값은 {matrix[x][y]}입니다.')
