import MySQLdb

tbl_name = 'example'

def main():
    con = MySQLdb.connect(host='localhost', user='jcheng',
                        passwd='jcheng', db='infodb')
    cur = con.cursor()
    
    create_query = ' CREATE TABLE IF NOT EXISTS {} ' \
                   ' (name VARCHAR(20), age INT) '.format(tbl_name)
    cur.execute(create_query)

    insert_query = " INSERT INTO {} (name, age) VALUES ('John', 20) " \
                   "".format(tbl_name)
    cur.execute(insert_query)

    select_query = ' SELECT * FROM {} '.format(tbl_name)
    cur.execute(select_query)
    
    for row in cur.fetchall():
        print row


if __name__ == '__main__':
    main()
