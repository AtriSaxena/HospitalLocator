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

## New Story

    - find_facility_types
* inform{"facility_type":"Public"}
    - slot{"facility_type":"Public"}
    - utter_ask_city
* search_provider{"city":"Kochi"}
    - slot{"city":"Kochi"}
    - find_hospitals_name
    - form{"name":"find_hospitals_name"}
    - slot{"city":"Kochi"}
    - slot{"facility_type":"Public"}
    - slot{"city":"Kochi"}
    - form{"name":null}
    - slot{"requested_slot":null}
* inform{"facility_id":"699"}
    - slot{"facility_id":"699"}
    - find_hospital_address
    - slot{"facility_address":"ofAmrita Institute Of Medical SciencesisPonekkara Post, Kochi, Kerala, Phone- (484 ) 2801234, 285 1234, 400 1234, 681234, Fax: 0091 (0) 4842802020"}
    - utter_address

## New Story

* inform{"facility_type":"Private"}
    - slot{"facility_type":"Private"}
    - utter_ask_city
* search_provider{"city":"Pune"}
    - slot{"city":"Pune"}
    - find_hospitals_name
    - form{"name":"find_hospitals_name"}
    - slot{"city":"Pune"}
    - slot{"facility_type":"Private"}
    - slot{"city":"Pune"}
    - form{"name":null}
    - slot{"requested_slot":null}
* inform{"facility_id":"784"}
    - slot{"facility_id":"784"}
    - find_hospital_address
    - slot{"facility_address":"ofColumbia Asia Hospital, Puneis22/2A, Near Nyati Empire,Kharadi Bypass Road, Kharadi,Pune, Maharashtra, Phone- (020) 71290222"}
    - utter_address
* thanks
    - utter_goodbye

## New Story

* out_of_scope
    - find_facility_types
* inform{"facility_type":"Public"}
    - slot{"facility_type":"Public"}
    - utter_ask_city
* search_provider{"city":"Meerut"}
    - slot{"city":"Meerut"}
    - find_hospitals_name
    - form{"name":"find_hospitals_name"}
    - slot{"city":"Meerut"}
    - slot{"facility_type":"Public"}
    - slot{"city":"Meerut"}
    - form{"name":null}
    - slot{"requested_slot":null}
