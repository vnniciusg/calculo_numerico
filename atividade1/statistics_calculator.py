class StatisticsCalculator:
    def __init__(self, data: any, mean: float, variation: float) -> None:
        """
        Initializes the StatisticsCalculator with data, ideal pulse rate, and variation.
        Args:
            data (any): Data to be analyzed.
            mean (int): Mean pulse rate
            variation (float): Acceptable variation from the ideal pulse rate.
        """
        self.data = data
        self.mean = mean
        self.variation = variation
        self.lower_limit, self.upper_limit = self.calculate_variance()

    def calculate_variance(self) -> tuple[float, float]:
        """
        Calculates the variance range based on the ideal pulse rate and variation.
        Returns:
            tuple[float, float]: Lower and upper limits of the acceptable variance range.
        """
        accept_range = self.variation * self.mean
        return self.mean - accept_range, self.mean + accept_range

    def calculate_absolute_error(self, value: float) -> float:
        """
        Calculates the absolute error between the ideal pulse rate and a given value.
        Args:
            value (int): The value to calculate the absolute error for.
        Returns:
            int: The absolute error between the ideal pulse rate and the given value.
        """
        return abs(self.mean - value)

    def calculate_relative_error(self, absolute_err: float) -> float:
        """
        Calculates the relative error between the ideal pulse rate and a given value.
        Args:
            absolute_err: The value to calculate the relative error for.
        Returns:
            float: The relative error between the ideal pulse rate and the given value.
        """
        return (absolute_err / self.mean) * 100

    def show_classification(self, value) -> str:
        """
        Determines the classification of a given value based on the acceptable variance range.
        Args:
            value: The value to classify.
        Returns:
            str: The classification of the value ('Dentro', 'Acima', or 'Abaixo').
        """
        if self.lower_limit <= value <= self.upper_limit:
            return "Dentro"
        elif value < self.lower_limit:
            return "Abaixo"
        else:
            return "Acima"

    def save_error_rates(self, output_file: str) -> None:
        """
        Saves the error rates to a file.
        Args:
            output_file (str): The path to the output file.
        """
        with open(output_file, "w") as file:
            for idx, value in enumerate(self.data, start=1):
                absolute_err = self.calculate_absolute_error(value)
                relative_err = self.calculate_relative_error(absolute_err)
                classification = self.show_classification(value)

                absolute_err_formatted = "{:.2f}".format(absolute_err)
                relative_err_formatted = "{:.2f}%".format(relative_err)

                file.write(f"{idx}\t{absolute_err_formatted}\t{relative_err_formatted}\t{classification}\n")
