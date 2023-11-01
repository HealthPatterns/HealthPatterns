# Health Patterns

> [!IMPORTANT]  
> Not all features described are implemented. Please have a look at the roadmap section.

Health Patterns is designed to allow users to easily track pain events. Details can be provided for further analysis and to discover the user's own patterns. Data can be exported as a PDF for offline storage or to show to healthcare professionals. The user system is completely anonymous if desired and it's possible to encrypt one's data.


## Roadmap

| **Feature**   | **Frontend**                    | **Backend**                      |
|---------------|---------------------------------|----------------------------------|
| Pain tracking | :white_check_mark: Implemented  | :white_check_mark: Implemented   |
| Analysis      | :x: Not implemented             | :x: Not  implemented             |
| PDF export    | :x: Not  implemented            | :x: Not  implemented             |
| Encryption    | :x: Not  implemented            | :x: Not  implemented             |
| User System   | :hammer: Partially implemented  | :white_check_mark: Implemented   |



## Installation

Make sure you have [docker](https://docs.docker.com/engine/install/) and [docker compose](https://docs.docker.com/compose/install/) installed on your system.

### Via GitHub

1. Clone the repository
    ```bash
    git clone https://github.com/wmneco/HealthPatterns.git
    ```
2. Go into the folder
    ```bash
    cd HealthPatterns
    ```

### With a project-ZIP

1. Unzip the project-ZIP with a tool like 7zip

2. Open the unzipped folder in the terminal

3. Make sure you are in the correct directory
    ```bash
    pwd #should return 'HealthPatterns'
    ```

## Usage

Launch health patterns with:

```bash
docker compose up
```
Once all the Docker containers are running, open your browser and check out your localhost.

```bash
http://localhost
```

If you would like to view our api-documentation or test endpoints that have no frontend yet, please use this link:

```bash
http://localhost:3000/docs
```

Stop Health Patterns with:

```bash
docker compose down
```

The database is persistent between container up/down. To reset the database do the following:

1. Stop the app:
    ```bash
    docker compose down
    ```

2. Remove the database container:
    ```bash
    docker rm aid-db
    ```

3. Remove the database volume:
    ```bash
    docker volume rm aid-vault_postgresql
    ```

4. Restart the app:
    ```bash
    docker compose up
    ```

Since all dependencies are installed in the containers there will be error-messages and no code suggestions in the local IDE. To remove the errors and get suggestions install the requirements on your local machine.

1. Backend requirements:
    - [Python 3.11.5](https://www.python.org/downloads/release/python-3115/)
    - dependencies (it is recommended to install those in a [virtual environment](https://docs.python.org/3/library/venv.html)):
    ```bash
    pip install -r backend/requirements_local.txt
    ```

2. Frontend requirements:
    - Nico bitte ergänzen
