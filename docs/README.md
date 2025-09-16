# Ronsare Core API

A **FastAPI-based backend** for user management, built with PostgreSQL and in-memory storage for demo purposes. Includes JWT authentication utilities, service layers, and modular architecture.

---

## Table of Contents

- [Features](#features)
- [Folder Structure](#folder-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [Testing](#testing)
- [API Endpoints](#api-endpoints)
- [Notes](#notes)

---

## Features

- FastAPI REST API
- Modular folder structure:
  - `api/v1/endpoints` → Route definitions
  - `services` → Business logic
  - `crud` → Data access layer
  - `schemas` → Pydantic models for request/response
  - `core` → Config, database, security, logger utilities
- JWT-based authentication (via `python-jose`)
- PostgreSQL integration (via SQLAlchemy)
- Alembic migrations

---

## Folder Structure

