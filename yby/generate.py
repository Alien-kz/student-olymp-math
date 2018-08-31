#! /bin/python3

# python3 generate.py pdf list.txt template.tex input_directory output_directory [additional_prefix] [additional_suffix]
# python3 generate.py pdf list.txt template.tex problems

import os
import sys

def parse_csv(data_file_name):
	full_data = list()

	with open(data_file_name, 'r') as data_file:
		print("------- parse csv -------")
		line = data_file.readline().strip()
		keys = line.split(', ')
		index = 0
		for line in data_file:
			index += 1
			row_value = line.strip() 
			if row_value:
				values = row_value.split(',')
				row_data = dict()
				for i in range(len(values)):
					row_data[keys[i].strip()] = values[i].strip()
				full_data.append(row_data)
				print('value ' + str(index) + ':\t' + str(full_data[-1]))
	return full_data

def replace_by_template(input_file, output_file, template, temp_info):
	try:
		input_tex_file = open(input_file, 'r')
		with input_tex_file:
			text = input_tex_file.read()
			template = template.replace("<Дата>", temp_info['date'])
			template = template.replace("<Олимпиада>", temp_info['name'])
			template = template.replace("<ВУЗ>", temp_info['hoster'])
			template = template.replace("<Город>", temp_info['city'])
			template = template.replace("<Текст>", text)
			with open(output_file, 'w') as output_tex_file:
				output_tex_file.write(template)
			return True
	except IOError:
		return False
	return False

def make_tex(input_directory, 
			 output_directory, 
			 template_file, 
			 list_of_temp_info, 
			 output_prefix_base,
			 output_suffix):
	output_file_names = list()
	with open(template_file, 'r') as temp_file:
		print("------- make tex -------")
		template = temp_file.read()
		for temp_info in list_of_temp_info:

			input_path = input_directory
			output_path = output_directory
			output_prefix = output_prefix_base
			if 'subdirectory' in temp_info:
				input_path += temp_info['subdirectory'] + "/"
				output_prefix +=  temp_info['subdirectory'] + "-"
			
			input_file_name = temp_info['file'] + ".tex"
			output_file_name = output_prefix + temp_info['file'] + output_suffix + ".tex"

			input_file = input_path + input_file_name
			output_file = output_path + output_file_name

			tex_status = replace_by_template(input_file, output_file, template, temp_info)
			
			print(input_file + "  ==>>  " + output_file + "\t" + str(tex_status))
			if (tex_status):
				output_file_names.append(output_file_name[:-4])
	return output_file_names

def make_pdf(output_directory, output_file_names):
	os.chdir(output_directory)
	quite = " 1>/dev/null"	# 	quite = ""
	print("------- make pdf -------")
	for file_name in output_file_names:
		tex_file = file_name + ".tex"
		pdf_file = file_name + ".pdf"
		cmd = "pdflatex " + tex_file + quite
		pdf_status = (os.system(cmd) == 0)
		print(tex_file + "  ==>>  " + pdf_file + "\t" + str(pdf_status))
	os.system("rm *log *aux")
	os.chdir("..")

def make_png(output_directory, output_file_names):
	os.chdir(output_directory)
	quite = " 1>/dev/null"	# 	quite = ""
	print("------- make png -------")
	for file_name in output_file_names:
		pdf_file = file_name + ".pdf"
		png_file = file_name + ".png"
		cmd = "convert -density 150 -quality 100 -trim " + pdf_file + " +profile 'icc' -alpha remove " + png_file
		png_status = (os.system(cmd) == 0)
		print(pdf_file + "  ==>>  " + png_file + "\t" + str(png_status ))
	os.chdir("..")

correct = [5, 6, 7, 8]
if (len(sys.argv) not in correct):
	print("execute example 1:")
	print("    python3 generate.py pdf    list.txt       template.tex  ../problems/  problems/  msu-        -problems")
	print("                        ^      ^              ^             ^             ^          ^           ^")
	print("                        level  template_info  template_file input_dir     output_dir add_prefix  add_suffix")
	print("")
	print("execute example 2:")
	print("    python3 generate.py pdf    list.txt       template.tex  problems")
	print("                        ^      ^              ^             ^")
	print("                        level  template_info  template_file key")
	print("")
	print("level:")
	print("    tex pdf png")
	print("")
	print("template_info file example:")
	print("    subdirectory, file, date, name, hoster, city")
	print("    math, 2011-1, 2011, Вступительный экзамен по математике, Казахстанский филиал МГУ имени М. В. Ломоносова, г. Астана")
else:
	all_levels = ['tex', 'pdf', 'png']
	level = sys.argv[1]
	data_file = sys.argv[2]
	template_file = sys.argv[3]
	input_directory = ""
	output_directory = ""
	output_prefix = ""
	output_suffix = ""
	
	if len(sys.argv) == 5:
		input_directory = "../" + sys.argv[4] + "/"
		output_directory = sys.argv[4] + "/"
		output_prefix = "msu-"
		output_suffix = "-" + sys.argv[4]
	else:
		input_directory = sys.argv[4]
		output_directory = sys.argv[5]
	
	if len(sys.argv) > 6:
		output_prefix = sys.argv[6]
	if len(sys.argv) > 7:
		output_suffix = sys.argv[7]
	print('template info:' + '\t\t' + data_file)
	print('template file:' + '\t\t' + template_file)
	print('input directory:' + '\t' + input_directory)
	print('output directory:' + '\t' + output_directory)

#	os.system("rm -rf " + output_directory)
	os.system("mkdir " + output_directory)
	list_of_temp_info = parse_csv(data_file)
	
	if level in all_levels[0:]:
		output_file_names = make_tex(input_directory, 
									output_directory, 
									template_file, 
									list_of_temp_info,
									output_prefix,
									output_suffix)
	if level in all_levels[1:]:
		make_pdf(output_directory, output_file_names)
	if level in all_levels[2:]:
		make_png(output_directory, output_file_names)
