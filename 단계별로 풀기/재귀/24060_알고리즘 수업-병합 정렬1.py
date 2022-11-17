import sys

input = sys.stdin.readline


def merge_sort(L):
    if len(L) == 1:  #주어진 값, L리스트에 있는 요소값이 하나 뿐이라면,
        return L  #그대로 리스트를 return한다.

    mid = (len(L) + 1) // 2  #mid는 L리스트의 중앙값이다.(=L리스트 길이에 1을 더한 값을 2로 나눈 값의 정수부분이다.)

    left = merge_sort(L[:mid])  #left는 L의 0번째 ~ 중앙값까지 포함한 리스트를 merge_sort함수로 return한 값이다.
    right = merge_sort(L[mid:])  #right는 L의 중앙값 + 1번째 ~ 마지막값까지 포함한 리스트를 merge_sort함수로 return한 값이다.

    i, j = 0, 0
    L2 = []
    while i < len(left) and j < len(right):  #left가 merge_sort함수를 처음 돌릴 때, left의 길이와 right의 길이가 0보다 크면 아래를 무한 반복해라.
        if left[i] < right[j]:  #left의 첫 번째 값이 right의 첫 번째값보다 작으면,
            L2.append(left[i])  #L2 리스트에 left의 첫 번째 값을 넣어라.
            ans.append(left[i])  #ans 리스트에 left의 첫 번째 값을 넣어라.
            i += 1  #그리고, i에 1을 더해라.
        else:  #그렇지 않고, right의 첫 번째값이 크거나 같다면,
            L2.append(right[j])  #L2 리스트에 right의 첫 번째값을 넣어라.
            ans.append(right[j])  #ans 리스트에 right의 첫 번째값을 넣어라.
            j += 1  #그리고, j에 1을 더해라.
    while i < len(left):  #left의 길이만 0보다 크다면,
        L2.append(left[i])  #L2 리스트에 left의 첫 번째값을 넣어라.
        ans.append(left[i])  #ans 리스트에 right의 첫 번째값을 넣어라.
        i += 1  #그리고, j에 1을 더해라.
    while j < len(right):  #right의 길이만 0보다 크다면,
        L2.append(right[j])  #L2 리스트에 right의 첫 번째값을 넣어라.
        ans.append(right[j])  #ans 리스트에 right의 첫 번째값을 넣어라.
        j += 1  #그리고, j에 1을 더해라

    return L2


n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = []
merge_sort(a)

if len(ans) >= k:
    print(ans[k - 1])
else:
    print(-1)