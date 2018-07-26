Структура:

math
|- math.tex (сборник)
|
|- problem (данные)
|  |- 2008.tex
|  |- 2009.tex
|  |- ...
|
|- solution (данные)
|  |- 2008-sol.tex
|  |- 2009-sol.tex
|  |- ...
|
|- result (данные)
|  |- 2008-res.tex
|  |- 2009-res.tex
|  |- ...
|
|- year by year (по годам)
|  |- generate.sh (скрипт, генерирующий обертку для каждого года)
|  |
|  |- problem 
|  |  |- template.tex (обертка для условий с input)
|  |  |- ...
|  |
|  |- solution
|  |  |- template.tex (обертка для решений с input)
|  |  |- ...
|  |
|  |- result
|  |  |- template.tex  (обертка для результатов input)
|  |  |- ...

============================

Как добавлять новую олимпиаду:
- math/problem/2020.tex - условия
- math/solution/2020.tex - решения
- math/result/2020.tex - результаты
- math/math.tex
   добавить строки
	\header{2020--2021}{20 декабря 2020}
	\input{result/2020}
	\newpage
	\header{2020--2021}{20 декабря 2020}
	\input{result/2020-sol.tex}
	\newpage
	\header{2020--2021}{20 декабря 2020}
	\input{result/2020-res.tex}
	\newpage
- math/year by year/generate.sh
    добавить строки
    	date=( "${date[@]}" "20 декабря 2020" )
	file=( "${file[@]}" "2020" )
	type=( "${type[@]}" "Открытая олимпиада по математике" )

============================

Выполнить:
1) cd math/year by year && bash generate-problems.tex
2) cd math/year by year && bash generate-solutions.tex
3) cd math/year by year && bash generate-results.tex
4) cd math && pdflatex math.tex

