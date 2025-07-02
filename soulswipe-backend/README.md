# SoulSwipe Backend

## Overview
SoulSwipe is a modern dating platform designed to help users find meaningful connections based on personality, interests, and values. This backend project is built using Flask and provides the necessary APIs to support the SoulSwipe application.

## Project Structure
```
soulswipe-backend
├── src
│   ├── app.py               # Entry point of the application
│   ├── models
│   │   └── user.py          # User model definition
│   ├── routes
│   │   └── auth.py          # Authentication routes
│   ├── services
│   │   └── match_service.py  # Matching logic
│   └── utils
│       └── helpers.py       # Utility functions
├── requirements.txt         # Project dependencies
├── .env.example             # Environment variable template
└── README.md                # Project documentation
```

## Setup Instructions
1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd soulswipe-backend
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   Copy `.env.example` to `.env` and fill in the required values.

6. **Run the application:**
   ```
   python src/app.py
   ```

## Usage
- The backend provides various endpoints for user registration, login, and matching functionalities. Refer to the API documentation for detailed usage instructions.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.