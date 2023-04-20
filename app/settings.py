from pydantic import BaseSettings, BaseModel


class Base(BaseSettings):
    CLOUD_SQL_PROXY_CRED: str
    CREDS_FILE: str = "./creds.json"
    DWH_CONN: str = ""
    PUGSQL_QUERIES: str = "./app/db/sql/"
    SEARCH_PATH: str = "awto_cl"
    APP_NAME: str = "ms-google-drive"
    LEASING_TABLE_DEF: dict = ""

    class Config:
        env_file = ".env"


settings = Base()
