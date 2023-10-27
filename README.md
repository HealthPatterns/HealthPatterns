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

1. Clone the repostory
    ```bash
    git clone https://github.com/wmneco/aid-vault.git
    ```
2. Go into the folder
    ```bash
    cd aid-vault
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

## License