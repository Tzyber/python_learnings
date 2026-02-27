from abc import ABC, abstractmethod


class Tier(ABC):
    @abstractmethod
    def mache_laute(self):
        pass

class Hund(Tier):
    def mache_laute(self):
        print("Wuff! Wuff! Wuff!")

class Katze(Tier):
    def mache_laute(self):
        print("Miau! Miau! Miau!")

class Fuchs(Tier):
    def mache_laute(self):
        print("ring ring ring ring ring ring ring ring")


def zoo_show(tiere):
    print("Willkommen zur Zoo-Show!")
    for tier in tiere:
        tier.mache_laute()


show = [Hund(), Katze(), Fuchs()]
zoo_show(show)