# AgentStack Receipt Manager

AgentStack Receipt Manager is an automated system designed to find and upload receipts for deductible business expenses. It monitors the Downloads folder for receipts and uploads them to a specified Google Drive folder.

## Features

- Automatically scans your Downloads folder for receipts
- Identifies potential deductible business expenses
- Uploads relevant receipts to a designated Google Drive folder

## Prerequisites

- Python 3.10 - 3.12
- Poetry for dependency management
- Google Cloud Platform account with Drive API enabled
- Google Drive folder for receipt storage
- Not tested with Windows and so assumes you're on a Mac or Linux system

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/agentstack_receipt_manager.git
   cd agentstack_receipt_manager
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   ```

3. Copy the `.env.example` file to `.env` and fill in the required environment variables:
   ```
   cp .env.example .env
   ```

4. Edit the `.env` file with your specific paths and credentials.

## REQUIRED: GDrive Folder Setup

1. Find or create the folder that you want Receipts uploaded to in Gdrive
2. Copy the URL which will look like this: `https://drive.google.com/drive/folders/{THIS IS YOUR FOLDER ID}`
3. Copy the folder ID and paste it into the `.env` file under `GDRIVE_UPLOAD_FOLDER_ID`

## REQUIRED: GDrive Permissions Setup (Service Account)

1. Visit https://console.cloud.google.com/apis/api/drive.googleapis.com
2. Create or select a project if required
3. Enable the Google Drive API
4. Click "Create Credentials" in the top banner after enabling the API
1. Select a Service Account as the credential type
2. After creating your service account (the names and scopes in the menus do not matter) navigate to the "Keys" tab of the account
3. Create a new key and download the JSON file
4. Rename the file `gcloud-service-account.json` and place it in the root of this project
5. In the Details tab of your service account, you'll see an email like this: `{YOUR SERVICE_ACCOUNT_NAME_HERE}@{YOUR PROJECT HERE}.iam.gserviceaccount.com`
6. Copy this email. Go to Google Drive and share the Google Drive folder you want to upload to with this email address (ensure they have Editor permissions)

## Usage

To run the receipt manager:

```
poetry shell
agentstack run
```

## Development

To add new agents or tasks, use the AgentStack CLI:

```
agentstack generate agent <agent_name>
agentstack generate task <task_name>
```

To add new tools:

```
agentstack tools add <tool_name>
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
