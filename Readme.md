## Getting Started

### Prerequisites
- Poetry (Python package manager)
- PostgreSQL
- Docker (for containerized deployment)

### Environment Setup

1. **Install dependencies and activate virtual environment:**
    ```bash
    poetry install
    poetry shell
    pip install -r requirements.txt
    ```

2. **Create an `.env` file in the root directory:**
    ```dotenv
    # Database Configuration
    POSTGRES_USER=your_postgres_username
    POSTGRES_PASSWORD=your_postgres_password
    POSTGRES_SERVER=localhost
    POSTGRES_PORT=5432
    POSTGRES_DB=coconut_db
    POSTGRES_TEST_DB=coconut_test_db

    # Application Settings
    FRONTEND_URL=http://localhost:3000
    SECRET_KEY=your_jwt_secret_key
    
    # OAuth Configuration
    CLIENT_ID=your_google_oauth_client_id
    CLIENT_SECRET=your_google_oauth_client_secret
    ```

3. **Export environment variables:**
    ```bash
    export $(grep -v '^#' .env | xargs)
    ```

## Docker Setup

### Using Docker Desktop
1. **Install Docker Desktop:**
   - Download and install from [Docker's official website](https://www.docker.com/products/docker-desktop)
   - Launch Docker Desktop and ensure it's running

2. **Build and run the application:**
   - Open Docker Desktop
   - Navigate to the "Containers" tab
   - Click "Build" and select the project directory
   - Or use the command line instructions below

### Using Docker CLI
1. **Build the Docker image:**
   ```bash
   docker build -t coconut-app .
   ```

2. **Run the container:**
   ```bash
   docker run -d -p 8000:8000 --env-file .env --name coconut-container coconut-app
   ```

3. **View logs:**
   ```bash
   docker logs coconut-container
   ```

4. **Stop the container:**
   ```bash
   docker stop coconut-container
   ```

## Database Migrations

**Create a new migration:**
```bash
alembic revision --autogenerate -m "description of changes"
```

**Apply migrations:**
```bash
alembic upgrade head
```

## Development Server

**Run the FastAPI development server:**
```bash
poetry run uvicorn app.main:app --reload
```

**Alternative using FastAPI CLI:**
```bash
fastapi dev app/main.py
```

## Project Structure
```
/Coconut
├── app/
│   ├── alembic/                # Database migration files
│   ├── api/
│   │   ├── middlewares/        # Authentication and other middleware
│   │   └── routes/             # API endpoint definitions
│   ├── core/                   # Core configuration
│   ├── crud/                   # CRUD operations
│   ├── models/                 # SQLModel database models
│   └── schemas/                # Pydantic schemas
├── scripts/                    # Utility scripts
├── .env                        # Environment variables
├── alembic.ini                 # Alembic configuration
├── pyproject.toml              # Project dependencies
└── Dockerfile                  # Docker configuration
```

## Google OAuth Setup

1. Create a project in the [Google Cloud Console](https://console.cloud.google.com/)
2. Configure the OAuth consent screen
3. Create OAuth credentials (Client ID and Client Secret)
4. Add authorized redirect URIs (e.g., `http://localhost:8000/auth/callback`)
5. Update your `.env` file with the OAuth credentials

## Testing Authentication

### OAuth 2.0 Testing Guide

1. **Access Google OAuth Playground:**
   - Visit [Google OAuth 2.0 Playground](https://developers.google.com/oauthplayground/)

2. **Configure OAuth credentials:**
   - Click the settings icon (⚙️) in the top right corner
   - Select "Use your own OAuth credentials"
   - Enter your Client ID and Client Secret
   - Click "Close"

3. **Authorize API access:**
   - Select `https://www.googleapis.com/auth/userinfo.email` scope
   - Click "Authorize APIs"
   - Sign in with your Google account and approve permissions

4. **Exchange authorization code for tokens:**
   - Click "Exchange authorization code for tokens"
   - You'll receive Access Token, Refresh Token, and ID Token

5. **Test the API:**
   - Use the ID Token for `/auth` endpoint:
     ```json
     {
         "id_token": "your_id_token_here"
     }
     ```
   - Use the returned Access Token to authorize other API requests

    <img src="https://github.com/user-attachments/assets/abda9d0c-125a-46c5-b5ab-e1541db216de" alt="Authentication Flow" width="300" />
    <br/>
   <img src="https://github.com/user-attachments/assets/e30a6e9c-77a3-430c-a61d-227a37f5343f" alt="Token Authorization" width="400" />

> **Tip:** Decode the ID Token at [jwt.io](https://jwt.io/) to inspect user information.

## API Documentation

Interactive API documentation is available at `http://localhost:8000/docs`

## Core Features

- **User Management:** Registration, profiles, and friendship management
- **Trip Planning:** Create trips, set dates, locations, and status
- **Collaboration:** Invite friends to trips with role-based permissions
- **Expense Tracking:** Record and split expenses among trip members
- **Media Sharing:** Share photos and other media related to trips


## License

This project is licensed under the MIT License.
