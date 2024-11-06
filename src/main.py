import random

from extract import generate_single_user
from load import create_user_fact_table, insert_user_into_fact_table


def main():

    # EXTRACT THE DATA
    users: list = []

    # generate a random amount of users between 1 & 1000
    for _ in range(random.randint(1, 1000)):
        user: dict = generate_single_user()
        users.append(user)

    # LOAD THE DATA

    insert_users = """INSERT INTO fact.users VALUES (%s)"""

    if create_user_fact_table():
        insert_user_into_fact_table(users, insert_users)


if __name__ == "__main__":
    main()
