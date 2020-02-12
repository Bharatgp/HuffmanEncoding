import csv
import io

encoded_input_file=r"C:\Users\Bharat\Documents\Python Scripts\Assignment1\Q3\EndcodedNamarie.txt"
output_file=r"C:\Users\Bharat\Documents\Python Scripts\Assignment1\Q3\deocded_Namarie.txt"
encodings_input_file=r"C:\Users\Bharat\Documents\Python Scripts\Assignment1\Q3\encoding.csv"

def get_key(val,my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key
    return -1

with io.open(encoded_input_file,'r',encoding='utf8') as f:
    text = f.read()
    text=text.strip(' ')

with open(encodings_input_file, 'r') as file:
    reader = csv.reader(file)
    list_of_codes=[]
    skip=0
    for row in reader:
        if(skip==0):
            skip=1
        else:
            list_of_codes.append((row[0],row[1]))
    CodeTable=dict(list_of_codes)
    pt1=0
    pt2=1
    decoded=""
    while(pt2<=len(text)):
        if(get_key(text[pt1:pt2],CodeTable)!=-1):
            decoded=decoded+get_key(text[pt1:pt2],CodeTable)
            pt1=pt2
            pt2=pt2+1
        else:
            pt2=pt2+1
    print("Following is the decoded text of the File ::: ")
    print(decoded)
with io.open(output_file,'w',encoding='utf8') as f:
    f.write(decoded)
