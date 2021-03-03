def filter(pool, papers):
    for i, question_tuple in enumerate(pool):
        if not (question_tuple[0] in papers):
            pool.pop(i)
    return pool
