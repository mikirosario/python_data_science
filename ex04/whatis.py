import sys


def intify(object: any) -> tuple[bool, int]:
    try:
        integer = int(object)
        return (True, integer)
    except Exception:
        return (False, -1)


if __name__ == "__main__":
    sys.tracebacklimit = 0
    argc = len(sys.argv)
    if argc < 2:
        exit(-1)
    assert argc < 3, "more than one argument is provided"
    result: tuple[bool, int] = intify(sys.argv[1])
    assert result[0] is True, "argument is not an integer"
    arg = result[1]
    isEven = arg % 2 == 0
    print(f"I'm {'Even' if isEven else 'Odd'}.")
