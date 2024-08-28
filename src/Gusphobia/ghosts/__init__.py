from typing import List

from pydantic import BaseModel

from .abilities import (
    Ability,
    SpiritAbility,
    PoltergeistAbility,
    MareAbility,
    DemonAbility,
    YokaiAbility,
    MylingAbility,
    RaijuAbility,
    MoroiAbility,
    WraithAbility,
    BansheeAbility,
    RevenantAbility,
    YureiAbility,
    HantuAbility,
    OnryoAbility,
    ObakeAbility,
    DeogenAbility,
    PhantomAbility,
    JinnAbility,
    ShadeAbility,
    OniAbility,
    GoryoAbility,
    TheTwinsAbility,
    TheMimicAbility,
    ThayeAbility,
)
from .evidences import (
    Evidence,
    EMF5,
    UltraViolet,
    WritingBook,
    Freezing,
    DOTS,
    GhostOrbs,
    SpiritBox,
)


class Ghost(BaseModel):
    name: str
    description: str  # TODO
    hunt_range: str
    ability: Ability
    evidences: List[Evidence, Evidence, Evidence]  # TODO: Fix weird typing's??


Spirit = Ghost(
    name="Spirit",
    description="",
    hunt_range="50%",
    ability=SpiritAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Poltergeist = Ghost(
    name="Poltergeist",
    description="",
    hunt_range="50%",
    ability=PoltergeistAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Mare = Ghost(
    name="Mare",
    description="",
    hunt_range="40% - 60%",
    ability=MareAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Demon = Ghost(
    name="Demon",
    description="",
    hunt_range="70% - 100%",
    ability=DemonAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Yokai = Ghost(
    name="Yokai",
    description="",
    hunt_range="50% - 80%",
    ability=YokaiAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Myling = Ghost(
    name="Myling",
    description="",
    hunt_range="50%",
    ability=MylingAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Raiju = Ghost(
    name="Raiju",
    description="",
    hunt_range="50% - 65%",
    ability=RaijuAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Moroi = Ghost(
    name="Moroi",
    description="",
    hunt_range="50%",
    ability=MoroiAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Wraith = Ghost(
    name="Wraith",
    description="",
    hunt_range="50%",
    ability=WraithAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Banshee = Ghost(
    name="Banshee",
    description="",
    hunt_range="50%",
    ability=BansheeAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Revenant = Ghost(
    name="Revenant",
    description="",
    hunt_range="50%",
    ability=RevenantAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Yurei = Ghost(
    name="Yurei",
    description="",
    hunt_range="50%",
    ability=YureiAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Hantu = Ghost(
    name="Hantu",
    description="",
    hunt_range="50%",
    ability=HantuAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Onryo = Ghost(
    name="Onryo",
    description="",
    hunt_range="60% - 100%",
    ability=OnryoAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Obake = Ghost(
    name="Obake",
    description="",
    hunt_range="50%",
    ability=ObakeAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Deogen = Ghost(
    name="Deogen",
    description="",
    hunt_range="40%",
    ability=DeogenAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Phantom = Ghost(
    name="Phantom",
    description="",
    hunt_range="50%",
    ability=PhantomAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Jinn = Ghost(
    name="Jinn",
    description="",
    hunt_range="50%",
    ability=JinnAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Shade = Ghost(
    name="Shade",
    description="",
    hunt_range="35%",
    ability=ShadeAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Oni = Ghost(
    name="Oni",
    description="",
    hunt_range="50%",
    ability=OniAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Goryo = Ghost(
    name="Goryo",
    description="",
    hunt_range="50%",
    ability=GoryoAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
TheTwins = Ghost(
    name="The Twins",
    description="",
    hunt_range="50%",
    ability=TheTwinsAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
TheMimic = Ghost(
    name="The Mimic",
    description="",
    hunt_range="50% - 100%",
    ability=TheMimicAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Thaye = Ghost(
    name="Thaye",
    description="",
    hunt_range="15% - 75%",
    ability=ThayeAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)

__all__ = [
    "Spirit",
    "Poltergeist",
    "Mare",
    "Demon",
    "Yokai",
    "Myling",
    "Raiju",
    "Moroi",
    "Wraith",
    "Banshee",
    "Revenant",
    "Yurei",
    "Hantu",
    "Onryo",
    "Obake",
    "Deogen",
    "Phantom",
    "Jinn",
    "Shade",
    "Oni",
    "Goryo",
    "TheTwins",
    "TheMimic",
    "Thaye",
]
