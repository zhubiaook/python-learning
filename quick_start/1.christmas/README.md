# Christmas

A demo Python project showcasing **src layout** and **absolute imports** following Google Python Style Guide best practices.

## Project Structure

```
christmas/
├── pyproject.toml          # Project configuration
├── README.md
├── src/
│   └── christmas/          # Main package
│       ├── main.py         # Entry point
│       ├── helper.py       # Helper utilities
│       └── middleware/     # Subpackage
│           ├── authn.py
│           └── token.py
└── tests/                  # Test directory
```

## Why Src Layout?

The src layout is recommended by Google and major Python organizations:

- **Prevents accidental imports** - Can't import uninstalled local code
- **Cleaner separation** - Source code isolated from project files
- **Production-ready** - Tests run against installed package, matching production

## Absolute Imports (Google Style)

All imports use absolute paths from the package root:

```python
# ✅ Correct - Absolute imports
from christmas import helper
from christmas.middleware import authn

# ❌ Avoid - Relative imports
from . import helper
from ..middleware import authn
```

---

## Development Setup

### Prerequisites

- Python 3.9+
- pip or [uv](https://github.com/astral-sh/uv) (recommended)

### Quick Start

```bash
# Clone the repository
git clone <repository-url>
cd christmas

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Install in editable mode with dev dependencies
pip install -e .[dev]

# Run the application
christmas
```

### Using uv (Faster Alternative)

```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sync dependencies
uv sync

# Run the application
uv run christmas
```

---

## Production Deployment

### Step 1: Build the Wheel Package

```bash
# Install build tool
pip install build

# Build wheel package
python -m build

# Output: dist/christmas-0.1.0-py3-none-any.whl
```

### Option A: Docker Deployment

Create `Dockerfile`:

```dockerfile
# Stage 1: Build
FROM python:3.11-slim as builder

WORKDIR /app
COPY . .

RUN pip install build && python -m build

# Stage 2: Runtime
FROM python:3.11-slim

WORKDIR /app

# Copy and install wheel
COPY --from=builder /app/dist/*.whl .
RUN pip install *.whl && rm *.whl

# Run the application
CMD ["christmas"]
```

Build and run:

```bash
# Build image
docker build -t christmas:latest .

# Run container
docker run --rm christmas:latest
```

### Option B: Systemd Deployment

1. **Install the wheel on target server:**

```bash
# Copy wheel to server
scp dist/christmas-0.1.0-py3-none-any.whl user@server:/tmp/

# On server: install globally or in venv
ssh user@server
sudo pip install /tmp/christmas-0.1.0-py3-none-any.whl
```

2. **Create systemd service file** `/etc/systemd/system/christmas.service`:

```ini
[Unit]
Description=Christmas Application
After=network.target

[Service]
Type=simple
User=www-data
ExecStart=/usr/local/bin/christmas
Restart=on-failure
RestartSec=5

# Environment variables (if needed)
# Environment=SOME_VAR=value

[Install]
WantedBy=multi-user.target
```

3. **Enable and start service:**

```bash
# Reload systemd
sudo systemctl daemon-reload

# Enable auto-start on boot
sudo systemctl enable christmas

# Start the service
sudo systemctl start christmas

# Check status
sudo systemctl status christmas
```

---

## Best Practices Summary

| Practice | Benefit |
|----------|---------|
| Src layout | Prevents accidental local imports |
| Absolute imports | Clear, explicit dependencies |
| Wheel packaging | Reproducible, versioned deployments |
| Multi-stage Docker | Smaller production images |
| Systemd service | Process management, auto-restart |

## License

MIT
