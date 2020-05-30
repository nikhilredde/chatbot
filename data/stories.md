## happy path
* get_started
  - utter_get_started

## happy path2
* send_mail
  - action_reset_all_slots
  - gmail_form
  - form{"name": "gmail_form"}
  - form{"name": null}
  - utter_confirm
* yes
  - utter_goodbye
  - action_reset_all_slots
 

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## affirm
* affirm
  - utter_ask_me

##deny
*deny
  - utter_no

## IITTP_only
* IITTP
  - utter_IITTP
  - utter_more_info
  - utter_do_you_need

## phase
*phase
  - utter_phase
  

## IITTP_location
* IITTP_location
   - utter_IITTP_location
   - utter_more_info
   - utter_do_you_need
   

## IITTP_year
* IITTP_year

   - utter_IITTP_year
   - utter_more_info
   - utter_do_you_need
   

## IITTP_branches
* IITTP_branches

   - utter_IITTP_branches
   - utter_more_info
   - utter_do_you_need
  

## IITTP_hostels
* IITTP_hostels
  - utter_IITTP_hostels
  - utter_more_info
  - utter_do_you_need

## comapny
*comapny
  - utter_company
  


