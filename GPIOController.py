import RPIO
import time

NRF_CE = 24

# set up output channel with an initial state
RPIO.setup(NRF_CE, RPIO.OUT, initial=RPIO.LOW)

for i in range(10):
    RPIO.output(NRF_CE, 1)
    time.sleep(1)
    RPIO.output(NRF_CE, 0)
    time.sleep(1)

# reset every channel that has been set up by this program,
# and unexport interrupt gpio interfaces
RPIO.cleanup()
