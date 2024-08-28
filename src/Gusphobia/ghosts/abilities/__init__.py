from pydantic import BaseModel


class Ability(BaseModel):
    description: str  # TODO


SpiritAbility = Ability(description="")
PoltergeistAbility = Ability(description="")
MareAbility = Ability(description="")
DemonAbility = Ability(description="")
YokaiAbility = Ability(description="")
MylingAbility = Ability(description="")
RaijuAbility = Ability(description="")
MoroiAbility = Ability(description="")
WraithAbility = Ability(description="")
BansheeAbility = Ability(description="")
RevenantAbility = Ability(description="")
YureiAbility = Ability(description="")
HantuAbility = Ability(description="")
OnryoAbility = Ability(description="")
ObakeAbility = Ability(description="")
DeogenAbility = Ability(description="")
PhantomAbility = Ability(description="")
JinnAbility = Ability(description="")
ShadeAbility = Ability(description="")
OniAbility = Ability(description="")
GoryoAbility = Ability(description="")
TheTwinsAbility = Ability(description="")
TheMimicAbility = Ability(description="")
ThayeAbility = Ability(description="")

__all__ = [
    "Ability",
    "SpiritAbility",
    "PoltergeistAbility",
    "MareAbility",
    "DemonAbility",
    "YokaiAbility",
    "MylingAbility",
    "RaijuAbility",
    "MoroiAbility",
    "WraithAbility",
    "BansheeAbility",
    "RevenantAbility",
    "YureiAbility",
    "HantuAbility",
    "OnryoAbility",
    "ObakeAbility",
    "DeogenAbility",
    "PhantomAbility",
    "JinnAbility",
    "ShadeAbility",
    "OniAbility",
    "GoryoAbility",
    "TheTwinsAbility",
    "TheMimicAbility",
    "ThayeAbility",
]
