from datetime import date
from requests import get, utils
from decimal import Decimal


def currency_rates(currency):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    if f"<CharCode>{currency.upper()}</CharCode>" in content:
        
        currency = currency.upper()
        nominal = int(content.split(currency)[1].split('<Nominal>')[1].split('</Nominal>')[0])
        currency_rate = Decimal(
            content.split(currency)[1].split("<Value>")[1].split("</Value")[0].replace(",", ".")) / nominal
        currency_rate = currency_rate.quantize(Decimal("1.00"))

        date_from_cdr = list(map(int, content.split('Date="')[1].split('"')[0].split(".")))
        currency_date = date(date_from_cdr[2], date_from_cdr[1], date_from_cdr[0])

        return currency_rate, currency_date
    else:
        return None


if __name__ == "__main__":
    result = currency_rates("eur")
    if result is None:
        print(result)
    else:
        print(f"{result[0]}, {result[1]}")
