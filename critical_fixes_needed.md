# Critical Fixes Required for Hospital Management System

## Immediate Action Items (MUST FIX TO RUN)

### 1. Syntax Error Fix
**Problem**: Line 1-6 contains Modal decorator without proper import
**Fix**: Remove or comment out the Modal decorator:
```python
# @app.function(
#     image=modal.Image.debian_slim()
#         .pip_install(["mysql.connector","time","datetime","tabulate"]),
#     gpu="A10G",
#     timeout=300, # 5m
# )
```

### 2. SQL Injection Vulnerabilities (CRITICAL SECURITY)
**Problem**: Direct string formatting in SQL queries
**Locations**: Lines 20, 50, 273, 279, 316, 319, 453, 459, 474, 720, 725, 833

**Example of vulnerable code**:
```python
cur.execute("select * from doctor where first_name='" + name + "'")
```

**Fix**: Use parameterized queries:
```python
cur.execute("select * from doctor where first_name=%s", (name,))
```

### 3. Logic Errors
**Line 396**: Missing parentheses
```python
# Wrong:
loading
# Correct:
loading()
```

**Line 614**: Incorrect string comparison
```python
# Wrong:
if p=='y'.lower():
# Correct:
if p.lower()=='y':
```

**Line 872**: Wrong condition check
```python
# Wrong:
if pid==' ':
# Correct:
if pid is None or pid == '':
```

## Quick Security Patches

### 1. Database Credentials
**Current**: Hardcoded credentials on line 12
```python
x=ms.connect(host='localhost',user='root',passwd='root')
```

**Better**: Use environment variables
```python
import os
x=ms.connect(
    host=os.getenv('DB_HOST', 'localhost'),
    user=os.getenv('DB_USER', 'root'),
    password=os.getenv('DB_PASSWORD', 'root')
)
```

### 2. Input Validation Template
Add this function for basic validation:
```python
def validate_input(value, input_type, max_length=None):
    if input_type == "name":
        return value.isalpha() and (max_length is None or len(value) <= max_length)
    elif input_type == "phone":
        return value.isdigit() and len(value) >= 10
    elif input_type == "age":
        return value.isdigit() and 0 < int(value) < 150
    return False
```

## Minimum Viable Fixes for Testing

### Create a Fixed Version Header:
```python
#!/usr/bin/env python3
"""
Hospital Management System
Version: 1.0 (Fixed)
Note: This version addresses critical syntax and security issues
"""

import mysql.connector as ms
import random
import time 
import datetime
import os
from tabulate import tabulate

# Database connection with environment variable support
try:
    x = ms.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', 'root')
    )
except ms.Error as e:
    print(f"Database connection failed: {e}")
    exit(1)
```

### Fix the create_cursor function:
```python
def create_cursor():
    return x.cursor(buffered=True)
```

### Fix critical SQL injection points:
Replace these patterns throughout the code:
```python
# Replace this pattern:
cur.execute("SELECT * FROM table WHERE column='{}'".format(value))
# With this:
cur.execute("SELECT * FROM table WHERE column=%s", (value,))

# Replace this pattern:
cur.execute("SELECT * FROM table WHERE column='" + value + "'")
# With this:
cur.execute("SELECT * FROM table WHERE column=%s", (value,))
```

## Database Schema Fixes

### Fix column name typos:
```sql
-- Change 'qualifation' to 'qualification' in nurse and doctor tables
ALTER TABLE nurse CHANGE qualifation qualification varchar(20);
ALTER TABLE doctor CHANGE Qualification qualification varchar(40);
```

### Fix foreign key references:
```sql
-- Ensure consistent naming in foreign key constraints
-- Update the lab_tests table foreign key reference
ALTER TABLE lab_tests DROP FOREIGN KEY lab_tests_ibfk_1;
ALTER TABLE lab_tests ADD FOREIGN KEY (pid) REFERENCES Patient(PID);
```

## Testing the Fixes

1. Remove the Modal decorator (lines 1-6)
2. Fix the loading() function call on line 396
3. Fix the string comparison on line 614
4. Fix the condition check on line 872
5. Test database connection with proper error handling

## Next Steps After Critical Fixes

1. Implement proper input validation for all user inputs
2. Add comprehensive error handling for database operations
3. Replace all SQL injection vulnerable queries with parameterized queries
4. Add password hashing for user authentication
5. Implement proper session management
6. Add logging for security and debugging purposes

---
**IMPORTANT**: Do not deploy this system in production until ALL SQL injection vulnerabilities are fixed and proper security measures are implemented.