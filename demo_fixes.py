#!/usr/bin/env python3
"""
Hospital Management System - Demo of Critical Fixes
This demonstrates the key issues found and their fixes
"""

def demonstrate_sql_injection_fix():
    print("=" * 60)
    print("SQL INJECTION VULNERABILITY FIXES")
    print("=" * 60)
    
    print("\n❌ VULNERABLE CODE (Original):")
    print("""
# Line 273 in original file - VULNERABLE TO SQL INJECTION
doc = input('ENTER DOCTOR FIRST NAME :: ')
cur.execute("select exists (select * from doctor where first_name='{}')".format(doc))

# What if user enters: '; DROP TABLE doctor; --
# The query becomes: select exists (select * from doctor where first_name=''; DROP TABLE doctor; --')
# This would DELETE the entire doctor table!
""")
    
    print("\n✅ SECURE CODE (Fixed):")
    print("""
# Fixed version using parameterized queries
doc = input('ENTER DOCTOR FIRST NAME :: ')
cur.execute("select exists (select * from doctor where first_name=%s)", (doc,))

# Now malicious input is treated as literal text, not SQL commands
# The database driver safely escapes the input automatically
""")

def demonstrate_syntax_fixes():
    print("\n" + "=" * 60)
    print("SYNTAX ERROR FIXES")
    print("=" * 60)
    
    print("\n❌ SYNTAX ERROR (Original):")
    print("""
# Lines 1-6 in original file
@app.function(
    image=modal.Image.debian_slim()
        .pip_install(["mysql.connector","time","datetime","tabulate"]),
    gpu="A10G", 
    timeout=300, # 5m
)
import mysql.connector as ms

# Error: NameError: name 'app' is not defined
# This decorator is for Modal cloud platform but 'app' was never imported
""")
    
    print("\n✅ FIXED VERSION:")
    print("""
# Option 1: Remove the decorator entirely for local execution
import mysql.connector as ms
import random
import time
import datetime
from tabulate import tabulate

# Option 2: If using Modal, properly import first
# import modal
# app = modal.App("hospital-management")
# @app.function(...)
""")

def demonstrate_logic_fixes():
    print("\n" + "=" * 60)
    print("LOGIC ERROR FIXES")
    print("=" * 60)
    
    print("\n❌ Logic Error #1 (Line 396):")
    print("""
loading    # Missing parentheses - this doesn't call the function!
""")
    
    print("✅ Fixed:")
    print("""
loading()  # Now actually calls the function
""")
    
    print("\n❌ Logic Error #2 (Line 614):")
    print("""
if p=='y'.lower():    # This compares p to the string 'y', not lowercase p
""")
    
    print("✅ Fixed:")
    print("""
if p.lower()=='y':    # Now correctly converts p to lowercase first
""")
    
    print("\n❌ Logic Error #3 (Line 872):")
    print("""
if pid==' ':    # Checks for single space, but empty might be None or ''
""")
    
    print("✅ Fixed:")
    print("""
if pid is None or pid == '' or not pid.strip():    # Handles all empty cases
""")

def demonstrate_security_improvements():
    print("\n" + "=" * 60)
    print("SECURITY IMPROVEMENTS")
    print("=" * 60)
    
    print("\n❌ HARDCODED CREDENTIALS (Original):")
    print("""
x=ms.connect(host='localhost',user='root',passwd='root')
# Credentials exposed in source code - major security risk!
""")
    
    print("\n✅ ENVIRONMENT VARIABLES (Improved):")
    print("""
import os
x=ms.connect(
    host=os.getenv('DB_HOST', 'localhost'),
    user=os.getenv('DB_USER', 'root'), 
    password=os.getenv('DB_PASSWORD', 'root')
)
# Credentials stored securely in environment variables
""")
    
    print("\n❌ PLAIN TEXT PASSWORDS (Original):")
    print("""
# Line 50: Passwords stored as plain text
cur.execute('insert into user values ({},"{}","{}")'.format(uid,user,passwd))
""")
    
    print("\n✅ HASHED PASSWORDS (Recommended):")
    print("""
import bcrypt

# Hash password before storing
hashed = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())
cur.execute('insert into user values (%s,%s,%s)', (uid, user, hashed.decode('utf-8')))

# Verify password during login
if bcrypt.checkpw(passwd.encode('utf-8'), stored_hash.encode('utf-8')):
    print('Login successful')
""")

