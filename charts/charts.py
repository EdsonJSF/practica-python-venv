import matplotlib.pyplot as plt


def generate_bar_chart(country, labels, values):
    country = country.lower()

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./charts/imgs/{country}_bar.png')
    plt.close()


def generate_pie_chart(continent, labels, values):
    continent = continent.lower().replace(" ", "_")

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig(f'./charts/imgs/{continent}_pie.png')
    plt.close()


if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 40, 800]
    generate_bar_chart("", labels, values)
    generate_pie_chart("", labels, values)
