from abc import ABC, abstractmethod


class State(ABC):
    """מחלקת בסיס מופשטת לכל מצבי המתג."""

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def light_on(self, switch):
        pass

    @abstractmethod
    def light_off(self, switch):
        pass

    def __str__(self):
        # מאפשר להדפיס את אובייקט המצב בתור שם קריא
        return self.name


class OnState(State):
    """ההתנהגות כשהמתג דולק."""

    @property
    def name(self):
        return "on"

    def light_on(self, switch):
        # המתג כבר דולק — אין שינוי
        pass

    def light_off(self, switch):
        # כיבוי של מתג דולק מעביר אותו למצב כבוי
        switch.set_state(OffState())


class OffState(State):
    """ההתנהגות כשהמתג כבוי."""

    @property
    def name(self):
        return "off"

    def light_on(self, switch):
        # הדלקה של מתג כבוי
        switch.set_state(OnState())
        print("Switch On")

    def light_off(self, switch):
        # לפי התרגיל: כיבוי של מתג שכבר כבוי מקלקל אותו
        switch.set_state(BrokenState())


class BrokenState(State):
    """ההתנהגות כשהמתג מקולקל."""

    @property
    def name(self):
        return "broken"

    def light_on(self, switch):
        # נשאר מקולקל
        print("Switch broken")

    def light_off(self, switch):
        # נשאר מקולקל
        print("Switch broken")


class LightSwitch:
    """המתג שומר מצב ומעביר אליו את בקשות הפעולה."""

    def __init__(self, state=None):
        # אם לא התקבל מצב התחלתי, מתחילים במצב כבוי
        if state is None:
            self._state = OffState()
        else:
            self._state = state

    @property
    def state(self):
        # מחזיר את אובייקט המצב הנוכחי
        return self._state

    def set_state(self, state):
        # מחליף את אובייקט המצב של המתג
        self._state = state

    def light_on(self):
        # מעביר את בקשת ההדלקה למצב הנוכחי
        self._state.light_on(self)

    def light_off(self):
        # מעביר את בקשת הכיבוי למצב הנוכחי
        self._state.light_off(self)


if __name__ == "__main__":
    switch = LightSwitch()
    print("Initial state:", switch.state)

    switch.light_on()
    print("After turning on:", switch.state)

    switch.light_on()
    print("After turning on again:", switch.state)

    switch.light_off()
    print("After turning off:", switch.state)

    switch.light_off()
    print("After turning off again:", switch.state)

    switch.light_on()
    print("After trying to turn on:", switch.state)

    switch.light_off()
    print("Final state:", switch.state)