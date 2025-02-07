# sisense-automl

`sisense-automl` is a Python package for automating machine learning processes using Sisense and AutoML. It provides easy-to-use interfaces for data preprocessing, model training, and evaluation.

## ⚠️ Disclaimer
This package is **not an official feature supported by Sisense**. It is an independent project demonstrating how AutoML can be integrated with Sisense. Use at your own discretion, and note that Sisense does not provide support for this package.

## ⚠️ Compatibility Warning
This package requires **Python 3.9** to function correctly. Please ensure you are using the correct Python version.

**Why only Python 3.9?**
- **Auto-sklearn** does not support Python 3.10 or newer.
- **Scikit-learn 0.24.0** (required by Auto-sklearn) works best with Python 3.9.
- **NumPy 1.23+** removed `numpy.distutils`, which some dependencies rely on.

## Features

- Preprocesses data by handling duplicates, splitting numerical and categorical features, and encoding them appropriately.
- Splits data into training and testing sets.
- Uses auto-sklearn for training classification and regression models.
- Saves trained models and datasets for later use.

## Installation

You can install the package using pip:

```sh
pip install sisense-automl
```

## System-Level Dependencies

Before installing the package, make sure you have the following system-level dependencies:

```sh
sudo apt-get install swig -y
```

## Python-Level Dependencies

The package will automatically install the required Python dependencies as specified in `setup.py`.

## Usage

Here is a basic example of how to use the 'sisense-automl' package:

```python
import pandas as pd
from sisense_automl import AutoMl

# Load your dataset
data = pd.read_csv("your_dataset.csv")

# Define your target column and objective
target_column = "target"
objective = "classification"  # or "regression"

# Define the folder path to save models and data
folder_path = "your_folder_path"

# Create an AutoMl instance and run the process
automl = AutoMl(data, target_column, objective, folder_path)
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Author
Himanshu Negi - himanshu.negi.08@gmail.com

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
