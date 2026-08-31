from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.clase import schemas, services
from src.database import get_db

router = APIRouter(
    prefix="/clases",
    tags=["clases"]
)

@router.post("/", response_model=schemas.Clase)
def create_clase(clase: schemas.ClaseCreate, db: Session = Depends(get_db)):
    return services.create_clase(db=db, clase=clase)

@router.get("/", response_model=list[schemas.Clase])
def read_clases(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return services.get_clases(db, skip=skip, limit=limit)

@router.get("/{clase_id}", response_model=schemas.Clase)
def read_clase(clase_id: int, db: Session = Depends(get_db)):
    db_clase = services.get_clase(db, clase_id=clase_id)
    if db_clase is None:
        raise HTTPException(status_code=404, detail="Clase no encontrada")
    return db_clase