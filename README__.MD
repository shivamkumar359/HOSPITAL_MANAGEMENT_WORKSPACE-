# Hospital Management WhatsApp Chatbot

A modular, production-oriented WhatsApp-based Hospital Management Chatbot built with **Python, FastAPI, WhatsApp Business Cloud API, and Google Sheets** as the initial data store.

The project is being developed incrementally with a clean separation between API handling, chatbot logic, business services, data repositories, and external integrations.

---

## 1. Project Overview

The goal of this project is to build a hospital management chatbot that allows patients to interact with hospital services through WhatsApp.

The initial system will use:

* **Python** for application development
* **FastAPI** for the backend API
* **WhatsApp Business Cloud API** for patient communication
* **Google Sheets** as the initial database
* **Git + GitHub** for version control
* **Docker** for future deployment
* **PostgreSQL** as a possible future database replacement

The architecture is designed so that the initial Google Sheets database can later be replaced by PostgreSQL without requiring major changes to the chatbot and business logic.

---

# 2. High-Level Architecture

```text
                    ┌──────────────────────┐
                    │       Patient        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       WhatsApp       │
                    └──────────┬───────────┘
                               │
                               ▼
              ┌────────────────────────────────┐
              │ WhatsApp Business Cloud API    │
              └───────────────┬────────────────┘
                              │
                              ▼
                    ┌──────────────────────┐
                    │       FastAPI        │
                    │     API Layer        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Chatbot Engine     │
                    │ Conversation Logic   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Service Layer     │
                    │   Business Rules     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Repository Layer    │
                    │    Data Access       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Google Sheets     │
                    │   Initial Database   │
                    └──────────────────────┘
```

---

# 3. Core Design Principles

The project follows a modular architecture.

### API Layer

Responsible for:

* HTTP endpoints
* Webhook endpoints
* Request handling
* Response handling

### Chatbot Layer

Responsible for:

* Conversation state
* Intent handling
* User interaction
* Bot responses
* Conversation flow

### Service Layer

Responsible for:

* Hospital business logic
* Patient workflows
* Appointment workflows
* Validation
* Business rules

### Repository Layer

Responsible for:

* Data access
* Data retrieval
* Data creation
* Data updates
* Database abstraction

### Integration Layer

Responsible for communication with external systems such as:

* WhatsApp Business Cloud API
* Google APIs

### Models Layer

Responsible for structured application data and domain models.

---

# 4. Technology Stack

| Technology                  | Purpose                      |
| --------------------------- | ---------------------------- |
| Python 3.11+                | Backend programming language |
| FastAPI                     | REST API framework           |
| Uvicorn                     | ASGI application server      |
| WhatsApp Business Cloud API | Patient communication        |
| Google Sheets               | Initial database             |
| Git                         | Version control              |
| GitHub                      | Source code hosting          |
| Docker                      | Containerization             |
| PostgreSQL                  | Future database option       |

---

# 5. Project Structure

The planned project structure is:

```text
hospital-whatsapp-chatbot/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── security.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── health.py
│   │
│   ├── chatbot/
│   │   ├── __init__.py
│   │   ├── engine.py
│   │   ├── states.py
│   │   ├── intents.py
│   │   └── responses.py
│   │
│   ├── services/
│   │   └── __init__.py
│   │
│   ├── repositories/
│   │   └── __init__.py
│   │
│   ├── integrations/
│   │   └── __init__.py
│   │
│   └── models/
│       └── __init__.py
│
├── tests/
│   ├── __init__.py
│   └── test_health.py
│
├── .vscode/
│   └── settings.json
│
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── Dockerfile
```

Some components are intentionally introduced gradually as development progresses.

---

# 6. Current Phase — Day 1

Day 1 establishes the backend foundation and development environment.

## Completed

* Python virtual environment
* FastAPI
* Uvicorn
* Project structure
* FastAPI application
* Root endpoint
* Health endpoint
* Git repository
* GitHub remote
* `.gitignore`
* VS Code project configuration
* Git branch workflow
* Initial GitHub commits
* GitHub push

---

# 7. Current API

## Root Endpoint

```http
GET /
```

Returns:

```json
{
  "message": "Hospital Management Chatbot API is running"
}
```

This endpoint confirms that the application is running.

---

## Health Endpoint

```http
GET /health
```

Returns:

```json
{
  "status": "ok"
}
```

The health endpoint currently verifies only that the API application is operational.

It does not claim that:

* WhatsApp is connected
* Google Sheets is connected
* a database is connected
* external services are available

External service health checks will be introduced when those integrations are implemented.

---

# 8. Running the Application

From the project root:

```bash
cd ~/Desktop/whatsapp_chatbot/hospital-whatsapp-chatbot
```

Activate the virtual environment if necessary:

```bash
source .venv/bin/activate
```

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

The application runs at:

```text
http://127.0.0.1:8000
```

