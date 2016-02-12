#lambda-python-plain

Simple example using AWS Lambda to call Postgres database.

##Includes

1. Create/Update script to deploy lambda function
2. Lambda function to call Postgres database
3. Pre-compiled psycopg2 sources for lambda AMI from [here](https://github.com/jkehler/awslambda-psycopg2)

##Config

1. Create role for lambda to write to log using the following policy:

```
{
    "Statement": [
        {
            "Resource": "arn:aws:logs:eu-west-1:*:*",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Effect": "Allow"
        }
    ],
    "Version": "2012-10-17"
}
```

2. Add role and account id to `run.py`
3. Add database settings to `handler.py`
4. ...Maybe create an API-Gateway endpoint for the lambda function to call it easier