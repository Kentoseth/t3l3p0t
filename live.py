# coding=utf-8
"""
This is the main Python file to execute.
Run this file after starting the telegram-cli
"""
from __future__ import unicode_literals
from pytg.receiver import Receiver  # get messages
from pytg.sender import Sender  # send messages, and other querys.
from pytg.utils import coroutine
import os
# Enable logging if something goes wrong
# import logging

# logging.basicConfig(level=logging.DEBUG)

__author__ = 'Kentoseth'

USER_ID = os.environ["ID"] # the ENV-VAR for the user ID you will forward the messages to.

def main():
    # get a Receiver instance, to get messages.
    msg_receiver = Receiver(host="localhost", port=4458)

    # get a Sender instance, to send messages, and other queries.
    msg_sender = Sender(host="localhost", port=4458)

    # start the Receiver, so we can get messages!
    msg_receiver.start()  # note that the Sender has no need for a start function.

    # add "alert" function as message listener. You can supply arguments here (like sender).
    msg_receiver.message(alert(msg_sender))  # now it will call the "alert" function and yield the new messages.

    # continues here, after exiting the while loop in example_function()

    # please, no more messages. (we could stop the the cli too, with sender.safe_quit() )
    msg_receiver.stop()

    print("Shutting down app! CLI will still be running")
    
# this is the function which will process our incoming messages
@coroutine
def alert(msg_sender):  # name "alert" and given parameters are defined in main()
    quit = False
    try:
        while not quit:  # loop for messages
            msg = (yield)  # it waits until the generator has a message here.
            msg_sender.status_online()  # so we will stay online.
            # (if we are offline it might not receive the messages instantly,
            #  but eventually we will get them).
            
            # print(msg) # in case you wish to see the output of what "msg" contains.
            
            if msg.event != "message":
                continue  # is not a message.
            if msg.own:  # the bot has send this message.
                continue  # we don't want to process this message.
             
                
            if 'media' in msg:  # the item is a media message.

                msg_sender.fwd_media(USER_ID, msg.id) # forward it to the specified user, USER_ID.
            
            elif 'text' in msg: # the item is a text message.
            
                msg_sender.fwd(USER_ID, msg.id) # forward it to the specified user, USER_ID.

            
    except GeneratorExit:
        # the generator (pytg) exited (got a KeyboardIterrupt).
        pass
    except KeyboardInterrupt:
        # we got a KeyboardIterrupt(Ctrl+C)
        pass
    else:
        # the loop exited without exception, becaues _quit was set True
        pass
    
# # program starts here ##
if __name__ == '__main__':
    main()  # executing main function.
# Last command of file (so everything needed is already loaded above)
