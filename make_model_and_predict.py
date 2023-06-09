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

        # self.update_model(data[predictor], data[response])

    def sampleIn(self, sample):
        self.totData.append(sample, ignore_index=True)
        self.totSample += 1
        if self.totSample % self.updateBuffer == 0:
            self.update_model()

    def predict_rate(self, sample):
        # print(self.model)
        if not self.model is None:
            # try:
            # print("sample", type(sample), sample)
            dct = {k: [v] for k, v in sample.items()}
            X = pd.DataFrame.from_dict(dct)
            # print(X)
            X = X[self.predictor]
            # print("X", type(X))
            pred = self.model.predict(X)
            return pred
        # except:
        #     return None

    def update_model(self):
        xgb_model = xgb.XGBRegressor(n_estimators=1000, learning_rate=0.05, n_jobs=-1)
        xgb_model.fit(self.totData[self.predictor], self.totData[self.response])
        self.model = xgb_model
