import hashlib

def phash(password):
    

    #Transformar a frase em bytes
    b = bytes(password, 'UTF-8')

    #Criar o objeto
    m = hashlib.sha256()

    m.update(b)

    final_hash = m.hexdigest()

    return final_hash
