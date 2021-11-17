import sqlite3

from openpyxl import Workbook, load_workbook

from contextlib import closing

def get_db_connection():

  conn = None
  try:
      conn = sqlite3.connect("excel")
      return conn
  except Error as e:
      print(e)

  return conn

def create_table(ws, conn, table_name):

  field_names = [ col[0].internal_value for col in ws.columns ]

  build_sql = "CREATE TABLE {} ( {} TEXT);".format(table_name,' TEXT, '.join(field_names))

  c = conn.cursor()
  c.execute(build_sql)
  conn.commit()

def insert_data(ws, conn, table_name):

  field_names = [ col[0].internal_value for col in ws.columns ]
  value_holder = ["?"]*len(field_names)
  row_values = []
  final_rows = []

  for row in ws.rows:
    row_values.append([i.internal_value for i in row])

  for row in row_values[1:]:
    conv = lambda i : i or ''
    final_rows.append([conv(i) for i in row])

  c = conn.cursor()
  cmd = "INSERT INTO {} ( {} ) VALUES ( {} );".format(table_name, ','.join(field_names), ",".join(value_holder)) 

  c.executemany(cmd, final_rows)
  conn.commit()

def read_data(ws, conn, table_name):

  c = conn.cursor()
  c.execute("SELECT * FROM " + table_name + ";")

  rows = c.fetchall()

  for row in rows:
      print(row)


if __name__ == "__main__":
  src_workbook = input("Enter path and name of src workbook: ")
  src_worksheet = input("Enter name of the src sheet: ")
  table_name = input("Enter name of the table: ")

  wb = load_workbook(src_workbook)
  ws = wb[src_worksheet]
  wb.active = ws

  conn = get_db_connection()

  create_table(ws, conn, table_name)
  insert_data(ws, conn, table_name)
  read_data(ws, conn, table_name )