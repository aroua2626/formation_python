grades = [
    ["Alice", "85", "90", "78"], 
    ["Bob", "72", "68", "80"], 
    ["Charlies", "95", "100", "92"],
    ["Diana", "50", "60", "55"], 
    ["Evan", "88", "79", "84"] 
]
filename = "grades.csv"
mode = "a"

with open(filename, mode) as f:
    for std in grades:
        line = ",".join(std) + "\n"
        f.write(line)

for grade in grades: 
   average=(int(grade[1])+int(grade[2])+int(grade[3]))/3
   if average>=50:
    print("pass")
   else:
    print("fail")    
   print("the average of", grade[0] ,"is", average) 

with open ("average.csv","w")as csv_file:
 for grade in grades:
  average
  status="pass"if average>=50 else "fail" 
  csv_file.write(f"{grade[0]},{average},{status}\n")
