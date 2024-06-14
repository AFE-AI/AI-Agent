## https://serper.dev/

from dotenv import load_dotenv # type: ignore
load_dotenv()
import os
from NewsWriterTool import NewsWriterTool as NewsWriterTool


# Web Searching tool
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

from crewai_tools import SerperDevTool # type: ignore

# Initialize the tool for internet searching capabilities
SerperDevTool = SerperDevTool()

# Initialize the writer tool
writer_tool = NewsWriterTool




