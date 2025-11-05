import pprint
import copy

# def load_names(filename):

    # fin = open(filename, 'r')
    # members = fin.readlines()
    # fin.close()

    # dct = {}

    # for name in members:
        # name = name.strip()
        # dct[name] = []
    
    # return dct

def load_results(filename) -> dict:
    fin = open(filename, 'r')
    lines = fin.readlines()
    fin.close()
    dct = {}
    for line in lines:
        line = line.strip()
        lst = line.split(' ')
        try:
            result = [float(lst[-1])]
            name = ' '.join(lst[:-1]).strip()
        except ValueError:
            name = line
            result = [0]
        dct[name] = result
    return dct
    
# def load_results(filename, dct):
    
    # fin = open(filename, 'r')
    # lines = fin.readlines()
    # fin.close()

    # for line in lines:
        # line = line.strip()
        # lst = line.split(' ')
        # try:
            # result = [float(lst[-1])]
            # name = ' '.join(lst[:-1]).strip()
        # except ValueError:
            # name = line
            # result = [0]
        # dct[name] += result

def append_results(dct1, dct2):
    for key, key in zip(dct1, dct2):
        dct1[key] += dct2[key] 

        
def normalize_dct(dct, max_point=10):
    print(dct)
    dct_norm = {}
    max_key = max([i[0] for i in dct.values()])
    print(max_key)
    if max_key == 0:
        return dct

    for name, grade in dct.items():
        grades_norm = float(grade[0]) * max_point / max_key
        dct_norm[name] = [grades_norm]
        
    return(dct_norm)

def sum_dct(dct) -> dict:
    dct_sum = {}
    for key in dct:
        dct_sum[key] = round(sum(dct[key]))
    return dct_sum



if __name__ == "__main__":    

    test_files = {
        'test1.txt': 7
        , 'board1.txt': 7
        , 'activity1.txt': 7
        , 'hw1volunt.txt': 5
        , 'hw1.txt': 7 # max 25+8(9)=33(34)
        #, 'test2.txt': 10
        #, 'activity2.txt': 10
        #, "project.txt": 10
        } 

    names = 'students_2025.txt'
    dct_glob = {}

    for file in test_files:
        dct = load_results(file) # Адельшинова Ева Тимуровна': [0, 2.0, 2.0, 0, 0],
        
        dct = normalize_dct(dct, test_files[file])
        
        if dct_glob == {}:
            #dct_glob = dct.copy()
            dct_glob = copy.deepcopy(dct)
        else:
            append_results(dct_glob, dct)

    pprint.pprint(dct_glob, sort_dicts=False)  
    dct_glob = sum_dct(dct_glob)
            
    #print(dict_31)
    pprint.pprint(dct_glob, sort_dicts=False)        

    # with open(__file__[:-2] + 'txt', 'w') as f:  
        # for name, grades in dict_31_norm.items():  
            # st = ',\t'.join([str(round(i)) for i in grades])
            # fstring = f'{name + ":":15s} {st}'
            # f.write(fstring + '\n')
            # print(fstring)
