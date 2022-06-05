import matplotlib.pyplot as plt
import pandas as pd

PATH = 'weight-data.csv'

# Read in weight data and resample to average on weekly basis
w_data = pd.read_csv(PATH, sep=",")
w_data["Date"] = pd.to_datetime(w_data["Date"])
w_data = w_data.set_index("Date")
w_data = w_data.resample("W").mean().dropna(axis="index", how="any")


# calculate weekly difference
diff = w_data.diff()
print(diff)
print(f"Average week-to-week gain: {diff.mean()}")


# plot data
w_data.plot()
plt.ylabel("Weight (in kg)")
plt.xlabel("Date")
plt.title("Weight on weekly average")
plt.savefig("weight-week-avg.png")
plt.show()




