import hashlib
import os


GIT_DIR = '.ugit'


def init ():
    os.makedirs (GIT_DIR)
    os.makedirs (f'{GIT_DIR}/objects')

def set_HEAD (oid):
    with open (f'{GIT_DIR}/HEAD', 'w') as f:
        f.write (oid)

        
def get_HEAD ():
    if os.path.isfile (f'{GIT_DIR}/HEAD'):
        with open (f'{GIT_DIR}/HEAD') as f:
            return f.read ().strip ()


# Writing the content of the file, with file name as hash
# Append type of the file followed by NULL byte to verify it's extracted and expected types
def hash_object (data, type_='blob'):
    obj = type_.encode () + b'\x00' + data
    oid = hashlib.sha1 (obj).hexdigest ()
    with open (f'{GIT_DIR}/objects/{oid}', 'wb') as out:
        out.write (obj)
    return oid

# Getting the content of the file from the hashed name
def get_object (oid, expected='blob'):
    with open (f'{GIT_DIR}/objects/{oid}', 'rb') as f:
        obj = f.read ()

    type_, _, content = obj.partition (b'\x00')
    type_ = type_.decode ()

    if expected is not None:
        assert type_ == expected, f'Expected {expected}, got {type_}'
    return content

