import unittest
import os

# THIS CODE WORKS ONLY OCCASIONALLY

def run_all_tests():
    # Get the absolute path of the test directory
    test_dir = os.path.join(os.path.dirname(__file__), 'test')

    # Discover all test files in the test directory
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=test_dir, pattern='test_*.py')

    # Run the tests
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # Return an appropriate exit code
    return not result.wasSuccessful()


if __name__ == '__main__':
    exit_code = run_all_tests()
    exit(exit_code)
