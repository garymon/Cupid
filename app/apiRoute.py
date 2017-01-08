# -*- coding: utf-8 -*-
import json, uuid
from flask import Blueprint, jsonify, request
from MysqlDAO import MysqlDAO
import datetime


api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/posts', methods=['POST', 'GET', 'PUT', 'DELETE'])
def index():
    if request.method == "GET":
        page_size = None
        page_num = None
        print(request.args)
        if 'page_size' in request.args and 'page_num' in request.args:
            page_size = int(request.args.get('page_size'))
            page_num = int(request.args.get('page_num'))

        all_posts = MysqlDAO.post_select(page_size, page_num)
        return jsonify(all_posts)

    elif request.method == "POST":
        insertObj = request.get_json()
        MysqlDAO.post_insert(insertObj)
        # fileDAO.save(insertObj)
        return ""

    elif request.method == "PUT":
        updateObj = request.get_json()
        MysqlDAO.post_update(updateObj)
        # fileDAO.modify(updateObj)
        return ""

    elif request.method == "DELETE":
        removeObj = request.get_json()
        MysqlDAO.post_delete(removeObj)
        return ""


