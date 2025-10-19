# Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Config
DATA_FILE = "buckling_raw_data_group_1.xlsx"
SHEET = 0
DATA_START_ROW = 5
DATA_END_ROW = 10

# Length values
LEN_1 = 8.5      # In column C and D
LEN_2 = 9        # In column E and F
LEN_3 = 12       # In column G and H
LEN_4 = 13.5     # In column I and J

# Range
skiprows = range(0, DATA_START_ROW - 1)
nrows = DATA_END_ROW - DATA_START_ROW + 1

# Read the data
dataF_1 = pd.read_excel(DATA_FILE, sheet_name=SHEET, usecols="D", header=None, skiprows=skiprows, nrows=nrows).iloc[:, 0]
dataF_2 = pd.read_excel(DATA_FILE, sheet_name=SHEET, usecols="F", header=None, skiprows=skiprows, nrows=nrows).iloc[:, 0]
dataF_3 = pd.read_excel(DATA_FILE, sheet_name=SHEET, usecols="H", header=None, skiprows=skiprows, nrows=nrows).iloc[:, 0]
dataF_4 = pd.read_excel(DATA_FILE, sheet_name=SHEET, usecols="J", header=None, skiprows=skiprows, nrows=nrows).iloc[:, 0]

# Convert to numeric & drop NaN
data_1 = pd.to_numeric(dataF_1, errors="coerce").dropna()
data_2 = pd.to_numeric(dataF_2, errors="coerce").dropna()
data_3 = pd.to_numeric(dataF_3, errors="coerce").dropna()
data_4 = pd.to_numeric(dataF_4, errors="coerce").dropna()

# Raw points
x_raw = ([LEN_1] * len(data_1)) + ([LEN_2] * len(data_2)) + ([LEN_3] * len(data_3)) + ([LEN_4] * len(data_4))
y_raw = list(data_1) + list(data_2) + list(data_3) + list(data_4)

# Calculate mean at each length
x_mean = [LEN_1, LEN_2, LEN_3, LEN_4]
y_mean = [data_1.mean(), data_2.mean(), data_3.mean(), data_4.mean()]
y_min = [data_1.min(), data_2.min(), data_3.min(), data_4.min()]
y_max = [data_1.max(), data_2.max(), data_3.max(), data_4.max()]

# Asymmetric bars: lower = mean - min, upper = max - mean
yerr_lower = np.array(y_mean) - np.array(y_min)
yerr_upper = np.array(y_max) - np.array(y_mean)
yerr = np.vstack([yerr_lower, yerr_upper])

# Linear fit to mean values
x_fit = np.array(x_mean, dtype=float)
y_fit = np.array(y_mean, dtype=float)

# Mask out NaNs in y_fit for the linear fit
mask = np.isfinite(y_fit)
slope, intercept = np.polyfit(x_fit[mask], y_fit[mask], 1)

x_line = np.linspace(np.min(x_fit[mask]), np.max(x_fit[mask]))
y_line = slope * x_line + intercept

# Plot
plt.figure()
plt.scatter(x_raw, y_raw, s=25, alpha=0.5, color="gray", label="datas")
plt.plot(x_line, y_line, color="tab:green", linewidth=2, label=f"Linear fit")
plt.errorbar(x_mean, y_mean, yerr=yerr, fmt="o", color="tab:blue", ecolor="tab:blue", capsize=4, label="Mean ± range")
plt.xlabel("Length (in)")
plt.ylabel("p_mean (oz)")
plt.title("Length vs. p_mean")
plt.grid(True)
plt.legend()
plt.show()