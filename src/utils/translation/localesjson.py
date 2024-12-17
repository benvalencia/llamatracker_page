import sys
import hashlib

class LocalesJson(dict):

    def __init__(self, errors=None):
        self.errors = errors

    def set_value(self, key, value, full_key):
        key_len = len(key)
        curr_key = key.pop(0)

        if curr_key in self:
            if key_len > 1:
                if isinstance(self[curr_key], str):
                    self.push_error('Wrong key definition "' + full_key + '". The key "' + curr_key + '" has a string value.')
                    sys.exit(1)

                self[curr_key].set_value(key, value, full_key)
            else:
                self.push_error('Warning: Value set twice "' + full_key + '".')
                self[curr_key] = value
        else:
            if key_len > 1:
                old_value = value
                value = LocalesJson(self.errors)
                value.set_value(key, old_value, full_key)
            elif value and value[0] == '[':
                value = value[1:-1].split(',')

            self[curr_key] = value

    def push_error(self, error):
        if self.errors is not None:
            key = hashlib.md5(error).hexdigest()
            self.errors[key] = error

