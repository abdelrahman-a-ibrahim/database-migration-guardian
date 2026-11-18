"""Initial application boundary for Database Migration Guardian.

The runtime is in development. Refine models and errors alongside the first
implementation; dict/list annotations mark contracts still to be formalized.
"""

class MigrationGuardian:
    def assess(self, migration: dict, database_context: dict) -> dict:
        """Explain risk and missing evidence; do not promise complete SQL safety analysis."""
        raise NotImplementedError("Runtime implementation is in development.")

    def verify(self, before: dict, after: dict) -> dict:
        """Compare invariants, row counts and application compatibility."""
        raise NotImplementedError("Runtime implementation is in development.")
