# Syslog Insight 📊

**Author:** Denis Naumov  
**Location:** Cologne, Germany  
**Repository:** [github.com/DenisNaumov7777/syslog-insight](https://github.com/DenisNaumov7777/syslog-insight)

---

**Syslog Insight** is a production-grade CLI utility designed to parse, analyze, and report on system logs. Built with Python, it employs an ETL (Extract, Transform, Load) approach to process unstructured log data into structured CSV reports.

This tool is engineered for performance and maintainability, featuring O(1) memory usage for stream processing, strict type hinting, and comprehensive unit testing.

---

## 🚀 Key Features

- **Regex-Based Parsing:** robustly extracts timestamps, hostnames, services, and log levels from raw syslog formats.
- **Memory Efficient:** Processes files line-by-line, making it capable of handling gigabyte-sized logs without memory overflow.
- **Statistical Reporting:** Aggregates error frequencies and exports actionable insights to CSV.
- **CLI Interface:** Fully configurable via command-line arguments using `argparse`.
- **Quality Assurance:** Core logic is verified with `pytest` suite.

---

## 📂 Project Structure

```text
syslog-insight/
├── data/
│   └── syslog.log          # Raw input data
├── src/
│   ├── __init__.py
│   └── analyzer.py         # Core parsing logic (OOP)
├── tests/
│   └── test_analyzer.py    # Unit tests (Pytest)
├── main.py                 # CLI Entry point
├── requirements.txt        # Project dependencies
├── LICENSE                 # MIT License
└── README.md               # Documentation

```

---

## 🛠️ Installation

1. **Clone the repository:**
```bash
git clone [https://github.com/DenisNaumov7777/syslog-insight.git](https://github.com/DenisNaumov7777/syslog-insight.git)
cd syslog-insight

```


2. **Set up a virtual environment (Recommended):**
```bash
python3 -m venv venv
source venv/bin/activate
# On Windows use: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```



---

## 💻 Usage

The tool is driven by the Command Line Interface.

### Standard Analysis

Run the tool pointing to your log file. It will output the top errors to the console and save a full report to CSV.

```bash
python3 main.py --input data/syslog.log --output error_report.csv

```

### Help Menu

To see all available arguments and defaults:

```bash
python3 main.py --help

```

---

## 🧪 Testing

To ensure the integrity of the parsing logic, run the automated test suite:

```bash
pytest tests/ -v

```

---

## 📜 License

This project is distributed under the **MIT License**. See `LICENSE` for more information.


