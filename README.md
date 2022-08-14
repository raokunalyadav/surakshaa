
# Surakshaa - Django Based Web App For Women Safety

We all know that indian citizens have to face some problems, and one of the major problem in india is related to women safety.

We are trying and making effort for women so that the problems they face can be reduced a little bit. For this we have come up with a web application called "Surakshaa"

Our Website:- https://surakshaa.herokuapp.com

# What This Web App Does?

This website asks data from woman (her name and multiple contact numbers of her relative in case of emergency.) and stores it in cookies so that it does not needs to be entered again and again whenever she opens the web page.

Woman user should allow location, bookmark the webpage and also place it's shortcut on home screen of phone.

Whenever she feels unsafe or she feels someone is going to harass her, she just needs to open our webpage and click on "I'm not safe" Button. As soon as she clicks that button, an SMS with her current location coordinates (latitude and longitude) will be sent to all her relatives (stored contact numbers). This is automated through SMS gateway API using Python Django.
## Usage/Examples
1. Keep your phone location (GPS) on.
2. Open our website https://surakshaa.herokuapp.com
3. Allow location
.


![App Screenshot](https://i.imgur.com/CkdHUwN.jpeg)

4. Fill your Data:
Name and Relative's mobile numbers in case of emergency

Numbers should be without country code and each number in each seperate line


![App Screenshot](https://i.imgur.com/FMWRRXb.png)

5. Click on SAVE blue-colored button.

6. Also, Bookmark our website and place it's shortcut in your home screen of device.

![App Screenshot](https://i.imgur.com/LGcC5Ed.jpg)

7. Now all set, whenever you feel in trouble, you need to open our website and click on I'm NOT SAFE red-colored button.

8. SMS Will be sent to all numbers provided by you. SMS will contain your latitude and longitude.

9. Your relatives should search that latitude and longitude value in google maps like shown below, and they can reach to you.


![App Screenshot](https://i.imgur.com/YsRSYQA.jpg)
##
![App Screenshot](https://i.imgur.com/w4OiDww.jpg)

##


## Authors

Kunal Yadav - [@raokunalyadav](https://www.github.com/raokunalyadav) - Backend (Django, JavaScript)

Sathvik N.G. - [@sathvik-ng-07](https://www.github.com/sathvik-ng-07) - Frontend (HTML, CSS)

Aizaz Ahmed



