from __future__ import annotations

from typing import Protocol


#Fast API
class UserInterface:
    """Driver Adapter(left of the hexagon)."""

    def __init__(self, application: Application) -> None:
        self.application = application


#Business Logic
class Application:
    """Core Business Logic(center of hexagon)."""

    def __init__(self, persistence: PersistencePort) -> None:
        self.persistence = persistence

class Model:
    pass

class PersistencePort(Protocol):
    def save(self, model: Model) -> None:
        pass

    def load(self, model_id: int) -> Model:
        pass

#Database class
class Persistence:
    """Driven adapter (right of hexagon)."""

    def save(self, model: Model) -> None:
        pass

    def load(self, model_id: int) -> Model:
        return Model()

db = Persistence()
app = Application(db)
ui = UserInterface(app)


