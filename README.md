# Ternary Plot Generator

This project is designed to visualize specific datasets using ternary plots. The data is loaded from Excel files and plotted using matplotlib. It includes functions for loading and converting data (`yukle_ve_donustur`) and for creating ternary plots (`ternary_plot_olustur`).

## Requirements

Before running the project, make sure the following libraries are installed:

- pandas
- matplotlib
- mpltern

You can install these libraries using pip:

```bash
pip install pandas matplotlib mpltern
```

# Usage

The project contains two main functions: `yukle_ve_donustur` for loading and converting data, and `ternary_plot_olustur` for creating the ternary plots.

1. **yukle_ve_donustur(file_path)**: This function loads data from the specified Excel file and converts it into a numpy array. It returns the transposed numpy array of the dataset.

2. **ternary_plot_olustur(t, l, r, data_list, labels, titles)**: This function creates a ternary plot for the specified datasets. It takes the datasets, their labels, and titles as parameters.

# Example Usage

```python
from mpltern.datasets import get_triangular_grid
```
## Data location for the triangular grid
t, l, r = get_triangular_grid()

## Load and parse data
data_np = yukle_ve_donustur("data.xlsx")
lab_data_np = yukle_ve_donustur("lab_data.xlsx")

## Create ternary plot
data_list = [data_np, lab_data_np, data_np]  # Third dataset for curve
labels = ['given data', 'lab data', 'curve for given data']
titles = ['Acetic acid (W/W,%)', 'Water \n(W/W,%)', 'Butyl acetate \n(W/W,%)']
ternary_plot_olustur(t, l, r, data_list, labels, titles)

# Output
![Figure_1](https://github.com/enes-yapici/ternaryPlot/assets/125216116/0df2f2aa-8ea2-430c-b661-0cdd603a9870)

