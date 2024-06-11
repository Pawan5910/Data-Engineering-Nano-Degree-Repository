# Project 3: STDEI Human Balance Analytics

## Introduction
Spark and AWS Glue allow you to process data from multiple sources, categorize the data, and curate it to be queried in the future for multiple purposes. As a data engineer on the STEDI Step Trainer team, you'll need to extract the data produced by the STEDI Step Trainer sensors and the mobile app, and curate them into a data lakehouse solution on AWS so that Data Scientists can train the learning model.

## Project Details
The STEDI Team has been hard at work developing a hardware STEDI Step Trainer that:

trains the user to do a STEDI balance exercise;
and has sensors on the device that collect data to train a machine-learning algorithm to detect steps;
has a companion mobile app that collects customer data and interacts with the device sensors.
STEDI has heard from millions of early adopters who are willing to purchase the STEDI Step Trainers and use them.

Several customers have already received their Step Trainers, installed the mobile application, and begun using them together to test their balance. The Step Trainer is just a motion sensor that records the distance of the object detected. The app uses a mobile phone accelerometer to detect motion in the X, Y, and Z directions.

The STEDI team wants to use the motion sensor data to train a machine learning model to detect steps accurately in real-time. Privacy will be a primary consideration in deciding what data can be used.

Some of the early adopters have agreed to share their data for research purposes. Only these customers’ Step Trainer and accelerometer data should be used in the training data for the machine learning model.

## Implementation

### Landing Zones

#### Customer Landing

![customer_landing](https://github.com/Pawan5910/Udacity_STEDI_project/assets/95497950/e27d6e17-1c8d-49ce-92a0-289e339afa51)

#### Accelerometer Landing

![accelerometer_landing](https://github.com/Pawan5910/Udacity_STEDI_project/assets/95497950/17b656f8-419f-48a6-8f3b-67cfa8fb4825)

#### Step_trainer Landing

![step_trainer_landing](https://github.com/Pawan5910/Udacity_STEDI_project/assets/95497950/e390dece-f566-4e2a-9fe9-77a02ce43aaf)

### Trusted Zones

#### Customer Trusted

![customer_trusted](https://github.com/Pawan5910/Udacity_STEDI_project/assets/95497950/f536fdc1-30c0-4234-9883-3c12de93b7c2)

#### Accelerometer Trusted

![accelerometer_trusted](https://github.com/Pawan5910/Udacity_STEDI_project/assets/95497950/c942a474-a6b1-45ab-b865-937e6878f3c0)

####  Step_trainer Trusted

![step_trainer_trusted](https://github.com/Pawan5910/Udacity_STEDI_project/assets/95497950/153c8010-f02f-40a2-9fab-4a1d35d5e508)

### Curated Zone

#### Customer Curated

![customer_curated](https://github.com/Pawan5910/Udacity_STEDI_project/assets/95497950/20163ed2-7506-4372-9727-ccb05fde8ded)

#### Machine Learning Curated

![machine_learning_curated](https://github.com/Pawan5910/Udacity_STEDI_project/assets/95497950/d6292d79-8216-474a-9fc2-885d091e4edd)

### Code Directory

#### Python Scripts: 
Contains the code for the creation of the trusted and curated zones.

#### SQL Scripts:
Contains the sql scripts for all the table creation.













