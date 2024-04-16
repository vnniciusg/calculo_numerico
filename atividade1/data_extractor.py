
class DataExtractor:
    def __init__(self, path: str) -> None:
        """
        Initializes the class with the file path
        Args:
            path (str): the file path
        """
        self.path = path

    def extract_data(self) -> list[float]:
        """
        Performs extract data on file
        Returns:
            data (list[float]): Extracted data
        """
        data = []
        with open(self.path, "r") as file:
            for line in file:
                data_line = line.strip().split("\t")
                data.append(float(data_line[1]))
        return data

