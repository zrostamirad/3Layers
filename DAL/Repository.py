from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from setting import setting

conn = setting()

engine = create_engine(str(conn.GetConnectionString()), echo=True)
print(str(conn.GetConnectionString()))
Sessions = sessionmaker(bind=engine)
session = Sessions()


class Ripository():
    def Add(self, obj):
        try:
            session.add(obj)
            session.commit()
            print("reg is ok")
            return True
        except:
            return False

    def Read(self, obj):
        try:
            return session.query(obj).all()
        except:
            return ()

    def Update(self, obj, id):
        try:
            obj1 = self.ReadById(obj, id)
            obj1 = obj
            session.commit()
            return True
        except:
            return False

    def Delete(self, obj):
        try:
            session.delete(obj)
            session.commit()
            return True
        except:
            return False

    def ReadById(self, obj, id):
        try:
            return session.query(obj).filter(obj.id == id).first()
        except:
            return False
