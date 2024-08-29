"""Submodule for api ghost related data."""

from typing import List, Optional, Union

from ...ghosts import (
    Ghost,
    Ghosts,
    Spirit,
    Poltergeist,
    Mare,
    Demon,
    Yokai,
    Myling,
    Raiju,
    Moroi,
    Wraith,
    Banshee,
    Revenant,
    Yurei,
    Hantu,
    Onryo,
    Obake,
    Deogen,
    Phantom,
    Jinn,
    Shade,
    Oni,
    Goryo,
    TheTwins,
    TheMimic,
    Thaye,
)
from ...ghosts.evidences import Evidence

ghost_map: dict[str, Ghost] = {
    "Spirit": Spirit,
    "Poltergeist": Poltergeist,
    "Mare": Mare,
    "Demon": Demon,
    "Yokai": Yokai,
    "Myling": Myling,
    "Raiju": Raiju,
    "Moroi": Moroi,
    "Wraith": Wraith,
    "Banshee": Banshee,
    "Revenant": Revenant,
    "Yurei": Yurei,
    "Hantu": Hantu,
    "Onryo": Onryo,
    "Obake": Obake,
    "Deogen": Deogen,
    "Phantom": Phantom,
    "Jinn": Jinn,
    "Shade": Shade,
    "Oni": Oni,
    "Goryo": Goryo,
    "TheTwins": TheTwins,
    "TheMimic": TheMimic,
    "Thaye": Thaye,
}
ghost_variations: dict[str, list[str]] = {  # TODO: Remove unnecessary " " characters.
    "Spirit": ["spirit"],
    "Poltergeist": ["poltergeist", "polter", "polty", "polt"],
    "Mare": ["mare"],
    "Demon": ["demon"],
    "Yokai": ["yokai"],
    "Myling": ["myling"],
    "Raiju": ["raiju"],
    "Moroi": ["moroi"],
    "Wraith": ["wraith"],
    "Banshee": ["banshee"],
    "Revenant": ["revenant", "rev"],
    "Yurei": ["yurei"],
    "Hantu": ["hantu"],
    "Onryo": ["onryo"],
    "Obake": ["obake"],
    "Deogen": ["deogen", "deo"],
    "Phantom": ["phantom"],
    "Jinn": ["jinn"],
    "Shade": ["shade"],
    "Oni": ["oni"],
    "Goryo": ["goryo"],
    "TheTwins": ["thetwins", "twins", "the twins"],
    "TheMimic": ["themimic", "mimic", "the mimic"],
    "Thaye": ["thaye"],
}


def identify_ghost(evidences: Union[List[str], List[Evidence]]) -> Optional[Ghost]:
    for ghost in Ghosts:
        if all(evidence in ghost.evidences for evidence in evidences):
            return ghost
    return None


def possible_ghosts(evidences: Union[List[str], List[Evidence]]) -> List[Ghost]:
    possible: list[Ghost] = []
    for ghost in Ghosts:
        if all(evidence in ghost.evidences for evidence in evidences):
            possible.append(ghost)
    return possible


__all__ = ["ghost_map", "ghost_variations", "identify_ghost", "possible_ghosts"]
