from pydantic import BaseModel, Field

class Inputdata(BaseModel):
   x1 : int = Field(
      ...,
      description="First input number",
      title="Input number 1",
      example=5
      )
   x2 : int = Field(
      ...,
      description="Second input number",
      title="Input number 2",
      example=10
   ) 