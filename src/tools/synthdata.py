# tools/synthdata.py

import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import numpy as np
from dateutil.relativedelta import relativedelta

from langchain.agents import tool
import json
from typing import Any, List

# import sys
# sys.path.append('../utils')
from utils.logger import log_tool_usage

# Initialize Faker for Canadian locale
fake = Faker('en_CA')

# Define the provinces and cities
provinces_cities = {
    'ON': {'name': 'Ontario', 'cities': ['Toronto', 'Kingston', 'Ottawa', 'Hamilton', 'London']},
    'AB': {'name': 'Alberta', 'cities': ['Edmonton', 'Calgary', 'Red Deer', 'Lethbridge', 'Medicine Hat']},
    'NS': {'name': 'Nova Scotia', 'cities': ['Halifax', 'Sydney', 'Dartmouth', 'Truro', 'New Glasgow']},
    'MB': {'name': 'Manitoba', 'cities': ['Winnipeg', 'Brandon', 'Thompson', 'Portage la Prairie', 'Steinbach']},
    'PE': {'name': 'Prince Edward Island', 'cities': ['Charlottetown', 'Summerside', 'Stratford', 'Cornwall', 'Montague']}
}

# Define programs and their codes
programs = {
    'Biochemistry': 'BIOCHE',
    'Engineering': 'ENGRNG',
    'Computer Technology': 'COMTEC',
    'Social Studies': 'SOCSTD',
    'Political Science': 'POLSCI',
    'Climate Change': 'CLIMCH',
    'Physics': 'PHYSIC',
    'Philosophy': 'PHILOS'
}

# Define colleges and their information
colleges = {
    'University of Toronto': {'code': 'UOTON', 'city': 'Toronto', 'province': 'ON'},
    'Queens University': {'code': 'QUEEN', 'city': 'Kingston', 'province': 'ON'},
    'University of Alberta': {'code': 'UALBE', 'city': 'Edmonton', 'province': 'AB'},
    'Dalhousie University': {'code': 'DALHO', 'city': 'Halifax', 'province': 'NS'},
    'University of Manitoba': {'code': 'UMANI', 'city': 'Winnipeg', 'province': 'MB'},
    'Holland College': {'code': 'HOLCO', 'city': 'Charlottetown', 'province': 'PE'}
}

# Define financial institutions
banks = {
    'Royal Bank of Canada': 'RBC',
    'Canadian Imperial Bank of Commerce': 'CIBC',
    'Bank of Montreal': 'BMO'
}

# Define enrollment types
enrollments = {
    'National Student Loans': 'NSL',
    'Canadian Apprenticeship Loans': 'CAL'
}

@tool
def generate_student_profile() -> dict:
    """Generate a synthetic student profile."""
    student_profile = {
        'Name': fake.name(),
        'Home Address': fake.street_address() + ', ' + random.choice(list(provinces_cities.keys())) + ', ' + fake.postalcode()
    }
    log_tool_usage("generate_student_profile", student_profile)
    return student_profile

@tool
def generate_loan_info() -> dict:    
    """Generate synthetic loan information."""
    log_tool_usage("generate_loan_info", None)  
    start_date = datetime(2019, 1, 1)
    end_date = datetime(2024, 12, 31)
    days_between_dates = (end_date - start_date).days

    # Generate disbursement date
    random_days = random.randrange(days_between_dates)
    disbursement_date = start_date + timedelta(days=random_days)

    # Generate loan info
    enrollment_type = random.choice(['NSL', 'CAL'])
    loan_amount = round(random.uniform(10000, 28000), 2)
    
    # Calculate loan balance based on probability
    prob = random.random()
    if prob < 0.6:  # 60% chance
        loan_balance = round(random.uniform(0.2 * loan_amount, 0.3 * loan_amount), 2)
        payoff_date = None
    elif prob < 0.9:  # 30% chance
        loan_balance = round(random.uniform(0.31 * loan_amount, 0.6 * loan_amount), 2)
        payoff_date = None
    else:  # 10% chance
        loan_balance = 0
        months_to_payoff = random.randint(12, 36)
        payoff_date = disbursement_date + relativedelta(months=months_to_payoff)
        
    percentage_paid = f"{int(((loan_amount - loan_balance) / loan_amount) * 100)}%"
    return {
        'Enrollment Type': enrollment_type,
        'Loan Amount': loan_amount,
        'Disbursement Date': disbursement_date.strftime('%Y-%m-%d'),
        'Loan Balance': loan_balance,
        'Percentage Paid': percentage_paid,
        'Payoff Date': payoff_date.strftime('%Y-%m-%d') if payoff_date else None,
    }

@tool
def generate_study_info() -> dict:
    """Generate synthetic study information."""
    program = random.choice(list(programs.keys()))
    program_code = programs[program]
    college = random.choice(list(colleges.keys()))
    college_info = colleges[college]
    study_info = {
        'Program': program,
        'Program Code': program_code,
        'College': college,
        'College Code': college_info['code'],
    }
    log_tool_usage("generate_study_info", study_info)
    return study_info

@tool
def generate_bank_info() -> dict:
    """Generate synthetic bank information."""
    bank_name = random.choice(list(banks.keys()))
    bank_code = banks[bank_name]
    bank_info = {
        'Bank Name': bank_name,
        'Bank Code': bank_code,
    }
    log_tool_usage("generate_bank_info", bank_info)
    return bank_info

@tool
def generate_communication_info() -> dict:
    """Generate synthetic communication information."""
    phone_number = fake.phone_number()
    email = fake.email()
    preference = random.choice(['Phone', 'Email'])
    communication_info = {
        'Phone Number': phone_number,
        'Email': email,
        'Preference': preference,
    }
    log_tool_usage("generate_communication_info", communication_info)
    return communication_info

