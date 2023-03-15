import pymem
import win32api
import time
import keyboard
import pymem.process

def bhop() -> None:
    LOCAL_PLAYER = 0xDEA964
    FORCE_JUMP = 0x52BBC7C
    HEALTH = 0x100
    FLAGS = 0x104

    pm = pymem.Pymem("csgo.exe")

    for module in list(pm.list_modules()):
        if module.name == "client.dll":
            client = module.lpBaseOfDll
    
    while True:
        time.sleep(0.01)

        if not win32api.GetAsyncKeyState(0x20):
            continue

        local_player: int = pm.read_uint(client + LOCAL_PLAYER)

        if not local_player:
            continue

        if not pm.read_int(local_player + HEALTH):
            continue

        if pm.read_uint(local_player + FLAGS) & 1 << 0:
            pm.write_uint(client + FORCE_JUMP, 6)
            time.sleep(0.01)
            pm.write_uint(client + FORCE_JUMP, 4)

if __name__ == "__main__":
    bhop()