# 🐍 Python Learning Syllabus

> **Organized by:** [Rawfu Siam](https://github.com)  
> **Rule:** Learn in order — top to bottom. Do not skip steps.

---

## 📗 PART 1 — Beginner Syllabus
> **Goal:** Understand Python fundamentals and write basic programs confidently.

### 🔰 Chapter 1 — Getting Started
- [ ] `print`
- [ ] `comment`
- [ ] `REPL`
- [ ] `keywords`
- [ ] `pip`
- [ ] `Tool, Module and Library`
- [ ] `Import`
- [ ] `math` / `random` / `pyttsx3` / `pyjokes`

### 🔰 Chapter 2 — Variables & Data Types
- [ ] `Variable`
- [ ] `Datatype` — string, integer, float, boolean, none
- [ ] `type()` function
- [ ] `typecasting`
- [ ] `input()` function

### 🔰 Chapter 3 — Operators
- [ ] `operators` — algebra, comparison, assignment, logical

### 🔰 Chapter 4 — Strings
- [ ] `string index`
- [ ] `string slicing`
- [ ] `escape sequence characters`
- [ ] `f-string`
- [ ] `len()`, `lower()`, `capitalize()`, `title()`
- [ ] `endswith()`, `startswith()`, `count()`, `replace()`, `find()`
- [ ] `join()` and `format()` methods

### 🔰 Chapter 5 — Data Structures
- [ ] `list` — indexing and slicing
- [ ] `append()`, `sort()`, `reverse()`, `remove()`, `pop()`, `clear()`, `insert()`
- [ ] `Tuples` — `count()`, `index()`
- [ ] `Dictionary`
- [ ] `items()`, `keys()`, `values()`, `update()`, `get()`
- [ ] `Dictionary merge & update operators`
- [ ] `set`
- [ ] `add()`, `remove()`, `discard()`, `pop()`, `union()`, `intersection()`, `difference()`

### 🔰 Chapter 6 — Control Flow
- [ ] `if` / `elif` / `else`
- [ ] `nested conditionals`
- [ ] `conditional expression` / `ternary operator` / `one liner`
- [ ] `in` keyword

### 🔰 Chapter 7 — Loops
- [ ] `for` / `range` / `while`
- [ ] `for loop with if and else`
- [ ] `break` / `continue` / `pass`
- [ ] `loop`
- [ ] `star pattern`

### 🔰 Chapter 8 — Functions
- [ ] `function`
- [ ] `function with arguments`
- [ ] `recursion` and `return`

### 🔰 Chapter 9 — File Handling
- [ ] `File I/O` — modes
- [ ] `with()`
- [ ] `readlines()`

### 🔰 Chapter 10 — Error Handling
- [ ] `exception handling`
- [ ] `try` / `except` / `else` / `finally`

### 🔰 Chapter 11 — OOP Basics
- [ ] `OOP` — what is it and why
- [ ] `class`
- [ ] `object`
- [ ] `attributes`
- [ ] `methods`
- [ ] `__init__` and `self`

---

## 📘 PART 2 — Intermediate Syllabus
> **Goal:** Write professional, clean, real-world Python. Build projects. Work in teams.

### ⚙️ Chapter 1 — Intermediate Functions
- [ ] `lambda functions`
- [ ] `map`, `filter`, `reduce`
- [ ] `enumerate function`
- [ ] `list comprehension`
- [ ] `*args` and `**kwargs`
- [ ] `global keyword`

### ⚙️ Chapter 2 — OOP Intermediate
- [ ] `attribute` and `static method`
- [ ] `inheritance` and types
- [ ] `super()` method
- [ ] `polymorphism`
- [ ] `abstraction` (abc module)
- [ ] `@classmethod`
- [ ] `@property` decorators
- [ ] `getters` and `setters`
- [ ] `operator overloading`
- [ ] `__str__` and `__len__` (dunder methods)

### ⚙️ Chapter 3 — Advanced OOP & Python Features
- [ ] `custom decorators`
- [ ] `iterators` and `generators`
- [ ] `match case`
- [ ] `__name__ == "__main__"`

### ⚙️ Chapter 4 — Type System (Professional Code)
- [ ] `types definition`
- [ ] `advanced type hints`
- [ ] `typing module`

### ⚙️ Chapter 5 — Working with Data
- [ ] `JSON handling`
- [ ] `regex` (regular expressions)

### ⚙️ Chapter 6 — Concurrency
- [ ] `async` / `await` basics
- [ ] `threading` basics


## ⚙️ PART 2.5 — The Enterprise Guardrails (The 8 Extras)

---

### 🛡️ Chapter 1 — Project Management & Sprint Operations (Extra 1)

- [ ]  Linear / Notion workspace setup for engineering Sprints
- [ ]  Writing explicit engineering issues with functional specs
- [ ]  Issue status tags — Backlog, Todo, In Progress, Review, Done
- [ ]  Git branch naming conventions linked to Issue IDs (e.g., feature/issue-102)
- [ ]  Smart commits — closing issues automatically via Git commit messages

---

### 🛡️ Chapter 2 — Production-Grade Structured Logging (Extra 2)

- [ ]  Python native logging module configuration
- [ ]  Log levels — DEBUG, INFO, WARNING, ERROR, CRITICAL
- [ ]  Log formatters — timestamps, log levels, file names, line numbers
- [ ]  Stream handlers (console output) vs File handlers (persistent storage)
- [ ]  RotatingFileHandler — setting maxBytes and backupCount to prevent memory overflow
- [ ]  Creating a reusable logger.py utility module

---

### 🛡️ Chapter 3 — Zero-Trust Environment Security (Extra 3)

- [ ]  Credential hygiene principles — why raw strings break security
- [ ]  python-dotenv library — loading keys via load_dotenv()
- [ ]  Accessing variables securely using os.environ.get()
- [ ]  Configuring .gitignore specifically to catch .env files
- [ ]  Creating a professional .env.example team template
- [ ]  Validating required environment variables at application startup

---

### 🛡️ Chapter 4 — Interactive Documentation & Deployment (Extra 4)

- [ ]  FastAPI framework initialization basics
- [ ]  Exposing background scripts as public HTTP endpoints
- [ ]  Auto-generated documentation engines — Swagger UI (/docs) and ReDoc (/redoc)
- [ ]  Deploying web services via cloud infrastructure providers (Railway / Render)
- [ ]  Exposing public service URLs for rapid Recruiter / Client testing

---

### 🛡️ Chapter 5 — Runtime Data Schema Validation (Extra 5)

- [ ]  Pydantic BaseModel setup for data parsing
- [ ]  Type enforcement, coercion, and automatic casting
- [ ]  Field validation guardrails — string lengths, numerical ranges, regex matching
- [ ]  Handling incoming JSON payloads securely
- [ ]  Pandera basics — validating tabular pandas DataFrames (Data Engineering checkpoint)
- [ ]  Graceful handling of ValidationError exceptions

---

### 🛡️ Chapter 6 — Automated Contract & Integration Testing (Extra 6)

- [ ]  pytest framework installation and configuration
- [ ]  Writing assertive test cases — test_* naming conventions
- [ ]  Testing FastAPI endpoints using TestClient
- [ ]  Mocking external components — unittest.mock and patch
- [ ]  Firing single-command integration tests (pytest -v)
- [ ]  Pre-commit hook integration — running tests automatically before a Git commit

---

### 🛡️ Chapter 7 — Slack Operations & Fail-Safe Error Alerting (Extra 7)

- [ ]  Remote agency engineering communication etiquette (Threads, Slack Markdown)
- [ ]  The danger of silent script death in production automation
- [ ]  Slack App creation basics via the Slack Developer Console
- [ ]  Generating and managing Slack Incoming Webhook URLs
- [ ]  Constructing automated payload alert blocks with tracebacks and error messages
- [ ]  Slack Block Kit Builder for designing rich, structured diagnostic reports
- [ ]  Slack Bolt Framework basics — handling custom Slash commands (e.g., /run-scraper)

---

### 🛡️ Chapter 8 — Low-Latency In-Memory Caching (Extra 8)

- [ ]  Caching principles — reducing infrastructure costs and heavy query latency
- [ ]  Cachetools library — TTL (Time-To-Live) and LRU (Least Recently Used) caching
- [ ]  Redis database fundamentals — key-value store architectures
- [ ]  Connecting Python scripts to a Redis instance via redis-py
- [ ]  Wrapping repetitive, expensive database lookups or external API requests in cache layers

---

### 🛡️ Chapter 9 — High-Velocity Guardrails & CI/CD Pipelines (Extra 9)

- [ ]  uv library setup — lightning-fast package resolution replacing traditional slow pip operations
- [ ]  Ruff framework execution — executing rapid static checking and automated PEP8 corporate style formatting
- [ ]  Bandit analyzer — running AST (Abstract Syntax Tree) scans to catch codebase injection flaws and loose dependencies
- [ ]  Automated Pre-Commit hooks — constructing a local .pre-commit-config.yaml matrix to block broken or unvetted git commits
- [ ]  Tenacity integration — wrapping flaky network requests or scrapers in self-healing exponential backoff decorators
- [ ]  GitHub Actions CI/CD workflows — building a .github/workflows/ci.yml pipeline to auto-test and badge code on every push

---

## 📙 PART 3 — The Bridge

> **Goal:** Connect your Python skills to the real world. 

---

### 🐍 Chapter 0 — Python Environment & Dependency Management

(Place before Phase 3 Chapter 1 — ~3-4 hours)

- [ ]  `python -m venv env — creating virtual environments`
- [ ]  `activating/deactivating — Linux/Mac vs Windows`
- [ ]  `pip install, pip uninstall, pip list`
- [ ]  `pip freeze > requirements.txt`
- [ ]  `pip install -r requirements.txt`
- [ ]  `.gitignore — never commit env/`
- [ ]  `why global installs cause conflicts`
- [ ]  `checking active interpreter — python --version, which python`
- [ ]  `requirements.txt vs requirements-dev.txt`
- [ ]  `pyproject.toml — recognition level only`
- [ ]  `venv vs Docker container isolation — conceptual link`


### 🔗 Chapter 1 — Git & GitHub Mastery (Professional Level)

- [ ]  `git init, clone, add, commit, push, pull`
- [ ]  `branching — git branch, checkout, merge`
- [ ]  `pull requests (PRs) and code reviews`
- [ ]  `git stash, git log, git diff`
- [ ]  `resolving merge conflicts`
- [ ]  `.gitignore — what to never push`
- [ ]  `GitHub Actions — basic CI/CD pipeline`
- [ ]  `open source contribution workflow`
- [ ]  `writing professional README.md files`
- [ ]  `semantic commit messages`


### 🔗 Chapter 2 — Working with APIs

- [ ]  `what is an API — REST vs GraphQL`
- [ ]  `HTTP methods — GET, POST, PUT, DELETE`
- [ ]  `requests library — get(), post(), headers`
- [ ]  `API keys — how to use and protect them`
- [ ]  `environment variables (.env files)`
- [ ]  `python-dotenv library`
- [ ]  `parsing JSON responses`
- [ ]  `error handling for API failures`
- [ ]  `rate limiting and pagination`
- [ ]  `authentication — Bearer tokens, OAuth basics`


### 🔗 Chapter 3 — Web Scraping

- [ ]  `BeautifulSoup4 — parsing HTML`
- [ ]  `requests + BeautifulSoup workflow`
- [ ]  `CSS selectors and HTML navigation`
- [ ]  `Selenium — scraping JavaScript-rendered pages`
- [ ]  `handling pagination in scrapers`
- [ ]  `rotating headers and user agents`
- [ ]  `storing scraped data to CSV/JSON`
- [ ]  `ethical scraping — robots.txt`
- [ ]  `Playwright (modern alternative to Selenium)`


### 🔗 Chapter 4 — Databases & SQL

- [ ]  `what is a database and why it matters`
- [ ]  `SQLite with Python — sqlite3 module`
- [ ]  `CREATE, INSERT, SELECT, UPDATE, DELETE`
- [ ]  `WHERE, ORDER BY, GROUP BY, JOIN`
- [ ]  `SQLAlchemy ORM — models and sessions`
- [ ]  `PostgreSQL basics — connecting via psycopg2`
- [ ]  `database design — tables, keys, relationships`
- [ ]  `CRUD operations in Python`
- [ ]  `migrations basics`
- [ ]  `MongoDB basics — PyMongo`


### 🔗 Chapter 5 — File Processing & Automation

- [ ]  `CSV processing — csv module and pandas basics`
- [ ]  `Excel automation — openpyxl`
- [ ]  `PDF reading — PyPDF2`
- [ ]  `sending emails with Python — smtplib`
- [ ]  `scheduling tasks — schedule library`
- [ ]  `automating file system tasks — os, shutil, pathlib`
- [ ]  `working with dates and times — datetime`
- [ ]  `logging — proper log files for production`
- [ ]  `argparse — command line tools`


### 🔗 Chapter 6 — Web Frameworks — FastAPI

- [ ]  `what is a web framework`
- [ ]  `FastAPI installation and project structure`
- [ ]  `creating routes — GET, POST, PUT, DELETE`
- [ ]  `path parameters and query parameters`
- [ ]  `request body with Pydantic models`
- [ ]  `response models and status codes`
- [ ]  `dependency injection basics`
- [ ]  `FastAPI automatic docs — Swagger UI`
- [ ]  `connecting FastAPI to a database`
- [ ]  `background tasks in FastAPI`
- [ ]  `CORS and middleware`
- [ ]  `deploying FastAPI to Railway or Render`


### 🔗 Chapter 7 — Automation with n8n & Make.com

- [ ]  `what is no-code automation`
- [ ]  `n8n — self-hosted setup with Docker`
- [ ]  `n8n workflows — triggers, nodes, connections`
- [ ]  `connecting n8n to external APIs`
- [ ]  `Make.com (Makefile) — visual workflow builder`
- [ ]  `Zapier basics and when to use it`
- [ ]  `webhooks — sending and receiving`
- [ ]  `combining Python scripts with n8n workflows`
- [ ]  `building client-ready automation workflows`
- [ ]  `error handling in automation workflows`


### 🔗 Chapter 8 — Docker & Deployment

- [ ]  `what is Docker and why it matters`
- [ ]  `Dockerfile — writing your first container`
- [ ]  `docker build, run, ps, stop, rm`
- [ ]  `docker-compose for multi-container apps`
- [ ]  `environment variables in Docker`
- [ ]  `pushing to Docker Hub`
- [ ]  `deploying to Railway, Render, or Fly.io`
- [ ]  `basic Linux commands for server management`
- [ ]  `SSH into a remote server`
- [ ]  `setting up a domain and HTTPS`


### 🔗 Chapter 9 — Agency-Grade Project Building

- [ ]  `project planning — scoping and requirements`
- [ ]  `folder structure for professional Python projects`
- [ ]  `writing technical documentation`
- [ ]  `unit testing — pytest basics`
- [ ]  `writing a requirements.txt and setup.py`
- [ ]  `code quality — black, flake8, isort`
- [ ]  `pre-commit hooks`
- [ ]  `project versioning — semantic versioning`
- [ ]  `writing client proposals and project briefs`
- [ ]  `delivering projects professionally`

---

## 📕 PHASE 4 — Specialization

> **Goal:** Become an AI Automation specialist.

---

### 🤖 Chapter 1 — OpenAI API & Prompt Engineering

- [ ]  `OpenAI API setup and authentication`
- [ ]  `GPT models — GPT-4o, GPT-4-turbo, GPT-3.5`
- [ ]  `chat completions — messages, roles, system prompts`
- [ ]  `temperature, max_tokens, top_p parameters`
- [ ]  `prompt engineering principles`
- [ ]  `few-shot prompting`
- [ ]  `chain of thought prompting`
- [ ]  `structured output — JSON mode`
- [ ]  `function calling in OpenAI`
- [ ]  `managing API costs and token usage`
- [ ]  `streaming responses`

---

### 🤖 Chapter 2 — LangChain Fundamentals

- [ ]  `what is LangChain and why it exists`
- [ ]  `LLMs and Chat Models in LangChain`
- [ ]  `prompt templates — PromptTemplate, ChatPromptTemplate`
- [ ]  `chains — LLMChain, SequentialChain`
- [ ]  `LangChain Expression Language (LCEL)`
- [ ]  `output parsers`
- [ ]  `document loaders — PDF, CSV, web pages`
- [ ]  `text splitters — chunking strategies`
- [ ]  `embeddings — OpenAI, HuggingFace`
- [ ]  `vector stores — ChromaDB, FAISS`
- [ ]  `retrievers and similarity search`
- [ ]  `memory — ConversationBufferMemory, SummaryMemory`

---

### 🤖 Chapter 3 — LangChain Advanced — Agents & Tools

- [ ]  `what are AI agents`
- [ ]  `LangChain tools — built-in and custom`
- [ ]  `ReAct agent pattern`
- [ ]  `building custom tools for agents`
- [ ]  `agent executors`
- [ ]  `tool calling and function routing`
- [ ]  `web search tool — Tavily, SerpAPI`
- [ ]  `code execution tools`
- [ ]  `agents with memory`
- [ ]  `LangSmith — debugging and monitoring agents`
- [ ]  `LangServe — deploying LangChain as an API`

---

### 🤖 Chapter 4 — CrewAI — Multi-Agent Systems

- [ ]  `what are multi-agent systems`
- [ ]  `CrewAI installation and architecture`
- [ ]  `agents — role, goal, backstory, tools`
- [ ]  `tasks — description, expected output, agent assignment`
- [ ]  `crew — process types (sequential, hierarchical)`
- [ ]  `custom tools for CrewAI agents`
- [ ]  `agent collaboration and delegation`
- [ ]  `human-in-the-loop workflows`
- [ ]  `CrewAI with LangChain tools`
- [ ]  `output handling and parsing crew results`
- [ ]  `CrewAI flows — event-driven agent pipelines`

---

### 🤖 Chapter 5 — RAG Systems & Vector Databases

- [ ]  `RAG architecture — deep understanding`
- [ ]  `chunking strategies — size, overlap, semantic`
- [ ]  `embedding models comparison`
- [ ]  `Pinecone — cloud vector database`
- [ ]  `ChromaDB — local vector database`
- [ ]  `Weaviate basics`
- [ ]  `hybrid search — keyword + semantic`
- [ ]  `reranking results`
- [ ]  `advanced retrieval strategies`
- [ ]  `RAG evaluation — precision, recall`
- [ ]  `building production RAG pipelines`

---

### 🤖 Chapter 6 — AI Automation Pipelines

- [ ]  `connecting AI agents to n8n workflows`
- [ ]  `AI-powered email processing and routing`
- [ ]  `document processing automation with AI`
- [ ]  `AI-powered data extraction from unstructured text`
- [ ]  `voice AI — Whisper for transcription`
- [ ]  `image analysis — GPT-4 Vision`
- [ ]  `AI-powered web scraping and summarization`
- [ ]  `trigger-based AI workflows`
- [ ]  `AI agents with database memory`
- [ ]  `monitoring and logging AI pipelines`

---

### 🤖 Chapter 7 — Building AI Products (Full Stack AI)

- [ ]  `AI product architecture — backend + frontend + AI`
- [ ]  `FastAPI + LangChain integration`
- [ ]  `streaming AI responses to frontend`
- [ ]  `user authentication for AI apps — JWT`
- [ ]  `rate limiting AI endpoints`
- [ ]  `usage tracking and billing logic`
- [ ]  `deploying AI apps — Railway, Render, AWS`
- [ ]  `cost optimization — caching, batching`
- [ ]  `AI product pricing models`
- [ ]  `building a waitlist and onboarding flow`

### 🤖 Chapter 8 — LangGraph & Stateful Multi-Agent Orchestration

- [ ]  `what is LangGraph and when to use it over CrewAI`
- [ ]  `State Graphs — nodes, edges, and conditional edges`
- [ ]  `State management — defining and updating the overall GraphState`
- [ ]  `Conditional routing — writing deterministic Python router logic`
- [ ]  `State persistence — implementing memory checkpoints and threads`
- [ ]  `Human-in-the-Loop (HITL) — interrupting graph execution for webhooks`
- [ ]  `Streaming states — monitoring token chunks and node transitions live`
- [ ]  `Sub-graphs — nestable graph architectures for complex workflows`
- [ ]  `Error handling and self-healing loops inside graph nodes`