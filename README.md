# paint-yourself-api

API for the Paint Yourself mobile application

## Getting Started

### Prerequisites

You will need to have installed:

1. [Python](https://www.python.org/) v3.9 or greater
1. [Poetry](https://python-poetry.org/docs/#installation) v1.1 or greater

### Running for development

1. Clone the repo.

   ```bash
   git clone https://github.com/TCDPaintYourself/paint-yourself-api
   ```

1. Navigate into the cloned GitHub repository.

   ```bash
   cd paint-yourself-api
   ```

1. Install the dependencies

   ```bash
   poetry install
   ```
   OR

   ```bash
   pip install -r requirements.txt
   ```
   and skip to last step

1. Activate the python virtual environment.

   ```bash
   poetry shell
   ```

1. Run the server.

   ```bash
   uvicorn paint_yourself_api.main:app --reload
   ```

   Alternatively, if you are using VSCode, you can use `f5` to launch a debug
   session (ensure that you have set up the [poetry python
   environment](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment)).

The API will be deployed locally at <http://localhost:8000> and the API
documentation can be found at <http://localhost:8000/docs>.
