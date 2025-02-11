from typing import List
def generatePascalsTriangle(numRows: int) -> List[int]:
    if numRows == 0:
        return []

    triangle = [1]

    for i in range(1, numRows):
        current_row = [1]
        for j in range(1, i):
            current_row.append(triangle[-i + j] + triangle[-i + j - 1])
        current_row.append(1)
        triangle.extend(current_row)

    return triangle

print(generatePascalsTriangle(5))