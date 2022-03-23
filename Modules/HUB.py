from Modules import CSVLoader
import datetime

"""
The HUB modules acts as 

"""

# Global Variables.
package_data = CSVLoader.load_package_data()  # Chaining Hashtable
distance_data = CSVLoader.load_distance_data()  # 2D List
address_data = CSVLoader.load_address_data()  # Dictionary


# Private: Calculate Distance Between Two Addresses.
def _distance_between(add1, add2):
    outer_index = address_data.get(add1)
    inner_index = address_data.get(add2)
    if inner_index > outer_index:
        temp = inner_index
        inner_index = outer_index
        outer_index = temp
    return distance_data[outer_index][inner_index]


def load_packages(truck1, truck2, truck3, all_packages):
    # Separate Priority and Standard Deliveries.
    priority = []
    standard = []
    for i in range(1, 41):
        package = all_packages.search(i)
        if package.deadline != "EOD":
            priority.append(package.package_id)
        else:  # EOD Packages
            standard.append(package.package_id)

    # Priority Mail
    for item in priority:
        package = all_packages.search(item)
        if package.notes != "":     # Has Special Notes
            space_index = package.get_notes().index(" ")
            keyword = package.get_notes()[0: space_index]
            if keyword == "Must":
                truck1.packages.append(package.package_id)
                truck1.priority_packages.append(package.package_id)
                package.set_truck(truck1.truck_id)
            elif keyword == "Can":
                truck2.packages.append(package.package_id)
                truck2.priority_packages.append(package.package_id)
                package.set_truck(truck2.truck_id)
            elif keyword == "Delayed":
                truck2.packages.append(package.package_id)
                truck2.priority_packages.append(package.package_id)
                package.set_truck(truck2.truck_id)
            elif keyword == "Wrong":
                package.delivery_add = "410 S State St"
                package.zipcode = "84111"
                truck3.packages.sppend(package.package_id)
                truck3.priority_packages.append(package.package_id)
                package.set_truck(truck3.truck_id)
        else:  # No Special Notes.
            package_zip = package.zipcode
            if package.package_id == 13:  # Brute Force Deliver Together.
                truck1.packages.append(package.package_id)
                truck1.priority_packages.append(package.package_id)
                package.set_truck(truck1.truck_id)
            elif package_zip.__contains__("8411"):
                truck1.packages.append(package.package_id)
                truck1.priority_packages.append(package.package_id)
                package.set_truck(truck1.truck_id)
            else:
                truck2.packages.append(package.package_id)
                truck2.priority_packages.append(package.package_id)
                package.set_truck(truck2.truck_id)
    # Standard Mail
    for item in standard:
        package = all_packages.search(item)
        if package.notes != "":
            space_index = package.get_notes().index(" ")
            keyword = package.get_notes()[0: space_index]
            if keyword == "Must":
                truck1.packages.append(package.package_id)
                truck1.standard_packages.append(package.package_id)
                package.set_truck(truck1.truck_id)
            elif keyword == "Can":
                truck2.packages.append(package.package_id)
                truck2.standard_packages.append(package.package_id)
                package.set_truck(truck2.truck_id)
            elif keyword == "Delayed":
                if package.deadline != "EOD":
                    truck2.packages.append(package.package_id)
                    truck2.standard_packages.append(package.package_id)
                    package.set_truck(truck2.truck_id)
                else:
                    truck3.packages.append(package.package_id)
                    truck3.standard_packages.append(package.package_id)
                    package.set_truck(truck3.truck_id)
            elif keyword == "Wrong":
                package.delivery_add = "410 S State St"
                package.zipcode = "84111"
                truck3.packages.append(package.package_id)
                truck3.standard_packages.append(package.package_id)
                package.set_truck(truck3.truck_id)
        else:
            package_zip = package.zipcode
            if package_zip.__contains__("8411") and len(truck1.packages) < 16:
                truck1.packages.append(package.package_id)
                truck1.standard_packages.append(package.package_id)
                package.set_truck(truck1.truck_id)
            elif len(truck2.packages) < 14:
                truck2.packages.append(package.package_id)
                truck2.standard_packages.append(package.package_id)
                package.set_truck(truck2.truck_id)
            else:
                truck3.packages.append(package.package_id)
                truck3.standard_packages.append(package.package_id)
                package.set_truck(truck3.truck_id)


def deliver_packages(truck, distance_traveled, address, order, all_packages):
    closest_location = ""
    current_location = address
    current_package = None
    total_distance_traveled = distance_traveled
    lowest = 140  # Initial Value
    order = order

    # Deliver Priority Packages.
    if len(truck.priority_packages) > 0:
        for item in truck.priority_packages:
            package = all_packages.search(item)
            distance = _distance_between(current_location, package.delivery_add)
            if distance < lowest:
                lowest = distance
                closest_location = package.delivery_add
                current_package = package
        total_distance_traveled += lowest

        # Base Case: Return to Hub.
        if current_package is None:
            total_distance_traveled += _distance_between("4001 South 700 East",
                                                         address) - 140  # Offsetting Initial Value.
            truck.set_end_time(total_distance_traveled / 18)
            truck.set_miles_traveled(total_distance_traveled)

        # Go To Next Address:
        else:
            # Stamping Delivery Time
            current_package.set_delivery_time(lowest / truck.speed)
            truck.packages.remove(current_package.package_id)
            truck.priority_packages.remove(current_package.package_id)
            order.append(current_package.package_id)
            # Recursive Function Call:
            deliver_packages(truck, total_distance_traveled, closest_location, order, all_packages)
    else:
        for item in truck.standard_packages:
            package = all_packages.search(item)
            distance = _distance_between(current_location, package.delivery_add)
            if distance < lowest:
                lowest = distance
                closest_location = package.delivery_add
                current_package = package
        total_distance_traveled += lowest

        # Base Case: Return to Hub.
        if current_package is None:
            total_distance_traveled += _distance_between("4001 South 700 East", address) - 140  # Offsetting Initial Value.
            truck.set_end_time(total_distance_traveled / 18)
            truck.set_miles_traveled(total_distance_traveled)

        # Go To Next Address:
        else:
            # Stamping Delivery Time
            current_package.set_delivery_time(lowest / truck.speed)
            truck.packages.remove(current_package.package_id)
            truck.standard_packages.remove(current_package.package_id)
            order.append(current_package.package_id)
            # Recursive Function Call:
            deliver_packages(truck, total_distance_traveled, closest_location, order, all_packages)

    return order    # Return Array of Package ID's in the order they were delivered.


def convert_time(start, truck, order, all_packages):

    # Determine Departure Time:
    today = datetime.date.today()

    # First Shift: 8AM
    if truck.truck_id == 1:
        start_time = datetime.time(hour=8)
        start_dt = datetime.datetime.combine(today, start_time)

    # Second Shift: 9:05 AM After Delayed Packages Arrive
    elif truck.truck_id == 2:
        start_time = datetime.time(hour=9, minute=5)
        start_dt = datetime.datetime.combine(today, start_time)

    # Subsequent Shifts: Use Returned Truck's Time.
    else:
        start_dt = start

    total_time_passed = start_dt

    # Converting Times.
    for item in order:
        package = all_packages.search(item)
        delivery_delta = datetime.timedelta(hours=package.delivery_time)
        total_time_passed = total_time_passed + delivery_delta
        package.set_delivery_time(total_time_passed)
        truck.packages.append(package.package_id)

    # End Time: Truck Return to Hub
    end_time = start_dt + datetime.timedelta(hours=truck.end_time)
    truck.set_end_time(end_time)
