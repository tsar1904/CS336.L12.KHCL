import glob
import numpy as np
import re
#B1: đọc file tạo 1 dictionary
files = glob.glob("./data/*.txt", recursive=True)
print(files)
dictionary=set()
list_content=[]
for f in files:
    file = open(f,'r',encoding="utf-8")
    file_content = file.read()
    list_content.append(file_content)
    words = set(file_content.replace('. ',' ').replace('"',' ').split())#xoá các kí tư ko liên quan
    dictionary.update(words)
#tạo một term doc & khai báo 0 cho các phần tử
term_doc_mat = np.zeros((len(dictionary),len(list_content)))
#print(term_doc_mat)
idx = 0 
for doc in list_content:
    term_doc_mat[:,idx]=np.array(([int(words in doc) for words in dictionary]))
    idx+=1
#print("Ma tran term_doc: \n",term_doc_mat)
print("Nhap cau truy van: ")
query = input()
tokens = re.findall('"(\w+)"',query)
and_or_xor_not = re.findall(' (\w+)',query)
#print(and_or_xor_not)



dictionary = list(dictionary)
#print(dictionary)
arr_vec_tor = []
vec_tor_query_1 = []
vec_tor_query_2 = []




for token in tokens:
    if token in dictionary:
        idx = dictionary.index(token)
        #print(idx)
        vec_tok = term_doc_mat[idx]
        arr_vec_tor.append(vec_tok) 
        #print('vec_to',token,":",vec_tok)
#print(arr_vec_tor)

#Hàm truy vấn dữ liệu
def Data_query(arr_vector):

    vec_tor_query_1 = arr_vec_tor [0]
    for i in range(0,len(and_or_xor_not)):
#AND    
        data_query = []
        vec_tor_query_2 = arr_vec_tor[i+1]
        if and_or_xor_not[i] == "AND" :
            for i in range(0,len(vec_tor_query_1)):
                data_query.append( vec_tor_query_1[i] and vec_tor_query_2[i])   

#OR
        elif and_or_xor_not[i] == "OR" :
            for i in range(0,len(vec_tor_query_1)):
                data_query.append( vec_tor_query_1[i] or vec_tor_query_2[i])

#XOR
        elif and_or_xor_not[i] == "XOR" :
            for i in range(0,len(vec_tor_query_1)):
                d = bool(vec_tor_query_1[i]) != bool(vec_tor_query_2[i])
                if d == True:
                    d = 1
                    data_query.append(d)
                else:
                    d = 0
                    data_query.append(d)

        vec_tor_query_1 = data_query
    return data_query

print(Data_query(arr_vec_tor))
vec_tor_query = Data_query(arr_vec_tor)
#tìm vị trí xuất hiện của query trong n bộ data 
for in_data in range(0,len(vec_tor_query)):
    if vec_tor_query[in_data] == 1:
        print('data :',in_data)