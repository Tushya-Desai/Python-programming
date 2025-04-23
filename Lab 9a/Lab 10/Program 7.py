import json
d={"Rollno":"24BCP139","Name": "Divyam Patel","Date_of_Joining": "2024-06-10","Fees": 224000}
fp=open("C:\Semester 2\Computer(Python)\Lab 10\Myfile7.txt",'a')
json.dump(d,fp)
fp.seek(0)
a=json.load(fp)
print(a)
fp.close()
