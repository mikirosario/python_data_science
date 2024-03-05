import typing


def default_predicate(object: any) -> bool:
    '''Returns truthiness of object'''
    return bool(object)


def ft_filter(pred: typing.Callable[[typing.Any], bool] | None,
              iterable: typing.Iterable):
    '''Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items that are
    true.'''
    try:
        if pred is None:
            pred = default_predicate
        filter_generator = (x for x in iterable if pred(x))
        for element in filter_generator:
            yield element
    except Exception as ex:
        print(ex)
