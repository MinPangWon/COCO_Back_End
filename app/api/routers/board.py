from pydantic import BaseModel
from fastapi import APIRouter
from crud.board import CrudBoard

router = APIRouter()

crudBoard = CrudBoard()

class Board(BaseModel):
    id: int
    context: str
    title: str
    rel_task: int
    time: str
    category: int
    likes: int
    views: int
    comments: int

#글쓴이
class Writer(BaseModel):
    user_id: str


@router.get('/board/', tags = ['board'])
async def check_board():
    return crudBoard.check_board()

@router.post('/board/{board_id}', tags=['board'])
async def board_detail(board_id: int):
    return crudBoard.board_detail(board_id)