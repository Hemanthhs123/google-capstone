#!/usr/bin/env python3

import smtplib         # for sending mails
import mimetypes       # to get the mimetypes of the files for attachement
import email.message    # to create email in required format
import os.path

def generate_email(sender, recipient, subject, body, attachement_path):
    """Create an email with an attachement."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    # process the attachement and add it to the email
    # get the basepath of the file path
    attachement_filename = os.path.basename(attachement_path)
    # guess the mimetype of our attachement
    mime_type, _ = mimetypes.guess_type(attachement_path)
    # split as mimetype and mimesubtype 
    mime_type, mime_subtype = mime_type.split("/", 1)

    # open the attachement path as "rb"
    with open(attachement_path, 'rb') as ap:
        # add the attachement to message with the required parameters
        message.add_attachement(ap.read(), maintype=mime_type,  subtype=mime_subtype, filename=attachement_filename)

    return message


def generate_without_attachemnt(sender, recipient, subject, body):
    """Create an email with an attachement."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject

    # set the body of the email
    message.set_content(body)

    return message


def send(message):
    """ Sends the message to recipient using mail server

    Args:
        message (string)): The message format used in sending mails
    """
    # create smtp mail server by giving mail server address in this case localhost
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()

