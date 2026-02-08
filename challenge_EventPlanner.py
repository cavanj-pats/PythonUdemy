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
    
    curYear = int(input('Enter Year: '))
    ep = EventPlanner(curYear)
    """
    tempDate = dt.datetime(curYear, 4, 30, 16, 30, 0)
    ep.add_event(tempDate, 'Send OSR')
    tempDate = dt.datetime(curYear, 6, 5, 16, 30, 0)
    ep.add_event(tempDate, 'First Part Delivery')
    tempDate = dt.datetime(curYear, 7, 29, 16, 30, 0)
    ep.add_event(tempDate, 'Part 2 and 3 Delivery')
    """
    
        #Abdul used input

    for i in range(3):    #add three events
        date = [int(x) for x in input('Enter Date dd/mm/yyy ').split('/')]
        time = [int(x) for x in input('Enter Time hr:min ').split(':')]
        when = dt.datetime(date[2], date[1], date[0], time[0], time[1])   #needed to swap time[0] and time[1] from Abdul screen
        details = input('Detials of Event: ')
        ep.add_event(when, details)
    
    ep.list_events()


    


