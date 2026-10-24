from dataclasses import dataclass


@dataclass(frozen=True)
class Persona:

    nombre: str

    def __post_init__(self):
        if not self.nombre or not self.nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        object.__setattr__(self, "nombre", self.nombre.strip())
