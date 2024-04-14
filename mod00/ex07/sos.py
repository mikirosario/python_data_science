import sys


class MorseDictionary:
    """A Morse Dictionary"""
    NESTED_MORSE = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
                    'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
                    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                    'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
                    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
                    'y': '-.--', 'z': '--..', '0': '-----', '1': '.----',
                    '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                    ' ': '/'}

    def Morseify(self, string_to_translate: str) -> str:
        """Morseifies Things"""
        translator: str = (self.NESTED_MORSE[c] for c in string_to_translate)
        return " ".join(translator)


def validate_args() -> tuple[str, int]:
    '''Validates the arguments expected by the program'''
    argc: int = len(sys.argv)
    args_are_valid: bool = argc == 2 \
        and all(c.isalnum() or c.isspace() for c in sys.argv[1])
    assert args_are_valid, "the arguments are bad"


def main():
    '''A program that takes a string as an argument and encodes it into Morse
    Code.'''
    try:
        morse_dictionary = MorseDictionary()
        validate_args()
        print(morse_dictionary.Morseify(sys.argv[1].lower()))
    except AssertionError as ass_err:
        print(f'Assertion Error: {ass_err}')
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
