questionTuplePool = []

for paper in range(1,4):
    for year in range(1987, 2018):
        question_range = None

        if year in range(1987, 1994):
            question_range = range(1, 17)
        elif year in range(1994, 2008):
            question_range = range(1, 15)
        elif year in range(2008, 2019):
            question_range = range(1, 14)

        for question in question_range:
            questionTuplePool.append((paper, year, question))
