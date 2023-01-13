from ast import Try
import datetime
import boto3


def getBill(event, lambda_context):
    client = boto3.client('ce')
    today = datetime.date.today()
    dateEnd = today.replace(day=30).strftime('%Y-%m-%d')
    dateStart = today.strftime('%Y-%m-%d')

    try:
        response = client.get_cost_and_usage(
            TimePeriod={
                'Start': dateStart,
                'End': dateEnd
            },
            Granularity='DAILY',
            Metrics=['NetUnblendedCost', 'AmortizedCost','BlendedCost','NetAmortizedCost','NormalizedUsageAmount','UnblendedCost','UsageQuantity'],
            GroupBy=[{
                'Type': 'TAG',
                'Key': 'Project_TAG'
            },]
        )

        print(response)
        return response, 200
    except:
        response = 'Data Unavailable'
        print(response)
        return (response), 400