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
|  |- template.tex (обертка для условий с input)
|  |
|  |- problems 
|  |  |- problems-2020.tex
|  |  |- problems-2020.pdf
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
	republic-math, 2020, 27 марта 2020, Открытая студенческая олимпиада по математике \\ Казахстанского филиала МГУ, Казахстанский филиала МГУ имени М. В. Ломоносова, г. Астана 

============================

Выполнить:
1) pdflatex math.tex
2) cd /year\ by\ year
3) python3 generate.py < list.txt

============================

Добавить на сайт
1) mymath.info/math/msu/problems/msu-2020-problems.tex
2) mymath.info/math/msu/problems/msu-2020-problems.pdf
3) mymath.info/math/msu/results/msu-2020-results.tex
4) mymath.info/math/msu/results/msu-2020-results.pdf
5) mymath.info/math/msu/solutions/msu-2020-solutions.tex
6) mymath.info/math/msu/solutions/msu-2020-solutions.pdf
7) mymath.info/script/run.php
math/msu/results/msu-2020-results
8) исправить mymath.info/math/show.php
if ($olymp == "msu")
for ($y = 2014; $y <= 2020; $y++)
============================

Выполнить:
1) cd math
2) pdflatex math.tex
3) cd /year\ by\ year
4) python3 generate.py < list.txt
