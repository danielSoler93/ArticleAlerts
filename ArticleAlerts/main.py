import alerts.main as cr


ALERTS = ["deep learning drug discovery", "p38 tab1", "ML drug discovery", "gpcr binding assay",
          "MDM2",]

def main():
    for alert in ALERTS:
        alert = cr.AlertManager(alert)
        alert.check()

if __name__ == "__main__":
    main()
