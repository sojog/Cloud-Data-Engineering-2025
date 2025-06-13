
import string


ALLOWED_CHARACTERS = string.ascii_letters + string.digits + ".@_-"

def este_valid(email:str):
    if "@" not in email:
        return False
    
    if "." not in email:
        return False

    username = email.split("@")[0]

    if not username:
        return False
    
    if any([ch not in ALLOWED_CHARACTERS for ch in email]):
        return False

    if len(username) > 64:
        return False    

    extensie = email.split(".")[-1]
    if len(extensie) < 2:
        return False

    if any ([ch not in string.ascii_letters for ch in extensie]):
        return False

    return True

