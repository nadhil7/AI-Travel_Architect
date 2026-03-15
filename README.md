# AI Travel Architect

AI Travel Architect is a high-performance, containerized full-stack application that leverages the power of Google's Gemini AI to synthesize personalized 3-day travel itineraries. The project features a modern, responsive frontend and a robust, secure backend with persistent storage and user authentication.

---

## 🏗️ Architecture Overview

The project is built with a microservices-inspired architecture, orchestrated using Docker Compose.

- **Frontend**: Built with **Next.js 15 (App Router)** and **Tailwind CSS**, providing a sleek, interactive user experience.
- **Backend API**: A high-performance **FastAPI (Python)** service that handles AI integration, user logic, and data processing.
- **Database**: **PostgreSQL 15** for reliable, ACID-compliant storage of user profiles and travel histories.
- **Cache/Session**: **Redis 7** for fast data handling and potential session management enhancements.

---

## 🔐 Authentication System (JWT)

Security is a core component of the project. We implement a robust authentication flow using **JSON Web Tokens (JWT)**.

1.  **Signup**: Users can create an account via the `/api/auth/signup` endpoint. Passwords are securely hashed using `bcrypt` before storage.
2.  **Login**: Upon successful login at `/api/auth/login`, the backend generates a signed JWT containing the user's identity.
3.  **Client-Side Storage**: The JWT is stored in an HTTP-safe cookie (or standard cookie handled by `js-cookie`) and included in the headers of subsequent API requests.
4.  **Protected Routes**: Backend endpoints (like `/api/history` and authenticated `/api/itinerary`) use a dependency injection pattern to validate the token and retrieve the current user's context.

---

## 🗄️ Database & Schema

We use **SQLAlchemy** as the ORM to interface with our **PostgreSQL** database. The schema is designed for scalability and clear relationships.

-   **Users (`users` table)**: Stores user details including full name, unique email (indexed), and securely hashed passwords.
-   **Itineraries (`itineraries` table)**: Stores the search history and generated results.
    -   `user_id`: Foreign key linking to the `users` table.
    -   `destination`, `style`, `days`: Captures the search parameters.
    -   `content`: Stores the full AI-generated response in a JSONB format for flexible querying.
    -   `created_at`: Automatic timestamping for historical tracking.

---

## 📜 API Documentation

The backend automatically generates interactive API documentation. Once the project is running, you can explore, test, and integrate with the API using:

-   **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
-   **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🚀 Getting Started

Follow these steps to get the project running locally in minutes:

### 1. Environment Configuration
Copy the template environment file and provide your Gemini API key:
```bash
cp .env.example .env
```
> [!IMPORTANT]
> Edit the `.env` file and set your `GOOGLE_API_KEY`. The database and redis URLs are pre-configured to work with the Docker network.

### 2. Launch with Docker
Use Docker Compose to build and start all services (Postgres, Redis, Backend, and Frontend):
```bash
docker compose up --build
```

### 3. Access the Application
-   **Frontend**: Navigate to [http://localhost:3000](http://localhost:3000)
-   **First Steps**: Go to the **Signup** page and create a new user account.
-   **Personalize**: Once logged in, generate your first travel plan and check your **History** to see it saved permanently in the PostgreSQL database.

---

## 🛠️ Tech Stack

-   **Language**: Python 3.11+, TypeScript
-   **Frameworks**: FastAPI, Next.js
-   **Database**: PostgreSQL 15, Redis 7 (Alpine)
-   **Styling**: Tailwind CSS, Lucide Icons
-   **Infrastructure**: Docker, Docker Compose
-   **AI**: Google Gemini API (Generative AI)
