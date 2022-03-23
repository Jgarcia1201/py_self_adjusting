import datetime

from Modules import HUB
from Model import Truck
from Modules import CSVLoader


def show_total_miles_traveled(all_packages):
    truck_one = Truck.Truck(1)
    truck_two = Truck.Truck(2)
    truck_three = Truck.Truck(3)
    HUB.load_packages(truck_one, truck_two, truck_three, all_packages)
    order1 = HUB.deliver_packages(truck_one, 0, "4001 South 700 East", [], all_packages)
    order2 = HUB.deliver_packages(truck_two, 0, "4001 South 700 East", [], all_packages)
    order3 = HUB.deliver_packages(truck_three, 0, "4001 South 700 East", [], all_packages)
    print("")
    print("***********************************************************************************")
    print("Total Miles Traveled")
    print("***********************************************************************************")

    print("------------------TRUCK {}-----------------------".format(truck_one.truck_id))
    print("{} Miles Traveled".format(int(truck_one.miles_traveled)))
    print("------------------TRUCK {}-----------------------".format(truck_two.truck_id))
    print("{} Miles Traveled".format(int(truck_two.miles_traveled)))
    print("------------------TRUCK {}-----------------------".format(truck_three.truck_id))
    print("{} Miles Traveled".format(int(truck_three.miles_traveled)))

    print("------------------- TOTAL -----------------------".format(truck_two.truck_id))
    print(int(truck_one.miles_traveled + truck_three.miles_traveled + truck_two.miles_traveled))

    print("")
    print("***********************************************************************************")


def show_package_status(truck1, truck2, truck3, time, all_packages):
    truck_one = truck1
    truck_two = truck2
    truck_three = truck3

    day = datetime.date.today()

    HUB.load_packages(truck_one, truck_two, truck_three, all_packages)

    # Simulate Delivery: Trucks 1 & 2
    order1 = HUB.deliver_packages(truck_one, 0, "4001 South 700 East", [], all_packages)
    order2 = HUB.deliver_packages(truck_two, 0, "4001 South 700 East", [], all_packages)
    HUB.convert_time(0, truck_one, order1, all_packages)
    HUB.convert_time(0, truck_two, order2, all_packages)

    # Determining First Truck to Return to HUB.
    end_time = truck_one.end_time
    if truck_one.end_time > truck_two.end_time:
        end_time = truck_two.end_time

    # Truck 3
    order3 = HUB.deliver_packages(truck_three, 0, "4001 South 700 East", [], all_packages)
    HUB.convert_time(end_time, truck_three, order3, all_packages)

    try:
        today = datetime.date.today()
        user_time = datetime.datetime.strptime(time, "%I:%M %p").time()
        user_dt = datetime.datetime.combine(today, user_time)

        print("---------------------------------------------------------")
        print("Delivery Status at {}".format(user_dt))
        print("---------------------------------------------------------")
        print("---------------------------------------------------------")

        for i in range(1, 41):
            package = all_packages.search(i)
            if package.truck == 3:
                if package.delivery_time < user_dt:
                    package.delivered = "Delivered"
                elif user_dt < end_time:
                    package.delivered = "At The Hub"
                else:
                    package.delivered = "En Route"
            elif package.truck == 2:
                start_time = datetime.time(hour=9, minute=5)
                start_dt = datetime.datetime.combine(today, start_time)
                if package.delivery_time < user_dt:
                    package.delivered = "Delivered"
                elif user_dt < start_dt:
                    package.delivered = "At The Hub"
                else:
                    package.delivered = "En Route"
            else:
                start = datetime.time(hour=8)
                start_dt = datetime.datetime.combine(day, start)
                if package.delivery_time < user_dt:
                    package.delivered = "Delivered"
                elif user_dt < start_dt:
                    package.delivered = "At The Hub"
                else:
                    package.delivered = "En Route"

            if package.delivered == "Delivered":
                print(
                    "Package ID: {} |  Delivery Address: {} |  Status: {} at {}".format(package.package_id,
                                                                                        package.delivery_add,
                                                                                        package.delivered,
                                                                                        package.delivery_time))
            else:
                print(
                    "Package ID: {} |  Delivery Address: {} |  Status: {}".format(package.package_id,
                                                                                  package.delivery_add,
                                                                                  package.delivered))

            print("---------------------------------------------------------------------------------------------------")
    except:
        print("Not a Valid Time. Time must be in hh:mm am/pm format. For Example: 1:00 pm")


