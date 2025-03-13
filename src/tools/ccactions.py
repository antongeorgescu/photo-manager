# tools/tools.py

from langchain.agents import tool
import json
from typing import Any, List
from utils.logger import log_tool_usage


@tool
def create_nonregistered_student(firstname:str,lastname:str,homeAddress:str) -> str:
    """Create non-registered student and return student id."""
    log_tool_usage("create_nonregistered_student", json.dumps({"firstName":firstname,"lastName":lastname,"homeAddress":homeAddress}))
    studentinfo = {"studentid": 1, "firstName": firstname, "lastName": lastname, "homeAddress": homeAddress}
    return json.dumps(studentinfo)

@tool
def add_communication_info(studentid :int, phoneNumber:str, email:str, preference:str) -> str:
    """Assign communication info to a non-registered student."""
    log_tool_usage("add_communication_info", json.dumps({"studentid":studentid,"phoneNumber":phoneNumber,"email":email,"preference":preference}))
    communication = {"studentid": studentid, "phoneNumber": phoneNumber, "email": email, "preference": preference}
    return json.dumps(communication)

@tool
def create_loan(studentid:int, loaninfo: List[str], collegecode:str, programofstudy:str) -> str:
    """Assign to a non-registered student a loan, a college and a program of study."""
    log_tool_usage("create_loan", {studentid,json.dumps(loaninfo),collegecode,programofstudy})
    return json.dumps(loaninfo)

@tool
def find_student_by_lastname(lastname :str) -> str:
    """Retrieve student information based on likeness to last name."""
    log_tool_usage("find_student_by_lastname", lastname)
    return lastname