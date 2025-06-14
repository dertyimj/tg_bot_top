# Telegram WebApp Store Bot

A full-featured Telegram bot store with a modern web interface, built using React and Python.

## Project Structure

```
├── frontend/           # React + TypeScript frontend
├── backend/           # Python FastAPI backend
│   ├── bot/          # Telegram bot logic
│   ├── api/          # REST API endpoints
│   └── database/     # Database models and migrations
└── docker/           # Docker configuration files
```

## Features

- 🛍️ Shop with product catalog
- 🎲 Roulette game (coming soon)
- 👤 User profiles with order history
- 🛒 Shopping cart functionality
- 🌙 Dark mode design
- 📱 Responsive Telegram WebApp interface

## Setup Instructions

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

1. Create a virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your Telegram bot token
```

4. Run the backend:
```bash
uvicorn main:app --reload
```

## Development

- Frontend runs on http://localhost:5173
- Backend API runs on http://localhost:8000
- API documentation available at http://localhost:8000/docs

## Deployment

1. Build the frontend:
```bash
cd frontend
npm run build
```

2. Use Docker Compose to deploy:
```bash
docker-compose up -d
``` #   t g _ b o t _ t o p  
 #   t g _ b o t _ t o p  
 