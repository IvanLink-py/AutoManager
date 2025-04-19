
from typing import List
import datetime

class Stop:
    _id: int
    name: str
    actuality: bool

class Route:
    _id: int
    name: str
    actuality: bool
    stops: List[Stop]

class Bus:
    _id: int
    number: str
    mark: str

class Driver:
    _id: int
    first_name: str
    last_name: str
    surname: str

class Schedule:
    _id: int
    start_time: datetime.time
    week_date: str
    route: Route

class Trip:
    _id: int
    bus_id: Bus
    driver_id: Driver
    schedule_id: Schedule