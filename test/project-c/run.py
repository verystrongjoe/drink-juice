import csv

def load_csv_file(fname):
    f = open(fname, encoding="utf-8")
    reader = csv.reader(f)
    lines = list(reader)
    f.close()
    return lines


def generate_csv_file_names(year, month):
    return year + month + ".csv"


def select_portfolio_by_low_per_pbr(investment, year, month, count):
    fname = generate_csv_file_names(year, month)
    lines = load_csv_file(fname)

    #------------------------------------------------------------------------------------------------------------------
    # per이 2.5 이상 10이하인 종목 선정
    #------------------------------------------------------------------------------------------------------------------
    portfolio_by_low_per = []
    for line in lines[1:]:
        code = line[1]
        per = line[6]
        pbr = line[8]
        close = line[4]
        close = int(close.replace(",", ""))
        per = per.replace(",", "")

        if per != '-' and (2.5 < float(per) < 10):
            portfolio_by_low_per.append([code, per, pbr, close])

    #------------------------------------------------------------------------------------------------------------------
    # 2.5 < PER <10 인 종목 중 PBR이 낮은 종목 30개 선정
    #------------------------------------------------------------------------------------------------------------------
    portfolio_by_low_per_pbr = sorted(portfolio_by_low_per, key=lambda x:x[2])
    portfolio_by_low_per_pbr = portfolio_by_low_per_pbr[:count]


    #------------------------------------------------------------------------------------------------------------------
    # 선종 종목에 대해서 투자금/N 금액으로 매수 시도
    #------------------------------------------------------------------------------------------------------------------
    for stock in portfolio_by_low_per_pbr:
        amount = investment / count
        close = stock[3]
        shares = int(amount / close)
        stock.append(shares)

    # code/per/pbr/close/shares
    return portfolio_by_low_per_pbr


def get_close_price(lines, code):
    for line in lines[1:]:
        cur_code = line[1]
        close = line[4]
        close = int(close.replace(",", ""))

        if cur_code  == code:
            return close


def rebalancing(investment, portfolio, year, month):
    fname = generate_csv_file_names(year, month)
    lines = load_csv_file(fname)

    cur_investment = 0

    for stock in portfolio:
        code = stock[0]
        #buy_close = stock[3]
        shares = stock[4]
        sel_close = get_close_price(lines, code)
        cur_eval = sel_close * shares
        cur_investment += cur_eval

    print("총 투자 금액: ", investment)
    print("총 평가 금액: ", cur_investment)

if __name__ == "__main__":
    investment = 150000000
    portfolio = select_portfolio_by_low_per_pbr(investment, "2017", "01", 30)

    for i in range(2, 8):
        month = "0" + str(i)
        rebalancing(investment, portfolio, "2017", month)




