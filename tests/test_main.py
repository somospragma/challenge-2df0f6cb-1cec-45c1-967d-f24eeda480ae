import pytest
from src.main import main

def test_main():
    assert main() == "Bienvenido al proyecto de optimización de flujo de trabajo con asistentes de IA."