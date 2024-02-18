import datetime as dt
import sys

def format_ft_time():
    dateTime = dt.datetime.now()
    unixTime: float = dateTime.timestamp()
    print(f'Seconds since January 1, 1970: {"{0:,.4f}".format(unixTime)} or {"{:.2e}".format(unixTime)} in scientific notation')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("A la mierda, usuario de mierda. Va sin argumentos esto, ¿o qué te has creído tú?")
        exit(1)
    format_ft_time()

