from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable


"""
TODO:
- Trie.push 구현하기
- (필요할 경우) Trie에 추가 method 구현하기
"""


T = TypeVar("T")


@dataclass
class TrieNode(Generic[T]):
    body: Optional[T] = None
    children: list[int] = field(default_factory=lambda: [])
    is_end: bool = False


class Trie(list[TrieNode[T]]):
    def __init__(self) -> None:
        super().__init__()
        self.append(TrieNode(body=None))

    def push(self, seq: Iterable[T]) -> None:
        """
        seq: T의 열 (list[int]일 수도 있고 str일 수도 있고 등등...)

        action: trie에 seq을 저장하기

        trie에 새로운 시퀸스 삽입
        Args:
            seq (Iterable[T]): 삽입할 데이터의 열 (예: 문자열 "cat")
        """
        current_idx = 0
        
        for element in seq:
            found_idx = None
            for child_idx in self[current_idx].children:
                if self[child_idx].body == element:
                    found_idx = child_idx
                    break
            if found_idx is None:
                new_node = TrieNode(body = element)
                self.append(new_node)
                found_idx = len(self) - 1
                self[current_idx].children.append(found_idx)

            current_idx = found_idx 
        
        self[current_idx].is_end = True 
    def get_child_idx(self, current_idx: int, element: T) -> Optional[int]:
        """
        현재 노드의 자식들 중 특정 글자 가진 자식노드의 인덱스 반환

        Args:
                current_idx (int): 현재 탐색 중인 노드의 인덱스 번호
                element (T): 찾고자 하는 다음 글자

            Returns:
                Optional[int]: 자식 노드의 인덱스 번호 (찾지 못하면 None)
        """
        for child_idx in self[current_idx].children:
            if self[child_idx].body == element:
                return child_idx
        return None 
    


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