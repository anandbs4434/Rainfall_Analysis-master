import pandas as pd
import joblib

def predict_rainfall(year, subdivision):
    model = joblib.load('model.joblib')
    df = pd.DataFrame({
        'YEAR': [year],
        'SUBDIVISION': [subdivision]
    })
    return model.predict(df)[0]


if __name__ == '__main__':
    print(predict_rainfall(2019, 'Andaman & Nicobar Islands'))