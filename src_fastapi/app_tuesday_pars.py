from fastapi_offline import FastAPIOffline

app = FastAPIOffline()

mylist = [10, 20, 30, 40]

@app.get('/')
def get_index():
    return {'HELLO': 'PYTHON'}

@app.get('/home/')
def home():
    return {'WELCOME': 'HOME'}

@app.get('/getitems/')
def get_all_items():
    return {'mylist': mylist}

@app.post('/add/{new_item}')
def add_item(new_item: int):
    mylist.append(new_item)
    return {'new mylist': mylist}

@app.post('/addindex/')
def add_item_by_index(index:int , new_item:int):
    if index< len(mylist):
        mylist.insert(index, new_item)
        return {'new mylist': mylist}
    else:
        return {'index out of range'}

@app.delete('/deleteitem')
def delete_item(item:int):
    if item in mylist:
        mylist.remove(item)
        return {f'{item} removed from mylist'}
    else:
        return {f'{item} Not Found'}

@app.delete('/deleteindex')
def delete_index(index : int = -1):
    if len(mylist) > 0 and index < len(mylist):
        mylist.pop(index)
        return {'new mylist': mylist}
    else:
        return {'index out of range'}


@app.put('/updateItem/')
def update_item(old_item:int, new_item:int):
    if old_item in mylist:
        index = mylist.index(old_item)
        mylist[index] = new_item
        return {f'{old_item} replaced by {new_item}'}
    else:
        return {f'{old_item} not Found'}


@app.put('/updateIndex')
def update_index(index:int, new_item:int):
    if index < len(mylist):
        mylist[index] = new_item
        return {f'item in {index} position updated'}
    else:
        return {'index out of range'}
    