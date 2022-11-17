def merge_sort(list):
    n = len(list)  #n은 list의 길이값이다.

    if n <= 1:  #list의 요소값이 하나거나 없다면,
        return list  #list를 그대로 return한다.
    mid = (n + 1) // 2  #mid는 중간값이다. -> 중간을 기준으로 두 그룹으로 나눔
    g1 = merge_sort(list[:mid])  # 재귀 호출로 첫 번째 그룹을 정렬  처음 부터 mid 까지
    g2 = merge_sort(list[mid:])  # 재귀 호출로 두 번째 그룹을 정렬  mid + 1 부터 끝까지
    result, i, j = [], 0, 0  #result는 리스트이고, 첫 번째 그룹과 두 번째 그룹을 하나씩 result에 넣고, i와 j를 카운트로 쓰기 위해 변수선언한다.

    while i < len(g1) and j < len(g2):  #처음 반복일때, g1의 길이가 0보다 크고, g2의 길이가 0보다 클 때, 아래를 무한 반복해라.
        if g1[i] < g2[j]:  #g1의 첫 번째값(i 번째 값)이 g2의 첫 번째값(j 번째 값)보다 작다면,
            result.append(g1[i])  #g1의 첫 번째 값(i 번째 값)을 result에 넣어라.
            res.append(g1[i])  #g1의 첫 번째 값(i 번째 값)을 res에 넣어라.
            i += 1  #그리고 i에 1을 더해라.
        else:  #그렇지 않고, g1의 i 번째 값이 g2의 j 번째 값보다 크다면(중복이 없기에 같은 경우는 없음),(=g1의 요소값들이 작아서 하나씩 result와 res에 넣다가, result와 res 리스트가 오름차순이 되야하기 때문에 g1의 i번째 값이 g2보다 크다면 작은 g2의 값이 먼저 result와 res에 들어가야 한다.)
            result.append(g2[j])  #g2의 첫 번째 값(j 번째 값)을 result에 넣어라.
            res.append(g2[j])  #g2의 첫 번째 값(j 번째 값)을 result에 넣어라.
            j += 1  #그리고 j에 1을 더해라.

    result.extend(g1[i:])
    result.extend(g2[j:])

    res.extend(g1[i:])
    res.extend(g2[j:])

    return result


N, M = map(int, input().split())
arr = list(map(int, input().split()))
res = []

merge_sort(arr)
print(res[M - 1]) if len(res) >= M else print(-1)