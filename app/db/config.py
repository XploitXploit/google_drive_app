from urllib.parse import quote
import pugsql
from app.settings import settings


def dwh_conn_string_with_path() -> str:
    path_opt = quote(f"-c search_path={settings.SEARCH_PATH}")
    all_opts = f"?application_name={settings.APP_NAME}&options={path_opt}"
    return settings.DWH_CONN + all_opts


def init_dwh_db():
    queries = pugsql.module(settings.PUGSQL_QUERIES)
    queries.connect(dwh_conn_string_with_path())
    return queries

