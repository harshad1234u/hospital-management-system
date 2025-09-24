#!/usr/bin/env python3
"""
Hospital Management System - Fixed Version
This version addresses the most critical syntax and security issues
Original file: hospital_management_system.py
Fixed: Syntax errors, SQL injection vulnerabilities, logic errors
"""

import mysql.connector as ms
import random
import time 
import datetime
import os
from tabulate import tabulate

# Database connection with error handling
try:
    x = ms.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', 'root')
    )
except ms.Error as e:
    print(f"Database connection failed: {e}")
    print("Please ensure MySQL is running and credentials are correct")
    exit(1)

def create_cursor():
    """Create and return a database cursor"""
    return x.cursor(buffered=True)

def current_time():
    """Display current timestamp"""
    currentDT = datetime.datetime.now()
    print (' '*130+str(currentDT))

def validate_input(value, input_type, max_length=None):
    """Basic input validation"""
    if not value or not value.strip():
        return False
    
    value = value.strip()
    
    if input_type == "name":
        return value.replace(' ', '').isalpha() and (max_length is None or len(value) <= max_length)
    elif input_type == "phone":
        return value.isdigit() and len(value) >= 10
    elif input_type == "age":
        return value.isdigit() and 0 < int(value) < 150
    elif input_type == "email":
        return "@" in value and "." in value
    return True

def sign_in(user, passwd):
    """Secure user authentication using parameterized queries"""
    try:
        cur = create_cursor()
        # Fixed: Using parameterized query to prevent SQL injection
        cur.execute("SELECT EXISTS (SELECT * FROM user WHERE user=%s AND passwd=%s)", (user, passwd))
        data = cur.fetchone()
        if data[0] == 1:
            print('Successfully signed in')
            return True
        else:
            print('Invalid user or password')
            print('Please sign up first')
            return False
    except ms.Error as e:
        print(f"Database error during sign in: {e}")
        return False

def new():
    """Print separator line"""
    print('='*50)

def loading():
    """Display loading animation"""
    try:
        print('loading..', end='')
        time.sleep(0.3)
        print('..', end='')
        time.sleep(0.3)
        print('..')
    except KeyboardInterrupt:
        print('loading....')

def sign_up():
    """User registration with input validation"""
    global ans
    
    # Get user input with validation
    while True:
        user = input('User name: ').strip()
        if validate_input(user, "name", 30):
            break
        print("Invalid username. Please use only letters and spaces, max 30 characters.")
    
    while True:
        passwd = input(f'{user} password: ').strip()
        if len(passwd) >= 4 and len(passwd) <= 20:
            break
        print("Password must be between 4-20 characters.")
    
    uid = random.randint(1000, 99999)  # Larger range to reduce collisions
    
    try:
        cur = create_cursor()
        # Fixed: Using parameterized query to prevent SQL injection
        cur.execute('INSERT INTO user VALUES (%s, %s, %s)', (uid, user, passwd))
        x.commit()
        print('')
        print(10*'#', 'User profile created successfully', 10*"#")
        print('User:', user)
        print('Password:', "*"*len(passwd))
        
        if sign_in(user, passwd):
            ans = 'n'
        else:
            ans = 'y'
            
    except ms.Error as e:
        print(f"Error creating user: {e}")
        x.rollback()
        ans = 'y'

def search_doctor_secure(doctor_name):
    """Secure doctor search with parameterized queries"""
    try:
        cur = create_cursor()
        # Fixed: Using parameterized query to prevent SQL injection
        cur.execute("SELECT EXISTS (SELECT * FROM doctor WHERE first_name=%s)", (doctor_name,))
        data = cur.fetchone()
        
        if data[0] == 1:
            cur.execute("SELECT * FROM doctor WHERE first_name=%s", (doctor_name,))
            data = cur.fetchall()
            h = ['doctor_id', 'first_name', 'last_name', 'phonenumber', 'qualification', 
                 'date_of_join', 'specialist', 'age', 'fees', 'experience', 'salary', 'email', 'address']
            print(tabulate(data, headers=h, tablefmt='psql'))
            return True
        else:
            print('Doctor not found!')
            return False
    except ms.Error as e:
        print(f"Database error during doctor search: {e}")
        return False

