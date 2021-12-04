class TimeSeriesProcessingParameters:
    def __init__(self, model_type: str = "ARIMA"):
        self.model_type = model_type


class TimeSeriesProcessing:
    def __init__(self, parameters: TimeSeriesProcessingParameters):
        self.model_type = parameters.model_type
        self.parameters = parameters

    def process(self):
        if self.model_type == "ARIMA":
            return self.__process_arima()

    def __process_arima(self):
        return None

