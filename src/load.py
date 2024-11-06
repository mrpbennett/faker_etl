import psycopg2

db = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="password",
    host="192.168.6.1",
    port="5432",
)


def create_user_fact_table() -> bool:

    try:
        with db as conn:
            with conn.cursor() as curs:
                curs.execute(
                    """
                    CREATE TABLE IF NOT EXISTS fact.users (
                       uuid UUID PRIMARY KEY,
                       timestamp DATE,
                       first_name VARCHAR,
                       last_name VARCHAR,
                       email VARCHAR,
                       phone VARCHAR,
                       address VARCHAR,
                       city VARCHAR,
                       country VARCHAR,
                       zip VARCHAR,
                       company_suffix VARCHAR,
                       job_title VARCHAR,
                       bank_country VARCHAR,
                       bban VARCHAR,
                       iban VARCHAR,
                       credit_card_number INT,
                       credit_card_secuirty_code INT,
                       ip_address VARCHAR,
                       mac_address VARCHAR,
                       user_agent VARCHAR,
                       passport_dob DATE,
                       passport_number VARCHAR  
                   );
                    """
                )

    except Exception as e:
        raise e

    return True


def insert_user_into_fact_table(insert_data: list, query: str) -> bool:

    values = [
        (
            d["uuid"],
            d["timestamp"],
            d["first_name"],
            d["last_name"],
            d["email"],
            d["phone"],
            d["address"],
            d["city"],
            d["country"],
            d["zip"],
            d["company"],
            d["company_suffix"],
            d["job_title"],
            d["bank_country"],
            d["bban"],
            d["iban"],
            d["credit_card_number"],
            d["credit_card_security_code"],
            d["ip_address"],
            d["mac_address"],
            d["user_agent"],
            d["passport_dob"],
            d["passport_number"],
        )
        for d in insert_data
    ]

    try:
        with db as conn:
            with conn.cursor() as curs:
                curs.executemany(query, values)

    except Exception as e:
        raise e

    return True
