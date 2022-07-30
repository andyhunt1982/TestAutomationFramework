from openpyxl import load_workbook
import os


class Config:
    @staticmethod
    def get_item_from_file(product, environment, item):
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
