import os.path as path
from bs4 import BeautifulSoup
import os, tempfile, subprocess, shutil

def filter(pool, topics):
    if "all" in topics:
        return pool
    
    src_dir = path.dirname(__file__)
    rel_dir = "../data/STEP_Questions_Database.html"

    question_topic = {}
    filtered_pool = []

    

    with open(path.join(src_dir, rel_dir), "r") as step_qns:
        soup = BeautifulSoup(step_qns.read(), "html.parser")

        for element in soup.find_all("li"):
            try:
                link = element.find("a")
                question = link.contents[0]

                thing = element.find("i")
                qn_topics = (thing.contents[0].contents[0].contents[0])

                question_topic[question] = qn_topics.lower()
            except:
                pass

    for i, question in enumerate(pool):
        name = str(question[1])[2:4] + "-S" + str(question[0]) + "-Q" + str(question[2])
        if name in question_topic:
            qn_topic = question_topic[name]
            append = False

            for topic in topics:
                if qn_topic.find(topic.lower()) != -1:
                    append = True

            if append:
                filtered_pool.append(question)
                    

    return filtered_pool