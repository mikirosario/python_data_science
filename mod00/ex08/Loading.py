# 158
def print_progress_bar(iteration, total, length=100, fill='█'):
    """Prints a progres bar iteration"""
    pct = "{:>3}".format("{0:.0f}".format(100 * (iteration / float(total))))
    filled_length = int(length * iteration // total)
    bar: str = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{pct}%|{bar}| {iteration}/{total}', end='')


def ft_tqdm(lst: range):
    """Runs a progress bar for a given range"""
    try:
        assert isinstance(lst, range), "Must Receive a Range"
        assert lst.start >= 0 and lst.stop > lst.start, "Invalid Range"
        total = len(lst)
        update_increment = 20

        for i, item in enumerate(lst, start=1):
            if i % update_increment == 0 or i == total:
                print_progress_bar(i, total)
            yield item
    except AssertionError as ass_err:
        print(f"Assertion Error: {ass_err}")
    except Exception as ex:
        print(f"{type(ex)}: {ex}")
