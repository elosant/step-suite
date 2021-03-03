import question

def filter(pool, categories):
    if "all" in categories:
        return pool

    for i, category in enumerate(categories):
        categories[i] = question.Question.questionCategory[category]

    filteredPool = []

    for i, question_tuple in enumerate(pool):
        temp_question = question.Question(*question_tuple, initGetTex=False)
        if temp_question.category in categories:
            filteredPool.append(question_tuple)

    return filteredPool


