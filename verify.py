#!/usr/bin/env python3
"""declared-behaviour: one page asks its host for a sound, a position and a map, and prints only what came back."""
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools"))
from appplayer import AppPlayer  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
CAP = os.path.join(HERE, "captures")
BUNDLE = os.path.join(HERE, "declared_behaviour.mbd")

ap = AppPlayer()
bid = ap.install_bundle(BUNDLE)
ap.restart()
ap.open_bundle(bid)
ap.wait_text("CAPABILITY_UNAVAILABLE")     # the map reported at build, no stand-in drawn
ap.shot(f"{CAP}/01_fresh.png")
ap.tap("File note (chime)")
ap.wait_text("onError did not fire")
ap.tap("File note with position")
ap.wait_text("LOCATION_UNAVAILABLE")
ap.shot(f"{CAP}/02_asked.png")
print("declared-behaviour: sound performed, position and map reported, nothing drawn in their place")
