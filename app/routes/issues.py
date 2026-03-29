from fastapi import APIRouter, HTTPException, status
from app.routes.storage import load_data, save_data
from app.schemas import IssueCreate, IssueUpdate, IssueOut
from uuid import uuid4

router = APIRouter(prefix="/api/v1/issues", tags=["issues"])
@router.get("/", response_model=list[IssueOut])
async def get_issues():
    """Get all issues."""
    issues = load_data()
    if issues is not None:
        return issues


@router.post("/", response_model=IssueOut, status_code=status.HTTP_201_CREATED)
async def create_issue(issue: IssueCreate):
    """Create a new issue."""
    issues = load_data()
    new_issue = IssueOut(
        id=str(len(issues) + 1),  # Simple ID generation (not for production)
        title=issue.title,
        description=issue.description,
        priority=issue.priority,
        status="open"
    )
    issues.append(new_issue.dict())  # Convert Pydantic model to dict before saving
    save_data(issues)
    return new_issue