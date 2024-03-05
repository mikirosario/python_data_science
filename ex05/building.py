import sys


def validation() -> str:
    '''Validates and returns user input. If input is invalid, an
    AssertionError exception is thrown.'''
    argc: int = len(sys.argv)
    assert argc < 3, "more than one argument is provided"
    if (argc < 2):
        return input("What is the text to count?\n")
    return sys.argv[1]


def main():
    '''Takes a single string argument and displays the sums of its upper-case
    characters, lower-case characters, punctuation characters, digits and
    spaces.'''
    try:
        string_punctuation: str = '!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~\\'
        user_input: str = validation()
        upper_count: int = sum(1 for c in user_input if c.isupper())
        lower_count: int = sum(1 for c in user_input if c.islower())
        punc_count: int = sum(1 for c in user_input if c in string_punctuation)
        space_count: int = sum(1 for c in user_input if c.isspace())
        digit_count: int = sum(1 for c in user_input if c.isdigit())
        total_count: int = len(user_input)
        print(f"""The text contains {total_count} characters:
              {upper_count} upper letters
              {lower_count} lower letters
              {punc_count} punctuation marks
              {space_count} spaces
              {digit_count} digits""")
    except AssertionError as ass_err:
        print(f'Assertion Error: {ass_err}')
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
