# tools/cctools.py

from langchain.agents import tool
import json
from typing import Any, List
from utils.logger import log_tool_usage
import requests
import os

BASE_URL = os.getenv("AZURE_APP_FUNCTION_API_BASEURL")

@tool
def create_nonregistered_student(firstname:str,lastname:str,homeAddress:str,phoneNumber:str,email:str,preference:str) -> str:
    """Create non-registered student and return student id."""
    log_tool_usage("create_nonregistered_student", json.dumps({"firstName":firstname,"lastName":lastname,"homeAddress":homeAddress}))
    
    url = f"{BASE_URL}/student/create-nonregistered"
    
    payload = {
        "firstName": firstname,
        "lastName": lastname,
        "homeAddress": homeAddress,
        "phoneNumber": phoneNumber,
        "email": email,
        "preference": preference
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
        return json.dumps(json.loads(response.text)["data"])
    
    except requests.exceptions.RequestException as e:
        return f"Error creating student: {str(e)}"
    
@tool
def add_communication_info(studentid :int, phoneNumber:str, email:str, preference:str) -> str:
    """Assign communication info to a non-registered student."""
    log_tool_usage("add_communication_info", json.dumps({"studentid":studentid,"phoneNumber":phoneNumber,"email":email,"preference":preference}))
    communication = {"studentid": studentid, "phoneNumber": phoneNumber, "email": email, "preference": preference}
    return json.dumps(communication)

@tool
def create_loan(studentid:int, loanamount:float, enrolltype:str,disbursedate:str,educationinstitution:int, programofstudy:int) -> str:
    """Assign to a non-registered student a loan, a college and a program of study."""
    log_tool_usage("create_loan", {studentid,loanamount,enrolltype,disbursedate,educationinstitution,programofstudy})
    
    url = f"{BASE_URL}/student/update/loan"

    payload = {
        "studentid":studentid,
        "loanAmount": loanamount,
        "enrollmentType": enrolltype,
        "disbursementDate": disbursedate,
        "studyinfoid" : programofstudy, 
        "educationinstitutionid" : educationinstitution
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
        return json.dumps(json.loads(response.text)["data"])
    
    except requests.exceptions.RequestException as e:
        return f"Error creating student: {str(e)}"

@tool
def make_loan_payment(loanid:int, payamount:float) -> str:
    """Make a loan payment that has to be at least 100CAD."""
    log_tool_usage("make_loan_payment", {loanid,payamount})
    
    url = f"{BASE_URL}/loans/make-payment"

    payload = {
        "loanid":loanid,
        "amount": payamount
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
        return json.dumps(json.loads(response.text)["data"])
    
    except requests.exceptions.RequestException as e:
        return f"Error creating student: {str(e)}"

@tool
def find_student_by_lastname(lastname :str) -> str:
    """Retrieve student information based on likeness to last name."""
    log_tool_usage("find_student_by_lastname", lastname)
    
    url = f"{BASE_URL}/students/lastname/{lastname}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
        return json.dumps(json.loads(response.text)["data"])
    
    except requests.exceptions.RequestException as e:
        return f"Error finding student: {str(e)}"