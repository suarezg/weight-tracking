from tkinter.tix import IMAGE
import matplotlib.pyplot as plt
import pandas as pd
import plotly.figure_factory as ff
from datetime import date

PATH = 'weight-data.csv'
IMAGE_PATH = 'weight-week-avg.png'
AUTOGEN_MD_PATH = "autogen.md"

# Read in weight data and resample to average on weekly basis
w_data = pd.read_csv(PATH, sep=",")
w_data["Date"] = pd.to_datetime(w_data["Date"])
w_data = w_data.set_index("Date")
w_data = w_data.resample("W").mean().dropna(axis="index", how="any")

# calculate weekly difference
diff = w_data.diff()
print(diff)
print(f"Average week-to-week gain: {diff.mean()}")

today = date.today()
today_str = today.strftime('%Y/%m/%d')

# plot data
w_data.plot()
plt.ylabel("Weight (in kg)")
plt.xlabel("Date")
plt.title(f"Weight weekly average")
plt.savefig(IMAGE_PATH)
plt.show()

# EXPORT Data
# auto-generate markdown text to include in README.md
md_text = diff.to_markdown()
out_file = open(AUTOGEN_MD_PATH, "w+")

# Format generated data in markdown
out_file.write(f"## Weight Data (as of {today_str})\n\n")

# create heading and data for diff table
out_file.write(f"### Weekly difference\n")
out_file.write(md_text + "\n\n")

# Create image embedding
out_file.write(f"### Average Weight per week\n")
out_file.write(f"![Weekly weight average plot](weight-week-avg.png)\n\n")

out_file.close()

