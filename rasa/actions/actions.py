# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted
from rasa_sdk.executor import CollectingDispatcher


class ActionItemRecommendation(Action):
    def name(self) -> Text:
        return "action_item_recommendation"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        sub_option_1 = tracker.slots["sub_option_1"]
        sub_option_2 = tracker.slots["sub_option_2"]

        if tracker.slots["sub_requested_for_recommendation"]:
            sub_requested_for_recommendation = tracker.slots["sub_requested_for_recommendation"]
            dispatcher.utter_message(text=f"I think the {sub_requested_for_recommendation} is super tasty")
        else:
            dispatcher.utter_message(text=f"I'd recommend the {sub_option_1}! It's a pretty popular dish.")

        return []

class ActionItemIngredients(Action):
    def name(self) -> Text:
        return "action_item_ingredients"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        sub_option_1 = tracker.slots["sub_option_1"]
        sub_option_2 = tracker.slots["sub_option_2"] 

        item_ingredients_requested = None 

        print(tracker.slots["item_ingredients_requested"])
        if tracker.slots["item_ingredients_requested"]:
            item_ingredients_requested = tracker.slots["item_ingredients_requested"] 
        else: 
            item_ingredients_requested = tracker.slots["sub_option_1"]

        if 'elote' in item_ingredients_requested.lower():
            dispatcher.utter_message(text=f"The Elote Mac is a mac and cheese topped with corn and tajin.")
        elif 'buffalo' in item_ingredients_requested.lower():
            dispatcher.utter_message(text=f"The Buffalo Mac is a mac and cheese topped buffalo hot sauce and chicken")
        elif 'vegan' in item_ingredients_requested.lower():
            dispatcher.utter_message(text=f"The Vegan Mac is a mac and cheese with a vegan cheese sauce")
        elif 'jalapeno' in item_ingredients_requested.lower():
            dispatcher.utter_message(text=f"The Vegan Mac is a mac and cheese with a spicy jalapeno cheese sauce")

        return []

class ActionMoreOptions(Action):
    def name(self) -> Text:
        return "action_more_options"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # api call to get more sub
        sub_option_1 = "Vegan mac"
        sub_option_2 = "Jalapeno mac"

        dispatcher.utter_message(text=f"We also have our {sub_option_1} or {sub_option_2}. Either of those sound good to you?")

        return [SlotSet("sub_option_1", sub_option_1), SlotSet("sub_option_2", sub_option_2)]


class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        metadata = tracker.get_slot("session_started_metadata")

        customer_name = tracker.slots["customer_name"]
        item_to_sub = tracker.slots["item_to_sub"]
        sub_option_1 = tracker.slots["sub_options"][0]
        sub_option_2 = tracker.slots["sub_options"][1]

        dispatcher.utter_message(text=f"Hi {customer_name}, it appears there is an issue with your order. We are out of the {item_to_sub}. Can I suggest the {sub_option_1} or {sub_option_2} instead?")

        # the session should begin with a `session_started` event and an `action_listen`
        # as a user message follows
        return [SessionStarted(), ActionExecuted("action_listen"), SlotSet("item_to_sub", tracker.slots["item_to_sub"]), SlotSet("sub_option_1", sub_option_1), SlotSet("sub_option_2", sub_option_2), SlotSet("customer_name", customer_name)]


class ActionHelloWorld(Action):

   def name(self) -> Text:
       return "action_set_item_to_sub"

   def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print(tracker.slots)
        print(tracker.slots['item_to_sub'])
        SlotSet("item_to_sub",tracker.slots["item_to_sub"])
        SlotSet("customer_name",tracker.slots["customer_name"])
        SlotSet("sub_options",tracker.slots["sub_options"])

        customer_name = tracker.slots["customer_name"]
        item_to_sub = tracker.slots["item_to_sub"]
        sub_option_1 = tracker.slots["sub_options"][0]
        sub_option_2 = tracker.slots["sub_options"][1]

        dispatcher.utter_message(text=f"Hi {customer_name}, it appears there is an issue with your order. We are out of the {item_to_sub}. Can I suggest the {sub_option_1} or {sub_option_2} instead?")

        #  return [SlotSet("item_to_sub",tracker.slots["item_to_sub"]), SlotSet("customer_name",tracker.slots["customer_name"]), SlotSet("sub_option_1",tracker.slots["sub_option_1"]), SlotSet("sub_option_2",tracker.slots["sub_option_2"])]
        return []

   #  def name(self) -> Text:
       #  return "action_hello_world"
#
   #  def run(self, dispatcher: CollectingDispatcher,
           #  tracker: Tracker,
           #  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
        #  dispatcher.utter_message(text=f"Hello, how can i help you")
#
        #  return []


