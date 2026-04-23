import sys
def company_price():
    if len(sys.argv) == 2:
        ticker = sys.argv[1]
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
        for company in COMPANIES.keys():
            if ( COMPANIES[company].lower() == ticker.lower() ):
                print(company + " " + str(STOCKS[COMPANIES[company]]))   
                flag = True 
        if not flag:
            print("Unknown ticker")

if __name__ == '__main__':
    company_price()