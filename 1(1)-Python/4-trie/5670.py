from lib import Trie
import sys


"""
TODO:
- 일단 Trie부터 구현하기
- count 구현하기
- main 구현하기
"""


def count(trie: Trie, query_seq: str) -> int:
    """
    trie - 이름 그대로 trie
    query_seq - 단어 ("hello", "goodbye", "structures" 등)

    returns: query_seq의 단어를 입력하기 위해 버튼을 눌러야 하는 횟수

    Args:
        trie (Trie): 단어들이 저장된 트라이 객체
        query_seq (str): 타이핑할 단어 문자열

    Returns:
        int: 버튼을 누르는 횟수
    """
    pointer = 0
    cnt = 0

    for element in query_seq:
        if len(trie[pointer].children) > 1 or trie[pointer].is_end:
            cnt += 1

        
        res_idx = trie.get_child_idx(pointer, element)
        if res_idx is not None:
            pointer = res_idx
        else:
            pointer = 0 

    return cnt + int(len(trie[0].children) == 1)


def main() -> None:
    """
    휴대폰 자판 전체 테스트 케이스 입력받아 평균 타이핑 횟수 출력 
    """
    #터미널의 모든 입력 읽어와 단어 단위로 쪼개 리스트 
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0

    while idx < len(input_data):
        n = int(input_data[idx]) #단어 개수 
        idx += 1
        
        words = []
        trie: Trie = Trie()
        
        for _ in range(n):
            word = input_data[idx]
            words.append(word)
            
            trie.push(word)
            idx += 1
            
        #각 단어마다 버튼을 몇번 누르는지 계산 
        total_clicks = 0
        for word in words:
            total_clicks += count(trie, word)
            
        #평균 
        average = total_clicks / n
        print(f"{average:.2f}")

if __name__ == "__main__":
    main()