import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option("display.max_columns", None)

def load_dataset(path: str) -> pd.DataFrame:
    dataset = pd.read_csv(path, low_memory=False)
    describe_dataset(dataset, path)
    return dataset

def describe_dataset(dataset: pd.DataFrame, path: str):
    print(f"DESCRIBE========={path}")
    print(dataset.describe())
    print("HEAD=========")
    print(dataset.head())
    print("TAIL=========")
    print(dataset.tail())
    print("==============")



def plot_dataset(dataset: pd.DataFrame) -> None:

    new_df = dataset.copy()
    new_df['DELAY'] = new_df[1 if new_df['DEPARTURE_DELAY'] > 0 or new_df['ARRIVAL_DELAY'] > 0 or new_df['SECURITY_DELAY'] > 0 or new_df['AIRLINE_DELAY'] > 0 or new_df['WEATHER_DELAY'] > 0 else 0]

    plt.scatter(x=new_df['AIRLINE'], y=new_df['DELAY'])
    plt.show()

def main():
    ds_flights = load_dataset("./data/flights.csv")
    plot_dataset(ds_flights)
    # ds_airports = load_dataset("./data/airports.csv")
    # ds_airlines = load_dataset("./data/airlines.csv")

if __name__ == "__main__":
    main()
