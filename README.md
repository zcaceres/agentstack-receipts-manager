# agentstack_receipt_manager
This is the start of your AgentStack project.

~~ Built with AgentStack ~~

Activate env with `poetry shell`

## GDrive Folder Setup
1. Find or create the folder that you want Receipts uploaded to in Gdrive
2. Copy the URL which will look like this: `https://drive.google.com/drive/folders/{THIS IS YOUR FOLDER ID}`
3. Copy the folder ID and paste it into the `.env` file under `GDRIVE_UPLOAD_FOLDER_ID`

## GDrive Permissions Setup (Service Account)

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



## How to build your Crew
### With the CLI
Add an agent using AgentStack with the CLI:
`agentstack generate agent <agent_name>`
You can also shorten this to `agentstack g a <agent_name>`
For wizard support use `agentstack g a <agent_name> --wizard`
Finally for creation in the CLI alone, use `agentstack g a <agent_name> --role/-r <role> --goal/-g <goal> --backstory/-b <backstory> --model/-m <provider/model>`

This will automatically create a new agent in the `agents.yaml` config as well as in your code. Either placeholder strings will be used, or data included in the wizard.

Similarly, tasks can be created with `agentstack g t <tool_name>`

Add tools with `agentstack tools add <tool_name>` and view tools available with `agentstack tools list`

## How to use your Crew
In this directory, run `poetry install`

To run your project, use the following command:
`crewai run` or `python src/main.py`

This will initialize your crew of AI agents and begin task execution as defined in your configuration in the main.py file.

#### Replay Tasks from Latest Crew Kickoff:

CrewAI now includes a replay feature that allows you to list the tasks from the last run and replay from a specific one. To use this feature, run:
`crewai replay <task_id>`
Replace <task_id> with the ID of the task you want to replay.

#### Reset Crew Memory
If you need to reset the memory of your crew before running it again, you can do so by calling the reset memory feature:
`crewai reset-memory`
This will clear the crew's memory, allowing for a fresh start.
