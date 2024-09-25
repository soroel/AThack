import africastalking



def send_sms_notification(phone_number, message):
    username = "soroel1"
    api_key = "atsk_0603f53475fc2c6a0d372720257a5d4709959226076d3017049b73c2bf1fbcd099455245"
    africastalking.initialize(username, api_key)
    sms = africastalking.SMS

    try:
        response = sms.send(message, [phone_number])
        print("SMS API Response:", response)  # Log the response for debugging
        return response
    except Exception as e:
        print(f"Error while sending SMS: {str(e)}")
        return None
