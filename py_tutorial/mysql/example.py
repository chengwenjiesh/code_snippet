import MySQLdb

tbl_name = 'info2'


def execute_query(query, *args):
    print args    

    con = MySQLdb.connect(host='localhost', user='jcheng',
                        passwd='jcheng', db='infodb')
    cur = con.cursor()
    
    # create_query = ' CREATE TABLE IF NOT EXISTS {} ' \
    #                ' (metric_name VARCHAR(20), metric_value FLOAT, ' \
    #                ' ts INT) ' \
    #                ''.format(tbl_name)
    # cur.execute(create_query)

    cur.execute(query, args[0])

    select_query = ' SELECT * FROM {} '.format(tbl_name)
    cur.execute(select_query)
   
    con.commit() 
    for row in cur.fetchall():
        print row
    con.close()


def main():
    insert_query = ' INSERT INTO {} (metric_name, metric_value, ' \
                   ' ts) VALUES (%s, %s, %s) '.format(tbl_name)
    execute_query(insert_query, ('abcd', 1.123, 1234))


if __name__ == '__main__':
    main()
