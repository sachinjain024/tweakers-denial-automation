from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, _app_ctx_stack
from flask.ext.cors import CORS

import db.mysql as db
import os
import random
import hashlib
from util import current_milli_time
import time
from ConfigParser import ConfigParser
import json

config = ConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config', 'config.cfg'))

conn, cursor = db.connect()
app_name = "local"

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.teardown_appcontext
def close_db_connection(exception):
    """Closes the database again at the end of the request."""
    # cursor.close()
    # conn.close()


@app.route('/')
def show_entries():
    return "Hello World"

@app.route('/getEntity')
def get_entity():
    attr_list = ['id', 'name', 'rating', 'imageUrl']
    sql_query = "SELECT "
    for attr in attr_list:
        sql_query+="`"+attr+"`,"
    sql_query = sql_query[:-1] + "FROM `entities` WHERE `enabled` = 1 ORDER BY `rating` DESC"
    print sql_query
    results = db.read(sql_query, cursor)
    result_list = []
    for result in results:
        result_dict = {}
        for (attrIndex) in zip(attr_list, xrange(len(attr_list))):
            result_dict[attrIndex[0]] = result[attrIndex[1]] 
        result_list.append(result_dict)
    return str(json.dumps(result_list)) 

@app.route('/getCatalog', methods=['GET'])
def get_menu():
    entity_id = request.values['entity_id']
    attr_list = ['id', 'name', 'price', 'imageUrl', 'description', 'stars']
    sql_query = "SELECT "
    for attr in attr_list:
        sql_query+="`"+attr+"`,"
    sql_query = sql_query[:-1] + "FROM `items` WHERE `entity` = " + entity_id +" AND `enabled` = 1 ORDER BY `price` ASC"
    # print sql_query
    results = db.read(sql_query, cursor)
    result_list = []
    for result in results:
        result_dict = {}
        for (attrIndex) in zip(attr_list, xrange(len(attr_list))):
            result_dict[attrIndex[0]] = result[attrIndex[1]] 
        result_list.append(result_dict)
    return str(json.dumps(result_list))

def create_transaction():
    pass

@app.route('/blockCatalog', methods=['GET'])
def update_catalog():
    transactions = json.loads(request.values['transaction'])
    dict_to_update = {}
    # dict_to_return = {}
    for transaction in transactions:
        dict_to_update[transaction['id']] = -1*transaction['quantity'] 
    attr_list = ['id', 'quantity']
    sql_read_query = "SELECT "
    for attr in attr_list:
        sql_read_query+="`"+attr+"`,"
    sql_read_query = sql_read_query[:-1] + "FROM `items` WHERE `id` IN ("
    for transaction in transactions:
        sql_read_query = sql_read_query + str(transaction['id'])+","
    sql_read_query = sql_read_query[:-1]+")"
    results = db.read(sql_read_query, cursor)
    is_available = True

    for result in results:
        dict_to_update[result[0]]+=result[1]
        for transaction in transactions:
            if(transaction['id'] == result[0]):
                transaction['quantityRemaining'] = dict_to_update[result[0]]
                break
        if(dict_to_update[result[0]]<0):
            is_available = False
    result_to_user = {}
    print is_available
    if(is_available):
        for result in results:
            sql_write_query = "UPDATE `items` set `quantity` = " + str(dict_to_update[result[0]]) + " WHERE `id` = "+str(result[0])
            db.write(sql_write_query, cursor, conn)
        result_to_user['status'] = 1
        # return "1"
    else:
        result_to_user['status'] = 0
        result_to_user['items'] = transactions
    return str(json.dumps(result_to_user))
        # return "0"
    
    # transaction_string = conn.escape_string(request.values['transaction'])
    # sql_transaction_query = "INSERT INTO `transactions`(`status`, `items`) VALUES ('0', \'"+transaction_string+"\')"
    # db.write(sql_transaction_query, cursor, conn)
    # sql_transaction_read_query = "SELECT `id` FROM `transactions` ORDER BY `id` DESC LIMIT 1"
    # id_to_return = str(db.read(sql_transaction_read_query, cursor)[0][0])
    # return id_to_return


if __name__ == '__main__':
    cors = CORS(app,resources={r"/*":{"origins":"*"}})
    app.run(host='0.0.0.0',threaded = True, port = 5002)
