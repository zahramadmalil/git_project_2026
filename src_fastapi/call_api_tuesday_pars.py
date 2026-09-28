import requests

def get_all_items():
    url = 'http://127.0.0.1:8000/getitems/'
    response = requests.get(url)

    if response.status_code != 200:
        return "ERROR"
    else:
        return response.json()

def add_item(new_item):
    url = f'http://127.0.0.1:8000/add/{new_item}'
    response = requests.post(url)

    if response.status_code != 200:
        return "ERROR"
    else:
        return response.json()

def delete_item(item):
    url = f'http://127.0.0.1:8000/deleteitem?item={item}'

    response = requests.delete(url)

    if response.status_code != 200:
        return "ERROR"
    else:
        return response.json()

def update_item(old_item , new_item):
    # url = f'http://127.0.0.1:8000/updateItem/?old_item={old_item}&new_item={new_item}'
    # response = requests.put(url)

    url2 = 'http://127.0.0.1:8000/updateItem/'
    params = {
        'old_item': old_item ,
        'new_item': new_item
    }
    response = requests.put(url2, params=params)

    if response.status_code != 200:
        return "ERROR"
    else:
        return response.json()
    
if __name__  == '__main__':
    # print(get_all_items())
    print(update_item(10, 510))