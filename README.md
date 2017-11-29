# FindMyiPhone

## Introduction

The code and procedure in this project describe how one can use the AWS IoT button to find the iPhone. This is equivalent to log in to the FindMyiPhone app in iPhone, and click the "Play Sound" button.


The following hardware and software are required for this program to work,

####Hardware:

AWS IoT Button

iPhone :-)

####Software

#####AWS Lambda

Follow [these](http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html) instructions to [create](http://docs.aws.amazon.com/lambda/latest/dg/get-started-create-function.html) the Lambda function package, and upload it to Lambda to create the Lambda function.

This project uses the [pyicloud](https://github.com/picklepete/pyicloud) Python program to call the "Play Sound" in findmyiphone app.

The findMyiPhone.py is the main code in AWS Lambda function that is triggerred when the AWS IoT buttion is pressed. The Lambda function will in turn call the "Play Sound" function.

#####AWS IoT Buttion

Follow the steps [here](http://docs.aws.amazon.com/iot/latest/developerguide/iot-button-lambda.html) to configure your IoT button.

Please select the Lambda function created above in step 4 when configuring the trigger.


