from tinydb import TinyDB, Query

db = TinyDB('db.json')

img_table = db.table('images')

def add_image(photo_id):
    '''
    Add image to database
    
    Args:
        image (str): Image name

    Returns:

    '''
    data = {
        'photo_id': photo_id,
        'likes': [],
        'dislikes': [],
    }

    if img_table.contains(Query().photo_id == photo_id):
        return False
    img_table.insert(data)
    return True

def like(photo_id, chat_id):
    '''
    Add user to likes list
    
    Args:
        photo_id (str): Image name
        chat_id (int): User chat id

    Returns:

    '''
    if not img_table.contains(Query().photo_id == photo_id):
        return False

    img = img_table.get(Query().photo_id == photo_id)
    if chat_id in img['likes']:
        return False

    if chat_id in img['dislikes']:
        img['dislikes'].remove(chat_id)
    
    img['likes'].append(chat_id)
    img_table.update(img)

    return True

def dislike(photo_id, chat_id):
    '''
    Remove user from likes list
    
    Args:
        photo_id (str): Image name
        chat_id (int): User chat id

    Returns:

    '''
    if not img_table.contains(Query().photo_id == photo_id):
        return False

    img = img_table.get(Query().photo_id == photo_id)
    if chat_id in img['dislikes']:
        return False

    if chat_id in img['likes']:
        img['likes'].remove(chat_id)
    
    img['dislikes'].append(chat_id)
    img_table.update(img)

    return True

def get_data(photo_id):
    '''
    Get image data
    
    Args:
        photo_id (str): Image name

    Returns:
        dict: Image data

    '''
    if not img_table.contains(Query().photo_id == photo_id):
        return False
    img = img_table.get(Query().photo_id == photo_id)
    return {
        'likes': len(img['likes']),
        'dislikes': len(img['dislikes']),
    }

# print(get_data('test.png'))
    
