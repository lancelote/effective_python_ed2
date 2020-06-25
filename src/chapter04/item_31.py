from collections.abc import Iterator
from pathlib import Path
from typing import Generator, Iterable, List

DATA = Path("data")


def normalize(numbers: Iterable[int]) -> List[float]:
    assert not isinstance(numbers, Iterator), "must supply container"

    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


class ReadVisits:
    def __init__(self, data_path: Path) -> None:
        self.data_path = data_path

    def __iter__(self) -> Generator[int, None, None]:
        with open(self.data_path) as data_file:
            for line in data_file:
                yield int(line)


def main() -> None:
    # make sure cwd is project root for this to work
    visits = ReadVisits(DATA / "my_numbers.txt")
    percentages = normalize(visits)
    print(percentages)
    assert sum(percentages) == 100.0


if __name__ == "__main__":
    main()
