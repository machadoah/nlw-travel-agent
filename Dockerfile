# Use the AWS base image for Python 3.12
FROM public.ecr.aws/lambda/python:3.12

# Install build-essential compiler and tools
RUN microdnf update -y && microdnf install -y gcc-c++ make

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Change working directory to the lambda task root
WORKDIR ${LAMBDA_TASK_ROOT}

# Copy the Poetry lock file and the pyproject.toml file
COPY pyproject.toml poetry.lock ./

# Install dependencies with Poetry
RUN poetry install --no-root --no-dev

# Copy function code
COPY travel_agent.py ./

# Set the permissions to make the file executable
RUN chmod +x travel_agent.py

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD ["travel_agent.lambda_handler"]
