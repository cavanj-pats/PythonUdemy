# challenge Event Planner




import datetime as dt



class EventPlanner:
    def __init__(self, year):
        self.year = year
        self.events = {}
    def add_event(self, when, details):
        if when.date()<dt.date.today() or when.year !=dt.date.today().year:
            raise Exception('Invalid Date')
        self.events[when] = details

    def remove_event(self, when):
        if when in self.events:
            del self.events[when]

    def list_events(self):
        print(f"\nEvents for {self.year}:")
        for datime, details in self.events.items():
            print(datime.strftime('%d, %B, %A  %Y, %I:%M'))
            print('Details: ', details)


if __name__ == "__main__":
    curYear = 2026
    ep = EventPlanner(curYear)
    tempDate = dt.datetime(curYear, 4, 30, 16, 30, 0)
    ep.add_event(tempDate, 'Send OSR')
    tempDate = dt.datetime(curYear, 6, 5, 16, 30, 0)
    ep.add_event(tempDate, 'First Part Delivery')
    tempDate = dt.datetime(curYear, 7, 29, 16, 30, 0)
    ep.add_event(tempDate, 'Part 2 and 3 Delivery')

    ep.list_events()


