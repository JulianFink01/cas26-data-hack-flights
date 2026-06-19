import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", "{:.2f}".format)

def reduce_dataset(df: pd.DataFrame) -> pd.DataFrame:
    new_df = df.copy()

    # Add new Rows
    delay_cols = [
        "DEPARTURE_DELAY",
        "ARRIVAL_DELAY",
        "SECURITY_DELAY",
        "AIRLINE_DELAY",
        "LATE_AIRCRAFT_DELAY",
        "WEATHER_DELAY",
        "AIR_SYSTEM_DELAY",
    ]

    delays = new_df[delay_cols].fillna(0)

    new_df["DELAY"] = (
            delays["DEPARTURE_DELAY"] +
            delays["ARRIVAL_DELAY"] +
            delays["SECURITY_DELAY"] +
            delays["AIRLINE_DELAY"] +
            delays["LATE_AIRCRAFT_DELAY"] +
            delays["WEATHER_DELAY"] +
            delays["AIR_SYSTEM_DELAY"]
    ).astype(int)

    # Remove not needed Rows
    new_df.drop(columns=["YEAR"], inplace=True)
    new_df.drop(columns=["SCHEDULED_DEPARTURE"], inplace=True)
    new_df.drop(columns=["DEPARTURE_TIME"], inplace=True)
    new_df.drop(columns=["DEPARTURE_DELAY"], inplace=True)
    new_df.drop(columns=["TAXI_OUT"], inplace=True)
    new_df.drop(columns=["TAXI_IN"], inplace=True)
    new_df.drop(columns=["WHEELS_OFF"], inplace=True)
    new_df.drop(columns=["WHEELS_ON"], inplace=True)
    new_df.drop(columns=["ELAPSED_TIME"], inplace=True)
    new_df.drop(columns=["AIR_TIME"], inplace=True)
    new_df.drop(columns=["ARRIVAL_TIME"], inplace=True)
    new_df.drop(columns=["AIRLINE_DELAY"], inplace=True)
    new_df.drop(columns=["LATE_AIRCRAFT_DELAY"], inplace=True)
    new_df.drop(columns=["DIVERTED"], inplace=True)
    new_df.drop(columns=["CANCELLED"], inplace=True)
    new_df.drop(columns=["CANCELLATION_REASON"], inplace=True)
    new_df.drop(columns=["ARRIVAL_DELAY"], inplace=True)
    new_df.drop(columns=["SECURITY_DELAY"], inplace=True)
    new_df.drop(columns=["WEATHER_DELAY"], inplace=True)
    new_df.drop(columns=["AIR_SYSTEM_DELAY"], inplace=True)
    return new_df



def load_dataset(path: str) -> pd.DataFrame:
    dataset = pd.read_csv(path, low_memory=False)
    dataset = reduce_dataset(dataset)
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

def map_nan(val):
    if val is None:
        return 0
    return 0

def plot_dataset(dataset: pd.DataFrame) -> None:
    new_df = dataset.copy()




    new_df = new_df[0:100000]

    sns.pairplot(new_df)
    plt.show()

def main():
    ds_flights = load_dataset("./data/flights.csv")
    plot_dataset(ds_flights)
    # ds_airports = load_dataset("./data/airports.csv")
    # ds_airlines = load_dataset("./data/airlines.csv")

if __name__ == "__main__":
    main()
