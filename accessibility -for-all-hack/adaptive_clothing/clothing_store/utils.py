import africastalking



def send_sms_notification(phone_number, message):
    username = "emid"
    api_key = "atsk_5030b662f32f208230123f920e16f1f90ae17379cc9922e5f97e442c423b9cceba1d9958"
    africastalking.initialize(username, api_key)
    sms = africastalking.SMS

    try:
        response = sms.send(message, [phone_number])
        print("SMS API Response:", response)
        return response
    except Exception as e:
        print(f"Error while sending SMS: {str(e)}")
        return None
