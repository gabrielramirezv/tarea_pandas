from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def ensure_output_dir(output_file: str) -> None:
    output_path = Path(output_file)

    if output_path.parent != Path("."):
        output_path.parent.mkdir(parents=True, exist_ok=True)


def plot_top_regulators(
    regulon: pd.DataFrame,
    output_file: str,
    top_n: int = 10,
) -> None:
    ensure_output_dir(output_file)

    top = regulon.sort_values(
        "total_genes",
        ascending=False,
    ).head(top_n)

    # Crear la figura
    plt.figure(figsize=(10, 5))

    # Crear el gráfico de barras
    plt.bar(top["TF"], top["total_genes"], color="skyblue")

    # Configurar etiquetas de ejes y título
    plt.xlabel("TFs")
    plt.ylabel("Número de Genes")
    plt.title(f"Top {top_n} TFs")

    # Rotar las etiquetas del eje x para mejor legibilidad
    plt.xticks(rotation=45, ha="right")

    # Ajustar el diseño para evitar solapamientos
    plt.tight_layout()

    # Guardar la figura
    plt.savefig(output_file, dpi=300)

    # Cerrar la figura para liberar memoria
    plt.close()


def plot_type_distribution(
    regulon: pd.DataFrame,
    output_file: str,
) -> None:
    ensure_output_dir(output_file)

    counts = regulon["type"].value_counts()

    # Crear la figura
    plt.figure(figsize=(6, 5))

    # Crear el gráfico de barras
    plt.bar(counts.index, counts.values)

    # Configurar etiquetas de ejes y título
    plt.xlabel("Tipo de Regulador")
    plt.ylabel("Conteos")
    plt.title("Reguladores por Tipo")

    # Ajustar el diseño para evitar solapamientos
    plt.tight_layout()

    # Guardar la figura
    plt.savefig(output_file, dpi=300)

    # Cerrar la figura para liberar memoria
    plt.close()