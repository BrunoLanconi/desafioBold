# This script will create an admin user on API database [users] which will be used to reference
# admin-only customers.
import requests
import os
from json.decoder import JSONDecodeError


def main():
    parent = os.environ.get("DJANGO_PARENT")
    parent_port = os.environ.get("DJANGO_PARENT_PORT")

    try:
        api_admin = requests.get(f"http://{parent}:{parent_port}/users/id/1/").json()
        api_admin_name = api_admin[0]["name"]

        print(f"Admin user already exists as {api_admin_name} on API database.")

    except (JSONDecodeError, IndexError):
        admin_login = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        admin_password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        data = {
            "name": admin_login,
            "username": admin_login,
            "password": admin_password,
            "is_new": False,
        }

        print(f"Admin user not exists on API database. Creating...")
        requests.post(url=f"http://{parent}:{parent_port}/users/",
                      data=data)


if __name__ == '__main__':
    main()
