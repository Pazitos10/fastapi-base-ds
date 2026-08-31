from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.departamento import schemas, services
from src.database import get_db

router = APIRouter(
    prefix="/departamentos",
    tags=["departamentos"]
)

@router.post("/", response_model=schemas.Departamento)
def create_departamento(departamento: schemas.DepartamentoCreate, db: Session = Depends(get_db)):
    return services.create_departamento(db=db, departamento=departamento)

@router.get("/", response_model=list[schemas.Departamento])
def read_departamentos(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return services.get_departamentos(db, skip=skip, limit=limit)

@router.get("/{departamento_id}", response_model=schemas.Departamento)
def read_departamento(departamento_id: int, db: Session = Depends(get_db)):
    db_departamento = services.get_departamento(db, departamento_id=departamento_id)
    
    if db_departamento is None:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
        
    return db_departamento