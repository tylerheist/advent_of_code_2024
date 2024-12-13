from pathlib import Path
from collections import Counter

INPUT_LOCATION_PATH = Path('inputs/day_1.txt')

def parse_input(fi: Path) -> list[list[int]]:
    left_list, right_list = [], []
    with fi.open() as f:
        for line in f:
            left_list.append(int(line.split()[0].strip()))
            right_list.append(int(line.split()[1].strip()))
    return [left_list, right_list]

def find_total_distance(left_list, right_list) -> int:
    left_list.sort()
    right_list.sort()
    distances = [abs(left_list[x] - right_list[x]) for x in range(len(left_list))]
    return sum(distances)

def calculate_similarity_score(left_list, right_list) -> int:
    count_right = Counter(right_list)
    similarity_score = 0
    for item in left_list:
        similarity_score += item * count_right[item]
    return similarity_score

if __name__ == "__main__":
    lists = parse_input(INPUT_LOCATION_PATH)
    print(f"Total Distance: {find_total_distance(lists[0], lists[1])}")
    print(f"Similarity Score: {calculate_similarity_score(lists[0], lists[1])}")