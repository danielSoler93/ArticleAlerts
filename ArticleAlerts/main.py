import os
import alerts.main as cr
import alerts.yaml_loader as yl

DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    yaml_file = os.path.join(DIR, "alerts.yaml")
    user_info = yl.YamlLoader(yaml_file).load()
    for alert in user_info["alerts"]:
        alert = cr.AlertManager(alert)
        alert.check()

if __name__ == "__main__":
    main()
