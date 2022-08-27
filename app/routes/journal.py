from fastapi import APIRouter


router = APIRouter()


@router.get('/')
async def get_journal():
    return

@router.post('/')
async def create_journal():
    return

@router.get('/{journal_id}')
async def get_journal(id: journal_id):
    return 

@router.delete('/{journal_id}')
async def delete_journal(id: journal_id):
    return
