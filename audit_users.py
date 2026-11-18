
import csv
from pathlib import Path

# Files used by the audit tool
BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "sample_users.csv"
OUTPUT_FILE = BASE_DIR / "sample_audit_report.csv"


def audit_accounts():
    """Check user accounts for common audit issues."""

    findings = []
    seen_usernames = set()

    # Open the sample account data
    with INPUT_FILE.open("r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

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

            # Record any issues found
            if issues:
                findings.append({
                    "username": username,
                    "email": email,
                    "status": status,
                    "issues": "; ".join(issues)
                })

    # Save the audit results
    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
        fieldnames = ["username", "email", "status", "issues"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(findings)

    print("Account audit completed successfully!")
    print(f"Issues found in {len(findings)} account records.")
    print(f"Report saved to: {OUTPUT_FILE.name}")


if __name__ == "__main__":
    audit_accounts()
