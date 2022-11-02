from command import *
from remote_control import remote
from appliances import *
def main():
    r = remote()
    light_1 = light()
    light_1_on = Light_on_command(light_1)
    light_1_off = Light_off_command(light_1)

    ac_1 = ac()
    ac_1_on = AC_on_command(ac_1)
    ac_1_off = AC_off_command(ac_1)

    tv_1 = tv()
    tv_1_on = tv_on_command(tv_1)
    tv_1_off = tv_off_command(tv_1)

    lightNac_on = bothAcAndLightOn(ac_1, light_1)
    lightNac_off = bothAcAndLightOff(ac_1, light_1)

    allon = allOn(light_1, ac_1, tv_1)
    alloff = allOff(light_1, ac_1, tv_1)
    r.set_command(0, light_1_on, light_1_off)
    r.set_command(1, ac_1_on, ac_1_off)
    r.set_command(2, tv_1_on, tv_1_off)
    r.set_command(3, lightNac_on, lightNac_off)
    r.set_command(4, allon, alloff)

    r.on_click(0)
    r.on_click(1)
    r.on_click(2)
    r.on_click(3)
    r.on_click(4)
    r.undo_but.undo()
if __name__ == '__main__':
    main()