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

## New Story

* inform{"facility_type":"Public"}
    - slot{"facility_type":"Public"}
    - slot{"facility_type":"Public"}
    - utter_ask_city
* search_provider{"city":"kochi"}
    - slot{"city":"kochi"}
    - slot{"city":"kochi"}
    - find_hospitals_name
    - form{"name":"find_hospitals_name"}
    - slot{"city":"kochi"}
    - slot{"facility_type":"Public"}
    - slot{"city":"kochi"}
    - form{"name":null}
    - slot{"requested_slot":null}
* inform{"facility_id":"701"}
    - slot{"facility_id":"701"}
    - slot{"facility_id":"701"}
    - find_hospital_address
    - slot{"facility_address":" of Sree Narayana Institute Of Medical Science is Chalakka, P.O. North Kuthiyathodu, Ernakulam Dist., Kerala, Phone- (0484) 2573023, 2573060"}
    - utter_address
* creator
    - slot{"facility_type":"Public"}
    - slot{"city":"kochi"}
    - slot{"facility_id":"701"}
    - utter_creator
* greet
    - find_facility_types
* inform{"facility_type":"Private"}
    - slot{"facility_type":"Private"}
    - utter_ask_city
* thanks
    - utter_goodbye

## New Story

* search_provider
    - find_facility_types
* inform{"facility_type":"Private"}
    - slot{"facility_type":"Private"}
    - utter_ask_city
* search_provider{"city":"delhi"}
    - slot{"city":"delhi"}
    - find_hospitals_name
    - form{"name":"find_hospitals_name"}
    - slot{"city":"delhi"}
    - slot{"facility_type":"Private"}
    - slot{"city":"delhi"}
    - form{"name":null}
    - slot{"requested_slot":null}
* inform{"facility_id":"80"}
    - slot{"facility_id":"80"}
    - find_hospital_address
    - slot{"facility_address":" of Action Cancer Hospital is A - 4, Paschim Vihar, Delhi, Phone- (011) 49222220."}
    - utter_address

## New Story

* out_of_scope
    - utter_creator

## New Story

* search_provider{"city":"Lucknow"}
    - slot{"city":"Lucknow"}
    - slot{"city":"Lucknow"}
    - find_facility_types
* inform{"facility_type":"Private"}
    - slot{"facility_type":"Private"}
    - find_hospitals_name
    - form{"name":"find_hospitals_name"}
    - slot{"city":"Lucknow"}
    - slot{"facility_type":"Private"}
    - slot{"facility_type":"Private"}
    - form{"name":null}
    - slot{"requested_slot":null}
* inform{"facility_id":"995"}
    - slot{"facility_id":"995"}
    - find_hospital_address
    - slot{"facility_address":" of Eye-Q Super Speciality Eye Hospitals, Aliganj is B-60, Sector-B, Aliganj, Lucknow, Uttar Pradesh, Phone- (0522) 4024306, 4101710, 2330739"}
    - utter_address

## New Story

* inform{"facility_type":"Public"}
    - slot{"facility_type":"Public"}
    - utter_ask_city
* search_provider{"city":"Pune"}
    - slot{"city":"Pune"}
    - find_hospitals_name
    - form{"name":"find_hospitals_name"}
    - slot{"city":"Pune"}
    - slot{"facility_type":"Public"}
    - slot{"city":"Pune"}
    - form{"name":null}
    - slot{"requested_slot":null}
* thanks
    - utter_goodbye

## New Story

* search_provider{"city":"Pune"}
    - slot{"city":"Pune"}
    - slot{"city":"Pune"}
    - find_facility_types
* inform{"facility_type":"Public"}
    - slot{"facility_type":"Public"}
    - find_hospitals_name
    - form{"name":"find_hospitals_name"}
    - slot{"city":"Pune"}
    - slot{"facility_type":"Public"}
    - slot{"facility_type":"Public"}
    - form{"name":null}
    - slot{"requested_slot":null}
* thanks
    - utter_goodbye

## New Story

* search_provider{"city":"meerut"}
    - slot{"city":"meerut"}
    - slot{"city":"meerut"}
    - find_facility_types
* inform{"facility_type":"Private"}
    - slot{"facility_type":"Private"}
    - slot{"city":"meerut"}
    - slot{"facility_type":"Private"}
    - find_hospitals_name
    - form{"name":"find_hospitals_name"}
    - slot{"city":"meerut"}
    - slot{"facility_type":"Private"}
    - slot{"facility_type":"Private"}
    - form{"name":null}
    - slot{"requested_slot":null}
* inform{"facility_id":"999"}
    - slot{"facility_id":"999"}
    - slot{"facility_id":"999"}
    - find_hospital_address
    - slot{"facility_address":" of Metro Hospital And Heart Institute, Lal Kurti is 47/G-5,Lal Kurty,Boundry Road,Meerut, Uttar Pradesh, Phone- (0121) 2665033/041/044, Ambulance: 09837291010"}
    - utter_address
* deny
    - slot{"city":"meerut"}
    - slot{"facility_type":"Private"}
    - slot{"facility_id":"999"}
    - utter_happy
* goodbye
    - utter_goodbye

## New Story

* creator
    - utter_creator
    - find_facility_types
