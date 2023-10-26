# HealthPatterns

> [!IMPORTANT]  
> Not all features described are implemented. Please have a look at the roadmap section.

Health Patterns is designed to allow users to easily track pain. Details can be provided for further analysis through Health Patterns and export as a PDF for doctors, for example. The user system is completely anonymous if desired. It should also be possible to encrypt one's own data.


## Roadmap

| **Feature**   | **Frontend**                    | **Backend**                      |
|---------------|---------------------------------|----------------------------------|
| Pain tracking | :white_check_mark: implemented  | :white_check_mark: implemented   |
| Analysis      | :x: not implemented             | :x: not  implemented             |
| PDF export    | :x: not  implemented            | :x: not  implemented             |
| Encryption    | :x: not  implemented            | :x: not  implemented             |
| User System   | :hammer: Partially implemented  | :white_check_mark: implemented   |



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

If you would like to view our backend documentation, please use this link:

```bash
http://localhost:3000/docs
```

Stop Health Patterns with:

```bash
docker compose down
```

## License