def show_all(all_packages):
    truck_one = Truck.Truck(1)
    truck_two = Truck.Truck(2)
    truck_three = Truck.Truck(3)
    # Load Packages.
    HUB.load_packages(truck_one, truck_two, truck_three, all_packages)
    # Simulate Delivery
    order1 = HUB.deliver_packages(truck_one, 0, "4001 South 700 East", [], all_packages)
    order2 = HUB.deliver_packages(truck_two, 0, "4001 South 700 East", [], all_packages)
    order3 = HUB.deliver_packages(truck_three, 0, "4001 South 700 East", [], all_packages)
    # Convert Times
    HUB.convert_time(0, truck_one, order1, all_packages)
    HUB.convert_time(0, truck_two, order2, all_packages)
    HUB.convert_time(truck_one.end_time, truck_three, order3, all_packages)

    print("**********************TRUCK 1**********************")
    for i in range(1, len(order1 + order2 + order3) + 1):
        package = all_packages.search(i)
        if package.truck == 1:
            print("Package ID: {} | Delivery Address: {} | Delivered: {}".format(package.package_id, package.delivery_add, package.delivery_time))
            print("------------------------------------------------------------------")
    print("Returned to Hub: {}".format(truck_one.end_time))
    print(" ")
    print("**********************TRUCK 2**********************")
    for i in range(1, len(order1 + order2 + order3) + 1):
        package = all_packages.search(i)
        if package.truck == 2:
            print("Package ID: {} | Delivery Address: {} | Delivered: {}".format(package.package_id, package.delivery_add, package.delivery_time))
            print("------------------------------------------------------------------")
    print("Returned to Hub: {}".format(truck_two.end_time))
    print(" ")
    print("**********************TRUCK 3**********************")
    for i in range(1, len(order1 + order2 + order3) + 1):
        package = all_packages.search(i)
        if package.truck == 3:
            print("Package ID: {} | Delivery Address: {} | Delivered: {}".format(package.package_id, package.delivery_add, package.delivery_time))
            print("------------------------------------------------------------------")
    print("Returned to Hub: {}".format(truck_three.end_time))
    print(" ")


def show_deadlines(all_packages):
    truck_one = Truck.Truck(1)
    truck_two = Truck.Truck(2)
    truck_three = Truck.Truck(3)
    # Load Packages.
    HUB.load_packages(truck_one, truck_two, truck_three, all_packages)
    # Simulate Delivery
    order1 = HUB.deliver_packages(truck_one, 0, "4001 South 700 East", [], all_packages)
    order2 = HUB.deliver_packages(truck_two, 0, "4001 South 700 East", [], all_packages)
    order3 = HUB.deliver_packages(truck_three, 0, "4001 South 700 East", [], all_packages)
    # Convert Times
    HUB.convert_time(0, truck_one, order1, all_packages)
    HUB.convert_time(0, truck_two, order2, all_packages)
    HUB.convert_time(truck_one.end_time, truck_three, order3, all_packages)

    for i in range(1, len(order1 + order2 + order3) + 1):
        pack = all_packages.search(i)
        if pack.deadline != "EOD":
            print("Package ID: {} | Deadline: {} | Delivered: {} | On Truck: {}".format(pack.package_id, pack.deadline, pack.delivery_time, pack.truck))
            print("-----------------------------------------------------------------------------")
