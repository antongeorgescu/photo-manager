# tools/cctools.py

from langchain.agents import tool
import json
from typing import Any, List

# import sys
# sys.path.append('../utils')
from utils.logger import log_tool_usage
import requests

@tool
def create_nonregistered_student(firstname:str,lastname:str,homeAddress:str,phoneNumber:str,email:str,preference:str) -> str:
    """Create non-registered student and return student id."""
    log_tool_usage("create_nonregistered_student", json.dumps({"firstName":firstname,"lastName":lastname,"homeAddress":homeAddress}))
    
    url = "https://student-loan-api.azurewebsites.net/api/student/create-nonregistered"
    
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
def create_loan(studentid:int, loanamount:float, enrolltype:str,disbursedate:str,collegecode:str, programofstudy:str) -> str:
    """Assign to a non-registered student a loan, a college and a program of study."""
    log_tool_usage("create_loan", {studentid,loanamount,enrolltype,disbursedate,collegecode,programofstudy})
    
    url = "https://student-loan-api.azurewebsites.net/api/student/update/loan"

    payload = {
        "studentid":studentid,
        "loanAmount": loanamount,
        "enrollmentType": enrolltype,
        "disbursementDate": disbursedate,
        "studyinfoid" : 295, 
        "educationinstitutionid" : 40
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
        return json.dumps(json.loads(response.text)["data"])
    
    except requests.exceptions.RequestException as e:
        return f"Error creating student: {str(e)}"

    return json.dumps(loaninfo)

@tool
def find_student_by_lastname(lastname :str) -> str:
    """Retrieve student information based on likeness to last name."""
    log_tool_usage("find_student_by_lastname", lastname)
    
    url = f"https://student-loan-api.azurewebsites.net/api/students/{lastname}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
        return json.dumps(json.loads(response.text)["data"])
    
    except requests.exceptions.RequestException as e:
        return f"Error finding student: {str(e)}"