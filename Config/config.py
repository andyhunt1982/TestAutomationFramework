from openpyxl import load_workbook
import os


class Config:
    @staticmethod
    def get_url(product, environment):
        try:
            cwd = os.getcwd().split("API")
        except Exception as e:
            print(e)
            cwd = os.getcwd().split("UI")

        # load workbook from Environments.xlsx
        rows = list(load_workbook(cwd[0] + "/Config/Environments.xlsx")["Sheet1"].rows)

        environment_urls = {}

        # get url from Environments.xlsx
        for row in rows:
            if row[0].value is not None:
                environment_urls.update(
                    {row[0].value: {rows[0][1].value: row[1].value, rows[0][2].value: row[2].value}})

        if environment_urls[environment][product] is None:
            assert False, f"Config.get_url() - environment: {environment} product: {product} is not defined"
        else:
            return environment_urls[environment][product]

    @staticmethod
    def get_username(product, environment):
        try:
            cwd = os.getcwd().split("API")
        except Exception as e:
            print(e)
            cwd = os.getcwd().split("UI")

        # load workbook from MyCredentials.xlsx
        rows = list(load_workbook(cwd[0] + "/Config/MyCredentials.xlsx")["Sheet1"].rows)

        usernames = {}

        # get username from MyCredentials.xlsx
        for row in rows:
            if row[0].value is not None:
                usernames.update(
                    {row[0].value: {rows[0][1].value: row[1].value, rows[0][2].value: row[2].value}})

        if usernames[environment][product] is None:
            assert False, f"Config.get_url() - environment: {environment} product: {product} is not defined"
        else:
            return usernames[environment][product]

    @staticmethod
    def get_password(product, environment):
        try:
            cwd = os.getcwd().split("API")
        except Exception as e:
            print(e)
            cwd = os.getcwd().split("UI")

        # load workbook from MyCredentials.xlsx
        rows = list(load_workbook(cwd[0] + "/Config/MyCredentials.xlsx")["Sheet2"].rows)

        passwords = {}

        # get password from MyCredentials.xlsx
        for row in rows:
            if row[0].value is not None:
                passwords.update(
                    {row[0].value: {rows[0][1].value: row[1].value, rows[0][2].value: row[2].value}})

        if passwords[environment][product] is None:
            assert False, f"Config.get_url() - environment: {environment} product: {product} is not defined"
        else:
            return passwords[environment][product]
