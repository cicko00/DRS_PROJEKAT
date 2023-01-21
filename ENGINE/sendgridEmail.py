import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv


load_dotenv()

TEMPLATE_ID = 'd-0ecc8736254647649239622739c72c20'


def SendHTML(emails,username,comment, tema):
    message = Mail(
        from_email='Stefan@kupisajt.rs',
        to_emails=emails,
        )

    message.template_id = TEMPLATE_ID
    message.dynamic_template_data = {
        "tema" : tema,
        "name" : username,
        "desc" : comment
    }


    try:
        print(message)
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

if __name__ == "__main__":
    SendHTML()