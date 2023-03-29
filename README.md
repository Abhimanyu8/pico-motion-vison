# pico-motion-vison
 A pico-based human-robot interaction platform
 
 
<img src="https://user-images.githubusercontent.com/54982599/228587986-6ad4d1ca-18b1-4376-b3a4-323dcc04c5e6.gif" width="400" height="250">


## Parts List
- Microcontroller compatible with MicroPython (I've used an RP2040 Pico)
- Two 8x8 LED Matrix with a backpack search for MAX7219 or HT16K33 driver chip
- Jumper Wire
- Pumpkin (depends on how close halloween is)

## How Does It Work
<p>
A body will emit thermal electromagnetic radiation, this is picked up by the plastic lens of a HC-SR501 and a pyroelectric sensor translates this into an electric current. The PIR will look for any change in the current, hence a change in the thermal electromagnetic radiation and set it's output pin to high if there is a change.
</p>
<p>
If a body/heat source sets this off and remains perfectly still it will measure this as the normal state after a certain time (configurable via a dial). If the body moves there is a change and the pin is held high again, which is then used to manupilate the 8x8 led matrix to track the movements of that body.
</p>

## Setup

### Connect up the following :

- 3v3 from the microcontroller VCC on your matrix
- GND to GND
- GPIO 7 to DIN
- GPIO 5 to CS
- GPIO 6 to CLK

Additionally you will need to connect your 2nd matrix to the 1st (if building full set of eyes). just match up the in and out it's very simple.

- VCC to VCC
- GND to GND
- DOUT to DIN
- CS to CS
- CLK to CLK

I used those pins and SPI 0 but you can change this but will need to change it in the code when you pass the SPI(0) to the max7219_matrix class.

## Gotchas

The plastic that focuses the infra red radiation comes off so you can see the VCC and GND labels.

There is a jumper that needs to be set, this held us up as it was factory set to Single Trigger. We had to move it from 'L' to 'H' to change it to repeat trigger. Made a big difference as before the change the digital out was flipping on and off like crazy.

<img src="https://user-images.githubusercontent.com/54982599/228584192-659a1f08-6603-4d6e-8ad1-143a6fc7e367.jpg" width='500' height='400'>

There are 2 adjustable dials, the center dial adjusts detection range supposedly counter clockwise to increase the range but it seemed to do the opposite on mine.

<img src="https://user-images.githubusercontent.com/54982599/228584667-90c00bb3-d3c8-4b1a-922d-f884d8fe4288.jpg" width='500' height='400'>

The other dial adjusts the timer I wanted this to be as short as possible thus turned fully counter clockwise.

