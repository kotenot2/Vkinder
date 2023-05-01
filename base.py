import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="")

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS profiles(
        id_user integer UNIQUE,
        name_profiles integer UNIQUE,
        );
        """)
        conn.commit()

def delete_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
        DELETE from profiles;
        """)
        conn.commit()

def insert_profiles(conn, id_user, profiles_find):
    with conn.cursor() as cur:
        cur.execute(""" 
            INSERT INTO profiles(
            id_user, profiles_find)
            VALUES(%s, %s, %s)
            # RETURNING id;
        """, (id_user, profiles_find))
        conn.commit()

def select_profiles(conn, id_user):
    with conn.cursor() as cur:
        cur.execute(""" 
                SELEST profiles_find FROM profiles WHERE id_user = ?
                """, (id_user))
        list_profiles = cur.fetchall()
        print(list_profiles)
    return list_profiles

