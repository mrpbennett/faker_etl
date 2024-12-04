import logging
import random

from extract import UserGenerator
from load import create_user_fact_table, insert_user_into_fact_table

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - line:%(lineno)d - %(filename)s:%(funcName)s -> %(message)s",
)


def main():

    user_generator = UserGenerator()
    users: list = []

    # generate a random amount of users between 1 & 1000
    for _ in range(random.randint(1, 5000)):
        user: dict = user_generator.generate_single_user()
        users.append(user)

    if create_user_fact_table():

        logging.info(f"{len(users)} users to be inserted.")
        insert_user_into_fact_table(users)

        logging.info("All have been inserted into the database")


if __name__ == "__main__":
    main()
