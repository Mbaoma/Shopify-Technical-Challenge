# Shopify Technical Challenge

## Description
This project is set to build an inventory tracking web application for a logistics company. The web application allows customers to:
- Create inventory items
- Edit inventory items
- Delete inventory items
- View a list of inventory items

Also,
- Each inventory item is associated with a city where the item is stored. There are only 5 possible cities used for storage.
- The list of items in the inventory includes the city and a simple textual description of the current weather.

Lastly, customers can sort items by tags.

## Setting Up
-   Ensure you have [Python](www.python.org) installed on your PC.
  
-   Run the following command in the terminal to create a virtual environment: 
```
$ python -m venv venv
```

-   Run the following command in the terminal to activate your virtual environment. The command is different for a linux machine, so use either of the below command:
 ``` 
 $ source venv/Scripts/activate
 $ source venv/bin/activate
```

-   Run the following command in the terminal to install the dependencies in the requirements.txt file. You might need to update pip also:
``` 
$ pip install --upgrade pip
$ pip install -r requirements.txt
```



## Test the Endpoints

-   Run ``` python app.py ``` to start the server.

-   Test the endpoints
POST request: http://127.0.0.1:5000/data/create
<img width="279" alt="image" src="https://user-images.githubusercontent.com/49791498/168648042-8cd3a85b-8d75-4ded-b463-2e9963b2209a.png">

GET request: http://127.0.0.1:5000/data
<img width="279" alt="image" src="https://user-images.githubusercontent.com/49791498/168650401-623f0e80-46c1-4efa-9210-b206db85fe97.png">

GET request: http://127.0.0.1:5000/data/<string:name> (single item)
<img width="279" alt="image" src="https://user-images.githubusercontent.com/49791498/168654547-ab2d3396-0d12-474c-b08a-d543bd87ffae.png">

DELETE requrst: http://127.0.0.1:5000/data/<string:name>/delete
<img width="342" alt="image" src="https://user-images.githubusercontent.com/49791498/168654755-4dd498d4-04e3-4239-99d2-ebe608a66e2b.png">

<img width="342" alt="image" src="https://user-images.githubusercontent.com/49791498/168654793-7f5a1b81-9f66-493b-a8e1-41ba0b06e717.png">
