import json

class Pakrat:
    def __init__(self) -> None:
        pass

    def is_installed(self, package: str) -> bool:
        check = self.load_packages()

        for c in check:
            if c["Name"] == package:
                return True

        return False

    def load_packages(self):
        with open("installed.json", "r") as installed:
            packages = json.load(installed)

        return packages

    def save_packages(self, packages: list):
        with open("installed.json", "w") as file:
            json.dump(packages, file, indent=4)

    def install(self, name: str, version: str):
        if self.is_installed(name):
            print(f"The package {name} is already installed.")
        else:
            package = {"Name": name, "Version": version}

            packages = self.load_packages()
            packages.append(package)

            self.save_packages(packages)

    def remove(self, name: str):
        if self.is_installed(name):
            packages = self.load_packages()

            packages = [
                package for package in packages
                if package["Name"] != name
            ]

            self.save_packages(packages)
        else:
            print("There is no package match.")

    def list_packages(self):
        