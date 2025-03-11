# Weather Agent Project

This project implements a simple weather agent that retrieves and processes weather data. The agent interacts with various components to provide weather-related functionalities.

## Project Structure

```
weather-agent
├── src
│   ├── agents
│   │   └── weatherAgent.py
│   ├── config
│   │   └── config.py
│   ├── services
│   │   └── weatherService.py
│   ├── tools
│   │   └── weatherTools.py
│   └── utils
│       └── logger.py
├── tests
│   ├── __init__.py
│   └── test_weatherAgent.py
├── .env
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd weather-agent
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   Create a `.env` file in the root directory and add your configuration settings, such as API keys.

## Usage

To run the weather agent, execute the following command:

```bash
python src/agents/weatherAgent.py
```

## Testing

To run the tests for the weather agent, use the following command:

```bash
python -m unittest discover -s tests
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.