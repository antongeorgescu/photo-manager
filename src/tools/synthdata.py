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

import re

# import sys
# sys.path.append('../utils')
from utils.logger import log_tool_usage
from utils.provinces_and_states import canadian_provinces, us_states, accepted_regions
import os

fake = Faker('en_CA')
# Suppress the output by setting show_feature_list to False
if hasattr(fake, '_show_feature_list'):
    fake._show_feature_list = False

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
        'Home Address': fake.street_address() + ', ' + random.choice(list(canadian_provinces.keys())) + ', ' + fake.postalcode()
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

@tool
def generate_random_education_institution() -> int:
    """Generate random education institutiod id."""
    min_val, max_val = map(int, os.getenv("RANGECOLLEGEID").split(','))
    result = random.randint(min_val, max_val)
    log_tool_usage("generate_random_education_institution", result)
    return result

@tool
def generate_random_program_of_study() -> int:
    """Generate random program of study id."""
    min_val, max_val = map(int, os.getenv("RANGEPROGRAMOFSTUDY").split(','))
    result = random.randint(min_val, max_val)
    log_tool_usage("generate_random_program_of_study", result)
    return result

@tool
def generate_random_address(country: str = None) -> dict:
    """
    Generate a random street address for either Canada or USA.
    Args:
        country: Optional - 'CA' for Canada, 'US' for USA. If None, randomly chooses.
    Returns:
        Dictionary containing address details
    """
    if not country:
        country = random.choice(['CA', 'US'])

    street_number = random.randint(1, 9999)
    street_name = fake.street_name()
    
    if country == 'CA':
        region_data = canadian_provinces
        postal_code = fake.postcode()
    else:  # US
        region_data = us_states
        postal_code = f"{random.randint(10000, 99999)}"
    
    region_code = random.choice(list(region_data.keys()))
    region_name = region_data[region_code]['name']
    city = random.choice(region_data[region_code]['cities'])
    
    address = {
        'street_number': street_number,
        'street_name': street_name,
        'city': city,
        'region_code': region_code,
        'region_name': region_name,
        'postal_code': postal_code,
        'country': 'Canada' if country == 'CA' else 'United States',
        'formatted_address': f"{street_number} {street_name}, {city}, {region_code} {postal_code}"
    }
    
    log_tool_usage("generate_random_address", address)
    return address

# @tool
# def is_canadian_address(address: str) -> bool:
#     """
#     Validate if an address is an accepted Canadian location based on the list of provinces and postal code format.
#     """
#     # Canadian postal code pattern: A1A 1A1 or A1A1A1
#     postal_pattern = r'[A-Z]\d[A-Z]\s*\d[A-Z]\d'
    
#     # Get list of all province codes and names
#     province_codes = list(accepted_regions.keys())
#     province_names = [prov['name'] for prov in accepted_regions.values()]
    
#     # Check if address contains a valid province
#     has_province = any(code in address.upper() for code in province_codes) or \
#                   any(name in address for name in province_names)
    
#     # Check if address contains valid postal code format
#     has_postal = bool(re.search(postal_pattern, address.upper()))
    
#     result = has_province and has_postal
#     log_tool_usage("is_canadian_address", {"address": address, "is_canadian": result})
    
#     return result