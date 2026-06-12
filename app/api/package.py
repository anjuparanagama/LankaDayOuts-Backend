from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.api.deps import get_db

router = APIRouter()


@router.get("/test-db")
def health_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"status": "TiDB connected successfully"}

@router.get("/packages")
def get_packages(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM packages"))
    rows = result.mappings().all()
    packages = []
    for r in rows:
        packages.append({
            "id": r.get("id"),
            "title": r.get("title"),
            "location": r.get("location"),
            "price": float(r.get("price") or 0),
            "rating": float(r.get("rating") or 0),
            "reviewsCount": r.get("reviews_count") or 0,
            "type": r.get("type"),
            "category": r.get("category"),
            "image": r.get("image"),
            "tags": r.get("tags") or [],
            "isFeatured": bool(r.get("is_featured") or 0),
        })
    return {"packages": packages}