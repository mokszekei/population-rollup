
INPUT_PATH = './input/censustract-00-10.csv'
OUTPUT_PATH = './output/report.csv'

def parse_line(raw_line):
    """
    This function splits the line read from csv by ",". It connects splited
    Core Based Statistical Area Title back and remove "\n" at each line.

    :param raw_line: line of text read from a csv file
    :return: list of variables from row of a csv file
    """
    line = raw_line.split(',')
    if len(line)>20:
        line[8] = line[8]+","+line[9]
        line.pop(9)
    line[19] = line[19].replace("\n",'')
    return line
    

def read_line(raw_line,keys):
    """
    This function integrates a list variables into a dictionary with keys read
    from the header of a csv.

    :param raw_line: line of text read from a csv file
    :param keys: list of string describing each variable in csv
    :return: dictionary representing data content of each line of csv
    """
    data_dict = {}
    parsed_line = parse_line(raw_line)
    for i in range(len(keys)):
        data_dict[keys[i]] = parsed_line[i]
    return data_dict  


def read_file(Lines):
    """
    This function reads each line of csv into a dictonary. Then it appends them
    into a list.

    :param Lines: every line of text from a csv file
    :return: list of dictionaries, each dictionary contain data from each row
    """
    df = []
    keys = Lines[0].split(',')
    keys[19] = keys[19].replace("\n",'')
    for i in range(1,len(Lines)):
        df.append(read_line(Lines[i],keys))
    return df


def get_pop(str):
    """
    This function converts string representing population in 2000/2010 into
    integer. Missing values (could be alphabet or empty list) would be
    detected with exception. Missing values would be treated as False, so
    that it wont change the sum of population in addition.

    :param str: string representing population in 2000/2010
    :return: integer converted from the string/ False when encounter missing
     value
    """
    try:
        res = int(str)
    except ValueError:
        return False
    return res


def get_ppc(str):
    """
    This function converts string representing population percent change into
    float. Missing values (could be alphabet or empty list) would be
    detected with exception. Missing values would be treated as False, so
    that it wont change the sum of population change in addition.

    :param str: string representing population change
    :return: integer converted from the string/ False when encounter missing
     value
    """
    try:
        res = float(str)
    except ValueError:
        return False
    return res


def get_ppc_count(str):
    """
    This function detects whether string for population change is valid. This
    function will be used to calculated the total data point of population
    change. (To handle situation that population data exist while population
    change data is missing)

    :param str: string representing population change
    :return: whether the string is convertible(1) to float ot not(False)
    """
    try:
        res = float(str)
    except ValueError:
        return False
    return 1


def process_data(df):
    """
    This function calculates the sum of population in 2000, sum of population
    in 2010, sum of population percent change for each Core Based Statistical
    Area. This function counts row of data and valid population change data.

    :param df: list of dictionaries representing the whole dataset
    :return: dictionary of statistical summary for each Core Based Statistical Area
    """
    summary = {}
    for row in df:
        key = row["CBSA09"]
        if key != '':
            if not (int(key) in summary.keys()):
                summary[int(key)]={
                    "CBSA_T" : row["CBSA_T"],
                    "count" : 0,
                    "POP00" : 0,
                    "POP10" : 0,
                    "PPCHG" : 0,
                    "count_ppc" : 0
                }
            summary[int(key)]["count"] += 1
            summary[int(key)]["POP00"] += get_pop(row["POP00"])
            summary[int(key)]["POP10"] += get_pop(row["POP10"])
            summary[int(key)]["PPCHG"] += get_ppc(row["PPCHG"])
            summary[int(key)]["count_ppc"] += get_ppc_count(row["PPCHG"])
    return summary


def write_file(summary, filename):
    """
    This function calculates average population percent change for each Core
    Based Statistical Area. This functions writes statistical summary of each
    CBSA, comma seperated, into a csv file. The lines in the csv file are
    sorted by CBSA Code (ascending).

    :param summary: dictionary of statistical summary for each Core Based
     Statistical Area
    :param filename: path + name of the output file
    """
    f = open(filename, 'w')
    list_keys = list(summary.keys())
    while list_keys != []:
        curr = min(list_keys)
        f.write('{},{},{},{},{},{:.2f}\n'.format(curr, 
            summary[curr]["CBSA_T"],
            summary[curr]["count"],
            summary[curr]["POP00"],
            summary[curr]["POP10"],
            summary[curr]["PPCHG"]/summary[curr]["count_ppc"]))
        # f.write('{},{},{},{},{},{:.2f}'.format(curr, 
        #     summary[curr]["CBSA_T"],
        #     summary[curr]["count"],
        #     summary[curr]["POP00"],
        #     summary[curr]["POP10"],
        #     summary[curr]["PPCHG"]/summary[curr]["count_ppc"]))
        # if len(list_keys) != 1:
        #     f.write('\n')
        list_keys.remove(curr)
    f.close()


if __name__ == '__main__':

    file1 = open(INPUT_PATH, 'r') 
    Lines = file1.readlines() 
    file1.close()

    df = read_file(Lines)
    summary = process_data(df)

    write_file(summary, OUTPUT_PATH)







