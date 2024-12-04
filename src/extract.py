import uuid
from datetime import datetime

from faker import Faker

fake = Faker()


class UserGenerator:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.company = None

    def create_email_address(
        self, first_name: str, last_name: str, company: str
    ) -> str:
        # Extract the first initial of the first name
        first_initial = first_name[0].lower()
        # Lowercase the last name
        last_name = last_name.lower()
        # Clean the company name (remove non-alphanumeric characters and lowercase it)
        company = "".join(char.lower() for char in company if char.isalnum())
        # Construct and return the email address
        return f"{first_initial}{last_name}@{company}.com"

    def generate_single_user(self) -> dict:
        # Generate random first name, last name, and company
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.company = fake.company()

        return {
            "uuid": str(uuid.uuid4()),
            "ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            # -- user info
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.create_email_address(
                self.first_name, self.last_name, self.company
            ),
            "phone": fake.phone_number(),
            # -- user address
            "address": fake.address().replace("\n", ", "),
            "country": fake.country_code(),
            # -- job
            "company": self.company,
            "job_title": fake.job(),
            # -- device
            "ip_address": fake.ipv4(),
            "mac_address": fake.mac_address(),
            "user_agent": fake.user_agent(),
        }