def demonstrate_input_validation():
    print("\n" + "=" * 60)
    print("INPUT VALIDATION IMPROVEMENTS")
    print("=" * 60)
    
    print("\n❌ NO VALIDATION (Original):")
    print("""
age = int(input('ENTER AGE :: '))    # Crashes if user enters text
phone = int(input('ENTER PHONE :: ')) # Crashes if user enters letters
# No bounds checking - could enter age 999 or negative numbers
""")
    
    print("\n✅ WITH VALIDATION (Improved):")
    print("""
def validate_age(age_str):
    try:
        age = int(age_str)
        return 0 < age < 150  # Reasonable age range
    except ValueError:
        return False

def validate_phone(phone_str):
    return phone_str.isdigit() and len(phone_str) >= 10

# Usage:
while True:
    age_input = input('ENTER AGE :: ')
    if validate_age(age_input):
        age = int(age_input)
        break
    print("Please enter a valid age (1-149)")
""")

def demonstrate_database_fixes():
    print("\n" + "=" * 60)
    print("DATABASE SCHEMA FIXES")
    print("=" * 60)
    
    print("\n❌ SCHEMA ISSUES (Original):")
    print("""
# Typo in column name
qualifation varchar(20)    # Should be 'qualification'

# Inconsistent casing
Qualification varchar(40)  # Mixed case with above

# Poor data types
phonenumber int(12)        # Should be VARCHAR for international numbers

# Wrong foreign key references
FOREIGN KEY (PID) REFERENCES Patient (PID)   # Case mismatch
FOREIGN KEY (did) REFERENCES Doctor(D_ID)    # Column name mismatch
""")
    
    print("\n✅ SCHEMA FIXES:")
    print("""
# Fixed column names
qualification varchar(40)     # Consistent naming and spelling

# Better data types  
phonenumber varchar(15)       # Supports international formats with +, -, spaces

# Correct foreign key references
FOREIGN KEY (pid) REFERENCES patient(PID)    # Consistent case
FOREIGN KEY (d_id) REFERENCES doctor(d_id)   # Matching column names
""")

def show_vulnerability_summary():
    print("\n" + "=" * 60)
    print("VULNERABILITY SUMMARY")
    print("=" * 60)
    
    vulnerabilities = [
        ("SQL Injection", "CRITICAL", "15+ instances", "Use parameterized queries"),
        ("Hardcoded Credentials", "HIGH", "Database password", "Use environment variables"),
        ("Plain Text Passwords", "HIGH", "User passwords", "Implement password hashing"),
        ("No Input Validation", "MEDIUM", "All user inputs", "Add validation functions"),
        ("Syntax Errors", "HIGH", "Code won't run", "Fix import and logic errors"),
        ("Logic Errors", "MEDIUM", "3+ instances", "Fix conditional statements"),
        ("Schema Issues", "LOW", "Typos and inconsistencies", "Update database schema")
    ]
    
    print(f"{'Vulnerability':<20} {'Severity':<10} {'Impact':<20} {'Fix':<30}")
    print("-" * 80)
    
    for vuln, severity, impact, fix in vulnerabilities:
        print(f"{vuln:<20} {severity:<10} {impact:<20} {fix:<30}")

def main():
    print("HOSPITAL MANAGEMENT SYSTEM - CODE ANALYSIS DEMONSTRATION")
    print("=" * 80)
    print("This demo shows the critical issues found and how to fix them")
    
    demonstrate_syntax_fixes()
    demonstrate_sql_injection_fix()
    demonstrate_logic_fixes()
    demonstrate_security_improvements()
    demonstrate_input_validation()
    demonstrate_database_fixes()
    show_vulnerability_summary()
    
    print("\n" + "=" * 80)
    print("CONCLUSION")
    print("=" * 80)
    print("""
The original hospital_management_system.py has severe security vulnerabilities
and syntax errors that prevent it from running safely. The main issues are:

1. CRITICAL: Multiple SQL injection vulnerabilities
2. CRITICAL: Syntax errors preventing execution  
3. HIGH: Hardcoded credentials and plain text passwords
4. MEDIUM: No input validation and logic errors

RECOMMENDATION: 
- Fix syntax errors first to make code runnable
- Immediately address ALL SQL injection vulnerabilities  
- Implement proper security measures before any deployment
- Add comprehensive input validation and error handling

FILES CREATED:
- code_analysis_report.md: Comprehensive analysis
- critical_fixes_needed.md: Quick fix guide
- hospital_management_system_fixed.py: Fixed version (partial)
- demo_fixes.py: This demonstration file

DO NOT USE THE ORIGINAL CODE IN PRODUCTION!
""")

if __name__ == "__main__":
    main()