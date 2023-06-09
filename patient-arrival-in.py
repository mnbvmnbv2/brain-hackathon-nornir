import requests
import time
import re
import ast
from make_model_and_predict import ArrivalPrediction
import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)
import pandas as pd
import numpy as np

predict_var = ["weekday", "month", "time"]
response = "arrivalrate"

data = pd.read_csv("data/data.csv")

predictor = ArrivalPrediction(data, predict_var, response, 1)

headers = {
    "Synx-Cat": "4",
}

data = {
    "token": "aToken_36d8715e3531fd8e8c01fcbfd26bf5af1908e14f15014d2d14817b568bc0bb0e",
    "objectID": "1",
}

url = "https://randoms-squad.cioty.com/patient-arrival"


def main():
    with requests.post(url, headers=headers, data=data, stream=True) as response:
        for line in response.iter_lines():
            if line:
                # print(line.decode("utf-8"))
                message = line.decode("utf-8")
                if "<SAMPLE>" in message:
                    # Take action based on the message
                    sample = ast.literal_eval(
                        re.search("<SAMPLE>(.*)</SAMPLE>", message).group(1)
                    )
                    time_to_wait = np.random.randint(1, 10)
                    # print(f"predict {time_to_wait} min")
                    pred = predictor.predict_rate(sample)
                    if pred is not None:
                        pred = round(pred[0])
                    print("pred", pred)
                    predictor.sampleIn(sample)
                    print("sample", sample)


if __name__ == "__main__":
    while True:
        main()
        time.sleep(10)
        print("iter")
