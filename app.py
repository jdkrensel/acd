#!/usr/bin/env python3
import os

import aws_cdk as cdk

from src.stack import Stack


app = cdk.App()

Stack(app, "Stack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
)

app.synth()
