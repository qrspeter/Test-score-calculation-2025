import pprint
import copy

def load_results(filename) -> dict:
    fin = open(filename, 'r', encoding='utf-8')
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
    

def append_results(dct1, dct2):
    for key, key in zip(dct1, dct2):
        dct1[key] += dct2[key] 

        
def normalize_dct(dct, max_point=10):
    dct_norm = {}
    max_key = max([i[0] for i in dct.values()])
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
        'activity.txt': 12
        , 'board.txt': 12
        , 'hw1.txt': 10 
        , 'test1.txt': 9
        , 'hw1volunt.txt': 5
        , 'test2.txt': 20
        , 'hw2.txt': 10 
        , "project.txt": 9 
        # max 67
        , "auxil.txt": 3 # 
        } 
    #assert sum([test_files[i] for i in test_files]) == 70, "Wrong total score."

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

    #pprint.pprint(dct_glob, sort_dicts=False)  
    with open("results_full.txt", "w") as output_file:
        pprint.pp(dct_glob, stream=output_file, indent=4)
        
    dct_glob = sum_dct(dct_glob)
    
    over60 = 0
    for key in dct_glob:
        dct_glob[key] = round(dct_glob[key]*1.4)
        if dct_glob[key] > 60:
            over60 += 1
    print(f"{over60=}")
            
    pprint.pprint(dct_glob, sort_dicts=False)        
    with open("results_summary.txt", "w") as output_file:
        pprint.pp(dct_glob, stream=output_file, indent=4)
    
