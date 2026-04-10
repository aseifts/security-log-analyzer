# security-log-analyzer
Security-focused log analysis engine to parse, normalize, and visualize authentication events.

Security Log Analyzer & Visualization
Overview
A Python-based security tool designed to ingest unstructured system logs, normalize the data, and generate visual intelligence on authentication patterns and potential threats.

Key Features
Log Normalization: Parsers for Auth.log and Syslog using optimized Regular Expressions.

Brute-Force Detection: Identification of high-frequency failure signatures.

Geospatial Analysis: Mapping of source IPs to identify attack origins.

Visual Dashboards: Time-series heatmaps generated via Matplotlib and Pandas.

Tech Stack
Language: Python

Data Processing: Pandas, NumPy

Visualization: Matplotlib, Seaborn

Regex: Standard re library

Installation
Bash
git clone https://github.com/aseifts/security-log-analyzer.git
cd security-log-analyzer
pip install -r requirements.txt
Usage
Place your raw log files in the /logs directory.

Run the analyzer:

Bash
python main.py --file logs/auth.log
View generated reports in the /output folder.
