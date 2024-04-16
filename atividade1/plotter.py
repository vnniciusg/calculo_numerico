import matplotlib.pyplot as plt
from statistics_calculator import StatisticsCalculator


class Plotter:
    def __init__(self, data, classification: StatisticsCalculator) -> None:
        """
        Initializes the class with the data to be plotted and the statistics calculator for classification.
        Args:
            data (list[float]): Extracted data to be plotted.
            classification (StatisticsCalculator): An instance of StatisticsCalculator used for classification.
        """
        self.data = data
        self.classification = classification

    def plot_graphic(self) -> None:
        """
        Plots a bar graph showing the distribution of data points based on classification.
        Returns:
            None
        """
        inside_range, above_range, below_range = self.calculate_classification_counts()

        categories = ['Dentro', 'Acima', 'Abaixo']
        values = [inside_range, above_range, below_range]

        plt.title('Frequência Cardíaca')
        plt.ylabel('Quantidade de funcionários')

        plt.bar(categories, values, color=['blue', 'red', 'green'])

        plt.show()

    def calculate_classification_counts(self) -> tuple[int, int, int]:
        """
        Calculates the counts of data points classified as 'Dentro', 'Acima', and 'Abaixo'.
        Returns:
            tuple[int, int, int]: A tuple containing the counts for 'Dentro', 'Acima', and 'Abaixo'.
        """
        inside_range = sum(1 for value in self.data if self.classification.show_classification(value) == "Dentro")
        above_range = sum(1 for value in self.data if self.classification.show_classification(value) == "Acima")
        below_range = sum(1 for value in self.data if self.classification.show_classification(value) == "Abaixo")
        return inside_range, above_range, below_range

