# Etoro Market Monitor App

A FastAPI learning project for monitoring eToro curated lists, watchlists, and portfolio data.

## Overview

This project is a backend application built with FastAPI to explore how APIs are structured and how external market data can be fetched and returned through custom endpoints.

The app connects to eToro public API endpoints using request headers configured through environment variables.

## Features

- Retrieve curated investment lists
- Retrieve watchlists
- Retrieve portfolio data
- Load settings from `.env`
- Organize routes using FastAPI routers
- Begin structuring auth, user, and database modules

## Tech Stack

- Python
- FastAPI
- Pydantic
- Pydantic Settings
- Requests
- Uvicorn

## Project Structure

```text
monitor_app/
  main.py
  api/
    router.py
    v1/
      auth/
      etoro/
      portfolio/
      user/
  core/
    config.py
  db/
    models.py
    session.py
