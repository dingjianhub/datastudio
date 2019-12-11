from openpyxl import load_workbook


def excel_add_sheet(dataframe, excel_writer, sheet_name):
    book = load_workbook(excel_writer.path)
    all_sheet_names = book.get_sheet_names()
    useless_sheet_list = ["Sheet1", sheet_name]
    for exist_sheet_name in all_sheet_names:
        for sheet_name in useless_sheet_list:
            if sheet_name == exist_sheet_name:
                book.remove(book[sheet_name])

    excel_writer.book = book
    dataframe.to_excel(excel_writer=excel_writer, sheet_name=sheet_name, index=None)
    excel_writer.close()
