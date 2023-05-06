from sqlalchemy.orm import Session



from . import models, schemas




def get_user(db: Session, user_id: int):

    return db.query(models.User).filter(models.User.id == user_id).first()




def get_user_by_email(db: Session, login: str):

    return db.query(models.User).filter(models.User.login == login).first()




def get_users(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.User).offset(skip).limit(limit).all()



def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(login=user.login, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
