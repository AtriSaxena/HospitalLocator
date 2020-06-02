# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
from typing import Any, Dict, List, NamedTuple, Optional, Set, Text, Tuple, Union
import requests


FACILITY_TYPES = {
    "Public",
    "Private"
}

class FindHospitalAddress(Action):

    def name(self) -> Text:
        return "find_hospital_address"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        facility_id = tracker.get_slot("facility_id")

        url = 'https://indian-hospital.herokuapp.com/api/v1/hospitals/'+facility_id+'/'
        print(url)
        payload = {}
        headers= {}

        response = requests.request("GET", url, headers=headers, data = payload)
        data = response.json()
        print(data)
        #res = ''
        if data:       
            name = data['name'].title()
            address = data['address'].title()
            #count+=1
            #res = res +'\n'+ str(count)+ '.Name:' + name + '\n' + 'Address:' + address
            #address = "AIIMS Delhi Ansari Nagar, Aurobindo Marg, New Delhi,Phone- (011) 26588500, 26588700, 26589900"
            #dispatcher.utter_message("Here is the address of the {} Hospital: {}".format(len(data), res))
            return [SlotSet("facility_address", address)]
        else:
           # dispatcher.utter_message("Sorry I am not able to find Hospitals in your city. I am working on it to update my data knowledge.")
            return [SlotSet("facility_address", "not found")]

class FindFacilityTypes(Action): 
    """This action class allows to display buttons for each facility type
    for the user to chose from to fill the facility_type entity slot."""
    
    def name(self) -> Text: 
        return "find_facility_types"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain :Dict[Text,Any]) -> List:
        buttons = []

        for t in FACILITY_TYPES: 
            #facility_type = FACILITY_TYPES[t]
            payload = "/inform{\"facility_type\": \"" + t + "\"}"

            buttons.append(
                {"title": "{}".format(t), "payload": payload})

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_button_template("utter_how_can_i_help", buttons, tracker)
        return []

class FindHospitalNames(FormAction):
    """This action helps to find all the hospitals name from the request
    and list as buttons to the user."""

    def name(self) -> Text: 
        return "find_hospitals_name"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["city","facility_type"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {'city': self.from_entity(entity="city", intent = ["inform","search_provider"]),
                "facility_type": self.from_entity(entity="facility_type", intent= ["inform", "search_provider"])}


    

    def submit(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        buttons = []

        city = tracker.get_slot("city")
        #state = tracker.get_slot("state")
        facility = tracker.get_slot('facility_type')
        print(facility)
        url = 'https://indian-hospital.herokuapp.com/api/v1/hospitals/?'
        # if state != None:
        #     url = url +'state=' + state + '&'
        url = url + 'city=' + city +'&' + "category=" + facility
        print(url)
        payload = {}
        headers= {}

        response = requests.request("GET", url, headers=headers, data = payload)
        data = response.json()
        print(data)
        if len(data)==0: 
            dispatcher.utter_message("Sorry, we could not find a {} Hospital in {}.".format(facility,city.title()))

            return []


        for d in data[:3]: 
            facility_id = d['id']
            payload = "/inform{\"facility_id\":\"" + str(facility_id) + "\"}"

            buttons.append({'title': "{}".format(d['name'].title()), "payload": payload})    

        if len(buttons) ==1 : 
            message = "Here is a {} Hospital near you.".format(facility)

        else:
            message = "Here are {} {}s near you:".format(len(buttons),facility)     
        dispatcher.utter_button_message(message, buttons)
        

        return []

