from openpyxl import load_workbook
import os
from src.API.Tests import conftest as API_conftest
from src.UI.Tests import conftest as UI_conftest

environment_data = {
    "test": {
        "UI": {
            "url": "https://www.saucedemo.com",
            "username": "standard_user",
            "password": "secret_sauce"
        },
        "API": {
            "url": "https://testapi.com",
            "username": "testapiuser",
            "password": "testapipassword"
        }
    },
    "prod": {
        "UI": {
            "url": "https://google.com",
            "username": "produiuser",
            "password": "produipassword"
        },
        "API": {
            "url": "https://prodapi.com",
            "username": "prodapiuser",
            "password": "prodapipassword"
        }
    }
}

try:
    environment = API_conftest.ENV
except AttributeError:
    environment = UI_conftest.ENV


class Config:
    @staticmethod
    def get_item_from_file(product, item):
        if item == "url":
            file_name = "Environments.xlsx"
            sheet_name = "Sheet1"
        elif item == "username":
            file_name = "MyCredentials.xlsx"
            sheet_name = "Sheet1"
        elif item == "password":
            file_name = "MyCredentials.xlsx"
            sheet_name = "Sheet2"
        else:
            raise Exception("Invalid item")

        try:
            cwd = os.getcwd().split("API")
        except Exception as e:
            print(e)
            cwd = os.getcwd().split("UI")

        # load workbook
        rows = list(load_workbook(cwd[0] + f"/Config/{file_name}")[f"{sheet_name}"].rows)

        items = {}

        # get item from workbook
        for row in rows:
            if row[0].value is not None:
                items.update(
                    {row[0].value: {rows[0][1].value: row[1].value, rows[0][2].value: row[2].value}})

        if items[environment][product] is None:
            assert False, f"environment: {environment} product: {product} is not defined for {item}"
        else:
            return items[environment][product]

    @staticmethod
    def get_item_from_environment_data(product, item):
        if item == "url":
            return environment_data[environment][product]["url"]
        elif item == "username":
            return environment_data[environment][product]["username"]
        elif item == "password":
            return environment_data[environment][product]["password"]
        else:
            raise Exception("Invalid item")
