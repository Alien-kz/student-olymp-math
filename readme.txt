Структура:

math
|- math.tex (сборник)
|
|- problems (данные)
|  |- 2008.tex
|  |- 2009.tex
|  |- ...
|
|- solutions (данные)
|  |- 2008.tex
|  |- 2009.tex
|  |- ...
|
|- results (данные)
|  |- 2008.tex
|  |- 2009.tex
|  |- ...
|
|- year by year (по годам)
|  |- generate.py (скрипт, генерирующий обертку для каждого года)
|  |- a4.tex (шаблон)
|  |- msu.txt (список подстановок в шаблон)
|  |
|  |- problems 
|  |  |- problems-2020.tex
|  |  |- problems-2020.pdf
|  |  |- problems-2020.png
|  |  |- ...
|  |
|  |- solutions
|  |  |- solutions-2020.tex
|  |  |- solutions-2020.pdf
|  |  |- ...
|  |
|  |- results
|  |  |- results-2020.tex
|  |  |- results-2020.pdf
|  |  |- ...

============================

Добавить олимпиаду:

1) problems/2020.tex - условия
2) solutions/2020.tex - решения
3) results/2020.tex - результаты
4) yby/2020.txt
	file, date, name, hoster, city
	2020, 27 марта 2020, Открытая студенческая олимпиада по математике \\ Казахстанского филиала МГУ, Казахстанский филиала МГУ имени М. В. Ломоносова, г. Астана 
5) cd yby
6) python3 generate.py png 2020.txt a4.tex problems
7) python3 generate.py pdf 2020.txt a4.tex solutions
8) python3 generate.py pdf 2020.txt a4.tex results

============================

Добавить в книгу:

1) math.tex
   добавить строки
	\header{2020--2021}{20 декабря 2020}
	\input{problems/2020}
	\newpage
	\header{2020--2021}{20 декабря 2020}
	\input{solutions/2020}
	\newpage
	\header{2020--2021}{20 декабря 2020}
	\input{results/2020}
	\newpage
2) pdflatex math.tex

============================

Добавить на сайт

0) cd yby
1) python3 generate.py png 2020.txt a5.tex  ../problems/ ~/http/mymath.info/math/msu/problems/ msu- -problems
   python3 generate.py pdf 2020.txt a4.tex  ../problems/ ~/http/mymath.info/math/msu/problems/ msu- -problems
2) python3 generate.py pdf 2020.txt a4.tex  ../solutions/ ~/http/mymath.info/math/msu/solutions/ msu- -solutions
3) python3 generate.py pdf 2020.txt a4.tex  ../results/ ~/http/mymath.info/math/msu/results/ msu- -results
4) на странице mymath.info/script/run.php сгенерировать результаты
   math/msu/results/msu-2020-results
5) исправить mymath.info/math/show.php
	if ($olymp == "msu")
		for ($y = 2014; $y <= 2020; $y++)

============================
