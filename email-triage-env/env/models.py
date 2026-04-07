from pydantic import BaseModel
from typing import Optional

class EmailObservation(BaseModel):
    email_id: str
    subject: str
    body: str
    customer_tier: str
    history: Optional[str]

class AgentAction(BaseModel):
    category: str
    priority: str
    response: str
    escalate: bool

class Reward(BaseModel):
    score: float
    feedback: str