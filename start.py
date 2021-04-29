import datetime
import pyodbc
import pandas as pd
# import numpy as np
connectionString = "Driver={ODBC Driver 17 for SQL Server};Server=stupa-testdb.cf0xlnbvxxos.us-east-1.rds.amazonaws.com;Database=StupaAiProdDb;uid=admin;pwd=stupa-ai-dev1"
connection = pyodbc.connect(connectionString)
cursor = connection.cursor()
temp_tbl_Game = pd.read_sql("SELECT * FROM temp_tbl_Game WHERE IsSynchronize=0 ", connection)

TEMPBULK=temp_tbl_Game['UploadId'].unique()

for L_UploadId in TEMPBULK:
    Required_IdData= temp_tbl_Game[temp_tbl_Game['UploadId'] == L_UploadId]
    if temp_tbl_Game['ServerMatchNo'].iloc[0] is None or temp_tbl_Game['ServerMatchNo'].iloc[0] == 0:

        cursor.execute("SELECT ISNULL(MAX(MatchNumber),0) + 1 FROM tbl_Match")
        for val in cursor.fetchall():
            MatchNumber = val[0]
            #date = date = datetime.date.today()

        sql = "INSERT INTO tbl_Match (MatchNumber,DOC,IsFreeAccess) VALUES (" + str(MatchNumber) + ",GETUTCDATE(),0)"
        cursor.execute(sql)
        cursor.commit()
    else:
        MatchNumber =  temp_tbl_Game['ServerMatchNo'].iloc[0]
        cursor.execute("DELETE FROM tbl_Primary_Database WHERE Match_No=" + MatchNumber)
        cursor.commit()
















