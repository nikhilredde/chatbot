from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk import Action,Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Dict, Text, Any, List, Union, Optional
import smtplib, ssl







class FormActionInfo(FormAction):
    
    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "gmail_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["SenderMail","Password","RecipientMail", "Subject", "Format"]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:


        """Define what the form has to do
        after all required slots are filled"""
    # utter submit template
        dispatcher.utter_message(template="utter_submit",SenderMail=tracker.get_slot('SenderMail'),Password=tracker.get_slot('Password'),
                                 RecipientMail=tracker.get_slot('RecipientMail'),Subject=tracker.get_slot('Subject'),Format=tracker.get_slot('Format'))

        sender_email = tracker.get_slot('SenderMail')
        rec_email = tracker.get_slot('RecipientMail')
        password = tracker.get_slot('Password')
        sub = tracker.get_slot('Subject')
        msg = tracker.get_slot('Format')
        message = "Subject:{} \n\n {}" .format(sub, msg)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("Login success")
        server.sendmail(sender_email, rec_email, message)
        print("Email has been sent to ", rec_email)

        


        return []    

   



    
    

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""
        return {
        "SenderMail": [self.from_text()],
        "Password": [self.from_text()],
        "RecipientMail": [self.from_text()],
        "Subject":[self.from_text()],    
        "Format": [self.from_text()]
         }







