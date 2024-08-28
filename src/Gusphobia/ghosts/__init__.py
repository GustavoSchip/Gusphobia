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


class Ghost(BaseModel):  # TODO: Add 'behaviours' trait?
    name: str
    description: str
    hunt_range: str
    ability: Ability
    evidences: List[Evidence, Evidence, Evidence]  # TODO: Fix weird typing's!??


Spirit = Ghost(
    name="Spirit",
    description="Spirits are very common ghosts. They are very powerful, but passive, only attacking when they need to. They defend their place of death to the utmost degree, killing anyone that is caught overstaying their welcome.",
    hunt_range="50%",
    ability=SpiritAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Poltergeist = Ghost(
    name="Poltergeist",
    description="One of the most famous ghosts, the Poltergeist. Known to manipulate objects around it to spread fear into its victims.",
    hunt_range="50%",
    ability=PoltergeistAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Mare = Ghost(
    name="Mare",
    description="A Mare is the source of all nightmares, making it most powerful in the dark.",
    hunt_range="40% - 60%",
    ability=MareAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Demon = Ghost(
    name="Demon",
    description="A Demon is one of the worst ghosts you can encounter. It has been known to attack without reason.",
    hunt_range="70% - 100%",
    ability=DemonAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Yokai = Ghost(
    name="Yokai",
    description="Yokai are common ghosts that are attracted to human voices. They can usually be found haunting family homes.",
    hunt_range="50% - 80%",
    ability=YokaiAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Myling = Ghost(
    name="Myling",
    description="A Myling is a very vocal and active ghost. They are rumoured to be quiet when hunting their prey.",
    hunt_range="50%",
    ability=MylingAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Raiju = Ghost(
    name="Raiju",
    description="A Raiju is a demon that thrives on electrical current. While generally calm, they can become agitated when overwhelmed with power.",
    hunt_range="50% - 65%",
    ability=RaijuAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Moroi = Ghost(
    name="Moroi",
    description="Moroi have risen from the grave to drain energy from the living. They have been known to place curses on their victims, curable only by antidotes or moving very far away.",
    hunt_range="50%",
    ability=MoroiAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Wraith = Ghost(
    name="Wraith",
    description="Wraiths are one of the most dangerous ghosts you will find. It is also the only known ghost that has the ability of flight and has sometimes been known to travel through walls.",
    hunt_range="50%",
    ability=WraithAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Banshee = Ghost(
    name="Banshee",
    description="The singing siren, known for attracting its victims through song. It has been known to single out its prey before making a killing blow.",
    hunt_range="50%",
    ability=BansheeAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Revenant = Ghost(
    name="Revenant",
    description="A Revenant is a violent ghost that will attack indiscriminately. Their speed can be deceiving, as they are slow while dormant; however, as soon as they hunt they can move incredibly fast.",
    hunt_range="50%",
    ability=RevenantAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Yurei = Ghost(
    name="Yurei",
    description="A Yurei is a ghost that has returned to the physical world, usually for the purpose of revenge or hatred.",
    hunt_range="50%",
    ability=YureiAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Hantu = Ghost(
    name="Hantu",
    description="A Hantu is a rare ghost that thrives in the coldest climates. The cold seems to make them more aggressive and empowered.",
    hunt_range="50%",
    ability=HantuAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Onryo = Ghost(
    name="Onryo",
    description="The Onryo is often referred to as 'The Wrathful Spirit'. It steals souls from dying victims' bodies to seek revenge. This ghost has been known to fear any form of fire, and will do anything to be far from it.",
    hunt_range="60% - 100%",
    ability=OnryoAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Obake = Ghost(
    name="Obake",
    description="Obake are terrifying shape-shifters, capable of taking on many forms. They have been seen taking on humanoid shapes to attract their prey.",
    hunt_range="50%",
    ability=ObakeAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Deogen = Ghost(
    name="Deogen",
    description="Sometimes surrounded by an endless fog, Deogen have been eluding ghost hunters for years. These ghosts have been reported to find even the most hidden prey, before stalking them into exhaustion.",
    hunt_range="40%",
    ability=DeogenAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Phantom = Ghost(
    name="Phantom",
    description="A Phantom is a ghost that can possess the living, inducing fear into those around it. They are most commonly summoned from Ouija Boards.",
    hunt_range="50%",
    ability=PhantomAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Jinn = Ghost(
    name="Jinn",
    description="A Jinn is a territorial ghost that will attack when threatened. It has also been known to be able to travel at significant speed.",
    hunt_range="50%",
    ability=JinnAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Shade = Ghost(
    name="Shade",
    description="A Shade is known to be very shy. There is evidence to suggest that a Shade will stop all paranormal activity if there are people nearby.",
    hunt_range="35%",
    ability=ShadeAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Oni = Ghost(
    name="Oni",
    description="Onis love to scare their victims as much as possible before attacking. They are often seen in their physical form, guarding their place of death.",
    hunt_range="50%",
    ability=OniAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Goryo = Ghost(
    name="Goryo",
    description="When a Goryo passes through a DOTS projector, using a video camera is the only way to see it.",
    hunt_range="50%",
    ability=GoryoAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
TheTwins = Ghost(
    name="The Twins",
    description="These ghosts have been reported to mimic each other's actions. They alternate their attacks to confuse their prey.",
    hunt_range="50%",
    ability=TheTwinsAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
TheMimic = Ghost(
    name="The Mimic",
    description="The Mimic is an elusive, mysterious, copycat ghost that mirrors traits and behaviours from others, including other ghost types.",
    hunt_range="50% - 100%",
    ability=TheMimicAbility,
    evidences=[EMF5, SpiritBox, WritingBook],
)
Thaye = Ghost(
    name="Thaye",
    description="Thaye have been known to rapidly age over time, even in the afterlife. From what we've learned, they seem to deteriorate faster while within the presence of the living.",
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
