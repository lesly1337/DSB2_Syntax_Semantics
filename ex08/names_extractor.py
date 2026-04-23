import sys
def extract():
    file_name = sys.argv[1]
    with open("employees.tsv", "w") as fw:
        with open(file_name) as fr:
            lines = fr.readlines()
            for line in lines:
                list1 = line.split('@')
                list2 = list1[0].split('.')
                name = list2[0][0].upper() + list2[0][1:]
                surname = list2[1][0].upper() + list2[1][1:]
                fw.write(name + '\t' + surname + '\t' + line)

if __name__ == '__main__':
    extract()