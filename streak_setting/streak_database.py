streak_database_file = 'streak_database.txt'


class StreakDatabase:
    def __init__(self, invoice_database_file='streak_database.csv'):
        self.streak_database_file = streak_database_file
        # self.streak_data = {}
        self.streak = 0

        try:
            with open(self.streak_database_file, 'r') as streak_database:
                last_entry = streak_database.readlines()[-1]
            last_date, last_time, last_streak_value = last_entry.split(",")
            self.streak = int(last_streak_value)

        except FileNotFoundError:
            with open(self.streak_database_file, 'w') as streak_database:
                self.streak += 0
                pass

    def get_streak_number(self):
        return self.streak

    def add_to_streak(self, date, time):
        streak_validity = self.check_streak_date_validity()
        if date == streak_validity:
            self.streak = self.get_streak_number()
        else:
            self.streak = self.get_streak_number() + 1
            line_format = "{},{},{}\n"
            with open(self.streak_database_file, 'a+') as streak_database:
                streak_database.write(line_format.format(date, time, self.streak))
        return self.streak

    def check_streak_date_validity(self):
        with open(self.streak_database_file, 'r') as streak_database:
            last_entry = streak_database.readlines()[-1]
        # print(last_entry)
        last_date, last_time, last_streak_value = last_entry.split(",")
        return last_date

    def streak_killed(self, date, time,):
        self.streak = 0
        line_format = "{},{},{}\n"
        with open(self.streak_database_file, 'a+') as streak_database:
            streak_database.write(line_format.format(date, time, self.streak))
        return self.streak


# sloe = StreakDatabase()
# sloe.check_streak_date_validity()
