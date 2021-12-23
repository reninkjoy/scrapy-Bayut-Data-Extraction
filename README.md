# scrapy-Bayut-Data-Extraction

## General info
Data extraction from websites using the Scrapy Tool.
The full code written in python.

## bayuts.py
bayuts.py is the main code to be run for the data extraction from the website["https://www.bayut.com/to-rent/property/dubai/"].
We fetch the URL and extract the information save it as JSON file.

## items.py
Created Field
```
    property_id
    purpose 
    type
    added_on
    furnishing
    price
    location
    bed_bath_size
    permit_number
    agent_name
    image_url
    breadcrumbs
    amenities
    description
```   
## Directory 
``` 
├── scrapy-Bayut-Data-Extraction-main
│   ├── bayut
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   ├── settings.py
│   │   └── spiders
│   │       ├── bayuts.py
│   │       └── __init__.py
│   ├── final.py
│   ├── output.json
│   └── README.md
└────── scrapy.cfg

``` 
## Setup
```
$ python3 -m pip install --user virtualenv
$ python3 -m venv env
$ source env/bin/activate
$ python3 -m pip install --user sceapy
```    
## Working
To run this project, install it locally using scrapy:

```
$ scrapy crawl bayuts -O output.json
$ python3 final.py  
```
## output.json
```
{
        "property_id": "Bayut - 646-Ap-R-6578",
        "purpose": "For Rent",
        "type": "Apartment",
        "added_on": "December 9, 2021",
        "furnishing": "Furnished",
        "price": {
            "currency": "AED",
            "amount": "105,000"
        },
        "location": "Millennium Binghatti Residences, Business Bay, Dubai",
        "bed_bath_size": {
            "bedrooms": "1 Bed",
            "bathrooms": "2 Baths",
            "size": "866 sqft"
        },
        "permit_number": "71158750999",
        "agent_name": "Ghulam Hanif",
        "image_url": "https://images.bayut.com/thumbnails/173137475-800x600.jpeg",
        "breadcrumbs": "Apartments for Rent in Dubai>Business Bay>Millennium Binghatti Residences Apartments>Bayut - 646-Ap-R-6578",
        "amenities": [
            "Furnished"
        ],
        "description": "apartment is available for rent. The fine finishing of the apartment along with a balcony is located in Business Bay and it is exactly what you are looking for: - -Brand New 1BR 19th Floor Canal View For Rent -Large Balcony -Size866 sq. ft -1BHK Apartment Gymnasium , Swimming pool , 24-hour security / CCTV ,Children play area ,Closer to Dubai Mall Closer to heart of Dubai , Walking distance Bus stop , Near by Metro , Closer to Schools , Central air conditioning ,Covered parking Gymnasium Intercom , On mid floor ,Pets allowed , Shared swimming pool , Steam room , View of sea/water , 24 hours Maintenance , Bus services , Children's play area , Clubhouse , Fitness Center , Mosque , Public park , Public parking , Public transport, Restaurants , Shops , Walking Trails Surrounded by Supermarket Near Hospital Near Bus Stop Near Hotels Near Restaurants Near Metro This Tower is just way from Dubai Mall and Burj khalifa. Easy excess to Al khail Road abd Sheik Zaid Road.  Millennium Binghatti Residences draws its inspiration from the timeless elegance of the deluxe Millennium Hotels & Resorts. The tower offers a number of premium Hotel-inspired means of comfort and recreational amenities ensuring excellence, comfort, and prestige. As the building sits directly on the Dubai Water Canal waterfront, the balconies provide direct views of the Dubai Water Canal and Dubai Skyline  is a trusted, well established real estate brokerage firm. Whether you're interested in Residential, Commercial or Investment property, our team of professionals will help you throughout the entire process. We offer a free consultation for all your property needs. With an overall leasing rate of 95% in the Tower projects, and an expansive presence in the region. "
    },
```
