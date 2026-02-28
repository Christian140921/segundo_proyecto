# NodalCMS

A modern, scalable content management system built with FastAPI and PostgreSQL.

## Features

- RESTful API
- User authentication & authorization
- Content management capabilities
- Machine learning integration
- Docker support
- Comprehensive testing

## Project Structure

```
nodalcms/
├── src/api/                 # Main API application
│   ├── core/               # Core functionality
│   ├── config/             # Configuration
│   ├── models/             # Database models
│   ├── schemas/            # Pydantic schemas
│   ├── services/           # Business logic
│   ├── repositories/       # Data access layer
│   ├── ml/                 # Machine learning modules
│   ├── utils/              # Utility functions
│   ├── middleware/         # Custom middleware
│   ├── workers/            # Background workers
│   └── main.py            # Application entry point
├── tests/                  # Test suites
├── scripts/                # Utility scripts
├── migrations/             # Database migrations
├── data/                   # Data files
├── docs/                   # Documentation
└── docker/                 # Docker configuration
```

## Quick Start

### Prerequisites

- Python 3.9+
- Docker & Docker Compose (optional)
- PostgreSQL 16+ (if running locally)

### Local Development

1. **Clone the repository:**
```bash
git clone <repository-url>
cd nodalcms
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment:**
```bash
cp .env.example .env
# Edit .env with your settings
```

5. **Run the application:**
```bash
uvicorn src.api.main:app --reload
```

The API will be available at http://localhost:8000

### Docker Deployment

```bash
docker-compose up -d
```

## API Documentation

Once the application is running, visit:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test type
pytest tests/unit/
pytest tests/integration/
pytest tests/e2e/
```

## Development

### Code Style

This project uses:
- **Black** for code formatting
- **isort** for import sorting
- **mypy** for type checking
- **flake8** for linting

```bash
# Format code
black src tests

# Sort imports
isort src tests

# Type checking
mypy src

# Linting
flake8 src tests
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, email support@nodalcms.com or open an issue on GitHub.
