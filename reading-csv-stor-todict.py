##Program to read from a csv file as key vale pair and return as a dictionary
##IF key is not unique then add same key's value in between and return the dict

import csv
def csv_to_dict(csv_path:str):
    try:
        with open(csv_path,mode='r') as fp:
            reader=csv.reader(fp)
            d = {}
            for items in reader:
                key = items[0]
                if key not in d:
                    values = items[1]
                    d[key] = values
                else:
                    d[key] = int(d[key]) + int(items[1])
        fp.close()
    except FileNotFoundError:
        print('ERROR:::File Name '+ csv_path + ' Not found:: Verify the file exists or not')
    return d
print(csv_to_dict('c:\sample-dictionary.csv'))


