# Student Loan API Test Plan

## 1. API Endpoints Testing

### Student Registration
#### POST /api/student/create-nonregistered
- **Positive Tests**
  * Valid Canadian student data with proper postal code (e.g., "M5V 2H1")
  * All required fields present
  * Valid communication preferences (SMS/Email)
- **Negative Tests**
  * Non-Canadian addresses
  * Missing required fields
  * Invalid postal code format

#### PUT /api/student/update-communication
- **Positive Tests**
  * Update existing student communication info
  * Change preference between SMS and Email
  * Update phone number format
- **Negative Tests**
  * Invalid student ID
  * Malformed phone numbers
  * Invalid email formats

### Loan Management
#### POST /api/loan/create
- **Test Data**
```python
test_cases = [
    {
        "studentId": "valid_id",
        "amount": 36000,
        "enrollmentType": "CAL",
        "disbursementDate": "2023-07-20",
        "institutionId": 12345,
        "programId": 67890
    },
    {
        "studentId": "invalid_id",
        "amount": -1000,
        "enrollmentType": "INVALID",
        "disbursementDate": "invalid_date",
        "institutionId": -1,
        "programId": -1
    }
]
```

#### POST /api/loan/payment
- **Test Data**
```python
payment_tests = [
    {"loanId": "valid_id", "amount": 143.00, "frequency": "MONTHLY"},
    {"loanId": "invalid_id", "amount": -50.00, "frequency": "INVALID"}
]
```

### Search Operations
#### GET /api/students/{lastname}
- **Test Scenarios**
  * Exact match search
  * Partial match search
  * Non-existent lastname
  * Special characters in lastname

## 2. Integration Test Flows

### Complete Student Registration Flow
```python
test_flow = [
    ("create_student", {"firstname": "John", "lastname": "Doe"}),
    ("add_communication", {"studentId": "{previous_response.id}", "phone": "123-456-7890"}),
    ("create_loan", {"studentId": "{previous_response.id}", "amount": 36000}),
    ("verify_student", {"lastname": "Doe"})
]
```

### Loan Management Flow
```python
loan_flow = [
    ("create_loan", {"amount": 36000, "type": "CAL"}),
    ("make_payment", {"amount": 143}),
    ("verify_balance", {"expected": 35857})
]
```

## 3. Performance Tests

### Load Testing
- Concurrent users: 10, 50, 100
- Response time targets:
  * P95 < 1000ms
  * P99 < 2000ms
- Error rate < 1%

### Stress Testing
- Maximum concurrent connections
- Recovery time measurement
- Database connection pool limits

## 4. Security Testing

### Authentication
- API key validation
- Invalid key handling
- Rate limiting verification

### Input Validation
- SQL injection prevention
- XSS attempt handling
- Maximum field lengths

## 5. Test Data Requirements

### Student Data
```python
test_provinces = [
    "ON", "AB", "NS", "MB", "PE"
]

test_cities = {
    "ON": ["Toronto", "Ottawa"],
    "AB": ["Edmonton", "Calgary"]
}

test_postal_codes = [
    "M5V 2H1",  # Valid
    "12345",    # Invalid
    "ABC DEF"   # Invalid
]
```

### Program Data
```python
test_programs = {
    "BIOCHE": "Biochemistry",
    "ENGRNG": "Engineering",
    "COMTEC": "Computer Technology"
}
```

## 6. Test Environment Setup

### Configuration
- Base URL: https://student-loan-api.azurewebsites.net/api
- Test database reset between runs
- Logging level: DEBUG for test runs

### Tools
- Postman for manual testing
- Python requests library for automation
- Newman for CI/CD integration

## 7. Reporting Requirements

- Test execution summary
- Pass/fail metrics
- Response time statistics
- Error frequency analysis