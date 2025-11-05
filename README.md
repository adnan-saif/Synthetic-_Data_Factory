# 🧬 Synthetic Data Factory (SDF)

## 📘 Introduction

The **Synthetic Data Factory (SDF)** is a web application built using **Streamlit** to generate intelligent, realistic, and statistically validated synthetic datasets. It enables users to create, extend, and manipulate data for testing, development, machine learning, and analytics applications. The tool supports CSV uploads, manual column specification, and direct database integration for generating high-quality datasets.

---

## 🎯 Objectives

- Generate synthetic datasets that replicate statistical properties of original data.  
- Support multiple input sources: CSV files, custom columns, and MySQL databases.  
- Provide automated data validation with quality metrics.  
- Enable easy export to CSV or direct insertion into databases.  
- Offer an interactive, visually appealing Streamlit interface.

---

## 🧰 Technologies Used

- **Programming Language**: Python  
- **Frameworks/Libraries**:
  - Streamlit (Web Interface)
  - Pandas, NumPy (Data Handling)
  - Scipy (Statistics)
  - Faker (Synthetic Data Generation)
- **Database**: MySQL via PyMySQL
- **Frontend Design**: Custom CSS, responsive layout
- **IDE/Tools**: VS Code, Jupyter Notebook  

---

## 💻 Web App Features

### 🏠 Home

- Overview of SDF capabilities.
- Key statistics: Supported data types, generation speed, 24/7 availability.
- Core features highlighted with visually engaging cards.
- Step-by-step workflow: Choose Source → Configure → Generate → Download.

### 📄 CSV Extension

- Upload CSV files to extend existing datasets.
- Maintain original distributions and statistical properties.
- Configure number of synthetic rows and output file name.
- Optionally run automated validation.
- Download the generated CSV.

### 🛠 Dummy Data Creation

- Create custom datasets by specifying column names.
- Intelligent detection of column types for realistic data generation.
- Configure number of rows and output filename.
- Generate and download synthetic data.

### 🗄 MySQL Operations

- Connect to MySQL database and list available tables.
- View table schema before generation.
- Generate synthetic data based on table structure.
- Optionally validate against existing data and insert into database.
- Download generated datasets.

### ℹ️ About

- Provides detailed project overview.
- Key features:
  - Statistical validation (KS tests, distribution analysis, quality scoring)
  - Multiple data sources (CSV, database, manual columns)
  - Smart AI-powered column detection and pattern recognition
  - Flexible export options (CSV download, database insertion)
  - Privacy & security (data anonymization, GDPR/CCPA compliant)
- Technology stack displayed with clear visual cards.
- Use cases: Testing & Development, Data Science, Business Intelligence, Privacy & Security.

---

## 📊 How It Works

1. **Choose Source**: CSV upload, manual column creation, or database connection.
2. **Configure**: Set number of rows, validation options, and output preferences.
3. **Generate**: Create and validate synthetic data with quality metrics.
4. **Download**: Export the generated dataset or insert it into a database.

---

## 🖥 How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/synthetic-data-factory.git
cd synthetic-data-factory
