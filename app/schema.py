from typing import Optional
from pydantic import BaseModel, validator
from datetime import datetime


class Leasing(BaseModel):
    Modelo: str
    PPU: str
    OP_LEASING: str
    LEASING: str
    Mes_Venta: Optional[datetime]
    Status: str
    Cruces: str
    RESUMEN: str
    CRUCE_PT_ESTADO: str
    PVTA_PPTO: float
    CTO_VTA_Teorico_cuoton_y_OPC: float
    Nueva_Fecha: Optional[datetime]

    @validator("Mes_Venta", "Nueva_Fecha", pre=True)
    def parse_dates(cls, value):
        if value == "SF":
            return None
        try:
            return datetime.strptime(value, "%d/%m/%Y")
        except ValueError:
            raise ValueError("invalid date format")

    @validator("PVTA_PPTO", "CTO_VTA_Teorico_cuoton_y_OPC", pre=True)
    def parse_floats(cls, value):
        if not value:
            return 0
        cleaned_value = value.replace(".", "")
        try:
            return float(cleaned_value)
        except ValueError:
            return "value is not a valid float"
