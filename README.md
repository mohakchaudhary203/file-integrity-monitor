# File Integrity Monitoring System (FIM)

## 📌 Overview
A Python-based File Integrity Monitoring (FIM) tool that detects unauthorized file changes using SHA-256 hashing, risk scoring, and SOC-style alerting.

---

## 🚀 Features
- Detects file modifications  
- Detects new file creation  
- Detects file deletion  
- Assigns severity levels (MEDIUM / HIGH / CRITICAL)  
- Calculates overall risk score  
- Provides final system status  
- Generates report file  

---

## 🧠 Detection Logic

### 🔹 File Modified
If file hash changes → indicates tampering  
→ Severity: HIGH  

### 🔹 New File Detected
Unknown file appears → possible unauthorized addition  
→ Severity: MEDIUM  

### 🔹 File Deleted
Expected file missing → possible data removal  
→ Severity: CRITICAL  

---

## 📁 Project Structure
file-integrity-monitor/
│── monitor.py  
│── baseline.json  
│── files/  
│── README.md  
│── .gitignore  

---

## ▶️ How to Run

### Step 1: Create baseline
```bash
python monitor.py