
import json, uuid

def get_all_posts():
    outputJson = read_file()
    if not outputJson:
        return []
    outputJson = json.loads(outputJson)
    outputJson.reverse()
    return outputJson


def save(post):
    post['uuid'] = str(uuid.uuid4())

    originJson = read_file()
    if not originJson:
        originJson = "[]"

    originDataArr = json.loads(originJson)
    originDataArr.append(post)
    write_file(json.dumps(originDataArr))


def modify(modifyPost):
    originJson = read_file()
    originData = json.loads(originJson)
    for post in originData:
        if post['uuid'] == modifyPost['uuid']:
            post['content'] = modifyPost['content']
            post['date'] = modifyPost['date']
            write_file(json.dumps(originData))
            return ;


def remove(removePost):
    originJson = read_file()
    originData = json.loads(originJson)
    n = 0
    for post in originData:
        if post['uuid'] == removePost['uuid']:
            originData.pop(originData.index(post))
            write_file(json.dumps(originData))
            return ;


def read_file():
    fRead = open("post.json", 'r')
    outputJson = fRead.read()
    fRead.close()
    return outputJson

def write_file(data):
    fWrite = open("post.json", 'w')
    fWrite.write(data)
    fWrite.close()