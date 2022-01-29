def right():
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED1, 0, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED2, 100, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED3, 0, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED4, 50, 67)
def back():
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED1, 100, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED2, 50, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED3, 100, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED4, 50, 67)
def front():
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED1, 0, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED2, 50, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED3, 0, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED4, 50, 67)
def left():
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED1, 0, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED2, 50, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED3, 0, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED4, 100, 67)
def stop():
    PCA9685.reset(67)
PCA9685.init(67, 0)
distance = 0
strip = neopixel.create(DigitalPin.P5, 18, NeoPixelMode.RGB)

def on_forever():
    global distance
    distance = sonar.ping(DigitalPin.P14, DigitalPin.P15, PingUnit.CENTIMETERS)
    serial.write_number(distance)
    serial.write_line("")
    if distance >= 15 and distance <= 30:
        front()
        strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
    if distance <= 10:
        back()
        strip.show_color(neopixel.colors(NeoPixelColors.PURPLE))
    if distance > 10 and distance < 15 or distance > 30:
        stop()
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
    basic.pause(100)
basic.forever(on_forever)
