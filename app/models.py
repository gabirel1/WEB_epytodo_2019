#!/usr/bin/env python3
from app import app
from config import *
import pymysql as sql
from flask import jsonify
from app.controller import *
import json
import datetime

def connect_to_database() :
    try :
        connect = sql.connect(host=DATABASE_HOST,
                              user=DATABASE_USER,
                              passwd=DATABASE_PASS,
                              db=DATABASE_NAME,
                              unix_socket=DATABASE_SOCK
                             )
        return connect
    except Exception : 
        return None

def create_full_user(username, password, email) :
    try :
        connect = connect_to_database()
        if (connect == None) :
            print("internal error")
            return (2)

        cursor = connect.cursor()
        user_already_exist = cursor.execute('SELECT * FROM user WHERE username = %s;', username)
        if (user_already_exist == 0) :
            cursor.execute('INSERT INTO user (username, password, email) VALUES (%s,%s,%s);', username, password, email)
            connect.commit()
            cursor.close()
            connect.close()
            return (0)
        else :
            cursor.close()
            connect.close()
            return (1)
    except Exception :
        print("Unexpected Error")
        return (84)

def create_task(title, start_date, end_date, status) :
    try :
        connect = connect_to_database()
        if (connect == None) :
            print("internal error")
            return (2)

        cursor = connect.cursor()
        cursor.execute('INSERT INTO task (title, begin, end, status) VALUES (%s,%s,%s,%s);', title, start_date, end_date, status)
        connect.commit()
        cursor.close()
        connect.close()
        return (0)

    except Exception :
        print("Unexpected Error")
        return (84)

def get_task_id(task_name) :
    try :
        connect = connect_to_database()
        if (connect == None) :
            print("internal error")
            return (2)

        cursor = connect.cursor()
        cursor.execute('SELECT task_id FROM task WHERE title = %s;', task_name)
        task_id = cursor.fetchall()
        cursor.close()
        connect.close()
        return (task_id)

    except Exception :
        print("Unexpected Error")
        return (84)

def get_user_id(username) :
    try :
        connect = connect_to_database()
        if (connect == None) :
            print("internal error")
            return (2)

        cursor = connect.cursor()
        cursor.execute('SELECT user_id FROM user WHER username = %s;', username)
        user_id = cursor.fetchall()
        cursor.close()
        connect.close()
        return (user_id)

    except Exception :
        print("Unexpected Error")
        return (84)

def assing_task_to_user(task_name, username) :
    task_id = get_task_id(task_name)
    user_id = get_user_id(username)

    try :
        connect = connect_to_database()
        if (connect == None) :
            print("internal error")
            return (2)

        cursor = connect.cursor()
        cursor.execute('INSERT INTO user_has_task (fk_user_id, fk_task_id) VALUES (%d, %d);', user_id, task_id)
        connect.commit()
        cursor.close()
        connect.close()
        return (0)

    except Exception :
        print("Unexpected Error")
        return (84)

def change_task_etat(task_id, etat) :
    try :
        connect = connect_to_database()
        if (connect == None) :
            print("internal error")
            return (2)

        if (etat == 0) :
            cursor = connect.cursor()
            cursor.execute('UPDATE task SET status = %s WHERE task_id = %d;', "not_started", task_id)
            connect.commit()
            cursor.close()
            connect.close()

        elif (etat == 1) :
            cursor = connect.cursor()
            cursor.execute('UPDATE task SET status = %s WHERE task_id = %d;', "in progress", task_id)
            connect.commit()
            cursor.close()
            connect.close()
        else :
            cursor = connect.cursor()
            cursor.execute('UPDATE task SET status = %s WHERE task_id = %d;', "done", task_id)
            connect.commit()
            cursor.close()
            connect.close()

    except Exception :
        print("Unexpected Error")
        return (84)