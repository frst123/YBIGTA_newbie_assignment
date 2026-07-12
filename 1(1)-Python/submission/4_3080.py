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
- 일단 lib.py의 Trie Class부터 구현하기
- main 구현하기

힌트: 한 글자짜리 자료에도 그냥 str을 쓰기에는 메모리가 아깝다



"""


def main() -> None:
    """
    조건 만족하는 이름 순서 가짓수 계산해 출력 
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])  #이름의 수 N
    names = input_data[1:n+1] #이름 한줄에 하나씩 

    trie: Trie = Trie()
    for name in names:
        trie.push(name)

    MOD = 1_000_000_007

    fact = [1] * 3005
    for i in range(1, 3005):
        fact[i] = (fact[i-1] * i) % MOD
    
    ans = 1 

    for node in trie:
        choices = len(node.children)

        if node.is_end:
            choices += 1
        
        ans = (ans * fact[choices]) % MOD
    
    print(ans)

if __name__ == "__main__":
    main()