# METRIX AI – Intelligent Instrument Validation & Risk Analysis System

<p align="center">

**An AI-powered analytics platform for instrument validation, clustering, performance comparison, and risk segmentation.**

</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit)
![Machine Learning](https://img.shields.io/badge/Domain-Machine%20Learning-orange)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

## Overview

**METRIX AI** is an intelligent data analytics and instrument validation platform developed as part of the **Smart India Hackathon (SIH)** project.

The platform focuses on analyzing instrument-related datasets, performing data preprocessing and feature engineering, comparing clustering techniques, validating results, and identifying potential risks through data-driven analysis.

METRIX AI provides an interactive dashboard that helps users explore datasets, evaluate clustering performance, analyze risk categories, and generate analytical reports.

Our objective is to transform raw instrument data into meaningful insights through machine learning techniques and interactive visualizations.

## Key Features

- **Dataset Explorer:** Explore and understand instrument-related datasets.
- **Data Preprocessing:** Clean and prepare datasets for analysis.
- **Feature Engineering:** Extract and transform meaningful features from raw data.
- **Clustering Analysis:** Apply and compare Euclidean and Manhattan distance-based clustering approaches.
- **Risk Segmentation:** Categorize records based on analytical risk indicators.
- **Instrument Validation:** Analyze instrument test records and inspector validation records.
- **Metric Comparison:** Compare clustering and analytical performance metrics.
- **Cluster Optimization:** Experiment with clustering configurations.
- **What-If Simulator:** Explore how changes in input conditions affect analytical outcomes.
- **Data Visualization:** Interactive charts and graphical representations.
- **Report Generation:** Generate and export analytical reports.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend / Dashboard | Streamlit |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Scientific Computing | SciPy |
| Data Visualization | Plotly, Matplotlib |
| Data Format | CSV |
| Version Control | Git & GitHub |

## System Architecture

The project follows a modular architecture:

1. **Data Layer:** Loads synthetic and processed instrument datasets.
2. **Preprocessing Layer:** Handles data preparation and transformation.
3. **Feature Engineering Layer:** Extracts useful analytical features.
4. **Clustering Layer:** Performs clustering using distance-based approaches.
5. **Validation Layer:** Evaluates instrument and inspector validation records.
6. **Risk Analysis Layer:** Performs risk segmentation and analysis.
7. **Visualization Layer:** Presents results through interactive dashboards.
8. **Reporting Layer:** Generates analytical reports and exports.

## Machine Learning & Analytical Methodology

METRIX AI incorporates the following analytical techniques:

### 1. Data Preprocessing
- Dataset loading and inspection.
- Data cleaning and transformation.
- Preparation of structured input features.

### 2. Feature Engineering
- Extraction of relevant features.
- Feature transformation.
- Preparation of data for clustering and analysis.

### 3. Clustering Techniques
- Euclidean Distance-based clustering.
- Manhattan Distance-based clustering.
- Hierarchical clustering experiments.

### 4. Validation & Risk Analysis
- Inspector validation analysis.
- Instrument test record analysis.
- Risk segmentation.
- Metric comparison and analytical reporting.

## Project Structure

```text
METRIX-AI-SIH/
│
├── app.py
├── common.py
├── config.py
├── requirements.txt
├── README.md
│
├── assets/
│   └── styles.css
│
├── data/
│   ├── exports/
│   ├── processed/
│   └── synthetic/
│
├── modules/
│   ├── clustering.py
│   ├── data_loader.py
│   ├── distance_metrics.py
│   ├── feature_engineering.py
│   ├── preprocessing.py
│   ├── report_generator.py
│   ├── risk_segmentation.py
│   └── validation.py
│
├── pages/
│   ├── 1_Data.py
│   ├── 2_Compare_Metrics.py
│   ├── 3_Risk.py
│   ├── 4_Validation.py
│   ├── 5_Reports.py
│   ├── 9_Cluster_Optimizer.py
│   ├── 10_What_If_Simulator.py
│   └── 11_Hierarchical_Experiment.py
│
└── tests/
    ├── test_app.py
    └── test_core.py
```

*Note: The pages directory contains additional experimental and alternative dashboard pages.*

## Installation & Setup

Follow these steps to run METRIX AI locally.

### Prerequisites

- Python 3.13
- Git
- pip

### Step 1: Clone the Repository

```bash
git clone https://github.com/Gabrubois/METRIX-AI-SIH.git
```

### Step 2: Navigate to the Project

```bash
cd METRIX-AI-SIH
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Environment

**Windows:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### Step 5: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 6: Run the Application

```bash
python -m streamlit run app.py
```

Open your browser and visit:

```text
http://localhost:8501
```

## Dataset Information

The project includes structured datasets organized into three categories:

- **Synthetic Data:** Synthetic inspector and instrument records.
- **Processed Data:** Processed features, clustering results, and validation records.
- **Exported Data:** Analytical reports, metric comparisons, and risk analysis outputs.

*Note: Clearly distinguish synthetic demonstration data from real-world instrument records when presenting project results.*

## Application Screenshots

Add screenshots of your actual application below.

| Dashboard | Clustering Analysis |
|---|---|
| ![Dashboard](screenshots/dashboard.png) | ![Clustering](screenshots/clustering.png) |

| Risk Analysis | Reports |
|---|---|
| ![Risk Analysis](screenshots/risk-analysis.png) | ![Reports](screenshots/reports.png) |

*Replace these image paths with your actual screenshots.*

## Testing

Run the test suite using:

```bash
python -m pytest
```

## Future Enhancements

- Integration with real-time instrument datasets.
- Advanced anomaly detection.
- Improved predictive risk assessment.
- Automated validation workflows.
- Enhanced model evaluation and optimization.
- Cloud-based deployment and accessibility.
- Advanced analytical dashboards.

## Project Information

| Detail | Information |
|---|---|
| Project Name | METRIX AI |
| Competition | Smart India Hackathon (SIH) |
| Domain | Artificial Intelligence & Data Analytics |
| Framework | Streamlit |
| Repository | [GitHub – METRIX AI](https://github.com/Gabrubois/METRIX-AI-SIH) |
| Development Status | Active |



We acknowledge the Smart India Hackathon initiative for providing an opportunity to develop innovative, technology-driven solutions to real-world challenges.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

<p align="center">

**METRIX AI – Turning Instrument Data into Intelligent Insights.**

Built with Python, Machine Learning & Streamlit.

</p>