API documentation is available through FastAPI's automatically generated documentation once the server is running.

---

# 9. Development Environment

The project uses an isolated Python virtual environment:

```text
.venv/
```

The virtual environment keeps project dependencies separate from the system Python installation.

VS Code is configured to use the project's virtual environment interpreter:

```text
.venv/bin/python3
```

The project-specific VS Code configuration is stored in:

```text
.vscode/settings.json
```

---

# 10. Environment Variables

Sensitive configuration will be stored through environment variables rather than directly inside source code.

Future configuration will include values such as:

```text
APP_NAME
WHATSAPP_VERIFY_TOKEN
WHATSAPP_ACCESS_TOKEN
WHATSAPP_PHONE_NUMBER_ID
GOOGLE_SHEET_ID
GOOGLE_SERVICE_ACCOUNT
```

Secrets must never be committed to GitHub.

The intended configuration files are:

```text
.env
.env.example
```

`.env` contains local secrets and is ignored by Git.

`.env.example` documents the required configuration without containing real credentials.

---

# 11. Git and GitHub

Git is used for source-code version control.

The primary branch is:

```text
main
```

Development work can be performed on feature branches.

Example:

```text
feature/appointment-booking
```

A typical workflow is:

```text
main
  ↓
Create feature branch
  ↓
Develop feature
  ↓
Commit changes
  ↓
Push branch
  ↓
Review / merge
  ↓
main
```

---

# 12. Commit Strategy

Commits should represent meaningful development milestones.

Examples:

```text
Create Phase 1 project structure
Add FastAPI application and health endpoint
Add project configuration
Add environment configuration template
Add chatbot conversation states
Add chatbot intent definitions
Implement chatbot engine
Add service layer foundation
Add repository abstraction
Implement Google Sheets repository
Add WhatsApp webhook
Add WhatsApp message handling
Add patient registration flow
Add appointment booking flow
Add chatbot tests
Add Docker configuration
Update project documentation
```

The objective is to maintain a clear and genuine development history.

---

# 13. `.gitignore`

The project excludes files that should not be committed, including:

```text
.venv/
.env
__pycache__/
.pytest_cache/
.vscode/
.idea/
build/
dist/
*.egg-info/
```

In particular, `.env` must remain excluded because it will contain sensitive credentials.

---

# 14. Planned Chatbot Capabilities

The completed system is intended to support hospital-related workflows such as:

* Patient registration
* Patient information
* Doctor information
* Department information
* Appointment booking
* Appointment management
* Appointment cancellation
* Basic hospital information
* Patient queries
* Structured conversational workflows

These features will be implemented progressively.

---

# 15. Planned Chatbot Architecture

The chatbot will use explicit conversation states.

Example:

```text
START
  ↓
MAIN_MENU
  ↓
SELECT_SERVICE
  ↓
PATIENT_INFORMATION
  ↓
APPOINTMENT
  ↓
SELECT_DOCTOR
  ↓
SELECT_DATE
  ↓
SELECT_TIME
  ↓
CONFIRM_APPOINTMENT
  ↓
COMPLETED
```

The exact state machine will be developed during the chatbot-engine phase.

---

# 16. Data Architecture

Google Sheets will initially act as the project's database.

Possible logical datasets include:

```text
Patients
Doctors
Departments
Appointments
Hospital Information
```

The application will not access Google Sheets directly from chatbot logic.

Instead:

```text
Chatbot
   ↓
Service
   ↓
Repository
   ↓
Google Sheets
```

This provides a clean abstraction between application logic and data storage.

---

# 17. Future Database Migration

The initial repository implementation will use Google Sheets.

Later, a PostgreSQL repository can replace it:

```text
Current:

Service
   ↓
Repository
   ↓
Google Sheets


Future:

Service
   ↓
Repository
   ↓
PostgreSQL
```

The service layer and chatbot engine should remain largely independent of the underlying database.

---

# 18. WhatsApp Integration

The production communication channel will use the official WhatsApp Business Cloud API.

The planned flow is:

```text
Patient
   ↓
WhatsApp
   ↓
WhatsApp Cloud API
   ↓
Webhook
   ↓
FastAPI
   ↓
Chatbot Engine
```

The WhatsApp integration will be implemented after the chatbot foundation is ready.

---

# 19. Security Considerations

Security will be introduced progressively.

Important principles include:

* Never hard-code secrets
* Never commit `.env`
* Validate webhook requests
* Validate incoming user input
* Separate authentication from business logic
* Restrict access to sensitive patient data
* Avoid exposing internal errors to users
* Validate external API responses
* Use secure production configuration
* Protect Google service credentials
* Apply appropriate logging practices

The system will be designed with patient-data privacy in mind.

---

# 20. Testing Strategy

Testing will be introduced alongside development.

Planned test categories include:

### Unit Tests

Testing individual components such as:

* Intent detection
* State transitions
* Validation
* Services
* Repository operations

