def seqsearch(n,S,X):
    location = 1
    while (location <= n and S[location] != x):
        location += 1
    if (location > n):
        location = 0
    return location

S = [0,10,7,11,5,13,8]

x = 5
location = seqsearch(len(S) - 1, S, x)
print('location =', location)

x = 4
location = seqsearch(len(S) - 1, S, x)
print('location=', location)

"""
- 문제 : 어떤 수 x가 n개의 수로 구성된 리스트 S에 존재하는가?
- 해답: x가 존재하면 x의 인덱스가, 존재하지 않으면 0이 해답
- 파라미터 : 정수n(>0), 리스트S(인덱스 범위는 1부터 n까지), 원소 x
- 입력 사례에 대한 해답 : location = 3
- 알고리즘 : 모든 x에 대해서 x의 인덱스를 찾아주는 단계별 절차
    - S의 첫번째 원소에서 시작하여 x를 찾을 때 까지(x가 없는 경우 끝까지)
    - 각 원소를 차례로 x와 비교한다.
    - 만약 x를 찾으면 x의 인덱스를 리턴하고,
    - x를 찾지 못하면 0을 리턴한다.
"""