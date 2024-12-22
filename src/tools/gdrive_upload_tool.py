import os
from crewai_tools import tool
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

FOLDER_ID = os.environ.get('GDRIVE_UPLOAD_FOLDER_ID')

@tool
def upload_file_to_drive_tool(file_path: str, file_name: str):
    """Uploads a file to Google Drive.

    Args:
        file_path: The path to the local file.
        file_name: The name to give the file on Google Drive.
                   If None, the original file name will be used.

    Returns:
        The ID of the uploaded file, or None if an error occurred.
    """
    try:
        # This will automatically read creds from `GOOGLE_APPLICATION_CREDENTIALS` in .env
        service = build('drive', 'v3')

        file_metadata = {'name': file_name, 'parents': [FOLDER_ID]}
        media = MediaFileUpload(file_path, resumable=True)

        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        print(f'File ID: {file.get("id")}')
        return file.get("id")

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
