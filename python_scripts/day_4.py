from pathlib import Path

INPUT_LOCATION_PATH = Path('inputs/day_4.txt')
WORDS_OF_INTEREST = ['XMAS', 'SAMX']
WORDS_OF_INTEREST_2 = ['MAS', 'SAM']

def parse_input(fi: Path) -> list[list[str]]:
    input = []
    with fi.open() as f:
       for line in f.readlines():
            input.append([x for x in line if x != '\n'])
    return input

def find_word_of_interest_count(search: list[list[str]]) -> int:
    num_col = len(search[0])
    num_row = len(search)
    return (
        find_by_row(search, num_col, num_row) +
        find_by_col(search, num_col, num_row) +
        find_by_diag(search, num_col, num_row)
    )

def find_by_row(search: list[list[str]], num_col: int, num_row: int) -> int:
    found = 0
    for row in search:
        for idx in range(num_col-3):
            found += ''.join(row[idx:idx+4]) in WORDS_OF_INTEREST
    return found

def find_by_col(search: list[list[str]], num_col: int, num_row: int) -> int:
    found = 0
    for col in zip(*search):
        for idx in range(num_row-3):
            found += ''.join(col[idx:idx+4]) in WORDS_OF_INTEREST
    return found

def find_by_diag(search: list[list[str]], num_col: int, num_row: int) -> int:
    found = 0
    for row in range(num_row-3):
        for col in range(num_col-3):
            first_diag = ''.join([search[row][col],
                                  search[row+1][col+1],
                                  search[row+2][col+2],
                                  search[row+3][col+3]])
            second_diag = ''.join([search[row+3][col],
                                  search[row+2][col+1],
                                  search[row+1][col+2],
                                  search[row][col+3]])
            found += first_diag in WORDS_OF_INTEREST
            found += second_diag in WORDS_OF_INTEREST
    return found
            
def find_diag_x_mas(search: list[list[str]]) -> int:
    found = 0
    num_col = len(search[0])
    num_row = len(search)
    for row in range(num_row-2):
        for col in range(num_col-2):
            first_diag = ''.join([search[row][col],
                                search[row+1][col+1],
                                search[row+2][col+2]])
            second_diag = ''.join([search[row+2][col],
                                search[row+1][col+1],
                                search[row][col+2]])
            found += (first_diag in WORDS_OF_INTEREST_2 and second_diag in WORDS_OF_INTEREST_2)
    return found

if __name__ == '__main__':
    to_search = parse_input(INPUT_LOCATION_PATH)
    print(find_word_of_interest_count(to_search))
    print(find_diag_x_mas(to_search))