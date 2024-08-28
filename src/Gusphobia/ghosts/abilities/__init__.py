from pydantic import BaseModel


class Ability(BaseModel):
    description: str


SpiritAbility = Ability(
    description="Incense is more effective, preventing a hunt for longer."
)
PoltergeistAbility = Ability(
    description="Capable of throwing multiple objects at once. Can throw objects at high velocities. Becomes powerless with no throwables nearby."
)
MareAbility = Ability(
    description="Has an increased chance to attack in the dark. Turning the lights on will reduce the chance of an attack. Will occasionally turn lights off right away. Will never turn a light on."
)
DemonAbility = Ability(
    description="Can initiate hunts more often. Can hunt at max sanity. Crucifix range is 50% larger than placement range indicator."
)
YokaiAbility = Ability(
    description="Talking near the Yokai will anger it, increasing the chance to attack. Can only hear voices close to it during a hunt."
)
MylingAbility = Ability(
    description="Produces quieter sounds during a hunt. Produces paranormal sounds more frequently on the Parabolic Microphone."
)
RaijuAbility = Ability(
    description="Moves faster near active electronic equipment. Disrupts electronic equipment from further away when it hunts."
)
MoroiAbility = Ability(
    description="Moves noticeably faster at low player sanity. Can curse players, making them lose sanity quicker than usual while in the investigation zone. Incense blinds the ghost for 50% longer during hunts."
)
WraithAbility = Ability(
    description="Cannot be tracked by footsteps. Will occasionally teleport to a random player. Will not step in salt."
)
BansheeAbility = Ability(
    description="Will target only one player at a time. Increased chance of performing a singing ghost event. Has a distinctive wail on the Parabolic Microphone."
)
RevenantAbility = Ability(
    description="Moves significantly faster if the player location is known during a hunt. Moves very slowly when not chasing a player."
)
YureiAbility = Ability(
    description="Has a stronger effect on sanity. Smudging the Yurei will temporarily trap it and reduce how often it wanders. Using its ability causes it to shut doors."
)
HantuAbility = Ability(
    description="Lower temperatures allow the Hantu to move faster. Warmer areas slow the Hantu's movement. Will produce freezing breath during a hunt if the fuse box is off. Will never turn the fuse box on."
)
OnryoAbility = Ability(
    description="A flame extinguishing can cause an Onryo to attack. The presence of flames reduces the Onryo's ability to attack."
)
ObakeAbility = Ability(
    description="Has a chance to not leave fingerprints when interacting with something. May leave fingerprints that disappear quicker. Has a small chance of leaving special fingerprints. Can quickly shapeshift into another model during a hunt."
)
DeogenAbility = Ability(
    description="Always knows where the player is during a hunt and moves very fast when going to their location. Moves very slowly when near its victim."
)
PhantomAbility = Ability(
    description="Looking at a Phantom will lower the player's sanity considerably. Will occasionally walk to a random player. Taking a photo of the Phantom will cause it to briefly disappear. Less visible during hunts."
)
JinnAbility = Ability(
    description="Travels at a faster speed if a distant player is in line of sight while the fuse box is on. Cannot use its ability if the fuse box is off. Will never turn the fuse box off directly."
)
ShadeAbility = Ability(
    description="Less likely to perform interactions. Cannot hunt if people are nearby."
)
OniAbility = Ability(
    description="Increased activity when players are nearby. More visible during hunts. Cannot perform the airball ghost event."
)
GoryoAbility = Ability(
    description="Can only enter a D.O.T.S. state when nobody is nearby. Its D.O.T.S. silhouette can only be seen through a Video Camera. Cannot wander far from its room, or change favorite rooms."
)
TheTwinsAbility = Ability(
    description="Either twin may start a hunt, though not at the same time. One twin is slow, the other is fast. Will often interact with the environment at the same time but usually in different places."
)
TheMimicAbility = Ability(
    description="Can mimic the abilities and traits of other ghosts. Will present fake Ghost Orbs as secondary evidence."
)
ThayeAbility = Ability(
    description="Much more active, aggressive and faster during hunts as soon as a player enters the location. Becomes slower and less active over time."
)

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
