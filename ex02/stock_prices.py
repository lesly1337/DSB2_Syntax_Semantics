import sys
def company_price():
    if len(sys.argv) == 2:
        company_name = sys.argv[1]
        flag = False
        COMPANIES = {
            'Apple': 'AAPL',
            'Microsoft': 'MSFT',
            'Netflix': 'NFLX',
            'Tesla': 'TSLA',
            'Nokia': 'NOK'
        }
        STOCKS = {
            'AAPL': 287.73,
            'MSFT': 173.79,
            'NFLX': 416.90,
            'TSLA': 724.88,
            'NOK': 3.37
        }
        for key in COMPANIES.keys():
            if (company_name.lower() == key.lower()):
                flag = True
                print(STOCKS[COMPANIES[key]])
        if not flag:
            print("Unknown company")
            

if __name__ == '__main__':
    company_price()