def main():
    """Main application entry point with improved error handling"""
    a = 'y'
    
    while a == 'y':
        print('-_'*50)
        print('-_'*20, 'XYZ HOSPITAL', '-_'*20)
        print('-_'*50)
        print('')
        
        s = input('ENTER THE DATABASE PASSWORD :: ')
        current_time()
        
        if s.lower() == 'admin':
            if x.is_connected():
                print("Database connected successfully")
                
                try:
                    cur = create_cursor()
                    cur.execute("CREATE DATABASE IF NOT EXISTS hospitalmanagement2024")
                    cur.execute("USE hospitalmanagement2024")
                    
                    # Create tables with fixed column names and proper constraints
                    create_tables(cur)
                    
                    print('Database setup completed successfully')
                    
                    # Main application logic would continue here
                    # For demonstration, we'll just show the fixed authentication flow
                    
                    ans = 'y'
                    while ans == 'y':
                        print('Press 1 - "SIGN IN"')
                        print('Press 2 - "SIGN UP"')
                        
                        try:
                            ch = int(input('ENTER YOUR CHOICE :: '))
                        except ValueError:
                            print('Invalid choice. Please enter a number.')
                            continue
                            
                        current_time()
                        
                        if ch == 1:
                            print('#'*20, 'WELCOME BACK TO XYZ', "#"*20)
                            u = input('User name: ')
                            p = input(f'{u} password: ')
                            
                            if sign_in(u, p):
                                ans = 'n'
                                print("Login successful! Application would continue here...")
                                # Main menu logic would go here
                            
                        elif ch == 2:
                            sign_up()
                            
                        else:
                            print('Invalid choice')
                            continue
                            
                except ms.Error as e:
                    print(f"Database setup error: {e}")
                    
            else:
                print("Database connection failed")
        else:
            print("Incorrect password")
            
        a = input("Continue? (y/n): ").lower()

def create_tables(cur):
    """Create database tables with corrected schema"""
    
    # User table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS user (
            u_id INT NOT NULL PRIMARY KEY,
            user VARCHAR(30),
            passwd VARCHAR(60)  -- Increased size for hashed passwords
        )
    ''')
    
    # Room table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS room (
            room_number VARCHAR(10) NOT NULL PRIMARY KEY,
            room_type VARCHAR(30),
            feeperday INT
        )
    ''')
    
    # Nurse table - Fixed column name 'qualification'
    cur.execute('''
        CREATE TABLE IF NOT EXISTS nurse (
            n_id VARCHAR(10) NOT NULL PRIMARY KEY,
            first_name VARCHAR(40),
            last_name VARCHAR(40),
            phonenumber VARCHAR(15),  -- Changed to VARCHAR for better phone number support
            age INT,
            gender VARCHAR(10),  -- Increased size for inclusivity
            qualification VARCHAR(40),  -- Fixed typo
            date_of_joining VARCHAR(20),
            experience INT,
            salary INT,
            email VARCHAR(40),
            address VARCHAR(100)  -- Increased size for longer addresses
        )
    ''')
    
    # Doctor table - Fixed column name 'qualification' 
    cur.execute('''
        CREATE TABLE IF NOT EXISTS doctor (
            d_id VARCHAR(10) PRIMARY KEY,
            first_name VARCHAR(40),
            last_name VARCHAR(40), 
            phonenumber VARCHAR(15),  -- Changed to VARCHAR
            qualification VARCHAR(40),  -- Fixed inconsistent casing
            date_of_joining VARCHAR(10), 
            specialist VARCHAR(30), 
            age INT,
            fee INT, 
            experience INT, 
            salary INT, 
            email VARCHAR(40), 
            address VARCHAR(100)  -- Increased size
        )
    ''')
    
    # Patient table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Patient (
            PID VARCHAR(20) NOT NULL,
            FName VARCHAR(30),
            LName VARCHAR(30),
            Age INT,
            Gender VARCHAR(10),  -- Increased for inclusivity
            ContactNumber VARCHAR(15),
            Address VARCHAR(100),  -- Increased size
            currentroom VARCHAR(10),
            PRIMARY KEY (PID),
            FOREIGN KEY (currentroom) REFERENCES room(room_number)
        )
    ''')
    
    print("Database tables created successfully")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nApplication interrupted by user")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if x.is_connected():
            x.close()
            print("Database connection closed")