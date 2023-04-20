from typing import List
from google.oauth2 import service_account
import gspread
import logging
from googleapiclient.errors import HttpError
from app.schema import Leasing
from app.db.config import init_dwh_db

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s [%(name)-12s] %(levelname)-8s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


class DriveHandler:
    def __init__(self, service_account_file):
        self.service_account_file = service_account_file

    def _create_service(self):
        try:
            credentials = service_account.Credentials.from_service_account_file(
                self.service_account_file,
                scopes=[
                    "https://www.googleapis.com/auth/spreadsheets",
                    "https://www.googleapis.com/auth/drive",
                ],
            )
            gc = gspread.authorize(credentials)
            return gc
        except Exception as e:
            print(f"Error creating service: {e}")
            return None

    def get_spreadsheet_values(self, file_id):
        try:
            gc = self._create_service()
            if not gc:
                return None
            sh = gc.open_by_key(file_id)
            worksheet = sh.get_worksheet(1)  # Get the first worksheet
            data = worksheet.get_all_records(expected_headers=[])
            leasing_instances = [Leasing(**d) for d in data]
            return leasing_instances
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None


class DwhUploader:
    def __init__(self):
        self.db = init_dwh_db()
    
    def upload_to_dwh(self, leasing_list: List[Leasing]):
        logger.info(f"Uploading {len(leasing_list)} leasing vehicles to DWH")
        leasing_dicts = [leasing_instance.dict() for leasing_instance in leasing_list]
        self.db.setup_leasing()
        self.db.insert_leasing(*leasing_dicts)
