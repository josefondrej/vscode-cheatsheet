def my_util():
    print("my_util")


class MyClass:
    def __init__(self, name: str) -> None:
        self._name = name

    def introduce(self) -> None:
        print(f"Hello, my name is {self._name}!")
