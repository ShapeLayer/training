/* 
  Refer BCM2835 ARM Peripherals 6 section
  + Raspberry Pi Bare metal Tutorial
    Part 3. GPIO https://www.youtube.com/watch?v=36hk_Qov5Uo
*/

#include "gpio.h"

void gpio_pin_set_func(u8 pinNumber, GpioFunc func) {
  u8 bitStart = (pinNumber * 3) % 30;
  u8 reg = pinNumber / 10;

  u32 selector = REGS_GPIO->func_select[reg];
  selector &= ~(7 << bitStart);
  selector |= (func << bitStart);

  REGS_GPIO->func_select[reg] = selector;
}

void gpio_pin_enable(u8 pinNumber) {
  REGS_GPIO->pupd_enable = 0;
  delay(150);
  REGS_GPIO->pupd_enable_clocks[pinNumber / 32] = 1 << (pinNumber % 32);
  delay(150);
  REGS_GPIO->pupd_enable = 0;
  REGS_GPIO->pupd_enable_clocks[pinNumber / 32] = 0;
}
