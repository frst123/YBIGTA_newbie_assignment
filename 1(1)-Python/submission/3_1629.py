# lib.py의 Matrix 클래스를 참조하지 않음
import sys


"""
TODO:
- fast_power 구현하기 
"""


def fast_power(base: int, exp: int, mod: int) -> int:
    """
    빠른 거듭제곱 알고리즘 구현
    분할 정복을 이용, 시간복잡도 고민!

    Args:
        base (int): 밑 (A)
        exp (int): 지수 (B)
        mod (int): 나누는 수 (C)

    Returns:
        int: (A^B) % C 결과값
    """
    #어떤 수의 0승은 1 
    if exp==0:
        return 1
    
    #Divide
    half = fast_power(base, exp//2, mod)
    if exp%2 == 0:
        return (half*half) % mod 
    else:
        return ((half * half) % mod) * (base % mod) % mod

    pass

def main() -> None:
    A: int
    B: int
    C: int
    A, B, C = map(int, input().split()) # 입력 고정
    
    result: int = fast_power(A, B, C) # 출력 형식
    print(result) 

if __name__ == "__main__":
    main()
