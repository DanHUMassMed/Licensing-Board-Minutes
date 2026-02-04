from dataclasses import dataclass


@dataclass
class RunResult:
    """
    Result of a single pipeline step.
    'proceed' determines if the pipeline should continue to the next step.
    'reason' provides context if it stops.
    """

    proceed: bool = True
    reason: str = ""
