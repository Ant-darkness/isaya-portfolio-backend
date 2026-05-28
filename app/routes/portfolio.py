from fastapi import APIRouter
from app.data.portfolio_data import portfolio_data

router = APIRouter(
    prefix="/api",
    tags=["Portfolio"]
)

@router.get("/portfolio")
def get_portfolio():
    return portfolio_data
