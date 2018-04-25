import csv
import pandas as pd

whole = []
with open('nodes.csv') as f:
    content = f.readlines()
    for x in content:
        line = x.strip().split(' ')
        new_line = []
        for l in line:
            if l != '':
                new_line.append(l)
        whole.append(','.join(new_line))

whole = ['0,Digital_Document_File,.000534', '1,Account_Type,.000178', '2,Pre-Paid_Debit_Card_Information,.000356']
# whole = ['Age,0,0,1,0,1,0,0,2,2,0.8,100', 'AirlineTicketBoardingPass,0,1,0,1,0,2,0,1,0,0.05,500', 'Allergies,0,0,0,0,0,0,1,1,0,0.4,250']
parse_file = []
for w in whole:
    print(w.split(',')[1])
    n = input("class: ")
    if n == '1':
        c = 'Human'
    elif n == '2':
        c = 'Device'
    else:
        c = 'Organization'
    w += ',' + str(c)
    parse_file.append(w)

# writer = csv.writer(open("classify.csv", 'w'))
# for item in parse_file:
#     writer.writerow([item])

with open('new_node.csv', 'w') as file:
    for line in parse_file:
        file.write(line)
        file.write('\n')


# data = pd.read_csv('csvfile.csv', delim_whitespace=True)
# print(data)

# you may also want to remove whitespace characters like `\n` at the end of each line
# content = [x.strip() for x in content]
# print(content)