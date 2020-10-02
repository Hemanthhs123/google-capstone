# Project Problem statement
You work for an online fruit store, and you need to develop a system that
will update the catalog information with data provided by your
suppliers. When each supplier has new products for your store, they give you an image and a description of each product.

Given a bunch of images and descriptions of each of the new products, you’ll:

- Upload the new products to your online store. Images and descriptions should
be uploaded separately, using two different web endpoints.
- Send a report back to the supplier, letting them know what you imported.

Since this process is key to your business's success, you need to make sure that it keeps running! So, you’ll also:

- Run a script on your web server to monitor system health.
- Send an email with an alert if the server is ever unhealthy.


## Modules used
- [Python Image Library (PIL)](https://pillow.readthedocs.io/) - [Tutorial](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html)
- [Requests](https://requests.readthedocs.io/) (HTTP client library) - [Quickstart](https://requests.readthedocs.io/en/master/user/quickstart/)
- [ReportLab](https://www.reportlab.com/docs/reportlab-userguide.pdf) (PDF creation library)
- [email](https://docs.python.org/3/library/email.examples.html) (constructing email)
- [psutil](https://psutil.readthedocs.io/) (processes and system utilization)
- [shutil](https://docs.python.org/3/library/shutil.html) (file operations)
- [smtplib](https://docs.python.org/3/library/smtplib.html) (sending email)

### Files 
- chanageImage.py - It will resize and change the image format from .tiff to .jpeg
- emails.py - sends email to recipient
- health_check.py - it checks the system health every hour and sends email about the shortage of resources or any specified error accurs
- run.py - uploads the descriptions about the images to webserver 
- reports.py - it creates the report about the description about the images in pdf form to the given directory
- supplier_image_upload.py - it uploads the iamges to the webserver 