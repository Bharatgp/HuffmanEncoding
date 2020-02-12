import io
import heapq


encoded_output_file=r"C:\Users\Bharat\Documents\Python Scripts\Assignment1\Q3\EndcodedNamarie.txt"
input_file=r"C:\Users\Bharat\Documents\Python Scripts\Assignment1\Q3\Namarie.txt"
encodings_output_file=r"C:\Users\Bharat\Documents\Python Scripts\Assignment1\Q3\encoding.csv"

with io.open(input_file,'r',encoding='utf8') as f:
    text = f.read()
    text=[i for i in text]
    unique_symbols=set(text)
    d={x:text.count(x) for x in text}
    freq_symbol=[(v, k) for k, v in d.items()]
    temp_heap=[]
    final_heap=[]
    heapq.heapify(temp_heap)
    heapq.heapify(final_heap)
    for i in freq_symbol:
        heapq.heappush(temp_heap,i)
    for i in range(len(temp_heap)-1):
        x=heapq.heappop(temp_heap)
        y=heapq.heappop(temp_heap)
        heapq.heappush(final_heap,x)
        heapq.heappush(final_heap,y)
        merged_node=(x[0]+y[0],x[1]+y[1])
        heapq.heappush(temp_heap,merged_node)
    list_of_heap=list(final_heap)
    list_of_heap.reverse()
    tree_with_0_1_edges=[]
    for i in range(0,len(list_of_heap),2):
        if(list_of_heap[i][0]>list_of_heap[i+1][0]):
            tree_with_0_1_edges.append((list_of_heap[i][1],1))
            tree_with_0_1_edges.append((list_of_heap[i+1][1],0))
        else:
            tree_with_0_1_edges.append((list_of_heap[i][1],0))
            tree_with_0_1_edges.append((list_of_heap[i+1][1],1))
    nodes_with_code=[]
    for i in tree_with_0_1_edges:
        code=""
        symbol=i[0]
        for j in tree_with_0_1_edges:
            if(symbol in j[0]):
                code=code+str(j[1])
        nodes_with_code.append((symbol,code))
    finalDic=[]
    for i in nodes_with_code:
        if(i[0] in unique_symbols):
            finalDic.append(i)
    CodeTable=dict(finalDic)
    avgg=0
    for k,v in CodeTable.items():
        avgg=avgg+(d[k]/len(text))*len(v)


    import csv
    with open(encodings_output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Symbol","Code"])
        for k,v in CodeTable.items():
             writer.writerow([k,v])
    encoded=""
    for i in text:
        encoded=encoded+CodeTable[i]
    with io.open(encoded_output_file,'w',encoding='utf8') as f:
        f.write(encoded)
