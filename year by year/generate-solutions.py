#! /bin/python3

math_open = "Открытая олимпиада по математике"
math_select = "Отборочная олимпиада по математике"
math_rep = "Республиканская студенческая предметная олимпиада \\\\ по направлению \\\\ <<Математика>> \\\\"
mcm_rep = "Республиканская студенческая предметная олимпиада \\\\ по направлению \\\\ <<Математическое и компьютеное моделирование>> \\\\"

olymp = set()
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

for key, value in olymp:
	print(key, value[0], value[1])

# cd problems
# index=0
# element_count=${#date[@]}
# while [ "$index" -lt "$element_count" ]
# do
#    texfile=problem-${file[$index]}.tex
#    cat template.tex | sed -r "s/<Дата>/${date[$index]}/" \
#                     | sed -r "s/<file>/problem\/${file[$index]}/" \
#                     | sed -r "s/<Олимпиада>/${type[$index]}/" \
#                     > $texfile
#    echo "==============="
#    echo $texfile
#    echo "---------------"
#    pdflatex $texfile 1>/dev/null
#    index=$(($index + 1))
#done
#rm *log
#rm *aux
#cd ..
