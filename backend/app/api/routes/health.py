from fastapi import APIRouter

print("health route loaded")

router = APIRouter()    

@router.get("/health",tags=["health"])
def health():
    return {"status": "ok"}

@router.get("/version",tags=["health"])
def version():
    return {"version": "phase-1-day-2"}