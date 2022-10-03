def solution(x, y, d):
    return len(range(x, y, d))
    pass


if __name__ == "__main__":
    print(solution(10, 85, 30) == 3)
