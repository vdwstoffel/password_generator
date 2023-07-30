import sqlite3
import uuid
from lib.logger import Logger

class Database:

    def __init__(self) -> None:
        self.logger = Logger()
        self.table = 'passwords'

    def connect_to_database(self):
        """
        Database connector
        """
        conn = sqlite3.connect("passwords.sqlite3")

        if conn:
            return conn
        else:
            self.logger.log("Database could not connect")
    
    def create_password_table(self):
        '''
        Create a new password table
        '''
        conn = self.connect_to_database()
        cur = conn.cursor()
        try:
            cur.execute(f'''
                        CREATE TABLE {self.table}(
                        pw_id VARCHAR(50) UNIQUE PRIMARY KEY,
                        domain VARCHAR(250),
                        username VARCHAR(250),
                        password VARCHAR(250)
                        );
                        ''')
            conn.commit()
            conn.close()
        except Exception as e:
            if e.__str__() != "table password already exists":
                conn.close()

    def insert_new_password(self, domain=None, username=None, password=None):
        """
        Insert a new username, domain, password and generates a unique uuid for the 
        primary key
        """
        if domain == "" and username == "" and password == "":
            # Return false, will be checked once the password is saved
            self.logger.log("No Details entered when trying to save password")
            return False
        else:
            conn = self.connect_to_database()
            cur = conn.cursor()
            try:
                cur.execute(f'''
                            INSERT INTO {self.table} (pw_id, domain, username, password)
                            VALUES (:pw_id, :domain, :username, :password)
                            ''', {"pw_id": str(uuid.uuid4()),
                                  "domain": domain,
                                  "username": username,
                                  "password": password})
                conn.commit()
                conn.close()
            except Exception as e:
                self.logger.log(e)
                conn.close()

    def get_all_records(self):
        conn = self.connect_to_database()
        cur = conn.cursor()
        try:
            cur.execute(f"""
                                    SELECT * FROM {self.table}
                                    ORDER BY domain;
                                """)
            query = cur.fetchall()
            conn.commit()
            conn.close()
            return query
        except Exception as e:
            self.logger.log(f"Error returning all values: {e}")
            conn.close()

    def delete_record(self, uuid):

        conn = self.connect_to_database()
        cur = conn.cursor()
        try: 
            cur.execute(f"""
                            DELETE FROM {self.table}
                            where pw_id = '{uuid}'                        
                        """)
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
            self.logger.log(f"Error when deleting item: {e}")    
            conn.close()
