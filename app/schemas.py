from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional


# Allowed values for an issue's lifecycle stage
class IssueStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"


    # Allowed values for an issue's urgency level
class IssuePriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


    # Schema for creating a new issue — sent by the client
class IssueCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)          # 3–100 chars, required
    description: str = Field(min_length=5, max_length=1000)   # 5–1000 chars, required
    priority: IssuePriority = IssuePriority.medium             # defaults to medium if not provided


    # Schema for updating an existing issue — all fields optional (send only what changed)
class IssueUpdate(BaseModel):
    title: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = Field(default=None, max_length=1000)
    priority: Optional[IssuePriority] = None
    status: Optional[IssueStatus] = None                      # allows moving issue through lifecycle


    # Schema for API responses — shape of data returned to the client
class IssueOut(BaseModel):
    id: str            # server-generated, not set by the user
    title: str
    description: str
    priority: IssuePriority
    status: IssueStatus