from flask import Flask, render_template, jsonify, request, flash, redirect
from forex_python.converter import CurrencyRates,CurrencyCodes
import forex_python
from decimal import *

app = Flask(__name__)
# currencys=['EUR ', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY', 'HUF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AUD', 'CHF', 'KRW', 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'USD', 'NOK', 'RUB', 'INR', 'MXN', 'CZK', 'BRL', 'PLN', 'PHP', 'ZAR']
app.config['SECRET_KEY'] = "password"

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == "POST":
        fromcurr = request.form.get("fromcurr")
        tocurr = request.form.get("tocurr")
        number = request.form.get("number")
        if fromcurr and tocurr and number:
            try:
                c = CurrencyRates(force_decimal=True)
                rate = c.convert(f'{fromcurr}', f'{tocurr}', Decimal(f'{number}'))
                twodecimalnumber = round(float(rate), 2)
                currencysymbol = CurrencyCodes()
                symbol = currencysymbol.get_symbol(f'{tocurr}')
                return render_template('index.html',result = f"{number} {fromcurr} convert to {tocurr} is {symbol}{twodecimalnumber}.")
            except forex_python.converter.RatesNotAvailableError:
                flash(f"{fromcurr} to {tocurr} conversion is currently not available.", 'error')
                return render_template('index.html',result = f"{fromcurr} convert to {tocurr} is not avaliable.")
            except forex_python.converter.DecimalFloatMismatchError:
                flash(f"{fromcurr} to {tocurr} conversion is currently not available.", 'error')
                return render_template('index.html',result = f"{fromcurr} convert to {tocurr} is not avaliable.")
        else:
            flash(f"Error occured")
            return redirect('/index')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
