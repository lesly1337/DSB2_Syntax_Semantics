import sys


def process_query():
    if ( len(sys.argv) == 2 ):
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
        query = sys.argv[1] #получаем 'TSLA , aPPle, Facebook'
        flag = False
        list = query.split(',') #получаем ['TSLA ',' aPPle',' Facebook']
        for word in list:
            word_no_spaces = word.strip()
            if ( word_no_spaces == ""):#если в списке есть пустая строка, тогда встретились две запятые
                flag = True
        if not flag:
            for word in list:
                word_no_spaces = word.strip()
                known_company = False
                for company in COMPANIES.keys():
                    if ( word_no_spaces.lower() == company.lower() ):
                        print(f"{company} stock price is {STOCKS[COMPANIES[company]]}")
                        known_company = True
                    if ( word_no_spaces.lower() == COMPANIES[company].lower()):
                        print(f"{word_no_spaces} is a ticker symbol for {STOCKS[COMPANIES[company]]}")
                        known_company = True
                if not known_company:
                    print(f"{word_no_spaces} is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
    process_query()