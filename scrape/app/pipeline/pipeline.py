import logging
from typing import Any

from app.storage.kv_store import KVStore
from app.storage.run_result import RunResult

logger = logging.getLogger(__name__)


class Pipeline:
    """
    Manages a sequence of processing steps.
    Each step is expected to have a 'run' method that returns a RunResult.
    """

    def __init__(self, kv_store: KVStore, steps: list[Any]):
        self.kv_store = kv_store
        self.steps = steps

    def run(self) -> RunResult:
        """Runs all steps in sequence."""
        for step in self.steps:
            step_name = step.__class__.__name__
            try:
                result = step.run()
                if not result.proceed:
                    logger.warning(
                        f"Pipeline stopped after {step_name}: {result.reason}"
                    )
                    return result
            except Exception as e:
                logger.error(f"Pipeline failed at step {step_name}: {e}")
                return RunResult(proceed=False, reason=str(e))

        return RunResult()
