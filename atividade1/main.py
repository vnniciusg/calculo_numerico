from data_extractor import DataExtractor
from statistics_calculator import StatisticsCalculator
from plotter import Plotter

TXT_PATH = "data/pulso.txt"
IDEAL_MEDIA_PULSE = 70
VARIATION = 0.11


def main():
    data_extractor = DataExtractor(TXT_PATH)
    data = data_extractor.extract_data()

    statistics_calculator = StatisticsCalculator(data, IDEAL_MEDIA_PULSE, VARIATION)
    statistics_calculator.save_error_rates("data/error_rates.txt")

    plotter = Plotter(data, statistics_calculator)
    plotter.plot_graphic()


if __name__ == "__main__":
    main()
