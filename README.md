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

<img width="634" alt="image" src="https://user-images.githubusercontent.com/49791498/168786496-4c3e7a99-cd87-4b7c-baeb-794a273b176e.png">


GET request: http://127.0.0.1:5000/data/tag/<string:tag>(search for items by tag)

<img width="634" alt="image" src="https://user-images.githubusercontent.com/49791498/168786273-99230332-4aad-43ea-9118-020953f526ef.png">

DELETE request: http://127.0.0.1:5000/data/<string:name>/delete

Clicking 'yes' will delete the item and return a page displaying the available items in the inventory

<img width="634" alt="image" src="https://user-images.githubusercontent.com/49791498/168787444-c051b49f-321f-424b-9182-71a1e6109e3e.png">