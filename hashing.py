from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        hashedPassword = pwd_cxt.hash(password)
        return hashedPassword
    
    def verify(hashed_password, clean_password):
        return pwd_cxt.verify(clean_password, hashed_password)