def replace_placeholders(message, patient_name, booked_provider, alternative_provider, time, date):
    message = message.replace("{Patient_name}", patient_name)
    message = message.replace("{Booked_Provider}", booked_provider)
    message = message.replace("{Alternative_Provider}", alternative_provider)
    message = message.replace("{Time}", time)
    message = message.replace("{Date}", date)
    return message
