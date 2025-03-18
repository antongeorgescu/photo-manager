# Call Centre Agent Assistant

A conversational AI assistant for call center operations that helps manage student information, loans, and communications using Azure OpenAI and LangChain.

## Features

- Create and manage non-registered student profiles
- Handle student communication information
- Process student loan applications
- Search for students by last name
- Generate synthetic data for testing
- Interactive command-line interface with Rich text formatting

## Concept Design

![Image](https://github.com/user-attachments/assets/9b02d15d-692f-448b-a7c5-5a9d8c3ca5d2)

## High-level Design Diagram

![Image](https://github.com/user-attachments/assets/83cc5e46-6d3b-4330-bbc2-d5998dd63013)

## Prerequisites

- Python 3.x
- Azure OpenAI API access
- Required environment variables:
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

## Installation

1. Clone the repository
2. Install dependencies:
```sh
pip install -r requirements.txt
```

## Usage

1. Set up your environment variables in `.env` file
2. Run the application:
```sh
python src/ccagent.py
```

### Available Commands

- `/help` - Show help message
- `/exit` - Exit the application

### Example Questions

- Create a non-registered student with firstname, lastname and home address
- Add communication info to a non-registered student
- Create a loan for a non-registered student with loan info, college code and program of study
- Find a student by last name

## Project Structure

```
.
├── references/
│   ├── openapi.yaml        # API specification
│   └── testplan.txt        # API test plan
├── src/
│   ├── ccagent.py         # Main application file
│   ├── tools/
│   │   ├── ccactions.py   # Core business actions
│   │   └── synthdata.py   # Synthetic data generation
│   └── utils/
│       ├── logger.py      # Logging utilities
│       └── question_samples.txt  # Sample test scenarios
├── tests/
│   └── test_ccagent.py    # Unit tests
├── .env.example           # Environment variables template
├── .gitignore            # Git ignore rules
├── README.md             # Project documentation
└── requirements.txt      # Project dependencies
```

Key components:
- `src/` - Source code directory
  - `ccagent.py` - Main application with CLI interface
  - `tools/` - Core functionality modules
  - `utils/` - Helper utilities and logging
- `references/` - API documentation and test plans
- `tests/` - Test suites and test data

## Dependencies

Key dependencies include:
- langchain
- openai
- rich (for CLI formatting)
- faker (for synthetic data)
- python-dotenv

For a complete list, see `requirements.txt`.