class Package:
    def __init__(self, package_id, delivery_add, city, state, zipcode, deadline, weight, notes):
        self.package_id = package_id
        self.delivery_add = delivery_add
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.truck = None
        self.delivery_time = None
        self.delivered = "At The Hub"

    def get_id(self):
        return self.package_id

    def get_delivery_add(self):
        return self.delivery_add

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zipcode(self):
        return self.zipcode

    def get_deadline(self):
        return self.deadline

    def get_weight(self):
        return self.weight

    def get_notes(self):
        return self.notes

    def get_all(self):
        to_return = [self.delivery_add, self.city, self.state, self.zipcode, self.deadline, self.weight, self.notes]
        return [self.package_id, to_return]

    def get_delivery_time(self):
        return self.delivery_time

    def get_delivered(self):
        return self.delivered

    def set_delivery_time(self, delivery_time):
        self.delivery_time = delivery_time

    def set_delivered(self, delivered):
        self.delivered = delivered

    def set_truck(self, truck):
        self.truck = truck
