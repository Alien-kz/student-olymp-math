#! /bin/python3

import os
def replace_by_template(input_file, output_file, template, olymp):
	try:
		input_tex_file = open(input_file, 'r')
		with input_tex_file:
			text = input_tex_file.read()
			template = template.replace("<Дата>", olymp['date'])
			template = template.replace("<Олимпиада>", olymp['name'])
			template = template.replace("<ВУЗ>", olymp['hoster'])
			template = template.replace("<Город>", olymp['city'])
			template = template.replace("<Текст>", text)
			with open(output_file, 'w') as output_tex_file:
				output_tex_file.write(template)
			quite = " 1>/dev/null"
#			quite = ""
			return os.system("pdflatex " + output_file + quite) == 0
	except IOError:
		return False
	return False

def make_pdf(directory, full_data):
	print(directory)
	with open('template.tex', 'r') as temp_file:
		template = temp_file.read()
		os.chdir(directory)
		for olymp in full_data:
			# print(olymp)
			# ../../problems/math/2014.tex
			input_file = "../../" + directory + "/" + olymp['file'] + ".tex"
			# problems/republic-math-2014-problems.tex
			output_file = olymp['prefix'] + "-" + olymp['file'] + "-" + directory + ".tex"
			print(output_file, end="\t")
			print(replace_by_template(input_file, output_file, template, olymp))
		os.system("rm *log *aux")
		os.chdir("..")

def parse_csv():
	full_data = list()

	keys = input().split(',')
	row = input()
	while row != "":
		values = row.split(',')
		row_data = dict()
		for i in range(len(values)):
			row_data[keys[i].strip()] = values[i].strip()
		full_data.append(row_data)
		row = input()
	return full_data

full_data = parse_csv()
make_pdf("problems", full_data)
make_pdf("solutions", full_data)
make_pdf("results", full_data)
