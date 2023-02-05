

import json
import io
import psycopg2

host = '130.193.39.134'

conn = psycopg2.connect(f"dbname=de user=jovyan password=jovyan host={host} port=5432")

with io.open('events-2022-Sep-30-2134.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

    fieldnames = data[0].keys()
    cur = conn.cursor()
    fstr = ','.join(['%s'] * len(data[0].values()))

    args_arr = []
    for d in data:
        values = d.values()
        args_str = str(cur.mogrify(str(f"({fstr})"), [str(v) for v in values]))[2:-1]
        args_arr.append(args_str)
    sql = f"insert into staging.events ({','.join(fieldnames)}) values " + ','.join(args_arr)
    cur.execute(sql)

conn.commit()




