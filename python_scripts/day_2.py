from pathlib import Path

INPUT_LOCATION_PATH = Path('inputs/day_2.txt')

def parse_input(fi: Path) -> list[str]:
    with fi.open() as f:
        return f.readlines()

def is_report_safe(report: str) -> bool:
    is_increasing = None
    numbers = int(report.split())
    for idx in range(len(numbers)-1):
        diff = (numbers[idx] - numbers[idx+1])
        if abs(diff) == 0 or abs(diff) > 3:
            return False
        if is_increasing is None:
            is_increasing = (diff < 0)
            continue
        if is_increasing == (diff > 0): #was increasing but is now decreasing
            return False
    return True

if __name__ == "__main__":
    reports = parse_input(INPUT_LOCATION_PATH)
    reports_safety = [is_report_safe(report) for report in reports]
    print(f"Total Number of Safe Reports: {sum(reports_safety)}")
