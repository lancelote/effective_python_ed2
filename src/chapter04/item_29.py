def get_batches(count: int, size: int) -> int:
    return count // size


def main() -> None:
    stock = {
        "nails": 125,
        "screws": 35,
        "wingnuts": 8,
        "washers": 24,
    }
    order = ["screws", "wingnuts", "clips"]

    found = {
        name: batches
        for name in order
        if (batches := get_batches(stock.get(name, 0), 8))
    }

    print(found)


if __name__ == "__main__":
    main()
