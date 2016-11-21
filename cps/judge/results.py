from enum import Enum
from django.utils.translation import ugettext_noop as _noop


class JudgeVerdict(Enum):

    invalid_submission = _noop("Invalid Submission")
    compilation_failed = _noop("Compilation Failed")
    crashed = _noop("Crashed")
    nonzero_exit_code = _noop("Exited with non-zero exit code")
    time_limit_exceeded = _noop("Time limit exceeded")
    memory_limit_exceeded = _noop("Memory limit exceeded")
    ok = _noop("OK")


class EvaluationResult(object):
    def __init__(
            self,
            success,
            verdict,
            exit_code=None,
            output_file=None,
            execution_time=None,
            execution_memory=None,
            message="",
    ):
        self.success = success
        self.output_file = output_file
        self.message = message
        self.execution_time = execution_time
        self.execution_memory = execution_memory
        self.verdict = verdict
        self.exit_code = exit_code
