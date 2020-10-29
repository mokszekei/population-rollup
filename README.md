# population-rollup

## Problem
  
The federal Census produces a lot of useful demographic data. There will be many interesting insights to be generated from the data. Therefore, in this task, I wrote a python script to take the [2000 to 2010 Census Tract Population Change](https://www.census.gov/data/tables/time-series/dec/metro-micro/tract-change-00-10.html) dataset, perform a few calculations and then write out a new file with the summarized data.

## Input dataset

Below is a sample `censustract-00-10.csv` file: 
```
GEOID,ST10,COU10,TRACT10,AREAL10,AREAW10,CSA09,CBSA09,CBSA_T,MDIV09,CSI,COFLG,POP00,HU00,POP10,HU10,NPCHG,PPCHG,NHCHG,PHCHG
02130000100,02,130,000100,4835.518216,1793.906364,,28540,"Ketchikan, AK",,2,C,3801,1736,3484,1694,-317,-8.34,-42,-2.42
02130000200,02,130,000200,5.204047664,0.4525275793,,28540,"Ketchikan, AK",,2,C,4909,2156,4884,2179,-25,-0.51,23,1.07
02130000300,02,130,000300,2.771683112,0.4653222332,,28540,"Ketchikan, AK",,2,C,3054,1493,2841,1394,-213,-6.97,-99,-6.63
02130000400,02,130,000400,14.91968071,0.3246679135,,28540,"Ketchikan, AK",,2,C,2310,891,2268,899,-42,-1.82,8,0.90
48487950300,48,487,950300,933.9565129,6.998080686,,46900,"Vernon, TX",,2,C,2304,916,1849,892,-455,-19.75,-24,-2.62
48487950500,48,487,950500,13.21399173,0.01418539391,,46900,"Vernon, TX",,2,C,3172,1338,2955,1388,-217,-6.84,50,3.74
48487950600,48,487,950600,10.65575478,0,,46900,"Vernon, TX",,2,C,6022,2715,5994,2781,-28,-0.46,66,2.43
48487950700,48,487,950700,13.01780124,0.0371546123,,46900,"Vernon, TX",,2,C,3181,1409,2737,1257,-444,-13.96,-152,-10.79
```
The first line of the input file is header, the following lines are population data for each census tract. The sample input file comes from [2000 to 2010 Census Tract Population Change](https://www.census.gov/data/tables/time-series/dec/metro-micro/tract-change-00-10.html), which contains population counts for census tracts and how much they've changed over the decade. The csv file is provided by "insight fellowship"

Metropolitan and Micropolitan statistical areas can span one or more counties and states. For instance, "New York-Northern New Jersey-Long Island, NY-NJ-PA" is a Metropolitan Statistical Area and Core Based Statistical Area that is centered around New York City, extends east through Long Island and west through northern New Jersey and parts of Pennsylvania.

In this task, I want to know for each Core Based Statistical Area, the 
* total number of census tracts, 
* total population in 2000, 
* total population in 2010 and 
* average population percent change for census tracts in this Core Based Statistical Area

## Output

After reading and processing the input file, my code will create an output file, `report.csv`, with as many lines as unique Core Based Statistical Areas found in the input file. If there are no core areas in the input file, my code will still create the `report.csv` file but it contains no lines.

For every line that exists in the output file, the following fields are written in this order:
* Core Based Statstical Area Code (i.e., CBSA09)
* Core Based Statistical Area Code Title (i.e., CBSA_T)
* total number of census tracts
* total population in the CBSA in 2000
* total population in the CBSA in 2010
* average population percent change for census tracts in this CBSA. Round to two decimal places using standard rounding conventions (i.e., Any percentage between 0.005% and 0.010%, inclusive, should round to 0.01% and anything less than 0.005% should round to 0.00%)

The lines in the output file are sorted by Core Based Statstical Area Code (ascending)

## Testing

* my_test_1 \
(a) I shuffled the order of rows, to test whether the code can catch every row of a Core Based Statistical Area when they are not grouped together \
(b) I added one mockup row with valid population data but invalid population percentage change data, to test whetehe the code can handle missing value in percentage change data.
* my_test_2 \
(a) I added one mockup row with empty string in population 2000/2010 but valid population percentage change data, to test whether the code can handle missing value in population while calculating the average percentage change correctly.
* my_test_3 \
(a) All rows in the input file contain no core areas data. The code should still creat report.csv but contains no line.

## Repo directory structure

    ├── README.md
    ├── run.sh
    ├── src
    │   └── population.py
    ├── input
    │   └── censustract-00-10.csv 
    ├── output
    |   └── report.csv 
    ├── insight_testsuite
        └── tests
            └── test_1
            |   ├── input
            |   │   └── censustract-00-10.csv
            |   |__ output
            |   │   └── report.csv
            ├── my-test_1
            |   ├── input
            |   │   └── censustract-00-10.csv
            |   |__ output
            |   │   └── report.csv   
            ├── my-test_2
            |   ├── input
            |   │   └── censustract-00-10.csv
            |   |__ output
            |   │   └── report.csv  
            ├── my-test_3
                ├── input
                │   └── censustract-00-10.csv
                |── output
                    └── report.csv

