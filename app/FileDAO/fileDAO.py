
import json, uuid


def get_all_posts():
    outputJson = readFile()
    if not outputJson:
        return []
    outputJson = json.loads(outputJson)
    outputJson.reverse()
    return outputJson


def save(post):
    post['uuid'] = str(uuid.uuid4())

    originJson = readFile()
    if not originJson:
        originJson = "[]"

    originDataArr = json.loads(originJson)
    originDataArr.append(post)
    writeFile(json.dumps(originDataArr))


def modify(modifyPost):
    originJson = readFile()
    originData = json.loads(originJson)
    for post in originData:
        if post['uuid'] == modifyPost['uuid']:
            post['content'] = modifyPost['content']
            post['date'] = modifyPost['date']
            writeFile(json.dumps(originData))
            return ;


def remove(removePost):
    originJson = readFile()
    originData = json.loads(originJson)
    n = 0
    for post in originData:
        if post['uuid'] == removePost['uuid']:
            originData.pop(originData.index(post))
            writeFile(json.dumps(originData))
            return ;


def readFile():
    fRead = open("post.json", 'r')
    outputJson = fRead.read()
    fRead.close()
    return outputJson

def writeFile(data):
    fWrite = open("post.json", 'w')
    fWrite.write(data)
    fWrite.close()