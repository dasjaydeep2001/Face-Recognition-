from sqlalchemy.orm import Session
from database import SessionLocal, engine
import schema

schema.Base.metadata.create_all(bind=engine)
db = SessionLocal()

def getId(db,name):
    return db.query(schema.User.id).filter(schema.User.Name==name.strip()).first()

def create_user(db, encode,name):
    id = getId(db,name)
    if not id:
       db_user = schema.User(Name=str(name), encoding=str(encode))
       db.add(db_user)
       db.commit()
       db.refresh(db_user)
       return db_user

def getencoding():
    try:
        encodeListKnown = []  # Initialize an empty list to store the results
        data = db.query(schema.User.encoding).order_by(schema.User.id).all()
        for encoding in data:
            encodeListKnown.append(encoding[0])        
        return encodeListKnown
    except Exception as e:
        print("error :: ",str(e))
    finally:
        db.close()

def classname():
    try:
        classnames = []
       
        data = db.query(schema.User.Name).order_by(schema.User.id).all()
        for name in data:
            print(name)
            classnames.append(name[0])        
        return classnames
    except Exception as e:
        print("error :: ",str(e))
    finally:
        print(classnames)
        db.close()


