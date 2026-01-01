from dataclasses import dataclass
from enum import StrEnum
from typing import Annotated , Literal
from langchain.messages import AIMessage , HumanMessage , ToolMessage
from langchain_core.language_models import BaseChatModel
from langgraph.graph import END , StateGraph
from langgraph.graph.message import add_messages
from langgraph.runtime import Runtime
from pydantic import BaseModel , Field
from Finasta.Config import config 
from Finasta.Tools import fetch_sec_filing_sections , get_historical_stock_prices

SUPERVISOR_PROMPT = """

"""