import os

from flask import Flask, render_template

app = Flask(__name__)

CUSTOMERS_FOLDER = os.path.join('static')
BILLING_FOLDER = os.path.join('static', 'billings')
TRANSACTIONS = os.path.join('static', 'transactions')
SMS_FOLDER = os.path.join('static', 'sms')

@app.route('/')
def index():
    images  = []
    for filename in os.listdir(CUSTOMERS_FOLDER):
        if filename.endswith('.png'):
            images.append(filename)

    return render_template('index.html',  active_page='dashboard', images=images)

@app.route('/transactions')
def transactions():
    images  = []
    processed = []
    successful = []
    pending = []
    for filename in os.listdir(TRANSACTIONS):
        if filename.strip():
            if filename.endswith('.png'):
                if 'processed' in filename.lower():
                    processed.append(filename)
                elif 'successful' in filename.lower():
                    successful.append(filename)
                elif 'pending' in filename.lower():
                    pending.append(filename)
                else:
                    images.append(filename)

    return render_template('transactions.html', active_page='transactions', images = images, processed=processed, successful=successful, pending = pending)

@app.route('/sms')
def sms():
    images  = []
    for filename in os.listdir(SMS_FOLDER):
        if filename.endswith('.png'):
            images.append(filename)

    return render_template('sms.html', active_page='sms', images = images)

@app.route('/billings')
def billings():
    images = []
    for filename in os.listdir(BILLING_FOLDER):
        if filename.endswith('.png'):
            images.append(filename)

    return render_template('billings.html', active_page='billings', images=images)

if __name__ == '__main__':
    app.run(debug=False, port=5000)
