class Truck:

    def __init__(self, truck_id):
        self.truck_id = truck_id
        self.speed = 18
        self.end_time = ""
        self.priority_packages = []
        self.standard_packages = []
        self.packages = []
        self.miles_traveled = 0

    def set_packages(self, packages):
        self.packages = packages

    def get_packages(self):
        return self.packages

    def remove_package(self, package):
        self.packages.remove(package)

    def set_end_time(self, end_time):
        self.end_time = end_time

    def get_end_time(self):
        return self.end_time

    def set_miles_traveled(self, miles_traveled):
        self.miles_traveled = miles_traveled