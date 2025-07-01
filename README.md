# 📝 Centralized Server Logging System

A powerful and lightweight centralized logging system that captures and stores logs for **errors**, **success events**, **warnings**, and **general information** from your server in real time. This system is designed to be easily integrated with any server to monitor and analyze server-side events efficiently.

---
## 📖 Overview

This Centralized Logging System is built to simplify and standardize the way servers handle logging. Whether it's an API server, a microservice, or a monolithic application, this logger provides a consistent structure to record all kinds of events — from errors and warnings to successful operations and debugging information.

It helps in:

- **Troubleshooting** by keeping detailed logs of what went wrong and when.
- **Monitoring** server performance and usage in real time.
- **Auditing** application behavior for security and compliance.
- **Analyzing** user behavior, system issues, and workflow efficiency.

This system is designed to be **plug-and-play**, making it easy to drop into any project and start logging with minimal setup.

---
## 🚀 Features

- ✅ Logs all types of events: Errors, Success, Warnings, Info, Debug
- 📦 Centralized logging for distributed environments
- 📄 Log format includes timestamp, log level, message, and optional metadata
- 🔧 Configurable logging levels
- 🗃️ Supports local file logging and database logging (extensible)
- 🛠️ Easy integration with existing server architectures
- 📈 Ready for log analysis and monitoring dashboards

---
## Technology Stack
- **Backend Framework**: FastAPI
- **Programming Language**: Python

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Madhur-Prakash/centralized-logging.git
   ```
2. Navigate to the project directory:
   ```bash
   cd centralized-logging
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
---

## Usage

1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
2. Access the API documentation at:
   ```
   http://127.0.0.1:8000/docs
   ```
3. Use the API to register, log in, and manage users with email-password, username-password, or phone number-password combinations.

---

## API Endpoints

### Authentication Endpoints
- **POST /create_new_logs

## Project Structure

```plaintext
centralized_logs/
├── logger/
│   ├── __init__           # initializes logger package
│   ├── log.py             # main logic
│   ├── models.py          # models
├── gitignore              # gitignore file for github
├── app.py                 # main fastapi app
└── README.md              # Project documentation
```

---


---
## Future Enhancements

- Remote logging support (e.g., Logstash, AWS CloudWatch)
- Real-time web dashboard for viewing logs
- Alert system for critical events
- Log rotation and archival
- Integration with monitoring tools (Grafana, Prometheus)
- Framework-specific plugins (FastAPI, Flask, etc.)

---
## Contribution Guidelines

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and submit a pull request.

---

## License
This project is distributed under the "Open Source License — Madhur Prakash", based on the MIT License. 
See the [LICENSE](LICENSE.md) file for details.

---

## Author
**Madhur Prakash**  
[GitHub](https://github.com/Madhur-Prakash) | [Medium](https://medium.com/@madhurprakash2005)

---
