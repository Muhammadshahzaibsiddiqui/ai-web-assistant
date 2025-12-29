from langchain.tools import Tool
from langchain_community.tools import DuckDuckGoSearchRun

duckduckgo_tool = DuckDuckGoSearchRun()

websearch_tool = Tool(
        name        = "DuckDuckGo_Search",
        func        = duckduckgo_tool.run,
        description = "Search the web using DuckDuckGo"
    )
