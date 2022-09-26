
def solution(A):
    q = 1
    while True:
        if q not in set(A):
            return q
        else:
            q += 1

    # write your code in Python 3.6
    pass



if __name__ == '__main__':
    A = [1, 3, 6, 4, 1, 2]
    print(solution(A))

    B = [1, 2, 3]
    print(solution(B))

    C = [-1, -3]
    print(solution(C))

