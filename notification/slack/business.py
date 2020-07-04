from slack import WebClient
from update_request.constants import EnumUpdateRequestStatus


class SlackNotification:

    bot_token = "xoxb-517055287185-843238946631-j0MzcWPXaOTbUo5AoPKjifpW"
    channel = "#dev-alerts"

    update_request = None

    def __init__(self, update_request):
        self.client = WebClient(token=self.bot_token)
        self.update_request = update_request

    def process_signal(self, state, status):
        if state == "created" and status == EnumUpdateRequestStatus.pending:
            self.send_pending_notification()

        elif state == "update" and status == EnumUpdateRequestStatus.finished:
            self.send_finished_notification()

    def send_pending_notification(self):
        user = self.update_request.user

        message = "O usuário {user} solicitou a atualização do ambiente Y".format(user=user)

        self.send_notification(message)

    def send_finished_notification(self):
        user = self.update_request.user

        message = "O usuário {user} atualizou o ambiente Y".format(user=user)

        self.send_notification(message)

    def send_notification(self, message):
        response = self.client.chat_postMessage(
            channel=self.channel,
            message=message
        )

        return response
