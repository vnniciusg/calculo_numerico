import matplotlib.pyplot as plt

TXT_PATH = "data/pulso.txt"
IDEAL_PULSE = 70
VARIATION = 0.11
ACCEPT_RANGE = VARIATION * IDEAL_PULSE
LOWER_LIMIT = IDEAL_PULSE - ACCEPT_RANGE
UPPER_LIMIT = IDEAL_PULSE + ACCEPT_RANGE


def extract_data(path):
    data = []
    with open(path, "r") as file:
        for line in file:
            data_line = line.strip().split("\t")
            data.append(float(data_line[1]))
    return data


def plot_graphic(inside_range, above_range, below_range):
    categories = ['Dentro', 'Acima', 'Abaixo']
    values = [inside_range, above_range, below_range]

    plt.title('Frequência Cardíaca')
    plt.ylabel('Quantidade de funcionarios')

    plt.bar(categories, values, color=['blue', 'red', 'green'])

    plt.show()


def main():
    data = extract_data(TXT_PATH)

    inside_range = sum(1 for i in data if LOWER_LIMIT <= i <= UPPER_LIMIT)
    below_range = sum(1 for i in data if i < LOWER_LIMIT)
    above_range = sum(1 for i in data if i > UPPER_LIMIT)

    plot_graphic(inside_range, above_range, below_range)


if __name__ == "__main__":
    main()
