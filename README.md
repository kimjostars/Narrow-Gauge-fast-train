# Narrow Gauge Fast Train Set
[English](./README.md) | [한국어](./README.ko.md)

Narrow Gauge Fast Train Set is an OpenTTD NewGRF that adds fictional 1067 mm gauge trains capable of speeds over 200 km/h, along with other rolling stock.
You can download it from the **[Github release page](https://github.com/kimjostars/Narrow-Gauge-fast-train/releases)**.
It is recommended to use this set together with **[JP+ Track](https://github.com/OpenTTD-JPplus/JPplusTracks)** when applying it to the game.
## Development
### How to Build
To build this NewGRF, you need [NML](https://github.com/OpenTTD/nml) (>= 0.9.0) and **Python 3**.
Merge files: `build.py --entry src/{main file}.pnml --merge {project name}/{main file}.nml`
Compile: `nmlc -l ./lang/ ./{main file}.nml`
### Translation
The default language of this set is Korean.
If you would like to translate it into another language, please open a Pull Request on this GitHub project.
If you are not familiar with creating a Pull Request, you may also submit it via Issues. Please translate the following file:
* **[src/lang/korean.lng](https://github.com/kimjostars/Narrow-Gauge-fast-train/blob/main/src/lang/korean.lng)** : Korean
Translations are always welcome.
### Contributors
code : kimjostars, irice7350

graghic : kimjostars, raeun_cos 
## License
This NewGRF is licensed under the **[Creative Commons Attribution-NonCommercial-ShareAlike 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)** (CC BY-NC-SA 3.0).

Contributing to this project implies agreement with this license.