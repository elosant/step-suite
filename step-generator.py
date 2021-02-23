import pyexcel_ods as pe
import os, sys, shutil, random, requests, datetime, tempfile, subprocess

USAGE = """USAGE
"""

MAIN_TEX = """\documentclass{{combine}}
\\begin{{document}}
\\begin{{papers}}
\\let\\clearpage\\relax
{}
\end{{papers}}
\end{{document}}"""

DB_ENDPOINT = "https://stepdatabase.maths.org/database/db/"
DB_TEX_ENDPOINT = DB_ENDPOINT + "{0}/{0}-S{1}.tex"

def get_questions(sheet_name: str, count: int=6):
    spreadsheet = None
    try:
        spreadsheet = pe.get_data(sheet_name)
    except:
        raise Exception("Cannot read from spreadsheet: " + sheet_name)

    questions = []
    for name, sheet in spreadsheet.items():
        for i, row in enumerate(sheet):
            for j, entry in enumerate(row):
                if entry == '?':
                    # [year, paper, question]
                    questions.append(list(map(int,
                        [str(row[0])[-2:], name[-1], sheet[1][j]])))

    return random.sample(questions, min(count, len(questions)))

def compile(questions: list):
    with tempfile.TemporaryDirectory() as t_dir:
        inner_tex = ""
        qNum = -1
        for year, paper, question in questions:
            url = DB_TEX_ENDPOINT.format(year, paper, question)
            res = requests.get(url)
            res.raise_for_status()

            qNum += 1
            data = res.text.replace("\\pagestyle{myheadings}",  '') \
                    .replace("\\setcounter{qnumber}{0}", \
                    "\\setcounter{qnumber}{"+str(qNum)+'}') # Hack to show correct question number

            qIndex = -1
            for n in range(question):
                qIndex = data.find("\\begin{question}", qIndex+1)

            q_str = data[qIndex:data.find("\\end{question}", qIndex)] + "\n\\textbf{{(S{0} {1} Q{2})}}\n".format(paper, year, question) + "\\end{question}"
            q_tex = data[:data.find("\\begin{document}")]+ "\\begin{document}" + '\n' \
                + q_str + '\n' + data[data.find("\\end{document}"):]

            with open(t_dir + "/{}-{}-{}.tex".format(year, paper, question), 'w') as tex_h:
                tex_h.write(q_tex)

            inner_tex += "\\import{" + "{}-{}-{}".format(year, paper, question) + '}\n'

        main_tex = MAIN_TEX.format(inner_tex)
        file_name = "step-paper-"+str(datetime.datetime.today())

        with open(t_dir + '/' + file_name + ".tex", 'w') as tex_h:
            tex_h.write(main_tex)

        subprocess.call(["latexmk", "-f", "-pdf", \
            "--interaction=nonstopmode", file_name], cwd=t_dir)
        shutil.move(t_dir + '/' + file_name + ".pdf", os.getcwd())

def main(argc: int, argv: list):
    if argc < 2:
        print(USAGE)
        return

    questions = get_questions(argv[1], argc >= 3 and int(argv[2]) or 6)
    compile(questions)

if __name__ == "__main__":
    args = sys.argv
    main(len(args), args)
