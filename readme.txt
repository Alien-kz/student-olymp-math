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

Как добавлять новую олимпиаду:
1) problems/2020.tex - условия
2) solutions/2020.tex - решения
3) results/2020.tex - результаты
4) math.tex
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
5) year by year/list.txt
	добавить строку
	2020, 27 марта 2020, Открытая студенческая олимпиада по математике \\ Казахстанского филиала МГУ, Казахстанский филиала МГУ имени М. В. Ломоносова, г. Астана 

============================

Выполнить:
1) pdflatex math.tex
2) cd yby
3) python3 generate.py png msu.txt a4.tex  ../problems/ problems/ msu- -problems
4) python3 generate.py pdf msu.txt a4.tex  ../solutions/ solutions/ msu- -solutions
5) python3 generate.py pdf msu.txt a4.tex  ../results/ results/ msu- -results

============================

Добавить на сайт
1) mymath.info/math/msu/problems/msu-2020-problems.tex
   mymath.info/math/msu/problems/msu-2020-problems.pdf
   mymath.info/math/msu/problems/msu-2020-problems.png

2) mymath.info/math/msu/solutions/msu-2020-solutions.tex
   mymath.info/math/msu/solutions/msu-2020-solutions.pdf

3) mymath.info/math/msu/results/msu-2020-results.tex
   mymath.info/math/msu/results/msu-2020-results.pdf

4) mymath.info/script/run.php
   math/msu/results/msu-2020-results

5) исправить mymath.info/math/show.php
if ($olymp == "msu")
    for ($y = 2014; $y <= 2020; $y++)

============================
