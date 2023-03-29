# pico-motion-vison
 A raspberry pico demonstration of human-robot interaction

## Parts List
- Microcontroller compatible with MicroPython (we used an RP2040 Pico)
- Two 8x8 LED Matrix with a backpack search for MAX7219 or HT16K33 driver chip
- Jumper Wire
- Pumpkin (depends on how close halloween is)

## How Does It Work
<p>
A body will emit thermal electromagnetic radiation, this is picked up by the plastic lens of a HC-SR501 and a pyroelectric sensor translates this into an electric current. The PIR will look for any change in the current, hence a change in the thermal electromagnetic radiation and set it's output pin to high if there is a change.
</p>
<p>
If a body/heat source sets this off and remains perfectly still it will measure this as the normal state after a certain time (configurable via a dial). If the body moves there is a change and the pin is held high again, which is then used to manupilate the movement of the eyes in the 8x8 matrix. 
</p>
