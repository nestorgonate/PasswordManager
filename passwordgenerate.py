import secrets
import string
def generatePassword():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = "".join(map(secrets.choice, [caracteres]*15))
    return password