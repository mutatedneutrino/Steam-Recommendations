
def connect(query):
    import pyodbc 

    results = []

    server = 'DESKTOP-PU2RB19'
    db1 = 'Project_Rec'
    tcon = 'yes'
    uname = 'VS_CODE'
    pword = 'VS_CODE'

    print('you arrived')

    conn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', host=server, database=db1,trusted_connection=tcon, user=uname, password=pword)

    cursor = conn.cursor()
    cursor.execute(query)

    for row in cursor:
        results.append(row)
    
    
    return results


def select(select='*',table='dbo.SteamRecommendations',extra_condition=''):

    query='SELECT '+select+' FROM '+table

    print(query)

    results = connect(query)

    for x in results:
        print(x) 

    
def join(select,table1,table2,join_type,join_property):

    query='SELECT '+select+' FROM '+ table1 + ' ' + ' ' + join_type + ' ' + table2 + ' ON ' + join_property

    print(query)

    results = connect(query)

    for x in results:
        print(x) 
