from abc import ABC, abstractmethod

class Footballmatch:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self._observers = []
        self._home_goals = 0
        self._away_goals = 0


    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        score = f"{self.home_team} {self._home_goals} - {self._away_goals} {self.away_team}"
        for observer in self._observers:
            observer.update(score)

    def score(self, home_team_goal):
        if home_team_goal:
            self._home_goals += 1
        else:
            self._away_goals += 1
        print(f"\n--- TOR für {self.home_team if home_team_goal else self.away_team}! ---")
        self.notify_observers()


class Observer(ABC):
    @abstractmethod
    def update(self,score):
        pass

class MobileApp(Observer):
    def update(self,score):
        print(f"[Handy-App] Eilmeldung: Neuer Spielstand: {score}")

class Webportal(Observer):
    def update(self,score):
        print(f"[Webportal] Aktueller Spielstand: {score}")

class TVTicker(Observer):
    def update(self,score):
        print(f"[TV-Ticker] Spielstand aktualisiert: {score}")


if __name__ == "__main__":
    match = Footballmatch("FC Bayern", "Borussia Dortmund")
    app = MobileApp()
    web = Webportal()
    tv = TVTicker()

    match.add_observer(web)
    match.add_observer(tv)
    match.add_observer(app)

    match.score(True)  # Tor für Heimteam
    match.score(False)  # Tor für Auswärtsteam
