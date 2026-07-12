from lib import create_circular_queue


"""
TODO:
- simulate_card_game 구현하기
    # 카드 게임 시뮬레이션 구현
        # 1. 큐 생성
        # 2. 카드가 1장 남을 때까지 반복
        # 3. 마지막 남은 카드 반환
"""


def simulate_card_game(n: int) -> int:
    """
    카드2 문제의 시뮬레이션
    맨 위 카드를 버리고, 그 다음 카드를 맨 아래로 이동

    Args:
        n (int): 카드의 총 개수 (1부터 n까지)

    Returns:
        int: 마지막까지 살아남은 카드의 번호
    """
    queue = create_circular_queue(n)
    while len(queue) > 1:
        queue.popleft()
        top_card = queue.popleft()
        queue.append(top_card)
        
    return queue.popleft()

def solve_card2() -> None:
    """입, 출력 format"""
    n: int = int(input())
    result: int = simulate_card_game(n)
    print(result)

if __name__ == "__main__":
    solve_card2()