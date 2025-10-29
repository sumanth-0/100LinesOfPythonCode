import sys
from ctypes import POINTER, cast
from typing import Any

# Optional runtime imports. Editors may show 'could not be resolved' if the
# workspace Python interpreter isn't set to the project's venv. Use guarded
# imports and type ignores so the file still loads in editors without errors.
try:
    from comtypes import CLSCTX_ALL, CoInitialize  # type: ignore
except Exception:  # pragma: no cover - editor/CI environments may not have comtypes
    CLSCTX_ALL = None  # type: ignore
    def CoInitialize() -> None:  # type: ignore
        return

try:
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume  # type: ignore
except Exception:  # pragma: no cover
    AudioUtilities: Any = None  # type: ignore
    IAudioEndpointVolume: Any = None  # type: ignore

def get_volume_interface():
    CoInitialize()  # Initialize COM
    # If editor couldn't resolve imports, make the runtime failure clearer
    if AudioUtilities is None or IAudioEndpointVolume is None:
        print("Missing dependencies: please install 'pycaw' and 'comtypes' in the Python environment used by your editor/runtime.")
        sys.exit(1)
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        if not interface:
            raise Exception("Could not get audio interface")
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        if not volume:
            raise Exception("Could not get volume control")
        return volume
    except Exception as e:
        print(f"Error accessing audio device: {e}")
        print("Make sure you have audio devices installed and Windows Audio service is running")
        sys.exit(1)

def get_volume():
    v = get_volume_interface()
    level = int(v.GetMasterVolumeLevelScalar() * 100)
    mute = v.GetMute()
    print(f"Volume: {level}% | Muted: {bool(mute)}")

def set_volume(level):
    v = get_volume_interface()
    level = max(0, min(100, int(level)))
    v.SetMasterVolumeLevelScalar(level / 100, None)
    print(f"Volume set to {level}%")

def change_volume(delta):
    v = get_volume_interface()
    current = int(v.GetMasterVolumeLevelScalar() * 100)
    new = max(0, min(100, current + delta))
    v.SetMasterVolumeLevelScalar(new / 100, None)
    print(f"Volume changed to {new}%")

def mute_volume():
    v = get_volume_interface()
    v.SetMute(1, None)
    print("Muted")

def unmute_volume():
    v = get_volume_interface()
    v.SetMute(0, None)
    print("Unmuted")

def toggle_mute():
    v = get_volume_interface()
    v.SetMute(0 if v.GetMute() else 1, None)
    print("Mute toggled")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python volume_win.py [up/down/set/mute/unmute/toggle/get] [value]")
        sys.exit(1)

    cmd = sys.argv[1].lower()
    val = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    if cmd in ("up", "increase"):
        change_volume(abs(val))
    elif cmd in ("down", "decrease"):
        change_volume(-abs(val))
    elif cmd == "set":
        set_volume(val)
    elif cmd == "mute":
        mute_volume()
    elif cmd == "unmute":
        unmute_volume()
    elif cmd == "toggle":
        toggle_mute()
    elif cmd == "get":
        get_volume()
    else:
        print("Invalid command")
