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

- Create your database models. Open a terminal in this directory and run:
```
$ db.create_all()
```


## Test the Endpoints

-   Run ``` python app.py ``` to start the server.

-   Test the endpoints using [Postman](https://app.getpostman.com/join-team?invite_code=d692faed7a5db8bdd2b7dadfd55a34cb&ws=85327001-f59e-4ad1-be89-49d0afa6456f)

    -   Steps
  
        1. Create items to be added to inventory
            http://127.0.0.1:5000/item/<name> [POST]

        2. Edit items in the inventory
            /item/name [PUT]
        
        3.  Delete items in the inventory
            /item/name [DELETE]
        
        4. View a list of items in the inventory

            /items [GET]

