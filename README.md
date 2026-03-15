# AI Travel Architect

A full-stack containerized application that generates a 3-day travel itinerary using the Gemini API.
The project features a sleek frontend built with Next.js and Tailwind CSS, and a robust backend built with Python and FastAPI.

## Project Structure
- `frontend/`: Next.js App Router UI
- `backend/`: FastAPI Python API

## Prerequisites
- Docker
- Docker Compose
- Google Gemini API Key

## Setup & Running

1. **Environment Configuration**
   Copy the example environment file to `.env`:
   ```bash
   cp .env.example .env
   ```
   Open `.env` and configure your `GOOGLE_API_KEY`.

2. **Start the Application**
   Run the following command to build and start the containers:
   ```bash
   docker-compose up --build
   ```

3. **Access the Application**
   - Frontend: [http://localhost:3000](http://localhost:3000)
   - Backend API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## Features
- **AI-Powered Itineraries:** Fully synthesized 3-day travel plans using Gemini.
- **Modern UI:** Responsive, attractive, animated interface built with Tailwind CSS.
- **Dockerized:** Simple `docker-compose up` to run both services seamlessly.
