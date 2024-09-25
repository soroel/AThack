import africastalking

# Initialize Africa's Talking
africastalking.initialize('soroel1', 'atsk_0603f53475fc2c6a0d372720257a5d4709959226076d3017049b73c2bf1fbcd099455245')  # Replace with your actual credentials

# Define the SMS sending function
def send_test_sms(phone_number, message):
    sms = africastalking.SMS
    try:
        response = sms.send(message, [phone_number])
        print("SMS Response:", response)
    except Exception as e:
        print(f"Error while sending SMS: {e}")

# Test the SMS function
send_test_sms("+254795553206", "Test message from sorophine, just testing my app. be blessed!")
