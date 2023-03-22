from nautobot.dcim.models import Device, Location
from nautobot.extras.jobs import JobButtonReceiver


class TestJobButtonReceiverSimple(JobButtonReceiver):
    def receive_job_button(self, obj):
        self.log_info(f"request.user: {self.request.user.username}")
        self.log_success(obj.name)


class TestJobButtonReceiverComplex(JobButtonReceiver):
    def receive_job_button(self, obj):
        self.log_info(f"request.user: {self.request.user.username}")
        if isinstance(obj, Device):
            self.log_success(f"Device: {obj}")
        elif isinstance(obj, Location):
            self.log_success(f"Location: {obj}")


class TestJobButtonReceiverFail(JobButtonReceiver):
    pass