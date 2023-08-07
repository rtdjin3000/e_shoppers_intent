from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class osi(BaseModel):
    Administrative: int
    Administrative_Duration: float
    Informational: int
    Informational_Duration: float
    ProductRelated: int
    ProductRelated_Duration: float
    BounceRates: float
    ExitRates: float
    PageValues: float
    SpecialDay: float
    Month: object
    OperatingSystems: int
    Browser: int
    Region: int
    TrafficType: int
    VisitorType: object
    Weekend: bool
    Revenue: bool