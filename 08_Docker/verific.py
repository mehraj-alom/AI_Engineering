from pydantic import BaseModel, Field
from typing import Optional

class Data(BaseModel):
    x1 : int = Field(...,
                    title="X1",
        description="X1 value",
        ge=0
    )
    x2 : int = Field(...,
                    title="X2",
        description="X2 value",
        ge=0
    )