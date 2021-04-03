from typing import List

return_list = []
def solution(arr: List[int], divisor: int):
    for item in arr:
        if item % divisor == 0:
            return_list.append(item)
    return_list.sort()
    if not return_list:
        return_list.append(-1)
    return return_list


'''
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
https://programmers.co.kr/learn/courses/30/lessons/12910
'''