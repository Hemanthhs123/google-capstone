#!/usr/bin/env python3

# import required libraries
import os 
import shutil
import psutil
import socket
import emails       # to send the mails automatically when detecting errors


def disk_space_alert():
    """check the free disk space 

    Returns:
        boolean: if free disk space is lower than 20%
    """
    disk_usage = shutil.disk_usage("/")
    percent_free = disk_usage.free/disk_usage.total * 100
    return percent_free < 20

def cpu_usage_alert():
    """checks the average cpu usage in 1 seconds

    Returns:
        boolean: if the cpu usage is greater than 80%
    """
    cpu_usage = psutil.cpu_percent(1)
    return cpu_usage > 80

def memory_alert():
    """checks the memory usage of the computer and convertss it to MB then check if memory available is less than 500

    Returns:
        boolean: if memory available is less than 500MB(true)
    """
    return psutil.virtual_memory().free/2**20 < 500

def check_localhost():
    """checks the localhost is correct in the machine or not

    Returns:
        boolean: if localhost is 127.0.0.1(true)
    """
    localhost = socket.gethostbyname("localhost")
    return localhost != "127.0.0.1"

def full_check():
    """It checks the full status of the system by using above functions and automatically sends email when the alert occurs
    """
    email_body = "Please check your system and resolve the issue as soon as possible."
    From = "automation@example.com"
    To =  "<email@example.com>"
    if disk_space_alert():
        subject = "Error - Available disk space is less than 20%" 
        message = emails.generate_without_attachemnt(From, To, subject, email_body)
        emails.send(message)

    if cpu_usage_alert():
        subject = "Error - CPU usage is over 80%"
        message = emails.generate_without_attachemnt(From, To, subject, email_body)
        emails.send(message)
        
    if memory_alert():
        subject = "Error - Available memory is less than 500MB"
        message = emails.generate_without_attachemnt(From, To, subject, email_body)
        emails.send(message)

    if check_localhost():
        message = emails.generate_without_attachemnt(From, To, "Error - localhost cannot be resolved to 127.0.0.1", email_body)
        emails.send(message)


if __name__=="__mian__":
    full_check()


# we have to run this every 60 minutes so we make use of cron jobs in linux and specify the path 