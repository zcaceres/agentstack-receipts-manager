import os
from crewai_tools import PDFSearchTool

pdf_search_tool = PDFSearchTool(directory=os.environ.get("DOWNLOADS_ABSOLUTE_PATH"))
