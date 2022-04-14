"""Factory Back Game. Check README file for game instructions"""

import random
import asyncio
from robot import Robot
import sys

foo = []
bar = []
foobar = []
euro = 0

# -----------Adjust weights to increase probability of a certain action for robot-------------
WEIGHTS = [20, 20, 20, 20, 20]

MAX_ROBOTS = 30
resources = {
    "foo": foo,
    "bar": bar,
    "foobar": foobar,
    "euro": euro
}

# -------Set two initial robot instances-----------
robots = []
for _ in range(2):
    robots.append(Robot())

print("Hi! This is automated Factory Back Game. The goal is to reach automatically 30 robots by assigning tasks to "
      "Robots randomly. Starts from 2 Robots and zero resources")

# -------Async execution of tasks by robots-----------
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
while len(robots) != MAX_ROBOTS:
    for r in robots:
        tasks = []
        ioloop = asyncio.get_event_loop()

        change_activity = random.choices([True, False])[0]
        if change_activity:
            r.change_activity()

        actions = [r.mine_foo, r.mine_bar, r.assembly_attempt, r.buy_robot, r.sell_foobar]
        tasks.append(ioloop.create_task(random.choices(actions, weights=WEIGHTS)[0](resources)))
        ioloop.run_until_complete(asyncio.wait(tasks))
        if r.create_robot:
            robots.append(Robot())
            print(robots)
            r.create_robot = False

        print(f"Foos: {len(resources['foo'])} Bars: {len(resources['bar'])} Foobars: {len(resources['foobar'])}"
              f" Euro: {resources['euro']}")
        print(f"Working Robots: {len(robots)} in total.")
ioloop.close()










# try:
#     if action[1]:
#         robots.append(Robot())
#         print(robots)
# except KeyError:
#     pass

# print(resources)
# print([f["foo_identifier"] for f in resources['foobar']])
# print([f["bar_identifier"] for f in resources['foobar']])


# if action.has_been_called:
#     print(f"This is {n}-d func called.")

#
# def change_activity(function):
#     time.sleep(5)
#     def wrapper():
#         function()
#     return wrapper
#
