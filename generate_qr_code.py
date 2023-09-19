import qrcode

def lambda_handler(event, context):
    # Retrieve the parameter from the API Gateway event
    parameter_value = event['queryStringParameters']['parameter']

    # Generate a QR code with the parameter value
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(parameter_value)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Return the QR code image as a base64-encoded PNG
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "image/png",
        },
        "body": img.save("/tmp/qr_code.png", format="PNG"),
        "isBase64Encoded": True,
    }
