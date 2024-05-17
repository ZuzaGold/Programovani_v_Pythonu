from dataclasses import dataclass

@dataclass
class Package:
    address: str
    weight: float
    state: str

@dataclass
class ValuablePackage(Package):
    value: int

package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, "nedoručen", 5500)
package_2 = Package("Godrikův důl 47", 1.9, "nedoručen")
package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, "doručen", 5500)

package_list = [package_1, package_2, package_3]

total_value = 0
for package in package_list:
    if isinstance(package, ValuablePackage) and getattr(package, 'state', '') == 'nedoručen':
        total_value += getattr(package, 'value', 0)

print(f"Celková hodnota neodručených cenných balíků v autě je: {total_value} Kč.")
