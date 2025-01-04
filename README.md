This project is under development right now.


# InsightFlow: House Price Prediction System

This project, InsightFlow, focuses on developing an end-to-end machine learning pipeline for predicting house prices using property features such as size and location. The pipeline integrates MLOps principles and utilizes tools like ZenML and MLflow to ensure scalability, reproducibility, and robustness.

---

## Project Highlights

### 1. Core Features
- Data Ingestion:
  - Abstracted data ingestion process using the Factory Design Pattern.
  - CSV files are extracted from `.zip` archives and read into Pandas DataFrames.

- Data Inspection:
  - Implemented the Strategy Design Pattern to support multiple inspection strategies:
    - Data Type Inspection: Displays data types and non-null counts.
    - Summary Statistics Inspection: Provides statistical summaries for numerical and categorical columns.

- Missing Values Analysis:
  - Utilized the Template Design Pattern for a structured approach to analyzing missing values.
  - Two key tasks:
    - Identify Missing Values: Counts missing values in each column.
    - Visualize Missing Values: Displays a heatmap to visualize missing data.

---

## Directory Structure

```
└── dhananjay6561-InsightFlow/
    ├── README.md
    ├── requirements.txt
    ├── analysis/
    │   ├── EDA.ipynb
    │   └── analyze_src/
    │       ├── basic_data_inspection.py
    │       └── missing_values_analysis.py
    ├── data/
    │   └── archive.zip
    ├── extracted_data/
    │   └── AmesHousing.csv
    └── src/
        └── ingest_data.py
```

---

## How to Use

### 1. Setup Environment
- Create a Python virtual environment:
  ```bash
  python -m venv insightflow
  ```
- Activate the virtual environment:
  - Windows:
    ```bash
    .\insightflow\Scripts\activate
    ```
  - Linux/Mac:
    ```bash
    source insightflow/bin/activate
    ```
- Install required packages:
  ```bash
  pip install -r requirements.txt
  ```

### 2. Run Scripts
- Data Ingestion:
  ```bash
  python src/ingest_data.py
  ```
- Data Inspection:
  ```bash
  python analysis/analyze_src/basic_data_inspection.py
  ```
- Missing Values Analysis:
  ```bash
  python analysis/analyze_src/missing_values_analysis.py
  ```

---

## Current Features

### Data Ingestion
- Extracts CSV files from `.zip` archives.
- Ensures only one `.csv` file exists in the archive.

### Data Inspection
- Strategy Design Pattern:
  - DataTypeInspectionStrategy: Displays data types and non-null counts.
  - SummaryStatisticsInspectionStrategy: Shows descriptive statistics for numerical and categorical columns.

### Missing Values Analysis
- Template Design Pattern:
  - Abstracted the process of identifying and visualizing missing values.
  - Concrete implementation visualizes missing values using Seaborn's heatmap.

---

## How to Contribute

We welcome contributions to make InsightFlow even better! Here's how you can contribute:

1. Fork the Repository:
   - Click the `Fork` button on the top-right corner of this repository.

2. Clone Your Fork:
   ```bash
   git clone https://github.com/dhananjay6561/InsightFlow.git
   ```

3. Create a Feature Branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. Make Changes and Commit:
   - Make your desired changes.
   - Commit your changes:
     ```bash
     git commit -m "Add your commit message here"
     ```

5. Push Changes and Submit Pull Request:
   ```bash
   git push origin feature/your-feature-name
   ```
   - Go to the original repository and submit a Pull Request.

6. Wait for Review:
   - Your changes will be reviewed, and feedback may be provided.

---

## Outro

Thank you for checking out InsightFlow! We are committed to making machine learning workflows more efficient and reproducible. If you have any suggestions or questions, feel free to open an issue or reach out. Together, we can make this project even better!