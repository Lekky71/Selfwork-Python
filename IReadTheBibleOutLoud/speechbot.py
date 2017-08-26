from __future__ import print_function
import urllib, urllib.request, json
import array
def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome, tell me any bible verse. " \
                    "I can read out bible verses for you, " \
                    "hi"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please tell me any bible verse, " \
                    "I'll read out for you."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying this app. " \
                    "Have a lovely day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def set_bible_verse(book,chapter,verse):
    option = book[0:3]
    if option == '1st':
        book = book.replace('1st ', '1')
    elif option == 'sec':
        book = book.replace('second ', '2')
    elif option == '3rd' :
        book = book.replace('3rd ', '3')
    print(book)
    u = urllib.request.urlopen('https://getbible.net/json?passage='+book+chapter+':'+verse)
    b = u.read()
    print (b)
    y = str(b)
    reading = 'a passage'
    if len(y) < 10 or book == '' or chapter == '' or verse == '':
        reading = "sorry, this bible passage does not exist."
    else:
        verse_place = y.find('"verse"')
        start = verse_place + 9
        stop = y.find('"', start + 1)
        reading = y[start:stop]
    return reading


def say_bible_in_session(intent, session):
    card_title = intent['name']
    session_attributes = {}
    reprompt_text = None
    bible_book = intent['slots']['Book']['value']
    bible_chapter = intent['slots']['Chapter']['value']
    bible_verse = intent['slots']['Verse']['value']
    speech_output = set_bible_verse(bible_book, bible_chapter, bible_verse)
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
                          card_title, speech_output, reprompt_text, should_end_session))


def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    if intent_name == "OpenBiblePage":
        return say_bible_in_session(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])

# --------------- Main handler ------------------


def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])





