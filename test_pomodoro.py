import unittest

from pomodoro import format_time, progress_bar


class PomodoroFormattingTests(unittest.TestCase):
    def test_format_time_zero_pads(self):
        self.assertEqual(format_time(0), "00:00")
        self.assertEqual(format_time(5), "00:05")
        self.assertEqual(format_time(65), "01:05")

    def test_progress_bar_renders_width_and_percent(self):
        bar = progress_bar(5, 10, width=10)
        self.assertEqual(bar, "[█████░░░░░] 50%")

    def test_progress_bar_rounds_down(self):
        bar = progress_bar(1, 3, width=10)
        self.assertEqual(bar, "[███░░░░░░░] 33%")


if __name__ == "__main__":
    unittest.main()
