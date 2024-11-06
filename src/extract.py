import logging
import uuid
from datetime import datetime

from faker import Faker

logging.basicConfig(level=logging.INFO)

fake = Faker()


def generate_single_user() -> dict:

    return {
        "uuid": str(uuid.uuid4()),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        # -- user info
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.company_email(),
        "phone": fake.phone_number(),
        # -- user address
        "address": fake.address().replace("\n", ", "),
        "city": fake.city(),
        "country": fake.country(),
        "zip": fake.postcode(),
        # -- job
        "company": fake.company(),
        "company_suffix": fake.company_suffix(),
        "job_title": fake.job(),
        # -- bank info
        "bank_country": fake.bank_country(),
        "bban": fake.bban(),
        "iban": fake.iban(),
        "credit_card_number": fake.credit_card_number(),
        "credit_card_security_code": fake.credit_card_security_code(),
        # -- device
        "ip_address": fake.ipv4(),
        "mac_address": fake.mac_address(),
        "user_agent": fake.user_agent(),
        # -- passport
        "passport_dob": fake.passport_dob().strftime("%Y-%m-%d"),
        "passport_number": fake.passport_number(),
    }
