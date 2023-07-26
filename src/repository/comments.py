from sqlalchemy.orm import Session

from src.database.models import Comment, Image, User
from src.schemas import CommentModel


async def get_comments(db: Session):
    return db.query(Comment).all()


async def get_comments_for_photo(image_id, db: Session):
    return db.query(Comment).filter_by(image_id=image_id).all()


async def get_comment_by_id(comment_id: int, db: Session):
    return db.query(Comment).filter_by(id=comment_id).first()


async def create_comment(body: CommentModel, current_user: User, db: Session):
    comment = Comment(**body.dict(), user_id=current_user.id)
    db.add(comment)
    db.commit()
    return comment


async def update_comment(body: CommentModel, comment_id, db: Session):
    comment = await get_comment_by_id(comment_id, db)
    if comment:
        comment.comment = body.comment
        db.commit()
    return comment


async def remove_comment(comment_id, db: Session):
    comment = await get_comment_by_id(comment_id, db)
    if comment:
        db.delete(comment)
        db.commit()
    return comment