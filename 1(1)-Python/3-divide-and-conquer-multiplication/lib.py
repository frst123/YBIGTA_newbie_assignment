from __future__ import annotations
import copy


"""
TODO:
- __setitem__ 구현하기
- __pow__ 구현하기 (__matmul__을 활용해봅시다)
- __repr__ 구현하기
"""


class Matrix:
    MOD = 1000

    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix = matrix

    @staticmethod
    def full(n: int, shape: tuple[int, int]) -> Matrix:
        return Matrix([[n] * shape[1] for _ in range(shape[0])])

    @staticmethod
    def zeros(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(0, shape)

    @staticmethod
    def ones(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(1, shape)

    @staticmethod
    def eye(n: int) -> Matrix:
        matrix = Matrix.zeros((n, n))
        for i in range(n):
            matrix[i, i] = 1
        return matrix

    @property
    def shape(self) -> tuple[int, int]:
        return (len(self.matrix), len(self.matrix[0]))

    def clone(self) -> Matrix:
        return Matrix(copy.deepcopy(self.matrix))

    def __getitem__(self, key: tuple[int, int]) -> int:
        return self.matrix[key[0]][key[1]]

    def __setitem__(self, key: tuple[int, int], value: int) -> None:
        """
        행렬의 (행, 열)에 값을 저장

        Args:
            key (tuple[int, int]): (행, 열) 인덱스 튜플
            value (int): 저장할 정수 값
        """
        
        self.matrix[key[0]][key[1]] = value
        

    def __matmul__(self, matrix: Matrix) -> Matrix:
        x, m = self.shape
        m1, y = matrix.shape
        assert m == m1

        result = self.zeros((x, y))

        for i in range(x):
            for j in range(y):
                for k in range(m):
                    result[i, j] += self[i, k] * matrix[k, j]
                result[i, j] %= self.MOD
        return result

    def __pow__(self, n: int) -> Matrix:
        """
        divide/conquer로 행렬 거듭제곱 계산
        
        Args:
            n (int): 제곱할 지수 (B)

        Returns:
            Matrix: (Matrix^B) 1000으로 나눈 나머지가 반영된 결과 행렬
        """
        if n == 1:
            res = self.clone()
            for i in range(res.shape[0]):
                for j in range(res.shape[1]):
                    res[i, j] %= self.MOD
            return res

        # divide 
        half = self.__pow__(n // 2)
        half_squared = half @ half 

        # conquer
        if n % 2 == 0:
            return half_squared
        else:
            return half_squared @ self

    def __repr__(self) -> str:
       """
       행렬을 문자열 형식으로 변환
       Returns:
            str: 줄바꿈과 공백으로 정렬된 행렬 문자열
       """
       lines = []
       for row in self.matrix:
        lines.append(' '.join(map(str, row)))

        return '\n'.join(lines)
        