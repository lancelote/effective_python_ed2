def slice_bananas(count: int) -> int:
    return 10 * count


def make_smoothies(pieces: int) -> str:
    return f"{pieces} smoothies"


def make_cider(count: int) -> str:
    return f"{count} cider"


def make_lemonade(count: int) -> str:
    return f"{count} lemonade"


def main() -> None:
    fresh_fruit = {
        "apple": 10,
        "banana": 8,
        "lemon": 5,
    }

    if (count := fresh_fruit.get("banana", 0)) >= 2:
        pieces = slice_bananas(count)
        to_enjoy = make_smoothies(pieces)
    elif (count := fresh_fruit.get("apple", 0)) >= 4:
        to_enjoy = make_cider(count)
    elif count := fresh_fruit.get("lemon", 0):
        to_enjoy = make_lemonade(count)
    else:
        to_enjoy = "nothing"

    print(to_enjoy)


if __name__ == "__main__":
    main()
