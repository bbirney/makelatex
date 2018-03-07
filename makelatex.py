# import libraries
import sys
import urllib2
from bs4 import BeautifulSoup

# check if hw # is supplied, help the user if not
if len(sys.argv) != 2:
    print "Usage: makelatex <hw number>"
    sys.exit()

# scrape raw html from specified hw url
url = 'https://www.usna.edu/Users/cs/aviv/classes/ic221/s18/hw/'
url += sys.argv[1]+'/hw.html'
rawhtml = urllib2.urlopen(url)

# parse the html and extract the questions (in an ol)
html = BeautifulSoup(rawhtml, 'html.parser')
html = html.find("ol")

# get all questions & code snippits
question_list = html.find_all("li")
code_snippits = html.find_all("code")

# create and write latex file header
latexfile = open("hw"+sys.argv[1]+".tex", "w")
l_header = "\documentclass{article}[9pt]\n\usepackage{listings}\n"
l_header += "\usepackage{fullpage}\n"
l_header += "\usepackage{textcomp}\n\usepackage{mdframed}\n"
l_header += "\lstset{ %\nbasicstyle=\\ttfamily\scriptsize,\n"
l_header += "commentstyle=\\ttfamily\scriptsize\emph,\n"
l_header += "upquote=true,\nframerule=1.25pt,\nbreaklines=true,\n"
l_header += "showstringspaces=false,\n"
l_header += "escapeinside={(*@}{@*)},\nbelowskip=2em,\naboveskip=1em,\n}"
l_header += "\\newenvironment{answerfont}{\\fontfamily{qhv}\selectfont}{\par}"
l_header += "\n\n\\newenvironment{myanswer}{\\begin{mdframed}"
l_header += "\\begin{answerfont}}{\end{answerfont}\end{mdframed}}\n"
l_header += "\\title{HW "+sys.argv[1]+"}\n\\author{Benjamin Birney}\n"
l_header += "\date{DATE GOES HERE}\n\\begin{document}"
l_header += "\maketitle\n\section*{Questions}\n\label{sec:orgfce6862}"
l_header += "\n\\begin{enumerate}"
latexfile.write(l_header+"\n\n\n")

i = 0  # for index values for questions[]
questions = {}  # array of questions in unicode string format
sub_questions = {}  # array of sub-question arrays (in html tag format)
last = "notinanything"  # arbitrary string for substring checking

# iterate through question list to generate string-formatted question array
for question in question_list:
    # filter sub-qeustions out of questions list (find_all catches them)
    if (
        ("points" not in question.text and question.text in last)
        or question.text in last
       ):
        print question.text
        continue
    else:
        # add question in string format to questions array
        questions[i] = question.text
        # remove all subquestions from their respective question
        if "ol" in question.text or "li" in question.text:
            sub_questions[i] = question.find_all("li")
            for j in sub_questions[i]:
                questions[i] = questions[i].replace(j.text, "")
    last = question.text  # allows to check for subquestions in question list
    i += 1  # iterate i

# (DOESNT WORK YET) filter out code snippits and make it look pretty
# for i in range(0, len(questions)):
#     for snip in code_snippits:
#         if snip.text in questions[i]:
#             print "we found one"
#             newval = "\\begin{vertbatim}\n"+snip.text+"\n\end{verbatim}\n"
#             questions[i].replace(snip.text, newval)

# iterate through each question, write to latex file
for i in range(0, len(questions)):
    # format questions so that LaTeX doesnt have a seizure
    questions[i] = questions[i].replace("\\", "\\\\")
    questions[i] = questions[i].replace("_", "\_")
    questions[i] = questions[i].replace("&", "\&")

    # write question to the file
    latexfile.write("\item "+questions[i].encode("utf8")+"\n")

    # if a question has parts, print out all the parts
    try:

        # check if subquestion is an empty array, artificially throw error
        if not sub_questions[i]:
            raise Exception("empty sub-question array")

        # after checking existance, actually write subquestions (list format)
        latexfile.write("\\begin{enumerate}\n")

        for j in sub_questions[i]:
            sub_text = j.text.replace("_", "\_").replace("&", "\&")
            latexfile.write("\item "+sub_text.encode("utf8")+"\n")
            latexfile.write("\\begin{myanswer}\nANSWER\n\end{myanswer}\n\n")

        latexfile.write("\end{enumerate}\n")

    # print a normal answer field if there aren't subquestions
    except Exception:
        # I check for points and point because Aviv has made this typo before
        if "points" in questions[i] or "point" in questions[i]:
            latexfile.write("\\begin{myanswer}\nANSWER\n\end{myanswer}\n\n")

# write file footer (close enumerate and document)
latexfile.write("\end{enumerate}\n\end{document}\n")
latexfile.write("\n%%% mode: latex\n% TeX-master: t\n%%% End:")
