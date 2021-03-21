import sys

input_str = list(map(str, sys.stdin.readline().strip().split('&')))

output_dic = dict()

for i in input_str:
    case = i.split('=')
    output_dic[case[0]] = case[1]

print(output_dic)
