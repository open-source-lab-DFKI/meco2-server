import get_trips
from common import store_trip_in_db, find_perturbed_trips
#import get_trips
from trip import E_Mission_Trip

#import Profiles

def calc_alternative_trips(trip_iterator):
    pass
    # trip_iterator in python does not have a hasNext(). This is not java
    # TODO: Fix this so that it works
    # while trip_iterator.hasNext():
    #     list_of_perturbed_trips = find_perturbed_trips(trip_iterator.next())
    #     schedule_queries(list_of_perturbed_trips)

def store_alternative_trips(tripObj):
    # store populated tripObj with _id (concatenated trip id and user id)
    return True

def get_alternative_trips(_id):
    # User Utility Pipeline calls this to get alternatve trips for one original trip (_id)
    return []    

