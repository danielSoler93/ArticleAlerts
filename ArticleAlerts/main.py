import alerts.main as cr
import alerts.yaml_loader as yl


def main():

    user_info = yl.YamlLoader("alerts.yaml").load()
    for alert in user_info["alerts"]:
        alert = cr.AlertManager(alert)
        alert.check()

if __name__ == "__main__":
    main()
