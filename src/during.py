def filter(pool, during):
    assert(len(during) in range(1, 3), "Invalid argument passed to --during!")

    interval = None
    if len(during) == 1:
        interval = range(during[0], during[0]+1)
    elif len(during) == 2:
        interval = range(during[0], during[1])

    filteredPool = []

    for question_tuple in pool:
        if question_tuple[1] in interval:
            filteredPool.append(question_tuple)

    return filteredPool
