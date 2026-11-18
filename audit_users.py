
import csv
from pathlib import Path

# File locations
BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "sample_users.csv"
OUTPUT_FILE = BASE_DIR / "sample_audit_report.csv"


def audit_accounts():
    findings = []
    seen_usernames = set()

    # Open the CSV file
    with INPUT_FILE.open(
        "r", newline="", encoding="utf-8-sig"
    ) as file:

        reader = csv.DictReader(file)

        # Validate required CSV headers
        required_headers = {"username", "email", "status"}
        actual_headers = set(reader.fieldnames or [])

        missing_headers = required_headers - actual_headers

        if missing_headers:
            raise ValueError(
                "Invalid CSV file. Missing required columns: "
                + ", ".join(sorted(missing_headers))
            )

        # Process each user account
        for row in reader:
            username = (row.get("username") or "").strip()
            email = (row.get("email") or "").strip()
            status = (row.get("status") or "").strip().lower()

            issues = []

            # Check for inactive accounts
            if status == "inactive":
                issues.append("Inactive account")

            # Check for duplicate usernames
            if username.lower() in seen_usernames:
                issues.append("Duplicate username")

            seen_usernames.add(username.lower())

            # Check for missing email addresses
            if not email:
                issues.append("Missing email address")

            # Record accounts with issues
            if issues:
                findings.append({
                    "username": username,
                    "email": email,
                    "status": status,
                    "issues": "; ".join(issues)
                })

    # Generate the audit report
    with OUTPUT_FILE.open(
        "w", newline="", encoding="utf-8"
    ) as file:

        fieldnames = [
            "username",
            "email",
            "status",
            "issues"
        ]

        writer = csv.DictWriter(
            file, fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(findings)

    # Display audit results
    print("Account audit completed successfully!")
    print(f"Issues found in {len(findings)} account records.")
    print(f"Report saved to: {OUTPUT_FILE.name}")


if __name__ == "__main__":
    audit_accounts()
