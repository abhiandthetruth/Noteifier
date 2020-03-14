# Noteifier
A django app to write notes built for learning purposes. 

## End User Instruction

The app is hosted at http://noteifier.herokuapp.com/. Register and start using it now!

### Features

* Register/Login to personalize notes
* Add/Delete Topics to group your notes
* Add/Edit/Delete notes taken
* Markdown Support! Make your notes more expressive

### Screenshots
Screenshots are inside the images directory. Here are a couple of them!

![image](images/image3.png)

![image](images/image4.png)

## Developer Instruction

Feel free to fork the repo and develop an app taking this as the base.

### Instructions for local deployment

Read the Note below first befre attempting to setup.

* Fork the repo into your account.
* Clone the repo present in your account into your local machine.
* Navigate to the folder `Noteifier/` or whatever you named your fork.
* Create a virtual environment `python -m venv env`. If you do not have venv installed in your system install it using `pip install venv`.
* Activate the virtual environment `source env/bin/activate` in linux/macOS `.\env\Scripts\activate` in Windows.
* Install the requirements `pip install -r requirements.txt`.
* Migrate the database. `python manage.py migrate`
* Collect Static files `python manage.py collectstatic`.
* Run the server `python manage.py runserver`. Choose a different port if `8000` is already occupied.
* Visit `localhost:8000` to view the app. If you used a different port no. use that instead.
* You can now tweak the source code to your choice.

---
**NOTE**

If you use `python3` instead of  `python`, use that only for creating the virtual environment. Inside the virtual environment use `python` anyways, since the `python` command inside a virtual environment points to the version of python with which the environment was created. Same for `pip` and `pip3`.

---
