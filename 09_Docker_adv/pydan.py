from pydantic import BaseModel, Field
from typing import Optional, List
class get_pydan(BaseModel):
    x1 : int = Field(
        ...,
        title="X1",
        description="X1 value",
        example=1
    )
    x2 : int = Field(
        ...,
        title="X2",
        description="X2 value",
        example=1
    )