### API Tests

Testing:

* `/`
* `/health`
* Webhook endpoints
* Request validation

### Integration Tests

Testing:

* Google Sheets integration
* WhatsApp integration
* End-to-end chatbot workflows

---

# 21. Docker

Docker will eventually be used to package the application consistently.

Planned deployment structure:

```text
Docker
  ↓
FastAPI
  ↓
Chatbot
  ↓
Services
  ↓
Repositories
  ↓
External Systems
```

Docker configuration will be added during the later project stages.

---

# 22. Development Roadmap

## Phase 1 — Backend Foundation

**Status: In progress / foundation established**

Focus:

* Project structure
* FastAPI
* Configuration
* Environment variables
* Basic API
* Testing foundation
* Git/GitHub
* Documentation
* Docker foundation

---

## Phase 2 — Chatbot Foundation

**Next development phase**

Planned work:

* Conversation states
* Intent definitions
* Response definitions
* Chatbot engine
* Message processing
* Basic conversation flows
* Chatbot tests

---

## Phase 3 — Service and Repository Architecture

Planned work:

* Service interfaces
* Business rules
* Repository interfaces
* Data models
* Validation
* Separation between business logic and data access

---

## Phase 4 — Google Sheets Integration

Planned work:

* Google API configuration
* Service-account authentication
* Google Sheets repository
* Patient data storage
* Doctor data storage
* Appointment data storage

---

## Phase 5 — WhatsApp Integration

Planned work:

* WhatsApp Cloud API configuration
* Webhook verification
* Incoming message handling
* Outgoing message handling
* WhatsApp message parsing
* Error handling

---

## Phase 6 — Patient Management

Planned work:

* Patient registration
* Patient lookup
* Patient profile
* Patient validation
* Patient interaction flow

---

## Phase 7 — Appointment Management

Planned work:

* Doctor selection
* Department selection
* Date selection
* Time selection
* Appointment creation
* Appointment confirmation
* Appointment cancellation
* Appointment status

---

## Phase 8 — Hospital Workflows

Planned work:

* Doctor information
* Department information
* Hospital information
* Patient support workflows
* Additional hospital services

---

## Phase 9 — Security and Reliability

Planned work:

* Authentication
* Authorization
* Webhook security
* Input validation
* Error handling
* Logging
* Sensitive-data protection
* Rate limiting where appropriate

---

## Phase 10 — Testing and Deployment

Planned work:

* Complete automated test suite
* Integration testing
* Docker
* Production configuration
* Deployment
* Monitoring
* Documentation

---

# 23. Future Architecture

The long-term architecture is:

```text
                         ┌──────────────┐
                         │   Patient    │
                         └──────┬───────┘
                                │
                                ▼
                         ┌──────────────┐
                         │   WhatsApp   │
                         └──────┬───────┘
                                │
                                ▼
                    ┌──────────────────────┐
                    │ WhatsApp Cloud API   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       FastAPI        │
                    │       API Layer      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Chatbot Engine     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Service Layer     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Repository Layer    │
                    └──────────┬───────────┘
                               │
                  ┌────────────┴────────────┐
                  ▼                         ▼
        ┌──────────────────┐      ┌──────────────────┐
        │  Google Sheets   │      │    PostgreSQL    │
        │   Initial DB     │      │    Future DB     │
        └──────────────────┘      └──────────────────┘
```

---

# 24. Project Status

### Current status

```text
Day 1
████████████████████████░░░░░░  Foundation
```

### Completed today

* Development environment
* Virtual environment
* VS Code configuration
* FastAPI foundation
* API endpoints
* Git configuration
* GitHub repository connection
* Git branching workflow

### Next session

```text
Phase 2 — Chatbot Foundation
```

---

# 25. Repository Information

**Project:**

```text
hospital-whatsapp-chatbot
```

**GitHub repository:**

```text
HOSPITAL_MANAGEMENT_WORKSPACE-
```

**Primary branch:**

```text
main
```

**Current major milestone:**

```text
FastAPI backend foundation
```

**Next major milestone:**

```text
Chatbot engine
```

---

# 26. Development Philosophy

The project is being developed incrementally rather than putting the entire system into one large implementation.

Each stage should:

1. Have a clearly defined responsibility.
2. Be independently testable.
3. Have meaningful Git commits.
4. Maintain separation of concerns.
5. Avoid unnecessary dependencies.
6. Protect credentials and sensitive data.
7. Keep future database and integration changes manageable.

The objective is to produce a maintainable software project rather than only a working prototype.

---

# 27. Current Milestone

**Day 1 — Backend and Development Environment Foundation**

The project has successfully established its initial FastAPI backend, Git/GitHub workflow, virtual environment, project architecture, and development structure.

The next development milestone is the **Chatbot Foundation**, where the conversational engine, states, intents, responses, and message-processing architecture will be developed.
