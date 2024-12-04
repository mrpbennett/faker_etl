import psycopg2

db = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="password",
    host="192.168.5.81",
    port="5432",
)


def create_user_fact_table() -> bool:

    try:
        with db as conn:
            with conn.cursor() as curs:
                curs.execute(
                    """
                    CREATE TABLE IF NOT EXISTS fact.users_pii (
                       uuid UUID PRIMARY KEY,
                       ts TIMESTAMP,
                       first_name VARCHAR,
                       last_name VARCHAR,
                       email VARCHAR,
                       phone VARCHAR,
                       address VARCHAR,
                       country VARCHAR,
                       company VARCHAR,
                       job_title VARCHAR,
                       ip_address VARCHAR,
                       mac_address VARCHAR,
                       user_agent VARCHAR
                   );
                    """
                )

    except Exception as e:
        raise e

    return True


def insert_user_into_fact_table(insert_data: list) -> bool:

    values = [
        (
            d["uuid"],
            d["ts"],
            d["first_name"],
            d["last_name"],
            d["email"],
            d["phone"],
            d["address"],
            d["country"],
            d["company"],
            d["job_title"],
            d["ip_address"],
            d["mac_address"],
            d["user_agent"],
        )
        for d in insert_data
    ]

    try:
        with db as conn:
            with conn.cursor() as curs:
                curs.executemany(
                    """
                    INSERT INTO fact.users_pii
                    (uuid, ts, first_name, last_name, email, phone, address, country, company, job_title, ip_address, mac_address, user_agent)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    values,
                ),
    except Exception as e:
        raise e

    return True
