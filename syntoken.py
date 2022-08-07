#!/usr/bin/env python3

import time
import pyotp

totp = pyotp.TOTP('YOUR_AUTHY_SECRET======')
totp.digits = 7
totp.interval = 10
totp.issuer = "synack"
print(totp.now())
