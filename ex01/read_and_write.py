def read_and_writecsv():
    with open("ds.tsv", "w") as fw:
        with open("ds.csv", "r") as fr:
            lines = fr.readlines()
            for line in lines:
                line = line.strip()
                columns = []
                current_column = ""
                in_brackets = False
                i = 0
                while i < len(line):
                    char = line[i]
                    if char == '"':
                        current_column += char
                        in_brackets = not in_brackets
                    elif char == ',' and not in_brackets:
                        columns.append(current_column)
                        current_column = ""
                    else:
                        current_column += char
                    i += 1
                columns.append(current_column)
                fw.write('\t'.join(columns) + '\n')
if __name__ == '__main__':
    read_and_writecsv()