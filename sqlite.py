import sqlite3

conn = sqlite3.connect('avacado.db')

print ("Opened database successfully");

# conn.execute('''CREATE TABLE TYPE_ID
#          (ID INT PRIMARY KEY     NOT NULL);''')

# print ("Table created successfully");

# conn.close()

# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()

# #Doping EMPLOYEE table if already exists
# cursor.execute("DROP TABLE TYPE")
# print("Table dropped... ")

# #Commit your changes in the database
# conn.commit()

# #Closing the connection
# conn.close()


# conn.execute('''CREATE TABLE SIZE
#          (ID INT PRIMARY KEY     NOT NULL,
#          SMALL_BAGS     FLOAT    NOT NULL,
#          LARGE_BAGS     FLOAT     NOT NULL,
#          XLARGE_BAGS    FLOAT      NOT NULL,
#          TOTAL_BAGS     FLOAT      NOT NULL);''')


# conn.execute('''CREATE TABLE PLU
#          (ID INT PRIMARY KEY     NOT NULL,
#          PLU_4046        FLOAT   NOT NULL,
#          PLU_4225        FLOAT    NOT NULL,
#          PLU_4770        FLOAT    NOT NULL);''')         


# conn.execute('''CREATE TABLE AVACADO
#          (ID INT PRIMARY KEY     NOT NULL,
#          AVG_PRICE      FLOAT    NOT NULL,
#          DATE           DATE     NOT NULL,
#          YEAR           YEAR     NOT NULL);''')

        
  
# # # conn.execute('''CREATE TABLE PURCHASE
# # #         (AVG_PRICE FLOAT PRIMARY KEY     NOT NULL,
# # #          TOTAL_VOLUME          FLOAT   NOT NULL);''')     


# print ("Table created successfully");

# conn.close()


# INPUTTING DATA INTO TYPE TABLE
conn.execute("INSERT OR REPLACE INTO TYPE_ID (ID) \
      VALUES (0)");

conn.execute("INSERT OR REPLACE INTO TYPE_ID (ID) \
      VALUES (0)");

conn.execute("INSERT OR REPLACE INTO TYPE_ID (ID) \
      VALUES (1)");

conn.execute("INSERT OR REPLACE INTO TYPE_ID (ID) \
      VALUES (0)");

conn.execute("INSERT OR REPLACE INTO TYPE_ID (ID) \
      VALUES (0)");

# # INPUTTING DATA INTO SIZE TABLE 
# conn.execute("INSERT OR REPLACE INTO SIZE (ID,SMALL_BAGS,LARGE_BAGS,XLARGE_BAGS,TOTAL_BAGS) \
#       VALUES (0, 87, 77, 20, 8.34)");

# conn.execute("INSERT OR REPLACE INTO SIZE (ID,SMALL_BAGS,LARGE_BAGS,XLARGE_BAGS,TOTAL_BAGS) \
#       VALUES (0, 81, 60, 81, 33.67)");

# conn.execute("INSERT OR REPLACE INTO SIZE (ID,SMALL_BAGS,LARGE_BAGS,XLARGE_BAGS,TOTAL_BAGS) \
#       VALUES (1, 31, 68, 10, 85.95)");

# conn.execute("INSERT OR REPLACE INTO SIZE (ID,SMALL_BAGS,LARGE_BAGS,XLARGE_BAGS,TOTAL_BAGS) \
#       VALUES (0, 19, 12, 73, 73.08)");

# conn.execute("INSERT OR REPLACE INTO SIZE (ID,SMALL_BAGS,LARGE_BAGS,XLARGE_BAGS,TOTAL_BAGS) \
#       VALUES (0, 62, 30, 92, 64.34)");

# # INPUTTING DATA INTO PLU TABLE

# conn.execute("INSERT OR REPLACE INTO PLU (ID,PLU_4046,PLU_4225,PLU_4770) \
#       VALUES (0, 30.81, 55.28, 8.34)");

# conn.execute("INSERT OR REPLACE INTO PLU (ID,PLU_4046,PLU_4225,PLU_4770) \
#       VALUES (0, 24.91, 17.56, 34.3)");

# conn.execute("INSERT OR REPLACE INTO PLU (ID,PLU_4046,PLU_4225,PLU_4770) \
#       VALUES (0, 39.92, 22.71, 35.61)");

# conn.execute("INSERT OR REPLACE INTO PLU (ID,PLU_4046,PLU_4225,PLU_4770) \
#       VALUES (0, 74.29, 45.34, 65.09)");

# conn.execute("INSERT OR REPLACE INTO PLU (ID,PLU_4046,PLU_4225,PLU_4770) \
#       VALUES (0, 78.97, 1.91, 99.47)");

# # INPUTTING DATA INTO AVACADO TABLE
# conn.execute("INSERT OR REPLACE INTO AVACADO (ID,AVG_PRICE,DATE,YEAR) \
#       VALUES (0, 9.03, 12/1/16, 2008)");

# conn.execute("INSERT OR REPLACE INTO AVACADO (ID,AVG_PRICE,DATE,YEAR) \
#       VALUES (0, 1.64, 5/1/20, 2004)");

# conn.execute("INSERT OR REPLACE INTO AVACADO (ID,AVG_PRICE,DATE,YEAR) \
#       VALUES (0, 3.31, 4/6/18, 1995)");

# conn.execute("INSERT OR REPLACE INTO AVACADO (ID,AVG_PRICE,DATE,YEAR) \
#       VALUES (0, 4.27, 5/18/17, 2009)");

# conn.execute("INSERT OR REPLACE INTO AVACADO (ID,AVG_PRICE,DATE,YEAR) \
#       VALUES (0, 8.00, 11/2/15, 1991)");

# # INPUTTING DATA INTO PURCHASE TABLE
# conn.execute("INSERT OR REPLACE INTO PURCHASE (AVG_PRICE,TOTAL_VOLUME) \
#       VALUES (9.03, 87.44)");

# conn.execute("INSERT OR REPLACE INTO PURCHASE (AVG_PRICE,TOTAL_VOLUME) \
#       VALUES (1.64, 86.41)");

# conn.execute("INSERT OR REPLACE INTO PURCHASE (AVG_PRICE,TOTAL_VOLUME) \
#       VALUES (3.31, 10.02)");

# conn.execute("INSERT OR REPLACE INTO PURCHASE (AVG_PRICE,TOTAL_VOLUME) \
#       VALUES (4.27, 43.16)");

# conn.execute("INSERT OR REPLACE INTO PURCHASE (AVG_PRICE,TOTAL_VOLUME) \
#       VALUES (8.00, 52.08)");


conn.commit()
print ("Records created successfully");
conn.close()

