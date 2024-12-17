#!/usr/bin/env python3
import os
import shutil
import json
import sys
import tempfile
import pandas as pd
import numpy as np
from localesjson import LocalesJson
import importlib
from spreadsheet import *

importlib.reload(sys)

root = os.environ['HOME']+'/Development/software/llamatracker/llamatracker_page'

if len(sys.argv)>1 and sys.argv[1] == 'out':
    translation_dir = tempfile.mkdtemp('','locales') + '/'
else:
    translation_dir = root + '/src/utils/i18n/'

oauth_json_file = root + '/src/utils/translation/oauth.json'
main_worksheet = SpreedSheet('1tDKXivT-aYW0HW7cWKZaKGFjrBYDyYXZuScKttcqyWI', json.load(open(oauth_json_file)), ['https://spreadsheet.google.com/feeds'])
countries_worksheet = SpreedSheet('1rtyKFp6emzCiHFVQ-0Alt8sg2DPX4YB0zFpHijzrdec', json.load(open(oauth_json_file)), ['https://spreadsheet.google.com/feeds'])
ss_list = main_worksheet.get_sheets()
sheets_list = countries_worksheet.get_values('languages')

def make_directory(language):
    # If directory exists, remove it
    if (os.path.exists(translation_dir+language)):
        shutil.rmtree(translation_dir+language)

    os.makedirs(translation_dir+language)


def make_files(rows, language, errors, worksheet_name='main'):
    files = {}
    i = 0
    col = 1 if language == 'en' else 2

    print('Translating sheet [' + worksheet_name + '] -> ' + language)

    # important! the spreadsheet only can contain 3 columns for languages different than en
    for row in rows:
        if row[0] and row[0] != '':
            row_split = row[0].split(':')
            filename = row_split[0]
            full_key = row[0]
            key = row_split[1].split('.')

            if len(row) == 2:
                value = row[1]
            elif len(row) >= 3 and row[col] == "":
                value = row[1]
            else:
                value = row[col]

            if not filename in files:
                files[filename] = LocalesJson(errors)

            files[filename].set_value(key, value, full_key)


    for filename in files:
        newfile = open(translation_dir+language+'/'+filename, 'w')
        newfile.write(json.dumps(files[filename], indent=4, ensure_ascii=False))

def main():
    errors = {}
    for tab_info in sheets_list:
        language = tab_info[0]
        make_directory(language)

        rows = main_worksheet.get_values(language)
        make_files(rows, language, errors, 'main')

    print('Directories and files created!')

    for error in errors:
        print(errors[error])

    if len(sys.argv)>1 and sys.argv[1] == 'out':
        sys.stdout.write(translation_dir)
        os.chmod(translation_dir, stat.S_IROTH)
        sys.stdout.write(translation_dir)
        sys.stdout.flush()
        sys.exit(0)

#----
#  START THE PROGRAM
#----
main()
