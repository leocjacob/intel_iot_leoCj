# intel_iot_leoCj
Intelligent IOT
# Project ICU

Project ICU is a smart iot device which can see and identify the physical world with the help of Intel Edison Board and cloud connectivity.This project aims to help blind people to read and identify text,label,landmarks,face,emotions and more from the real world !!
### Version
0.0.1

### Tech

Project ICU uses a number of latest technologies to work properly:

* [Intel Edison Board] - To view the real world and communicate with the blind man!
* [Google Cloud Service & API] - for object detection and manipulation

### Installation

You need a latest python version which (includes pip) and a windows pc recommend :
```sh
* Download the project 'intel_iot_leoCj.zip' and extract it to the desktop.
```
The project folder 'intel_iot_leoCj' should contain following files
* v_d_f.json
* serviceaccount.json
* icu. py
* folder named 'images' which includes two pictures '1.jpg' & '2.jpg'
```sh
Open command prompt in administrator mode
```
Following steps are very important !
```sh
cd C:\Users\username\Desktop\intel_iot_leoCj
````
```sh
pip install --upgrade google-api-python-client
```
Help link : https://developers.google.com/api-client-library/python/start/installation

```sh
set GOOGLE_APPLICATION_CREDENTIALS=serviceaccount.json
```
If the above command does'nt workout,try to set environmental variable GOOGLE_APPLICATION_CREDENTIALS to the path of 'serviceaccount.json'

```sh
python icu.py images/1.jpg
```
wait for some time... be patient :)

Final result here...
```sh
Found label: _____ for images/1.jpg
```
