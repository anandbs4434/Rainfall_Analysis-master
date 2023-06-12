from flask import Flask, render_template,request
import pandas as pd
import  plotly.express as px
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

def predict_rainfall(year, subdivision):
    model = joblib.load('model.joblib')
    df = pd.DataFrame({
        'YEAR': [year],
        'SUBDIVISION': [subdivision]
    })
    return model.predict(df)[0]

def load_data():
    df = pd.read_csv('dataset/data.csv')
    return df 

@app.route('/')
def index():
    return render_template('home.html')
    
@app.route('/graphs')
def graph1():
    rain=  load_data()
    grouped_obj = rain.groupby(["YEAR"]).sum()
    grouped_obj.drop(['ANNUAL'], axis=1, inplace=True)
    month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT','NOV', 'DEC']
    fig1 = px.area(grouped_obj, x=grouped_obj.index, y=month, title='Rainfall YEAR-wise',labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows  monthly rainfall.'
    fig1.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    grouped_obj = rain.groupby(["YEAR"]).sum()
    fig2 = px.area(grouped_obj, x=grouped_obj.index, y='ANNUAL', title='Rainfall year-wise')
    conclusion = 'The graph shows the yearly rainfall.'
    fig2.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    fig3 = px.bar(grouped_obj, x=grouped_obj.index, y='ANNUAL', title='Rainfall year-wise')
    conclusion = 'The graph shows the yearly rainfall.'
    fig3.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT','NOV', 'DEC']
    fig4 = px.bar(grouped_obj, x=grouped_obj.index, y=month, title='Rainfall month-wise',labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows the monthly rainfall.'
    fig4.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN']
    fig5 = px.bar(grouped_obj, x=grouped_obj.index, y=month, title='Rainfall semi-annual',labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows the monthly rainfall.'
    fig5.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month = ['JUL', 'AUG', 'SEP', 'OCT','NOV', 'DEC']
    fig6 = px.bar(grouped_obj, x=grouped_obj.index, y=month, title='Rainfall semi-annual',labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows the monthly rainfall.'
    fig6.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month = ['JAN', 'FEB', 'MAR']
    fig7 = px.bar(grouped_obj, x=grouped_obj.index, y=month, title='Rainfall quater-wise',labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows the monthly rainfall.'
    fig7.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month = ['APR', 'MAY', 'JUN']
    fig8 = px.bar(grouped_obj, x=grouped_obj.index, y=month, title='Rainfall quater-wise',labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows the monthly rainfall.'
    fig8.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month = ['JUL', 'AUG', 'SEP']   
    fig9 = px.bar(grouped_obj, x=grouped_obj.index, y=month, title='Rainfall quater-wise',labels={'index':'YEAR', 'value':' Rainfall (in mm)'})
    conclusion = 'The graph shows the monthly rainfall.'
    fig9.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month = ['OCT','NOV', 'DEC']
    fig10 = px.bar(grouped_obj, x=grouped_obj.index, y=month, title='Rainfall quater-wise',labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows the monthly rainfall.'
    fig10.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    fig11 = px.scatter(grouped_obj, x=grouped_obj.index, y='ANNUAL', title='Rainfall year-wise')
    conclusion = 'The graph shows the yearly rainfall.'
    fig11.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month=['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG','SEP', 'OCT','NOV', 'DEC']
    fig12 = px.ecdf(grouped_obj, x=grouped_obj.index,y=month, title='Rainfall Yearly')
    conclusion = 'The graph shows the yearly rainfall.'
    fig12.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    fig13 = px.area(grouped_obj, x=grouped_obj.index, y='ANNUAL', title='Yearly rainfall state-wise')
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig13.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    fig14 = px.area(rain, x='SUBDIVISION', y=['ANNUAL'], title='Average Rainfall ',labels={'value':'Rainfall in mm'})
    mean_rainfall = rain['ANNUAL'].mean()
    fig14.add_annotation(xref='paper', yref='paper', x=0.1, y=1, text=f"Average Rain = {mean_rainfall:.0f}",showarrow=False)

    fig15 = px.bar(grouped_obj, x=grouped_obj.index, y='ANNUAL', title='State-wise')
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig15.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    fig16 = px.line(grouped_obj, x=grouped_obj.index, y='ANNUAL', title='Rainfall year-wise')
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig16.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT','NOV', 'DEC']
    fig17 = px.bar(grouped_obj, x=grouped_obj.index, y=month, title='State-wise',height=600,labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig17.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN']
    fig18 = px.funnel(grouped_obj, x=grouped_obj.index, y=month, title='State-wise',height=600)
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig18.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month = ['JUL', 'AUG', 'SEP', 'OCT','NOV', 'DEC']
    fig19 = px.funnel(grouped_obj, x=grouped_obj.index, y=month, title='State-wise',height=600)
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig19.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG','SEP', 'OCT','NOV', 'DEC']
    fig20 = px.density_contour(grouped_obj, x=grouped_obj.index, y=month, title='State-wise',height=600,labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig20.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN']
    fig21 = px.ecdf(grouped_obj,x=grouped_obj.index, y=month, title='State-wise',height=600)
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig21.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month = ['JUL', 'AUG', 'SEP', 'OCT','NOV', 'DEC']
    fig22 = px.ecdf(grouped_obj,x=grouped_obj.index, y=month, title='State-wise',height=600)
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig22.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month = ['JAN', 'FEB', 'MAR'] 
    fig23 = px.line(grouped_obj, x=grouped_obj.index, y=month, title='Rainfall quaterly-wise',labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig23.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month=['APR', 'MAY', 'JUN']
    fig24 = px.line(grouped_obj, x=grouped_obj.index, y=month, title='Rainfall quater-wise',labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig24.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month=['JUL', 'AUG', 'SEP']
    fig25 = px.line(grouped_obj, x=grouped_obj.index, y=month, title='Rainfall quater-wise',labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig25.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month=['OCT','NOV', 'DEC']
    fig26 = px.line(grouped_obj, x=grouped_obj.index, y=month, title='Rainfall quater-wise',labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows rainfall from every year.'
    fig26.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    return render_template('graphs.html', fig1=fig1.to_html(),
                           fig2 = fig2.to_html(),
                            fig3 = fig3.to_html(),
                            fig4 = fig4.to_html(),
                            fig5 = fig5.to_html(),
                            fig6 = fig6.to_html(),
                            fig7 = fig7.to_html(),
                            fig8 = fig8.to_html(),
                            fig9 = fig9.to_html(),
                            fig10 = fig10.to_html(),
                            fig11 = fig11.to_html(),
                            fig12 = fig12.to_html(),
                            fig13 = fig13.to_html(),
                            fig14 = fig14.to_html(),
                            fig15 = fig15.to_html(),
                            fig16 = fig16.to_html(),
                            fig17 = fig17.to_html(),
                            fig18 = fig18.to_html(),
                            fig19 = fig19.to_html(),
                            fig20 = fig20.to_html(),
                            fig21 = fig21.to_html(),
                            fig22 = fig22.to_html(),
                            fig23 = fig23.to_html(),
                            fig24 = fig24.to_html(),
                            fig25 = fig25.to_html(),
                            fig26 = fig26.to_html())


def retreive_data():
    df = pd.read_csv('dataset/rainfall_India_2017.csv')
    return df 


@app.route('/eda/1')
def eda1():
    return render_template('eda1.html')   

# predict
@app.route('/predict', methods=['GET','POST'])
def predict():
    subdivisions = load_data()['SUBDIVISION'].unique()
    years = list(range(2050, 1990, -1))
    prediction = None
    if request.method == 'POST':
        year = int(request.form['year'])
        subdivision = request.form['subdivision']
        prediction = predict_rainfall(year, subdivision)
        return render_template('predict.html', prediction=prediction, year=year, subdivision=subdivision, subdivisions=subdivisions, years=years)
    return render_template('predict.html', subdivisions=subdivisions, years=years)  


    


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)