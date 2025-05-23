# ошибки


def error_alert(error, location, info):

    from apps.logs.models import LogsError, TYPE_LOGS_ERROR,LogsInfoError,LogsOrderError

    t = TYPE_LOGS_ERROR
    if error == "file structure":
        type_error = t[0]

        error_alert = LogsError.objects.create(
            type_error="type_error", location=location, info=info
        )

    elif error == "file api":
        type_error = t[1]

        error_alert = LogsError.objects.create(
            type_error="type_error", location=location, info=info
        )
    elif error == "file_api_error":
        type_error = t[1]

        error_alert = LogsError.objects.create(
            type_error="type_error", location=location, info=info
        )

    elif error == "error":
        type_error = t[1]

        error_alert = LogsError.objects.create(
            type_error="type_error", location=location, info=info
        )
    elif error == "file_error":
        type_error = t[1]

        error_alert = LogsError.objects.create(
            type_error="type_error", location=location, info=info
        ) 
           
    elif error == "info_error":
        type_error = t[1]

        error_alert = LogsInfoError.objects.create(
            type_error="type_error", location=location, info=info
        )
    
    elif error == "info_error_order":
        type_error = t[1]
        error_alert = LogsOrderError.objects.create(
            type_error="type_error", location=location, info=info
        )

    # return error_alert
