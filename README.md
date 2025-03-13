# Call Centre Agent Assistant

A conversational AI assistant for call center operations that helps manage student information, loans, and communications using Azure OpenAI and LangChain.

## Features

- Create and manage non-registered student profiles
- Handle student communication information
- Process student loan applications
- Search for students by last name
- Generate synthetic data for testing
- Interactive command-line interface with Rich text formatting

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
├── src/
│   ├── ccagent.py          # Main application file
│   ├── tools/
│   │   ├── ccactions.py    # Core business actions
│   │   └── synthdata.py    # Synthetic data generation
│   └── utils/
│       └── logger.py       # Logging utilities
├── requirements.txt        # Project dependencies
└── .env                   # Environment variables (not in repo)
```

## Dependencies

Key dependencies include:
- langchain
- openai
- rich (for CLI formatting)
- faker (for synthetic data)
- python-dotenv

For a complete list, see `requirements.txt`.