from lib import Trie
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