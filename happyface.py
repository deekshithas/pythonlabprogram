import random
import csv
attributes=[['Round','Square'],['Triangle','Square'],['Round','Square'],['Purple','Yellow'],['Yes','No']];
num_attributes=len(attributes)
print("\n The most general hypothesis:['?','?','?','?','?','?']\n")
print("\n The most specific hypothesis:['0','0','0','0','0','0']\n")
a=[]
print("\n The Given Training Data Set\n")
with open('face.csv','r') as csvFile:
    reader=csv.reader(csvFile)
    for row in reader:
        a.append(row)
        print(row)
print("\n The initial value of hypothesis:")
hypothesis=['0']*num_attributes
print(hypothesis)
for j in range(0,num_attributes):
    hypothesis[j]=a[0][j];
print("\n Find S:Finding a maximaly specific hypothesis\n")
for i in range(0,len(a)):
    if a[i][num_attributes]=='Yes':
        for j in range(0,num_attributes):
            if a[i][j]!=hypothesis[j]:
                    hypothesis[j]='?'
            else:
                    hypothesis[j]=a[i][j]
print("for training example{0} the hypothesis is ".format(i),hypothesis)
print("\n maximally specific hypothesis for given training examples\n")
print(hypothesis)
    

