import sys
def start():
    email = sys.argv[1]
    with open("employees.tsv") as fr:
        lines = fr.readlines()
        for line in lines:
            sp_list = line.strip().split('\t') #strip потому что в конце перенос строки и мешает сравнению почты
            if (email == sp_list[2]):
                print(f"Dear {sp_list[0]}, welcome to our team! We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")

if __name__ == '__main__':
    start()
