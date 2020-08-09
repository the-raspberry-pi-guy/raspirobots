# Learn Robotics with Raspberry Pi - Code Repository

![alt text](https://www.theraspberrypiguy.com/wp-content/uploads/2018/12/blank_3dbook_slider.png)

## Purchase Book: https://mybook.to/raspirobots (Amazon Worldwide Link)

## Book Description

Learn Robotics with Raspberry Pi will take you from inexperienced maker to robot builder. You’ll start off building a two-wheeled robot powered by a Raspberry Pi minicomputer and then program it using Python, the world’s most popular programming language. Gradually, you’ll improve your robot by adding increasingly advanced functionality until it can follow lines, avoid obstacles, and even recognize objects of a certain size and color using computer vision.

Learn how to:

* Control your robot remotely using only a Wii remote
* Teach your robot to use sensors to avoid obstacles
* Program your robot to follow a line autonomously
* Customize your robot with LEDs and speakers to make it light up and play sounds
* See what your robot sees with a Pi Camera

As you work through the book, you’ll learn fundamental electronics skills like how to wire up parts, use resistors and regulators, and determine how much power your robot needs. By the end, you’ll have learned the basics of coding in Python and know enough about working with hardware like LEDs, motors, and sensors to expand your creations beyond simple robots.

Requirements: Raspberry Pi and Python 3

## Author Bio

Matt Timmons-Brown runs the world’s most-popular Raspberry Pi YouTube channel, “The Raspberry Pi Guy” (www.youtube.com/theraspberrypiguy) with over 6 million views. Originally from Cambridge, UK, Matt is a Computer Science student at the University of Edinburgh and has worked for Amazon Robotics and Huawei. He is a Robotics Research Intern in the School of Informatics, Edinburgh.

## This repository?

This repository stores all of the code and resources used in the book. It will be updated when necessary and if the code requires changes.

## How to download?

You can download this code directly onto your Raspberry Pi with the terminal command:

`git clone https://github.com/the-raspberry-pi-guy/raspirobots`

Alternatively you can download this code locally by clicking on the "Clone or download" button at the top of the page. You will also find a zipped version of this code on the No Starch Press product page: https://nostarch.com/raspirobots

## Requirements/Recommendations

This book is compatible with all models of Raspberry Pi.

Recommended Pi Model: Raspberry Pi 3B+/3A+ or Pi Zero W (more efficient and lower power consumption)

## Erratum

If you stumble upon any errors or incorrect parts of my book, please submit a PR to document them in this section, or send me an email for me to investigate into (theraspberrypiguy [at] gmail.com). Below is a list of known minor errata (page numbers from physical book). These have been fixed in the second reprint of the book (Aug 2020):
* Chapter 5, p115 - In the terminal prompt where I show the outputted distance metric from the HC-SR04 sensor, the command shown to have been run is ```python3 button.py``` whereas it should be the same as the previous page: ```python3 distance_test.py```
* Chapter 6, p140 - The ```wget``` links to the raw audio files are slightly different due to reorganisation of this Git repo. To download the audio files to your Pi, the commands should be:
    * ```wget https://github.com/the-raspberry-pi-guy/raspirobots/tree/master/Chapter%206%20-%20Adding%20RGB%20LEDs%20and%20Sound/sounds/beep.wav```
    * ```wget https://github.com/the-raspberry-pi-guy/raspirobots/tree/master/Chapter%206%20-%20Adding%20RGB%20LEDs%20and%20Sound/sounds/horn.wav```
* Appendix: Resistor Guide, p203 - The example resistor calculation should result in a value of 560,000Ω (560kΩ), not 56,000Ω (56kΩ)

Thanks to Minoosh Heidari & Daryoush Alipour for spotting these errors.

## Parts List

The following is an exhaustive list of the parts that I use in the book, Chapter by Chapter. I have tried to make things as cheap and accessible as possible. Please note that all parts are not required to follow the book, you can mix and match as you please, and do the Chapters that you feel would be of most interest!

All of the electronic components in the book can be purchased from online shops like eBay, or dedicated online electronics stores such as Adafruit, Pimoroni, The Pi Hut, CPC Farnell, and RS Components. This list is by no means exhaustive and you may find cheaper, closer online retailers in your own country. You might even be fortunate enough to have a local electronics hardware store where you can grab your stuff! For this list, I have mixed and matched - let me know if any of the listings are unavailable and I will seek to update.

### Chapter 1: Getting Up and Running
|Part   |UK Link   |USA Link   |
|---    |---       |---        |
|Raspberry Pi 3 Model B+| https://thepihut.com/products/raspberry-pi-3-model-b-plus | https://www.adafruit.com/product/3775 | 
|8GB+ microSD card| https://thepihut.com/products/noobs-preinstalled-sd-card | https://www.adafruit.com/product/1294 |
|HDMI cable/USB keyboard mouse  |  https://thepihut.com/products/official-raspberry-pi-hdmi-cable | https://www.adafruit.com/product/608 |
|5V micro USB power adapter | https://thepihut.com/products/official-raspberry-pi-universal-power-supply | https://www.adafruit.com/product/1995 |

### Chapter 2: Electronics Basics
|Part   |UK Link   |USA Link   |
|---    |---       |---        |
|400 point breadboard| https://thepihut.com/products/raspberry-pi-breadboard-half-size | https://www.adafruit.com/product/4539 | 
|1x LED and appropriate resistor (for basic HW project)| https://thepihut.com/products/ultra-bright-led-5mm-white-10-pack | https://www.adafruit.com/product/754 |
|Jumper wires (an assortment)  |  https://thepihut.com/pages/search-results?q=jumper%20wire&page_num=5 | https://www.adafruit.com/?q=jumper%20wires |
|1x Momentary push button | https://thepihut.com/products/mini-push-button-switch-5-pcs | https://www.adafruit.com/product/367 |

### Chapter 3: Building Your Robot
|Part   |UK Link   |USA Link   |
|---    |---       |---        |
|Robot chassis (make out of what you wish - more details in the book!)| Lego, cardboard boxes | Plastic, wood etc! |
|2x brushed 5V to 9V DC motors with tires | https://thepihut.com/products/dc-motor-3v-inc-gearbox-wheel-and-tyre | https://www.adafruit.com/product/3216 |
|6xAA battery box  | https://thepihut.com/products/panel-mount-battery-box-6x-aa-9v | https://ebay.to/3cGDS70 |
|6x AA batteries (I recommend rechargeable, but can use disposable) | https://www.amazon.co.uk/s?k=6+rechargeable+battery+aa&ref=nb_sb_noss_1 | https://www.amazon.com/s?k=6+rechargeable+battery+aa&ref=nb_sb_noss_1 |
|LM2596 buck converter module | https://bit.ly/2XFMaru | https://ebay.to/2Uf0cyw |
|L293D motor driver chip | https://bit.ly/3f0OD5Z | https://ebay.to/3eS3IGE |

### Chapter 4: Making Your Robot Move
|Part   |UK Link   |USA Link   |
|---    |---       |---        |
|Official Nintendo Wiimote (Second-hand works great! Just not 3rd party)| https://bit.ly/3dHgpE9 | https://ebay.to/2XIubkB |

### Chapter 5: Obstacle Avoidance
|Part   |UK Link   |USA Link   |
|---    |---       |---        |
|HC-SR04 Ultrasonic Distance Sensor | https://thepihut.com/products/ultrasonic-distance-sensor-hcsr04 | https://www.adafruit.com/product/3942 |
|1kΩ resistor and 2kΩ resistor (invest in a resistor assortment!) | https://bit.ly/379ajtR | https://ebay.to/2MDdh0h|

### Chapter 6: Adding RGB LEDs and Sound
|Part   |UK Link   |USA Link   |
|---    |---       |---        |
|NeoPixel stick with headers | https://thepihut.com/products/adafruit-neopixel-stick-8-x-5050-rgb-led-with-integrated-drivers | https://www.adafruit.com/product/1426 |
|Small 3.5mm speaker | https://bit.ly/2APaJcw | https://ebay.to/2MEkahC|

### Chapter 7: Line Following
|Part   |UK Link   |USA Link   |
|---    |---       |---        |
|2x TCRT5000-based infrared line-following modules | https://bit.ly/2Y6Qors | https://ebay.to/2MxM8M8 |

### Chapter 8: Computer Vision: Follow a Colored Ball
|Part   |UK Link   |USA Link   |
|---    |---       |---        |
|Official Raspberry Pi camera module | https://thepihut.com/products/raspberry-pi-camera-module | https://www.adafruit.com/product/3099 |

You also may find these tools/materials handy along the way:
* Variety of screwdrivers
* Hot-glue gun
* Multimeter
* Soldering iron
* Wire stripper
* Sticky tack/Velco/3M Dual Lock
