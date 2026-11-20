import json
import sys
from pathlib import Path
import pandas as pd

OUTPUT_PATH = Path("/home/amaru/dev/amarufo.github.io/dph/data.js")

COLUMNAS = [
    "n",
    "modalidad",
    "entidad",
    "nombre",
    "dpto",
    "lat",
    "lng",
    "cui",
    "monto",
    "ejecutor",
    "supervisor",
    "estado",
    "tipo",
]


def limpiar_texto(valor) -> str:
    if pd.isna(valor):
        return ""
    return str(valor).strip()


def limpiar_numero(valor, como_int: bool = False):
    if pd.isna(valor) or str(valor).strip() == "":
        return None
    if isinstance(valor, (int, float)):
        return int(valor) if como_int else float(valor)
    texto = str(valor).strip().replace(" ", "").replace(",", "")
    return int(float(texto)) if como_int else float(texto)


def cargar_archivo(ruta_archivo: Path) -> pd.DataFrame:
    ext = ruta_archivo.suffix.lower()
    if ext == ".ods":
        engine = "odf"
    elif ext in {".xlsx", ".xls"}:
        engine = "openpyxl" if ext == ".xlsx" else None
    else:
        raise ValueError(f"Formato no soportado: {ext}. Usa .ods, .xlsx o .xls")

    df = pd.read_excel(ruta_archivo, engine=engine)
    df.columns = [str(col).strip().lower() for col in df.columns]

    faltantes = [col for col in COLUMNAS if col not in df.columns]
    if faltantes:
        raise ValueError(f"Faltan columnas en el archivo: {', '.join(faltantes)}")

    return df


def construir_proyectos(df: pd.DataFrame) -> list[dict]:
    proyectos = []
    for idx, fila in df.iterrows():
        n_val = limpiar_numero(fila["n"], como_int=True)
        if n_val is None:
            n_val = idx + 1

        proyecto = {
            "n": n_val,
            "modalidad": limpiar_texto(fila["modalidad"]),
            "entidad": limpiar_texto(fila["entidad"]),
            "nombre": limpiar_texto(fila["nombre"]),
            "dpto": limpiar_texto(fila["dpto"]),
            "lat": limpiar_numero(fila["lat"], como_int=False),
            "lng": limpiar_numero(fila["lng"], como_int=False),
            "cui": limpiar_texto(fila["cui"]),
            "monto": limpiar_numero(fila["monto"], como_int=False),
            "ejecutor": limpiar_texto(fila["ejecutor"]),
            "supervisor": limpiar_texto(fila["supervisor"]),
            "estado": limpiar_texto(fila["estado"]),
            "tipo": limpiar_texto(fila["tipo"]),
        }
        proyectos.append(proyecto)
    return proyectos


def main():
    if len(sys.argv) < 2:
        print("Uso: python actualizar_proyectos.py <ruta_archivo.ods|.xlsx>")
        sys.exit(1)

    input_path = Path(sys.argv[1]).expanduser().resolve()
    if not input_path.exists():
        print(f"Error: no se encontró el archivo '{input_path}'")
        sys.exit(1)

    df = cargar_archivo(input_path)
    proyectos = construir_proyectos(df)

    contenido_js = f"const PROYECTOS = {json.dumps(proyectos, indent=4, ensure_ascii=False)};\n"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(contenido_js, encoding="utf-8")

    print(f"Actualizado {OUTPUT_PATH} con {len(proyectos)} proyectos.")


if __name__ == "__main__":
    main()
