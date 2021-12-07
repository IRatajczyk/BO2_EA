class TimeSeriesProcessingParameters:
    def __init__(self, model_type: str = "ARIMA"):
        self.model_type = model_type


class TimeSeriesProcessing:
    def __init__(self, parameters: TimeSeriesProcessingParameters):
        self.model_type = parameters.model_type
        self.parameters = parameters

    def process(self, data):
        if self.model_type == "ARIMA":
            return self.__process_arima(data)
        elif self.model_type == "NAIVE":
            return self.__process_naive(data)

    def __process_arima(self, data):
        return None

    def __process_naive(self, data):
        return data

