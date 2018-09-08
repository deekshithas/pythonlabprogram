import random
import csv
attributes=[['Japan','USA'],['Honda','Toyota','Chrysler'],['Blue','Green','Red','White'],['1980','1970','1990'],['Economy','Sports']];
num_attributes=len(attributes)
print("\n The most general hypothesis:['?','?','?','?','?','?']\n")
print("\n The most specific hypothesis:['0','0','0','0','0','0']\n")
a=[]
print("\n The Given Training Data Set\n")
with open('japancar.csv','r') as csvFile:
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
    if a[i][num_attributes]=='Positive':
        for j in range(0,num_attributes):
            if a[i][j]!=hypothesis[j]:
                    hypothesis[j]='?'
            else:
                    hypothesis[j]=a[i][j]
print("for training example{0} the hypothesis is ".format(i),hypothesis)
print("\n maximally specific hypothesis for given training examples\n")
print(hypothesis)
    

