
import pandas as pd
import xgboost as xgb

class ArrivalPrediction:
    
    def __init__(self, X, y) -> None:
        self.totData = X
        self.totResponse = y
        self.model = self.make_model(X, y)
    
    def predict_rate(self, df):
        cat_cols = list(df.select_dtypes(exclude="number").columns)
        for col in cat_cols:
            y = pd.get_dummies(df[col], prefix = col)
            df.drop(col, axis = 1)
            df.join(y)
        
        return self.model.predict(df)

    def make_model(self, df, df_y):
        cat_cols = list(df.select_dtypes(exclude="number").columns)
        for col in cat_cols:
            y = pd.get_dummies(df[col], prefix = col)
            df.drop(col, axis = 1)
            df.join(y)
        
        xgb_model = xgb.XGBRegressor(n_estimates = 1000,
                                learning_rate = 0.05,
                                n_jobs = -1)
        xgb_model.fit(df, df_y)
        return xgb_model