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
