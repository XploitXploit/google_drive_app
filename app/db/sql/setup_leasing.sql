-- :name setup_leasing

DROP TABLE IF EXISTS vehicle_leasing;

CREATE TABLE IF NOT EXISTS vehicle_leasing (
    id SERIAL PRIMARY KEY,
    Modelo VARCHAR(255),
    PPU VARCHAR(255),
    OP_LEASING VARCHAR(255),
    LEASING VARCHAR(255),
    Mes_Venta DATE,
    Status VARCHAR(255),
    Cruces VARCHAR(255),
    RESUMEN VARCHAR(255),
    CRUCE_PT_ESTADO VARCHAR(255),
    PVTA_PPTO FLOAT,
    CTO_VTA_Teorico_cuoton_y_OPC FLOAT,
    Nueva_Fecha DATE
);