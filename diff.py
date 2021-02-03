#!/usr/bin/env python

from difflib import context_diff

from sqlalchemy import create_engine
from sqlalchemy.sql import text


def create_tables(url):
    engine = create_engine(url)#, echo=True)
    conn = engine.connect()

    for table in conn.execute("SHOW tables;").fetchall():
        table = table[0]
        ct = conn.execute("SHOW CREATE TABLE `%s`;" % table).fetchone()
        yield ct[0], ct[1]


if __name__ == '__main__':
    import sys
    from pprint import pprint

    a = dict(create_tables(sys.argv[1]))

    tables = set()
    for table, ct in create_tables(sys.argv[2]):
        tables.add(table)
        print()
        if table not in a:
            print("[NEW] ", table)
            continue
        if ct == a[table]:
            print("[SAME] ", table)
            continue
        print("[CHANGED] ", table)
        for diff in context_diff(ct.split('\n'), a[table].split('\n')):
            print(diff)
    for old in tables - set(a.keys()):
        print("[REMOVED] ", old)
