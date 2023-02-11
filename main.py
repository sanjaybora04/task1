import reader

res = reader.read("data/table.pdf") # file_path

for i,page in enumerate(res):
    print("PAGE :- ",i+1,"\n\n")
    print(page)
    print("\n\n")