import os
from crewai_tools import DirectoryReadTool

dir_read_tool = DirectoryReadTool(directory=os.environ.get("DOWNLOADS_ABSOLUTE_PATH"))
