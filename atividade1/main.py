import matplotlib.pyplot as plt

TXT_PATH = "data/pulso.txt"
IDEAL_MEDIA_PULSE = 70
VARIATION = 0.11


def extract_data(path):
    data = []
    with open(path, "r") as file:
        for line in file:
            data_line = line.strip().split("\t")
            data.append(float(data_line[1]))
    return data


def calculate_mean(data):
    return sum(data) / len(data)


def calculate_variance(mean, variation):
    accept_range = variation * mean
    return mean - accept_range, mean + accept_range


def calculate_absolute_error(mean, value):
    return abs(mean - value)


def calculate_relative_error(absolute_err, mean):
    return (absolute_err / mean) * 100


def show_classification(lower_limit, upper_limit, value):
    if lower_limit <= value <= upper_limit:
        return "Dentro"
    elif value < lower_limit:
        return "Abaixo"
    else:
        return "Acima"


def plot_graphic(inside_range, above_range, below_range):
    categories = ['Dentro', 'Acima', 'Abaixo']
    values = [inside_range, above_range, below_range]

    plt.title('Frequência Cardíaca')
    plt.ylabel('Quantidade de funcionarios')

    plt.bar(categories, values, color=['blue', 'red', 'green'])

    plt.show()


def main():
    data = extract_data(TXT_PATH)

    mean = calculate_mean(data)

    lower_limit, upper_limit = calculate_variance(IDEAL_MEDIA_PULSE, VARIATION)

    with open("data/errors.txt", "w") as file:
        for idx, value in enumerate(data, start=1):
            absolute_err = calculate_absolute_error(IDEAL_MEDIA_PULSE, value)
            relative_err = calculate_relative_error(absolute_err, IDEAL_MEDIA_PULSE)
            classification = show_classification(lower_limit , upper_limit , value)

            absolute_err_formatted = "{:.2f}".format(absolute_err)
            relative_err_formatted = "{:.2f}".format(relative_err)

            file.write("{}\t{}\t{}\t{}\n".format(idx, absolute_err_formatted, relative_err_formatted, classification))

    inside_range = sum(1 for i in data if lower_limit <= i <= upper_limit)
    below_range = sum(1 for i in data if i < lower_limit)
    above_range = sum(1 for i in data if i > upper_limit)

    plot_graphic(inside_range, above_range, below_range)


if __name__ == "__main__":
    main()
