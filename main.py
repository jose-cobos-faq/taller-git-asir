import importlib
import pkgutil
import alumnos


def main():
    print("=== Taller Git · 2º ASIR ===")
    for mod in sorted(pkgutil.iter_modules(alumnos.__path__), key=lambda m: m.name):
        try:
            modulo = importlib.import_module(f"alumnos.{mod.name}")
            modulo.saludar()
        except AttributeError:
            print(f"[AVISO] {mod.name}.py no tiene la función saludar()")
        except Exception as e:
            print(f"[ERROR] {mod.name}.py: {e}")


if __name__ == "__main__":
    main()