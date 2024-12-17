import gspread
import json

class SpreedSheet:

    def __init__(self, id, jsonKey, scope):

        gc = gspread.service_account(filename='./oauth.json')

        self._spreadSheet = gc.open_by_key(id)

    def write (self, len, matrix, sheet, isThird):
        worksheet = self.select_sheet(sheet)

        col = 'C' if isThird else 'B'
        cell_list = worksheet.range('A1:'+col+str(len))

        x = 0
        for cell in cell_list:
            if x>=len:
                break

            cell.value = matrix[x]
            x+=1

        worksheet.update_cell(cell_list)

    def get_sheets(self):
        return self._spreadSheet.worksheets()

    def select_sheet(self, language):
        return self._spreadSheet.worksheet(language)

    def get_values(self, language):
        worksheet = self.select_sheet(language)
        return worksheet.get_all_values()
