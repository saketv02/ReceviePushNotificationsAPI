#Author:Saket Vishwasrao
from flask import Flask,jsonify
from py4j.java_gateway import JavaGateway

def add_notifications(message):
    gateway = JavaGateway()
    # call the java instance
    sendNotification = gateway.entry_point  #create an instance of the class
    #call java class method here as entry point
    sendNotification.callPushSystemAPI(message.messageId,message.body)
    return "Success",200
