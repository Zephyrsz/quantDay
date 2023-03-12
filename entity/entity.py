from typing import Optional, List, Dict
# from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel


class Data(BaseModel):
    uri: str
    column_list: List[str]
