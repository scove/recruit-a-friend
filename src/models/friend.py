from dataclasses import dataclass
from typing import Optional


@dataclass
class RequiredData():
  pass

@dataclass
class Friend(RequiredData):
  name: str
  email: Optional[str]
  phone_number: Optional[int]
  interests: list