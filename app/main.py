from .calculator import add


def is_even(value: int) -> bool:
    return value % 2 == 0


def main() -> None:
    print("devops-platform-lab sample app")
    print("2 + 3 =", add(2, 3))
    print("4 is even?", is_even(4))


if __name__ == "__main__":
    main()
x = 1
