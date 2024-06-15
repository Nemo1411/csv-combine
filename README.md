# csv-combine
Voici un exemple de fichier README pour votre script Python que vous pouvez publier sur GitHub:

```markdown
# Combine CSV Files Script

This Python script combines all CSV files in a specified folder into a single CSV file and removes duplicate rows.

## Features

- Combines multiple CSV files into one.
- Removes duplicate rows to ensure the output file has unique entries.

## Requirements

- Python 3.x
- pandas library

## Installation

1. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).
2. Install the `pandas` library using pip:

   ```bash
   pip install pandas
   ```

## Usage

1. Clone this repository or download the script.
2. Modify the `input_folder` and `output_file` variables in the script to specify the path to your folder containing the CSV files and the path where you want to save the combined CSV file.

   ```python
   input_folder = 'path/to/your/folder'  # Replace with the path to your folder containing CSV files
   output_file = 'path/to/your/output/combined_file.csv'  # Replace with the path to your output CSV file
   ```

3. Run the script:

   ```bash
   python combine_csv_files.py
   ```

## Example

Assuming your folder structure is as follows:

```
/path/to/your/folder/
    file1.csv
    file2.csv
    file3.csv
```

And you set the `input_folder` to `/path/to/your/folder` and `output_file` to `/path/to/your/output/combined_file.csv`, the script will combine `file1.csv`, `file2.csv`, and `file3.csv` into a single file `combined_file.csv` and save it to `/path/to/your/output/`.


## Author

Your Name - [your-email@example.com](mailto:ryaneirbouh@gmail.com)
