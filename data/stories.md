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

<!-- ## hospital search state city Happy
* greet
  - find_facility_types
* search_provider{"facility_type":"Public","state":"Uttar Pradesh"}
  - utter_ask_city
* search_provider{"city":"Lucknow"}
  - action_facility_search
* thanks
  - utter_goodbye

## hospital search 
* greet
  - find_facility_types
* search_provider{"facility_type":"Public"}
  - utter_ask_location
* inform{"city":"Kanpur"}
  - action_facility_search
* thanks
  - utter_goodbye

## hospital search city happy
* greet
  - find_facility_types
* search_provider{"city":"Pune"}
  - find_facility_types
* search_provider{"facility_type": "Public"}
  - action_facility_search
* thanks
  - utter_goodbye

## hospital search state facility city happy
* greet
  - find_facility_types
* search_provider{"state": "Kerala"}
  - utter_ask_city
* search_provider{"city": "Pune"}
  - utter_ask_facility
* search_provider{"facility_type": "Private"}
  - action_facility_search

## hospital search facility city happy
* greet 
  - find_facility_types
* search_provider{"facility_type": "Public"}
  - utter_ask_location
* search_provider{"city":"Pune"}
  - action_facility_search -->


## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot