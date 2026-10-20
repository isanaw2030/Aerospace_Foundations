# save some telemetry report inside telemetry_report.txt file
from mission_safety import is_collect_stats
rocket = is_collect_stats()
def write_report():
    rocket_name = rocket
    mission_status = "Successful"
    warning_count = 2
    mission_signal = "Strong"

    with open("telemetry_report.txt", "w") as file:
        file.write(f"Rocket : {rocket_name}\n")
        file.write(f"Mission Status : {mission_status}\n")
        file.write(f"Number of Warnings : {warning_count}\n")
        file.write(f"Mission Signal : {mission_signal}\n")


def read_report():
    with open("telemetry_report.txt", "r") as file:
        contents = file.read()
        return (contents)

