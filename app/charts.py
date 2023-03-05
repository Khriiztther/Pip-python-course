import matplotlib.pyplot as plt

def generate_bar(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'{name}bar.png')
    plt.close()

def generate_pie(name, labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig(f'{name}pie.png')
    plt.close()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 295, 800]
    generate_bar(labels, values)
    generate_pie(labels, values)
  