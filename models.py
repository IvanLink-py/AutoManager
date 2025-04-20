from typing import List
import datetime
from dataclasses import dataclass

@dataclass
class Stop:
    _id: int
    name: str
    actuality: bool

@dataclass
class Route:
    _id: int
    name: str
    actuality: bool
    stops: List[Stop]

@dataclass
class Bus:
    _id: int
    number: str
    mark: str

@dataclass
class Driver:
    _id: int
    first_name: str
    last_name: str
    surname: str

@dataclass
class Schedule:
    _id: int
    start_time: datetime.time
    week_days: str
    route: Route

@dataclass
class Trip:
    _id: int
    bus_id: Bus
    driver_id: Driver
    schedule_id: Schedule
    success: bool
    send_time: datetime.datetime