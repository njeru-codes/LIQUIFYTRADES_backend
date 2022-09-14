from fastapi import APIRouter, Depends, status, HTTPException
from ..database import get_db
from sqlalchemy.orm import Session
from ..schemas import Journal
from ..auth import get_current_user
from .. import model
from fastapi import Depends


router = APIRouter()


@router.get('/journal')
async def get_journal( db: Session=Depends(get_db), user_id:int =Depends(get_current_user) ):
    journal = db.query( model.Journal).filter( model.Journal.user_id == user_id).all()
    return journal


@router.post('/journal')
async def create_journal(journal:Journal, db:Session=Depends(get_db) , user_id:int =Depends(get_current_user)):
    journal.user_id = user_id
    new_journal = model.Journal( **journal.dict() )
    db.add( new_journal)  
    db.commit()
    db.refresh(new_journal)
    return new_journal


@router.get('/journal/{journal_id}')
async def get_journal(journal_id:int, db: Session=Depends(get_db) , user_id:int =Depends(get_current_user)  ):
    journal = db.query( model.Journal).filter( model.Journal.user_id == user_id, model.Journal.id == journal_id ).first()
    if not journal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"access to journal with id {journal_id} denied")
    return journal


@router.delete('/{journal_id}')
async def delete_journal(journal_id: int ):
    return {'deleted journal'}
