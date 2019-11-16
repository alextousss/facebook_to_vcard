# facebook_to_vcard
I lost all my contacts, and since Facebook's Cambridge Analytica scandal, you can download a zip file containing all the informations facebook has about you ... 

Including <strong>your</strong> contacts ! 

Here is a simple parser to translate the HTML file to the vCard format 

### Usage:
It's easy as hell :
- python3 facebook_to_vcard.py -i < HTML input file > -o < vCard file location >

### Caveats

 - Contacts emails are only included if they've [opted in](https://www.facebook.com/settings?tab=account&section=email&view).
 - There is no corresponding setting for phone number, so you won't get your friends numbers this route.

In fact, your export will only include contact names with the occasional email address.
