import os
import hashlib
import json
from datetime import datetime

DIRECTORY = "files"
BASELINE_FILE = "baseline.json"

# Severity mapping
SEVERITY = {
    "NEW FILE DETECTED": ("MEDIUM", 30),
    "FILE MODIFIED": ("HIGH", 50),
    "FILE DELETED": ("CRITICAL", 80)
}

def get_file_hash(filepath):
    with open(filepath, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def create_baseline():
    baseline = {}

    for filename in os.listdir(DIRECTORY):
        path = os.path.join(DIRECTORY, filename)

        if os.path.isfile(path):
            baseline[filename] = get_file_hash(path)

    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f, indent=4)

    print("✅ Baseline created.")

def check_integrity():
    if not os.path.exists(BASELINE_FILE):
        print("❌ Baseline not found. Create it first.")
        return

    with open(BASELINE_FILE, "r") as f:
        baseline = json.load(f)

    current = {}
    alerts = []

    for filename in os.listdir(DIRECTORY):
        path = os.path.join(DIRECTORY, filename)

        if os.path.isfile(path):
            current[filename] = get_file_hash(path)

    # Detect new / modified
    for file, hash_val in current.items():
        if file not in baseline:
            alerts.append((file, "NEW FILE DETECTED"))
        elif baseline[file] != hash_val:
            alerts.append((file, "FILE MODIFIED"))

    # Detect deleted
    for file in baseline:
        if file not in current:
            alerts.append((file, "FILE DELETED"))

    print("\n--- FILE INTEGRITY ALERTS ---\n")

    total_risk = 0

    if not alerts:
        print("✅ No changes detected.")
    else:
        for file, issue in alerts:
            severity, score = SEVERITY[issue]
            total_risk += score
            print(f"{file} → {issue} | Severity: {severity}")

    print("\n--- RISK SCORE ---\n")
    print(f"Total Risk Score: {total_risk}")

    # Final verdict
    if total_risk >= 100:
        print("\nFINAL STATUS: SYSTEM COMPROMISED 🔴")
    elif total_risk >= 50:
        print("\nFINAL STATUS: SUSPICIOUS ACTIVITY 🟠")
    else:
        print("\nFINAL STATUS: NORMAL 🟢")

    # Save report
    with open("report.txt", "w") as f:
        f.write(f"Report Time: {datetime.now()}\n\n")
        for file, issue in alerts:
            severity, score = SEVERITY[issue]
            f.write(f"{file} → {issue} ({severity})\n")
        f.write(f"\nTotal Risk Score: {total_risk}\n")

    print("\nReport saved as report.txt")

if __name__ == "__main__":
    print("1. Create Baseline")
    print("2. Check Integrity")

    choice = input("Enter choice: ")

    if choice == "1":
        create_baseline()
    elif choice == "2":
        check_integrity()