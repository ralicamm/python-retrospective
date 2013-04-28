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
    for i in range(0, len(iterables)):
        args = []
        for iterable in iterables:
            if i == len(iterable):
                return
            args.append(iterable[i])
        yield func(*args)
        i += 1


def cache(func, cache_size):
    cached_items = []

    def func_cached(x):
        result = [func_result for (arg, func_result) in cached_items
                  if arg == x]
        if [] != result:
            return result[0]
        result = func(x)
        if len(cached_items) == cache_size:
            cached_items.remove(cached_items[0])
        cached_items.append((x, result))
        return result
    return func_cached
