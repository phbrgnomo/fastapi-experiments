### Installation

#### Conda

1. Make sure you have Conda installed. If not, you can install it from [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

2. Create a Conda environment using the provided `environment.yml` file:

```bash
conda env create -f environment.yml
```

3. Activate the Conda Environment

```bash
conda activate myenv  # Replace "myenv" with the actual environment name
```

#### Poetry

4. Install poetry dependencies

```bash
poetry install
```

### Usage

To start the web server with hot reload run the following

```bash
uvicorn main:app --reload
```

> **Note**:
The command uvicorn `main:app` refers to:
`main`: the file [main.py](main.py) (the Python "module").
`app`: the object created inside of [main.py](main.py) with the line app = FastAPI().
`--reload`: make the server restart after code changes. Only use for development.

## API Docs

FastAPI auto generates the API documentation. You can see them on the following links after starting the uvicorn server:

http://localhost:8000/docs

http://localhost:8000/redoc

The documentation schema can be found here:

http://localhost:8000/openapi.json