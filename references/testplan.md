# Student Loan API Test Plan

## 1. Student Management Endpoints

### POST /api/student/create-nonregistered
- **Positive Tests**
  * Valid student data with Canadian address
  * Minimum required fields only
  * All optional fields included
- **Negative Tests**
  * Invalid postal code format
  * Missing required fields
  * Non-Canadian address
  * Malformed JSON payload

### PUT /api/student/update-communication
- **Positive Tests**
  * Add new phone and email
  * Update preference to SMS
  * Update preference to Email
- **Negative Tests**
  * Invalid student ID
  * Invalid phone format
  * Invalid email format
  * Invalid preference value

## 2. Loan Management Endpoints

### POST /api/loan/create
- **Positive Tests**
  * Create NSL loan type
  * Create CAL loan type
  * Valid amount range (10000-50000)
- **Negative Tests**
  * Invalid student ID
  * Amount below minimum
  * Amount above maximum
  * Invalid enrollment type

### POST /api/loan/payment
- **Positive Tests**
  * Valid payment amount
  * Multiple payments
  * Full loan amount payment
- **Negative Tests**
  * Payment exceeds balance
  * Invalid loan ID
  * Zero or negative amount
  * Non-numeric amount

## 3. Search Operations

### GET /api/students/{lastname}
- **Positive Tests**
  * Exact match search
  * Partial match search
  * Multiple results
  * Case-insensitive search
- **Negative Tests**
  * Non-existent lastname
  * Special characters in lastname
  * Empty lastname parameter

## 4. Data Validation Tests

### Address Validation
```python
test_addresses = [
    "123 Maple St, Toronto, ON M5V2T6",  # Valid Canadian
    "456 Oak Ave, New York, NY 10001",    # Valid US
    "789 Invalid St, XX 123456"           # Invalid
]
```

### Amount Validation
```python
test_amounts = [
    36000.00,   # Valid
    9999.99,    # Below minimum
    50000.01,   # Above maximum
    0.00,       # Zero amount
    -100.00     # Negative amount
]
```

### Date Format Validation
```python
test_dates = [
    "2024-03-15",  # Valid ISO format
    "03/15/2024",  # Invalid format
    "2024-13-15",  # Invalid month
    "2024-03-32"   # Invalid day
]
```

## 5. Performance Tests

### Load Testing
- Concurrent user simulation
  * 10 simultaneous requests
  * 50 simultaneous requests
  * 100 simultaneous requests
- Response time metrics
  * Average response time < 500ms
  * 95th percentile < 1000ms
  * Error rate < 1%

### Stress Testing
- Burst traffic patterns
- Maximum concurrent connections
- Recovery time monitoring

## 6. Security Tests

### Authentication
- Valid API key tests
- Invalid API key tests
- Expired API key tests
- Missing API key tests

### Input Validation
- SQL injection attempts
- XSS payload attempts
- Special character handling
- Maximum field length tests

## 7. Integration Tests

### End-to-End Workflows
1. Student Registration Flow
   ```
   create-nonregistered → update-communication → create-loan
   ```

2. Loan Management Flow
   ```
   create-loan → payment → get-balance
   ```

3. Search and Update Flow
   ```
   find-by-lastname → update-communication → verify-update
   ```

## Test Execution Environment

### Configuration
- Base URL: https://student-loan-api.azurewebsites.net/api
- API Version: 1.0
- Test Data Source: synthdata.py
- Environment: Test/Staging

### Tools
- Postman for manual testing
- Python requests for automation
- Newman for CI/CD integration

## Reporting

### Metrics to Track
- Test case pass/fail rates
- API response times
- Error frequency by endpoint
- Coverage percentage