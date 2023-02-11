# Task1

## Step 1:-
```
git clone git@github.com:sanjaybora04/task1.git
```
---

## Step 2:-
* Enter the file path in main.py
```
import reader

res = reader.read("data/table.pdf") # file_path

for i,page in enumerate(res):
    print("PAGE :- ",i+1,"\n\n")
    print(page)
    print("\n\n")
```
---

## Step 3:-
* run main.py
---


> Note: Only image or pdf files can be read