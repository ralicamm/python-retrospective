from collections import OrderedDict


def groupby(func, seq):
    dictionary = {}
    items = [(func(x), x) for x in seq]
    for key, value in items:
        if key not in dictionary.keys():
            dictionary[key] = [value]
        else:
            dictionary[key].append(value)
    return dictionary


def composition(func1, func2):
    return lambda x: func1(func2(x))


def iterate(func):
    composition_func = lambda x: x
    while True:
        yield composition_func
        composition_func = composition(composition_func, func)


def zip_with(func, *iterables):
    if len(iterables) == 0:
        return
    iterators = [iter(i) for i in iterables]

    while True:
        args = [next(it) for it in iterators]
        if len(iterables) != len(args):
            return
        yield func(*args)


def cache(func, cache_size):
    if cache_size <= 0:
        return func
    cached_items = OrderedDict()

    def func_cached(*args):
        if args not in cached_items:
            result = func(*args)
            if len(cached_items) == cache_size:
                cached_items.popitem(False)
            cached_items[args] = result
        return cached_items[args]
    return func_cached
