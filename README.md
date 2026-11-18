# User Account Audit Tool

A Python-based IT automation project that simulates an Identity and Access Management (IAM) audit using fictional employee account data.

## Project Overview

This project demonstrates how Python can automate basic user account auditing tasks, identify potential account management issues, and generate a structured CSV report.

The tool was developed as a hands-on learning project to strengthen Python scripting, troubleshooting, and IT automation skills.

## Features

- Identifies inactive user accounts
- Detects duplicate usernames
- Flags accounts with missing email addresses
- Generates a CSV report of identified issues
- Runs through GitHub Actions without requiring a local Python installation

## Technologies Used

- **Python 3** — Automation and data processing
- **CSV** — Structured user account data and reporting
- **GitHub** — Source control and project documentation
- **GitHub Actions** — Automated script execution and report generation

## Project Structure

```text
user-account-audit-tool/
├── .github/
│   └── workflows/
│       └── account-audit.yml
├── README.md
├── audit_users.py
├── sample_users.csv
└── sample_audit_report.csv
```

## How It Works

1. The Python script reads fictional account information from `sample_users.csv`.
2. It evaluates each account for inactive status, duplicate usernames, and missing email addresses.
3. It records identified issues.
4. It generates `sample_audit_report.csv`.
5. GitHub Actions allows the audit to be executed manually and provides the generated report as a downloadable artifact.

## Running the Audit

1. Open this repository in GitHub.
2. Select the **Actions** tab.
3. Choose **User Account Audit**.
4. Select **Run workflow** on the `main` branch.
5. Wait for the workflow to complete.
6. Download the generated audit report from the workflow's **Artifacts** section.

The script can also be run locally with Python installed:

```bash
python audit_users.py
```

## Testing and Results

The tool was tested using eight fictional user account records.

The completed audit successfully identified:

| Issue Type | Findings |
|---|---:|
| Inactive accounts | 3 |
| Missing email addresses | 2 |
| Duplicate usernames | 1 |
| **Total individual issues** | **6** |

Five account records were flagged, with one record containing multiple issues.

The generated CSV report was reviewed to verify the expected findings.

## Troubleshooting Experience

During initial testing, the GitHub Actions workflow executed successfully, but the generated report contained incorrect account information.

**Problem:** The CSV input file contained an empty first line, causing Python's CSV reader to interpret the column headers incorrectly.

**Investigation:** Reviewed the generated audit report and inspected the original CSV file in GitHub.

**Resolution:** Removed the blank first line so the expected column headers appeared at the beginning of the file.

**Verification:** Reran the GitHub Actions workflow and confirmed that the generated report correctly identified all six expected issues across five account records.

This experience demonstrated the importance of validating input data, investigating unexpected output, and
