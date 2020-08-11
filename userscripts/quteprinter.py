import os

def _qute_print(msg, cmd):
    with open(os.environ["QUTE_FIFO"], "w") as f:
        f.write("{} '{}'\n".format(cmd, msg.translate("".maketrans("", "", "\"'"))))

def qute_print(msg):
    _qute_print(msg, "message-info")

def qute_eprint(msg):
    _qute_print(msg, "message-error")

def qute_wprint(msg):
    _qute_print(msg, "message-warning")
