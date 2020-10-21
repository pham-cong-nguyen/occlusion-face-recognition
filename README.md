#### Benchmarking 
|Dataset| Identify Acuracy|
|:---:|:---:|
| LFW| 99.46%|
| ARface-scarf (protocol2)| 99.17%|
| ARface-scarf (protocol1)| 100%|
| ICPR-45 (protocol2)| 85.1%|
| ICPR-30 (protocol2)| 91.1%|
| ICPR-45 (protocol1)| 89.7%|
| ICPR-30 (protocol1)| 94.0%|

> protocol1: 
> - Gallery set: more than 1 image per identity. With ICPR test use (+-15) image
> - Probe set: all of other image is used to indentify (not verify) 

> protocol2: 
> - Gallery set: 1 image per identity. With ARface-scarf test, colected gallery set is used.
> - Probe set: all of other image is used to indentify (not verify) 
