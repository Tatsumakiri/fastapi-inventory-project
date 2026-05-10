
from fastapi import FastAPI, Depends, HTTPException
from app.database import Base, engine
from app.routers import items
from app.database import SessionLocal
from sqlalchemy.orm import Session
from app import models, schemas

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
#Base.metadata.create_all(bind=engine)

@app.put("/items/{item_id}")
def update_item(
    item_id: int,
    item: schemas.ItemCreate,
    db: Session = Depends(get_db)
):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()

    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db_item.name = item.name
    db_item.quantity = item.quantity

    db.commit()
    db.refresh(db_item)

    return db_item

@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()

    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(db_item)
    db.commit()

    return {"message": "Item deleted successfully"}

@app.get("/items/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return item

app.include_router(items.router)

