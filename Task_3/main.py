import os

folder = 'files'
current = os.getcwd()
full_path = os.path.join(current, folder)
files = []
for file in os.listdir(full_path):
    files.append(file)

dict_files = {}
for file in files:
    with open(os.path.join(full_path, file), 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
        dict_files[len(lines)] = [file, lines]
        sorted_dict = dict(sorted(dict_files.items()))

with open('result.txt', 'w', encoding = 'utf-8') as file:
    for k, v in sorted_dict.items():
        file.write(f'{v[0]}\n')
        file.write(f'{k}\n')
        file.writelines(v[1])
        file.write('\n\n')








