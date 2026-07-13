from pathlib import Path
import importlib.util
import unittest

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "learning-architect/scripts/validate_learning_system.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("learning_validator", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class LearningSystemValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validator = load_validator()
        cls.skill_root = ROOT / "learning-architect"
        cls.fixtures = ROOT / "tests/learning-architect/fixtures"

    def test_skill_assets_and_valid_learner_pass(self):
        self.assertEqual(self.validator.validate_skill_assets(self.skill_root), [])
        self.assertEqual(
            self.validator.validate_learner_system(
                self.skill_root, self.fixtures / "valid-learner"
            ),
            [],
        )

    def test_curriculum_cycle_is_rejected(self):
        errors = self.validator.validate_learner_system(
            self.skill_root, self.fixtures / "invalid-cycle"
        )
        self.assertTrue(any("cycle" in error.lower() for error in errors), errors)

    def test_unknown_competency_evidence_reference_is_rejected(self):
        errors = self.validator.validate_learner_system(
            self.skill_root, self.fixtures / "invalid-evidence-ref"
        )
        self.assertTrue(any("unknown competency" in error.lower() for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
