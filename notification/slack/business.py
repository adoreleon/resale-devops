from update_request.constants import EnumUpdateRequestStatus


class SlackNotification:
    update_request = None

    def __init__(self, update_request):
        self.update_request = update_request

    def process_signal(self, state, status):
        if state == "created" and status == EnumUpdateRequestStatus.pending:
            self.send_pending_notification()

        elif state == "update" and status == EnumUpdateRequestStatus.finished:
            self.send_finished_notification()

    def send_pending_notification(self):
        pass

    def send_finished_notification(self):
        pass
