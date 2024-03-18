from typing import List, Tuple

def is_valid_colouring(N: int, E: List[Tuple[int, int]], C: List[int]) -> bool:
    for i in E:
        if (C[i[0]] + C[i[1]]) % 2 != 0:
            return False
    return True


assert is_valid_colouring(4, [[0, 1], [0, 2], [2, 3]], [5, 7, 3, 1])
print(is_valid_colouring(4, [[0, 1], [0, 2], [2, 3]], [5, 7, 3, 1]))