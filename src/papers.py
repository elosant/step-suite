def filter(pool, papers):
    newPool = []

    for i, question_tuple in enumerate(pool):
        if (question_tuple[0] in papers):
            newPool.append(question_tuple)
    
    return newPool
