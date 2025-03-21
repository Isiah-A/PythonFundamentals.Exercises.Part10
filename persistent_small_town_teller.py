import pickle
import small_town_teller
import json



class PersistenceUtils:



    def __init__(self):
        pass

    @staticmethod
    def write_pickle(file_path, data):
        with open(file_path, "wb") as handler:
            pickle.dump(data, handler)

    @staticmethod
    def load_pickle(file_path):
        with open(file_path, 'rb') as handler:
            data = pickle.load(handler)
        return data

class Bank(small_town_teller.Bank, PersistenceUtils):

    def save_file(self):
        self.write_pickle('/Users/isiah/Projects/P1/PythonFundamentals.Exercises.Part10/Bank storage', self.customers)
        self.write_pickle('/Users/isiah/Projects/P1/PythonFundamentals.Exercises.Part10/Bank storage',self.accounts)

    def load_file(self):
        self.customers = self.load_pickle('/Users/isiah/Projects/P1/PythonFundamentals.Exercises.Part10/Bank storage')
        self.accounts = self.load_pickle('/Users/isiah/Projects/P1/PythonFundamentals.Exercises.Part10/Bank storage')
