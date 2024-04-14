import sys
import ft_filter


def intify(object: any) -> tuple[bool, int]:
    '''Converts object into an integer. Returns a tuple containing a bool
    indicating whether the operation was successful and the successfully
    converted object or -1.'''
    try:
        integer = int(object)
        return (True, integer)
    except Exception:
        return (False, -1)


def validate_args() -> tuple[str, int]:
    '''Validates the arguments expected by the program'''
    string_punctuation: str = '!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~\\'
    err_str: str = "the arguments are bad"
    argc: int = len(sys.argv)
    assert argc == 3, err_str
    arg1: str = sys.argv[1]
    intification_result: tuple[bool, int] = intify(sys.argv[2])
    arg1_has_punc: bool = any(c in string_punctuation for c in arg1)
    arg2_is_int = intification_result[0]
    assert str.isprintable(arg1) and not arg1_has_punc and arg2_is_int, err_str
    return (arg1, intification_result[1])


def main():
    '''A program that accepts two arguments: a string(S), and an integer(N).
    The program outputs a list of words from S that have a length greater than
    N. The filter function it uses is custom-made for this exercise. ;)'''
    try:
        args: tuple[str, int] = validate_args()
        strArg: str = args[0]
        intArg: int = args[1]
        wordList: list[str] = strArg.split()
        filtList = ft_filter.ft_filter(lambda w: (len(w) > intArg), wordList)
        print(list(filtList))
    except AssertionError as ass_err:
        print(f'Assertion Error: {ass_err}')
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
