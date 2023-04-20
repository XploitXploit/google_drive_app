from app.handlers import DriveHandler, DwhUploader
from app.settings import settings


def leasing():
    dh = DriveHandler(settings.CREDS_FILE)
    data = dh.get_spreadsheet_values('14geSRGuxFPNe1E7YhN70uhWmIUSfP0x7HG1LiT9oNiY')
    uploader = DwhUploader()
    uploader.upload_to_dwh(data)


if __name__ == "__main__":
    leasing()
