import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_dataset() -> pd.DataFrame:
    dataset = pd.read_csv("./data/flights.csv", low_memory=False)
    return dataset

def describe_dataset(dataset: pd.DataFrame):
    print(dataset.describe())
    print("-----")
    print(dataset.head())

def plot_dataset(dataset: pd.DataFrame) -> None:
    sns.pairplot(dataset)
    plt.show()

def main():
    ds = load_dataset()
    describe_dataset(ds)
    plot_dataset(ds)

if __name__ == "__main__":
    main()
