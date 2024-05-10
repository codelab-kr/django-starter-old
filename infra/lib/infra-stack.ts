import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class InfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const lambdaFunction = new lambda.Function(this, 'LambdaFunction', {
      runtime: lambda.Runtime.PYTHON_3_12,
      code: lambda.Code.fromAsset('aws_lambda_artifact.zip'),
      handler: 'main.handler',
      environment: {
        'ENVIRONMENT': process.env.ENVIRONMENT || 'development',
        'SECRET_KEY': process.env.SECRET_KEY as string,
        'ENCRYPT_KEY': process.env.ENCRYPT_KEY as string,
        'DATABASE_URL': process.env.DATABASE_URL as string,
        'POSTGRES_RDS': process.env.POSTGRES_RDS as string,
      }
    });

    const functionUrl = lambdaFunction.addFunctionUrl({
      authType: lambda.FunctionUrlAuthType.NONE,
      cors: {
        allowedOrigins: ['*'],
        allowedMethods: [lambda.HttpMethod.ALL],
        allowedHeaders: ['*']
      }
    });

    new cdk.CfnOutput(this, 'Url', {
      value: functionUrl.url
    });
  }
}

//
