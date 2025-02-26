# README.md

# FastAPI WebSocket Server

This project is a FastAPI WebSocket server that allows real-time communication between clients. It is designed to handle multiple rooms and broadcast messages to connected clients.

## Features

- WebSocket support for real-time communication
- Room management for organizing connections
- Simple API for sending and receiving messages

## Project Structure

```
fastapi-websocket-server
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── config
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── core
│   │   ├── __init__.py
│   │   └── websocket.py
│   └── utils
│       ├── __init__.py
│       └── helpers.py
├── tests
│   ├── __init__.py
│   └── test_websocket.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fastapi-websocket-server.git
   cd fastapi-websocket-server
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

## Docker

To build and run the application using Docker, use the following commands:

1. Build the Docker image:
   ```bash
   docker build -t fastapi-websocket-server .
   ```

2. Run the Docker container:
   ```bash
   docker-compose up
   ```

## Testing

To run the tests, use the following command:

```bash
pytest tests/
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details."# python_oncomp_colab" 
