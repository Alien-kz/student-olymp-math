#! /bin/python3

import os
def replace_by_template(input_file, output_file, template, value):
	try:
		input_tex_file = open(input_file, 'r')
	except IOError:
    		return False
	with input_tex_file:
		text = input_tex_file.read()
		template = template.replace("<Дата>", value[0])
		template = template.replace("<Олимпиада>", value[1])
		template = template.replace("<Текст>", text)
		with open(output_file, 'w') as output_tex_file:
			output_tex_file.write(template)
		return os.system("pdflatex " + output_file + " 1>/dev/null") == 0
	return False

def make_pdf(directory, olymp, suffix):
	print(directory)
	os.chdir(directory)
	with open('template.tex', 'r') as temp_file:
		template = temp_file.read()
		for key, value in olymp.items():
			input_file = "../../" + directory + "/" +  key + suffix + ".tex"
			output_file = directory + "-" + key + ".tex"
			print(output_file, end="\t")
			print(replace_by_template(input_file, output_file, template, value))
	os.system("rm *log *aux")
	os.chdir("..")

math_open = "Открытая олимпиада по математике"
math_select = "Отборочная олимпиада по математике"
math_rep = "Республиканская студенческая предметная олимпиада \\\\ по направлению \\\\ <<Математика>> \\\\"
mcm_rep = "Республиканская студенческая предметная олимпиада \\\\ по направлению \\\\ <<Математическое и компьютеное моделирование>> \\\\"

olymp = dict()
olymp["2008"] = "7 декабря 2008", math_open;
olymp["2009"] = "6 декабря 2009", math_open;
olymp["2010"] = "12 декабря 2010", math_open;
olymp["2011"] = "10 декабря 2011", math_open;
olymp["2012"] = "21 декабря 2012", math_open;
olymp["2013"] = "20 декабря 2013", math_open;
olymp["2014-bonus"] = "15 марта 2014", math_select;
olymp["2014"] = "10 декабря 2014", math_open;
olymp["2015"] = "19 декабря 2015", math_open;
olymp["2016"] = "10 декабря 2016", math_open;
olymp["2017"] = "19 декабря 2017", math_open;
olymp["2018-bonus"] = "13 марта 2018", math_open;

olymp["2016-rep-math"] = "1 апреля 2016", math_rep;
olymp["2016-rep-mcm"] = "1 апреля 2016", mcm_rep;
olymp["2017-rep-math"] = "13 апреля 2017", math_rep;

make_pdf("problems", olymp, "")
make_pdf("results", olymp, "-res")
make_pdf("solutions", olymp, "-sol")
