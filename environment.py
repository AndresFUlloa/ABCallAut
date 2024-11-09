from utils.driver_utils import DriverUtils


def after_scenario(context, scenario):
    # Aquí colocas el código que deseas ejecutar después de cada escenario
    print(f"Finalizando el escenario: {scenario.name}")
    DriverUtils.close_driver()
