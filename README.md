# Customer Experience Analytics 📊

A project for analyzing customer experience data using modern data engineering and analytics tools.

## Table of Contents

- [Overview](#overview) 📖
- [Features](#features) ✨
- [Requirements](#requirements) 🛠️
- [Setup](#setup) ⚙️
    - [Clone the Repository](#clone-the-repository) 🧬
    - [Environment Variables](#environment-variables) 🔑
    - [Install Dependencies](#install-dependencies) 📦
    - [Oracle Database Setup with Docker](#oracle-database-setup-with-docker) 🐳
- [Usage](#usage) 🚀
- [Project Structure](#project-structure) 🗂️
- [Contributing](#contributing) 🤝
- [License](#license) 📄

---

## Overview 📖

This project provides tools and scripts to ingest, process, and analyze customer experience data. It leverages an Oracle database for data storage and supports integration with various analytics platforms.

## Features ✨

- Data ingestion pipelines
- Data transformation and cleaning
- Analytics and reporting modules
- Oracle database integration

## Requirements 🛠️

- Docker 🐳
- Docker Compose (optional)
- Python 3.8+ 🐍
- [Other dependencies as required by your project]

## Setup ⚙️

### Clone the Repository 🧬

```bash
git clone https://github.com/your-username/customer-experience-analytics.git
cd customer-experience-analytics
```

### Environment Variables 🔑

Copy the example environment file and update it with your configuration:

```bash
cp .env.example .env
```

Edit `.env` to set your Oracle DB credentials and other settings.

### Install Dependencies 📦

Install Python dependencies:

```bash
pip install -r requirements.txt
```

### Oracle Database Setup with Docker 🐳

You can run an Oracle Database instance locally using Docker. The following steps use the official Oracle Database image.

#### 1. Pull the Oracle Database Docker Image

```bash
docker pull container-registry.oracle.com/database/express:21.3.0-xe
```

#### 2. Run the Oracle Database Container

```bash
docker run -d \
    --name oracle-xe \
    -p 1521:1521 -p 5500:5500 \
    -e ORACLE_PWD=YourPassword123 \
    container-registry.oracle.com/database/express:21.3.0-xe
```

- Replace `YourPassword123` with a secure password.
- The database will be accessible on port `1521`.

#### 3. Connect to Oracle Database

You can connect using any Oracle client or via SQL*Plus:

```bash
sqlplus system/YourPassword123@localhost:1521/XEPDB1
```

Update your `.env` file with these credentials.

#### 4. (Optional) Stop and Remove the Container

```bash
docker stop oracle-xe
docker rm oracle-xe
```

## Usage 🚀

1. Ensure the Oracle database is running.
2. Run your data ingestion and analytics scripts as described in the project documentation.

## Project Structure 🗂️

```
customer-experience-analytics/
├── data/
├── src/
|   ├──notebooks
|   ├──scripts
|   ├──test
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Contributing 🤝

Contributions are welcome! Please open issues or submit pull requests.

## License 📄

[MIT License](LICENSE)