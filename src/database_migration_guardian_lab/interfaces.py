"""Proposed application boundary for Database Migration Guardian Lab.

This is a design scaffold, not a functional SDK or service. Refine the return
models during milestone 1; dict/list types leave that decision open deliberately.
"""

class MigrationGuardian:
    def assess(self, migration: dict, database_context: dict) -> dict:
        """Explain risk and missing evidence; do not promise complete SQL safety analysis."""
        raise NotImplementedError("Implement this boundary with behavior tests first.")

    def verify(self, before: dict, after: dict) -> dict:
        """Compare invariants, row counts and application compatibility."""
        raise NotImplementedError("Implement this boundary with behavior tests first.")

