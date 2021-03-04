import question

def filter(pool, searches):
    if "all" in searches:
        return pool

    filteredPool = []

    for i, question_tuple in enumerate(pool):
        temp_question = question.Question(*question_tuple)
        for j, search in enumerate(searches):
            if temp_question.tex.lower().find(search.lower()) != -1:
                filteredPool.append(question_tuple)
                continue

            

    return filteredPool
