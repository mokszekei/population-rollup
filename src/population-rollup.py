

def parse_line(raw_line):
    line = raw_line.split(',')
    if len(line)>20:
        line[8] = line[8]+","+line[9]
        line.pop(9)
    line[19] = line[19].replace("\n",'')
    return line
    

def read_line(raw_line,keys):
    data_dict = {}
    parsed_line = parse_line(raw_line)
    for i in range(len(keys)):
        data_dict[keys[i]] = parsed_line[i]
    return data_dict  


def read_file(Lines):
    df = []
    keys = Lines[0].split(',')
    keys[19] = keys[19].replace("\n",'')
    for i in range(1,len(Lines)):
        df.append(read_line(Lines[i],keys))
    return df


def checkKey(dict, key): 
      
    if key in dict.keys(): 
        print("Present, ", end =" ") 
        print("value =", dict[key]) 
    else: 
        print("Not present") 


def get_pop(str):
    try:
        res = int(str)
    except ValueError:
        return False
    return res


def get_ppc(str):
    try:
        res = float(str)
    except ValueError:
        return False
    return res


def get_ppc_count(str):
    try:
        res = float(str)
    except ValueError:
        return False
    return 1


def process_data(df):
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
        list_keys.remove(curr)
    f.close()



file1 = open('../input/censustract-00-10.csv', 'r') 
Lines = file1.readlines() 

df = read_file(Lines)
summary = process_data(df)

write_file(summary, '../output/report.csv')







