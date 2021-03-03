def filter(pool, papers):
    newPool = []

    for i, question_tuple in enumerate(pool):
        print(question_tuple[0], (question_tuple[0] in papers))
        if (question_tuple[0] in papers):
            newPool.append(question_tuple)
    
    return newPool
