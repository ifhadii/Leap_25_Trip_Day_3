from typing import List


def getSkyline(buildings: List[int]) -> List[int]:
    if not buildings:
        return []

    # Find the range of x-coordinates
    min_x = min(buildings[i] for i in range(0, len(buildings), 3))
    max_x = max(buildings[i + 1] for i in range(0, len(buildings), 3))

    result = []
    prev_height = 0

    for x in range(min_x, max_x + 1):
        max_height = 0
        for i in range(0, len(buildings), 3):
            start = buildings[i]
            end = buildings[i + 1]
            height = buildings[i + 2]
            if start <= x < end:
                max_height = max(max_height, height)

        if max_height != prev_height:
            result.append(x)
            result.append(max_height)
            prev_height = max_height

    return result