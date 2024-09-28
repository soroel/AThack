import africastalking



def send_sms_notification(phone_number, message ):
    username = "EMID"
    api_key = "atsk_5030b662f32f208230123f920e16f1f90ae17379cc9922e5f97e442c423b9cceba1d9958"
    sender="AFTKNG"
    africastalking.initialize(username, api_key)
    sms = africastalking.SMS

    try:
        response = sms.send(message, [phone_number], sender)
        print("SMS API Response:", response)  # Log the response for debugging
        return response
    except Exception as e:
        print(f"Error while sending SMS: {str(e)}")
        return None
