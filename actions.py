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
from typing import Any, Dict, List, NamedTuple, Optional, Set, Text, Tuple, Union
import requests
class ActionFacilitySearch(Action):

    def name(self) -> Text:
        return "action_facility_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot("city")
        state = tracker.get_slot("state")
        facility = tracker.get_slot('facility_type')
        url = 'https://indian-hospital.herokuapp.com/api/v1/hospitals/?'
        if state != None:
            url = url +'state=' + state + '&'
        elif city !=None: 
            url = url + 'city=' + city +'&'
        elif facility !=None: 
            url = url + 'category=' +facility +'&'

        payload = {}
        headers= {}

        response = requests.request("GET", url, headers=headers, data = payload)
        data = response.json()

        count = 0
        res = ''
        if len(data) > 0:
            for d in data: 
                name = d['name']
                address = d['address']
                count+=1
                res = res +'\n'+ str(count)+ '.Name:' + name + '\n' + 'Address:' + address
            #address = "AIIMS Delhi Ansari Nagar, Aurobindo Marg, New Delhi,Phone- (011) 26588500, 26588700, 26589900"
                dispatcher.utter_message("Here is the address of the {} in {}: {}".format(len(data), city, res))
        else:
            dispatcher.utter_message("Sorry I am not able to find Hospitals in your city. I am working on it to update my data knowledge.")

        return [SlotSet("address", address)]
