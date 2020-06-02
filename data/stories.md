## happy path
* greet
  - utter_how_can_i_help
* mood_great
  - utter_happy


## hospital search City Happy 
* greet 
  - find_facility_types
* search_provider{"facility_type":"Private","city":"Lucknow"}
  - find_hospitals_name
  - form{"name":"find_hospitals_name"}
  - form{"name":null}
* inform{"facility_id" : 1}
  - find_hospital_address
  - utter_address
* thanks
  - utter_goodbye

## hospital search state city Happy
* greet
  - find_facility_types
* search_provider{"facility_type":"Public","state":"Uttar Pradesh"}
  - utter_ask_city
* search_provider{"city":"Lucknow"}
  - find_hospitals_name
  - form{"name":"find_hospitals_name"}
  - form{"name":null}
* inform{"facility_id": 1}
  - find_hospital_address
  - utter_address
* thanks
  - utter_goodbye

## hospital search city happy
* greet
  - find_facility_types
* search_provider{"city":"Pune"}
  - find_hospitals_name
  - form{"name":"find_hospitals_name"}
  - form{"name":null}
* inform{"facility_id": 1}
  - find_hospital_address
  - utter_address
* thanks
  - utter_goodbye

## hospital search state facility city happy
* greet
  - find_facility_types
* search_provider{"state": "Kerala"}
  - utter_ask_city
* search_provider{"city": "Pune"}
  - find_hospitals_name
  - form{"name":"find_hospitals_name"}
  - form{"name":null}
* inform{"facility_id": 1}
  - find_hospital_address
  - utter_address
* thanks
  - utter_goodbye

## happy path multi request
* greet
  - find_facility_types
* search_provider{"facility_type":"Private","city":"Lucknow"}
  - find_hospitals_name
  - form{"name":"find_hospitals_name"}
  - form{"name":null}
* inform{"facility_id" : 1}
  - find_hospital_address
  - utter_address
* search_provider{"facility_type":"Private","city":"Lucknow"}
  - find_hospitals_name
  - form{"name":"find_hospitals_name"}
  - form{"name":null}
* inform{"facility_id" : 1}
  - find_hospital_address
  - utter_address
* thanks
  - utter_goodbye


## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
