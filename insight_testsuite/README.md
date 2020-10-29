* my_test_1 \
(a) I shuffled the order of rows, to test whether the code can catch every row of a Core Based Statistical Area when they are not grouped together \
(b) I added one mockup row with valid population data but invalid population percentage change data, to test whetehe the code can handle missing value in percentage change data.
* my_test_2 \
(a) I added one mockup row with empty string in population 2000/2010 but valid population percentage change data, to test whether the code can handle missing value in population while calculating the average percentage change correctly.
* my_test_3 \
(a) All rows in the input file contain no core areas data. The code should still creat report.csv but contains no line.
