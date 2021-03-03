import pyexcel_ods as pe

def filter(pool, mark_range, spreadsheet_name):
    spreadsheet = pe.get_data(spreadsheet_name)

    spreadsheet_pool = []
    for name, sheet in spreadsheet.items():
        paper = int(name[-1])
        for i, row in enumerate(sheet):
            for j, entry in enumerate(row):
                try:
                    year = int(row[0])
                    question_number = int(sheet[1][j])

                    if entry == "":
                        entry = -1
                    elif entry == "?":
                        entry = 0
                    else:
                        entry = int(entry) or -2
                        

                    spreadsheet_pool.append((paper, year, question_number, entry))
                except:
                    continue

    filteredPool = []

    for paper, year, question, mark in spreadsheet_pool:
        if mark_range[0] <= mark <=mark_range[1] and (paper, year, question) in pool:
            filteredPool.append((paper, year, question))

    return filteredPool
