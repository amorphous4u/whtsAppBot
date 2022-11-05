from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

whtAppBot = Flask(__name__)


@whtAppBot.route('/mybot', methods=['POST'])
def mybot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'hi' == incoming_msg:
        # Return response for Hi
        msg.body("Hello, I am your Bot!")
    if 'quote' == incoming_msg:
        r = request.get('http://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'Sorry I am unable to retreive quote at this time'
        msg.body(quote)
        responded = True
    if 'who are you' in incoming_msg:
        msg.body("Hi, I am whatsapp Bot created by Amit Verma")
        responded = True

    if not responded:
        msg.body("Hi, I am not able to understand your message")

    return str(resp)


if __name__ == '__main__':
    whtAppBot.run(debug=True)
