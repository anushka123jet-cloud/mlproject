import sys
import logging




    return error_message


class CustomException(Exception):

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)

        self.error_message = error_message_details(
            error_message,
            error_detail=error_detail
        )

    def __str__(self):
        return self.error_message

    
