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
    file_content= file.read()
    list_content.append(file_content)
    words=set(file_content.replace('. ',' ').replace('"',' ').split())#xoá các kí tư ko liên quan
    dictionary.update(words)
term_doc_mat=np.zeros((len(dictionary),len(list_content)))
print(term_doc_mat)
idx = 0 
for doc in list_content:
    term_doc_mat[:,idx]=np.array(([int(words in doc) for words in dictionary]))
    idx+=1
print("Ma tran term_doc: \n",term_doc_mat)
query =' "Ronaldo" AND "Brazil" '
tokens = re.findall('"(\w+)"',query)
dictionary=list(dictionary)
for token in tokens:
    if token in dictionary:
        idx= dictionary.index(token)
        vec_tok = term_doc_mat[idx]
        print('vec_to',token,":",vec_tok)