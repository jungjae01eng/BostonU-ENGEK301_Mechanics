# Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Config
DATA_FILE = "assets/buckling_raw_data_group_1.xlsx"
SHEET = 0
DATA_START_ROW = 5
DATA_END_ROW = 10

# Length values
LEN_1 = 8.5      # In column C and D
LEN_2 = 9        # In column E and F
LEN_3 = 12       # In column G and H
LEN_4 = 13.5     # In column I and J

# Range
skiprow = range(0, DATA_START_ROW - 1)
nrow = DATA_END_ROW - DATA_START_ROW + 1

# Read the data
dataF_1 = pd.read_excel(DATA_FILE, sheet_name=SHEET, usecols="D", skiprows=skiprow, nrows=nrow).iloc[:, 0]
dataF_2 = pd.read_excel(DATA_FILE, sheet_name=SHEET, usecols="F", skiprows=skiprow, nrows=nrow).iloc[:, 0]
dataF_3 = pd.read_excel(DATA_FILE, sheet_name=SHEET, usecols="H", skiprows=skiprow, nrows=nrow).iloc[:, 0]
dataF_4 = pd.read_excel(DATA_FILE, sheet_name=SHEET, usecols="J", skiprows=skiprow, nrows=nrow).iloc[:, 0]

# Convert data to numeric & drop any missing values (NaN)
data_1 = pd.to_numeric(dataF_1, errors="coerce").dropna()
data_2 = pd.to_numeric(dataF_2, errors="coerce").dropna()
data_3 = pd.to_numeric(dataF_3, errors="coerce").dropna()
data_4 = pd.to_numeric(dataF_4, errors="coerce").dropna()

# x and y values for plotting
x_raw = ([LEN_1] * len(data_1)) + ([LEN_2] * len(data_2)) + ([LEN_3] * len(data_3)) + ([LEN_4] * len(data_4))
y_raw = list(data_1) + list(data_2) + list(data_3) + list(data_4)

# Calculate Mean
x_mean = [LEN_1, LEN_2, LEN_3, LEN_4]
y_mean = [data_1.mean(), data_2.mean(), data_3.mean(), data_4.mean()]

# Plotting
plt.figure()
plt.scatter(x_raw, y_raw, s=25, alpha=0.5, label="datas")
plt.plot(x_mean, y_mean, marker="o", linestyle="-", label="mean values")
plt.xlabel("Length (in)")
plt.ylabel("p_mean (oz)")
plt.title("Length vs. p_mean")
plt.grid(True)
plt.legend()
plt.show()