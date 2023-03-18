import pandas as pd
import xgboost as xgb

class ArrivalPrediction:
    
    def __init__(self, data, predictor, response, updateBuffer) -> None:
        self.totData = data
        self.model = None
        self.predictor = predictor
        self.response = response
        self.totSample = data.shape[0]
        self.updateBuffer = updateBuffer
        
        self.update_model(data[predictor], data[response])
    
    def sampleIn(self, sample):
        self.totData = self.totData.concat(pd.DataFrame(sample))
        self.totSample += 1
        if self.totSample % self.updateBuffer == 0:
            self.update_model()
    
    def predict_rate(self, sample):
        return self.model.predict(sample)

    def update_model(self):
        xgb_model = xgb.XGBRegressor(n_estimates = 1000,
                                learning_rate = 0.05,
                                n_jobs = -1)
        xgb_model.fit(self.totData[self.predictor], self.totData[self.response])
        self.model = xgb_model