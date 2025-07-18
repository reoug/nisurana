from flask import Flask,redirect,render_template,request,session,url_for

app = Flask(__name__)
app.config["SECRET_KEY"] = 'secret_key'

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        session['hourlywage'] = request.form['hourlywage']
        session['time'] = request.form['time']
        session['tax'] = request.form['tax']
        hourlywage =int( session['hourlywage'])
        time = float(session['time'])
        tax = float(session['tax']) 
        amountpaid = hourlywage * time    
        total = amountpaid - tax
        session['amountpaid'] = amountpaid
        session['total'] = total
        return redirect(url_for('Viewc'))
    return render_template('Calculate.html')

@app.route('/Viewc')
def Viewc():
    return render_template('Viewc.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000) 