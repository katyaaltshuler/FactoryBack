import functools
import random
from typing import Dict
import time
import asyncio

from foo import Foo
from bar import Bar
from foobar import Foobar


def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)

    return wrapped


def trackcalls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.has_been_called = True
        return func(*args, **kwargs)

    wrapper.has_been_called = False
    return wrapper


class Robot:
    def __init__(self):
        self.left_factory = {}
        self.create_robot = False

    @trackcalls
    async def mine_foo(self, resources: Dict) -> Dict:
        """Updates resources after mining"""
        await asyncio.sleep(1)
        resources['foo'].append(Foo())
        print("+1 Foo")
        return resources

    @trackcalls
    async def mine_bar(self, resources: Dict) -> Dict:
        """Updates resources after mining"""
        await asyncio.sleep(random.uniform(0.5, 2))
        resources['bar'].append(Bar())
        print("+1 Bar")
        return resources

    @trackcalls
    async def buy_robot(self, resources: Dict):
        """If resources are sufficient allows creating new Robot instance"""
        await asyncio.sleep(0)
        if resources['euro'] - 3 >= 0 and len(resources['foo']) - 6 >= 0:
            resources['euro'] -= 3
            resources['foo'] = resources['foobar'][6:]
            print("+1 Robot")
            self.create_robot = True
            return resources, self.create_robot
        print("Not enough resources to buy Robot.")
        return resources

    @trackcalls
    async def sell_foobar(self, resources: Dict):
        """If resources are sufficient removes foobars from stock and inserts them into new list"""
        for n in range(5, 0, -1):
            if len(resources['foobar']) - n >= 0:
                await asyncio.sleep(10)
                self.left_factory = []
                self.left_factory = resources['foobar'][:n]
                resources['foobar'] = resources['foobar'][n:]
                resources['euro'] += n
                print(f"The {n} Foobars sold")
                break
        return resources

    def change_activity(self):
        print("Activity changed.")
        time.sleep(5)

    def _assembly_success(self, resources: Dict) -> Dict:
        print(f"Success! The Foobar has been assembled.")
        resources['foobar'].append(Foobar().create_foobar(resources['foo'][0], resources['bar'][0]))
        resources['foo'].pop(0)
        resources['bar'].pop(0)
        return resources

    def _assembly_fail(self, resources: Dict) -> Dict:
        resources['foo'].pop(0)
        print(f"Fail to assembly! You've lost one Foo.")
        return resources

    @trackcalls
    async def assembly_attempt(self, resources: Dict):
        """Attempts assembly with a certain probability of positive outcome"""
        assembl_result = {
            "success": self._assembly_success,
            "fail": self._assembly_fail
        }
        if len(resources['foo']) - 1 >= 0 and len(resources['bar']) - 1 >= 0:
            await asyncio.sleep(10)
            return assembl_result[random.choices(list(assembl_result.keys()), weights=[60, 40])[0]](resources)
        print("Not enough resources for assembling.")
        return resources


