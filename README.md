
# User Account Audit Tool

A Python-based IT automation project that simulates an
Identity and Access Management (IAM) audit using fictional
employee account data.

## Project Overview

This project demonstrates how Python can automate basic
user account auditing tasks, identify potential account
management issues, and generate a structured CSV report.

The tool was developed as a hands-on learning project
to strengthen Python scripting, troubleshooting,
testing, and IT automation skills.

## Features

- Identifies inactive user accounts
- Detects duplicate usernames (case-insensitive)
- Flags accounts with missing email addresses
- Validates required CSV column headers
- Stops execution when required headers are missing
- Generates a CSV report of identified issues
- Runs through GitHub Actions without requiring
  a local Python installation

## Technologies Used

- **Python 3** - Automation and data processing
- **CSV** - Structured account data and reporting
- **GitHub** - Version control and documentation
- **GitHub Actions** - Automated workflow execution
- **IAM Concepts** - User account auditing
- **Exception Handling** - Input validation and errors

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

1. The Python script reads fictional employee account
   information from `sample_users.csv`.
2. It validates that the required CSV headers exist:
   `username`, `email`, and `status`.
3. If required headers are missing, the script raises
   a `ValueError` and stops execution.
4. If the file is valid, the script checks each account
   for inactive status, duplicate usernames, and
   missing email addresses.
5. It records all identified issues.
6. It generates `sample_audit_report.csv`.
7. GitHub Actions allows the script to run manually
   and provides the report as a downloadable artifact.

## Running the Audit

### Run Using GitHub Actions

1. Open this repository in GitHub.
2. Select the **Actions** tab.
3. Choose **User Account Audit**.
4. Click **Run workflow**.
5. Select the `main` branch.
6. Wait for the workflow to complete.
7. Download the generated report from the
   **Artifacts** section.

### Run Locally

With Python 3 installed, run:

```bash
python audit_users.py
```

The script reads `sample_users.csv` and writes
`sample_audit_report.csv` in the project directory.

## Testing and Results

The tool was tested using eight fictional user
account records.

### Verified Audit Findings

| Issue Type | Findings |
|---|---:|
| Inactive accounts | 3 |
| Missing email addresses | 2 |
| Duplicate usernames | 1 |
| **Total individual issues** | **6** |

Five account records were flagged, with one record
containing multiple issues.

The generated CSV report was reviewed to verify
the expected findings.

## Input Validation and Error Handling

The script includes CSV header validation to prevent
incorrect reports from being generated when required
columns are missing.

Two test scenarios were completed to verify the
script's behavior.

### Test 1: Valid CSV Input

**Objective:** Confirm the script successfully
processes correctly formatted account data.

**Test Data:** Eight fictional employee accounts
with valid CSV column headers.

**Expected Result:**
- Script completes successfully
- Audit report is generated
- Five account records are flagged
- Six individual issues are identified

**Actual Result: PASSED**

GitHub Actions completed successfully, and the
generated report contained the expected findings.

### Test 2: Invalid CSV Input

**Objective:** Verify that the script detects
missing required CSV headers.

**Test Procedure:**

1. Created a separate GitHub branch named
   `test-invalid-csv`.
2. Changed the CSV header from `email` to
   `email_address`.
3. Committed the intentionally invalid CSV.
4. Executed the GitHub Actions workflow using
   the testing branch.
5. Reviewed the workflow execution logs.

**Expected Result:**

The script should detect the missing `email`
column, stop execution, and display an error.

**Actual Result: PASSED**

The script produced the following error:

```text
ValueError: Invalid CSV file. Missing required columns: email
```

GitHub Actions reported:

```text
Error: Process completed with exit code 1.
```

The report upload step was skipped because
the audit script failed validation.

This confirmed that the program correctly
rejects input missing required headers.

### Testing Approach

A separate GitHub branch was used for negative
testing to protect the functioning `main` branch.

Testing demonstrated:

- Positive and negative test scenarios
- Input validation
- Python exception handling
- Expected versus actual result verification
- GitHub Actions troubleshooting
- Safe testing using Git branches

## Troubleshooting Experience

During initial development, the GitHub Actions
workflow executed successfully, but the generated
report contained incorrect account information.

### Problem

The original CSV input file contained an empty
first line, causing Python's CSV reader to
interpret the column headers incorrectly.

### Investigation

Reviewed the generated audit report and inspected
the CSV input file in GitHub to identify the
source of the incorrect results.

### Resolution

Removed the blank first line so the expected
column headers appeared at the beginning
of the CSV file.

### Verification

Reran the GitHub Actions workflow and confirmed
the report correctly identified six individual
issues across five account records.

### Preventive Improvement

Added required-header validation to the Python
script so files with missing required columns
cause an explicit error instead of silently
generating misleading results.

The improvement was tested using both valid
and intentionally invalid CSV input.

## Skills Demonstrated

### Python and Automation
- Python scripting fundamentals
- CSV data processing
- Conditional logic
- Sets and duplicate detection
- File input and output
- Exception handling
- Input validation

### IT and Security
- Identity and Access Management concepts
- User account auditing
- Inactive account identification
- Data quality verification
- Basic account review procedures

### Development and Testing
- GitHub version control
- Git branching
- GitHub Actions workflow configuration
- Positive and negative testing
- Debugging and troubleshooting
- Test result verification
- Technical documentation

## Security and Privacy

All account information used in this project
is fictional and was created for testing.

No real employee, student, or organizational
account data is included.

This project demonstrates introductory IAM
auditing concepts and is not intended to
replace a production identity management
or security auditing system.

## Future Improvements

Potential enhancements include:

- Detect blank or malformed account records
- Validate unexpected CSV column names
- Detect invalid account status values
- Add configurable audit rules
- Generate automated summary statistics
- Create automated unit tests
- Support larger account datasets
- Export additional report formats

## Career Development

This project was created to develop practical
IT automation skills that complement professional
experience in technical support, user account
management, and troubleshooting.

It demonstrates the ability to build a functional
Python automation tool, configure a GitHub Actions
workflow, investigate unexpected results,
implement input validation, and verify
successful error handling.

These skills support continued professional
development toward advanced technical support,
systems administration, and IT automation roles.
