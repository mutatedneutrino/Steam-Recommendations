
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


def select(filter='*',table='dbo.SteamRecommendations'):

    query='SELECT '+filter+' FROM '+table

    print(query)

    results = connect(query)

    for x in results:
        print(x) 
    