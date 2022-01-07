import os
import pandas as pd


class TimeSeriesProcessingParameters:
    def __init__(self, model_type: str = "ARIMA"):
        self.model_type = model_type


class TimeSeries:
    def __init__(self, parameters: TimeSeriesProcessingParameters):
        self.model_type = parameters.model_type
        self.original_data = self.__read_original_data()
        self.forecast = self.__read_forecast()

    def get_forecast(self):
        return self.forecast.values.reshape(-1)

    def get_original_data(self):
        return self.original_data.values

    def __read_original_data(self):
        # to be done
        pass

    def __read_forecast(self):
        if os.path.isfile("data/predictions.csv"):
            return pd.read_csv("data/predictions.csv", index_col=0)
