from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def display_excel():
    excel_data = pd.read_excel('./Test Sheet.xlsx')

    html_table = excel_data.to_html(classes='table table-striped', index=False)

    return render_template('index.html', table=html_table)

if __name__ == '__main__':
    app.run(debug=True)
