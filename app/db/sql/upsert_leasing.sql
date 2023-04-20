-- :name insert_leasing :insert
INSERT INTO
    vehicle_leasing (
        Modelo, 
        PPU,
        OP_LEASING,
        LEASING,
        Mes_Venta,
        Status,
        Cruces,
        RESUMEN,
        CRUCE_PT_ESTADO,
        PVTA_PPTO,
        CTO_VTA_Teorico_cuoton_y_OPC,
        Nueva_Fecha
    )
VALUES
    (
        :Modelo,
        :PPU,
        :OP_LEASING,
        :LEASING,
        :Mes_Venta,
        :Status,
        :Cruces,
        :RESUMEN,
        :CRUCE_PT_ESTADO,
        :PVTA_PPTO,
        :CTO_VTA_Teorico_cuoton_y_OPC,
        :Nueva_Fecha
    )
;