# Shopify Technical Challenge

## Description
This project is set to build an inventory tracking web application for a logistics company. The web application allows customers to:
- Create inventory items
- Edit inventory items
- Delete inventory items
- View a list of inventory items

Also,
- Each inventory item is associated with a city where the item is stored. 

Lastly, customers can search for items by tags.

## Setting Up
-   Ensure you have [Python](www.python.org) installed on your PC.
  
-   Run the following command in the terminal to create a virtual environment: 
```
$ python3 -m venv venv
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

-   Run ``` python3 app.py ``` to start the server.

-   Test the endpoints

POST request: http://127.0.0.1:5000/data/create

<img width="634" alt="image" src="https://user-images.githubusercontent.com/49791498/168780479-96902e08-206d-433c-817c-2cc8f143eb49.png">


GET request: http://127.0.0.1:5000/data
<img width="634" alt="image" src="https://user-images.githubusercontent.com/49791498/168780663-7a830624-b7ea-4d88-a1b9-452131c3f22f.png">


GET request: http://127.0.0.1:5000/data/<string:name> (single item)

<img width="279" alt="image" src="https://user-images.githubusercontent.com/49791498/168654547-ab2d3396-0d12-474c-b08a-d543bd87ffae.png">

GET request: http://127.0.0.1:5000/data/tag/<string:tag>(search for items by tag)
<img width="342" alt="image" src="https://user-images.githubusercontent.com/49791498/168660368-c4fc4955-80f4-4601-b3c7-e0b51efa1ef0.png">

DELETE request: http://127.0.0.1:5000/data/<string:name>/delete

<img width="342" alt="image" src="https://user-images.githubusercontent.com/49791498/168654755-4dd498d4-04e3-4239-99d2-ebe608a66e2b.png">

Clicking 'yes' will delete the item and return a page displaying the available items in the inventory
<img width="342" alt="image" src="https://user-images.githubusercontent.com/49791498/168654793-7f5a1b81-9f66-493b-a8e1-41ba0b06e717.png">
