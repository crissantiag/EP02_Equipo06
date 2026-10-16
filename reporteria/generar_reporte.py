# -*- coding: utf-8 -*-
"""Mini reporte: imprime en una tabla los 3 KPIs energéticos."""
from pathlib import Path

import pandas as pd

BASE = Path(__file__).resolve().parent.parent
RUTA_OPERACIONES = BASE / "datos" / "operacion_sedes.csv"


def main():
    if not RUTA_OPERACIONES.exists():
        raise FileNotFoundError(f"No se encuentra el archivo: {RUTA_OPERACIONES}")

    df_op = pd.read_csv(RUTA_OPERACIONES)
    df_op["generacion_kwh"] = pd.to_numeric(df_op["generacion_kwh"], errors="coerce")
    df_op["demanda_kwh"] = pd.to_numeric(df_op["demanda_kwh"], errors="coerce")

    energia_total = df_op["generacion_kwh"].sum()
    demanda_total = df_op["demanda_kwh"].sum()
    deficit_total = (df_op["demanda_kwh"] - df_op["generacion_kwh"]).clip(lower=0).sum()

    reporte = pd.DataFrame({
        "Indicador": ["Energía generada total", "Demanda total", "Déficit total"],
        "Valor (kWh)": [f"{energia_total:,.2f}", f"{demanda_total:,.2f}", f"{deficit_total:,.2f}"],
    })

    print("=" * 42)
    print("      MINI REPORTE DE KPIs ENERGÉTICOS")
    print("=" * 42)
    print(reporte.to_string(index=False))
    print("=" * 42)


if __name__ == "__main__":
    main()
