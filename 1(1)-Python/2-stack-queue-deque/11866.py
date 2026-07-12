from lib import create_circular_queue, rotate_and_remove


"""
TODO:
- josephus_problem 구현하기
    # 요세푸스 문제 구현
        # 1. 큐 생성
        # 2. 큐가 빌 때까지 반복
        # 3. 제거 순서 리스트 반환
"""


def josephus_problem(n: int, k: int) -> list[int]:
    """
    요세푸스 문제 해결
    n명 중 k번째마다 제거하는 순서 리스트 반환

    Args:
        n (int): 사람의 수
        k (int): 매번 제거할 k번째 위치

    Returns:
        list[int]: 사람들이 제거된 순서가 담긴 리스트
    """
    
    queue = create_circular_queue(n)
    result: list[int] = []

    while queue:
        removed_person = rotate_and_remove(queue, k)
        result.append(removed_person)
    return result 
    

def solve_josephus() -> None:
    """입, 출력 format"""
    n: int
    k: int
    n, k = map(int, input().split())
    result: list[int] = josephus_problem(n, k)
    
    # 출력 형식: <3, 6, 2, 7, 5, 1, 4>
    print("<" + ", ".join(map(str, result)) + ">")

if __name__ == "__main__":
    solve_josephus()