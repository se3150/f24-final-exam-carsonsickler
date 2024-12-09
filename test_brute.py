import pytest
import unittest.mock
from brute import Brute

todo = pytest.mark.skip(reason='todo: pending spec')

'''
For the bruteMany method, implement test doubles for the hash and/or randomGuess methods as you deem appropriate. For simplicity, avoid patching the hashlib module directly. Use stubs to force the desired test outcomes, and use mocks to verify correct implementation details.
'''

def describe_Brute():

    @pytest.fixture
    def cracker():
        return Brute("TDD")

    def describe_bruteOnce():
        # write your test cases here
        
        def it_returns_true_if_attempt_matches_target(cracker):
            assert cracker.bruteOnce("TDD") == True

        def it_returns_false_if_attempt_does_not_match_target(cracker):
            assert cracker.bruteOnce("tdd") == False

        def it_returns_false_when_attempt_is_empty(cracker):
            assert cracker.bruteOnce('') == False

        

        def describe_attempt_is_not_a_string():
             
            def it_raises_a_type_error_when_attempt_is_missing(cracker):
                try:
                    e = cracker.bruteOnce()
                    assert e == False
                except Exception as e:
                    assert type(e) == TypeError

            def it_raises_a_type_error_when_attempt_is_an_int(cracker):
                try:
                    e = cracker.bruteOnce(29)
                    assert e == False
                except Exception as e:
                    assert type(e) == TypeError

            def it_raises_a_type_error_when_attempt_is_a_float(cracker):
                try:
                    e = cracker.bruteOnce(2.2)
                    assert e == False
                except Exception as e:
                    assert type(e) == TypeError


    def describe_bruteMany():
        # write your test cases here
        def it_only_attempts_up_to_limit_times(cracker):
            with unittest.mock.patch.object(cracker, 'randomGuess', return_value='TDD') as mock:
                assert cracker.bruteMany(1) > 0
                assert mock.call_count == 1

        def it_returns_time_taken_to_crack_for_succesful_crack(cracker):
            with unittest.mock.patch.object(cracker, 'randomGuess', return_value='TDD') as mock:
                assert cracker.bruteMany() > 0
                assert mock.call_count > 0

        def it_returns_negative_one_if_unsuccseful(cracker):
            with unittest.mock.patch.object(cracker, 'randomGuess', return_value='tdd') as mock:
                assert cracker.bruteMany() == -1
                assert mock.call_count > 0

        def it_does_not_attempt_if_limit_is_negative(cracker):
            with unittest.mock.patch.object(cracker, 'randomGuess', return_value='TDD') as mock:
                assert cracker.bruteMany(-1) == -1
                assert mock.call_count == 0

        def it_does_not_attempt_if_limit_is_0(cracker):
            with unittest.mock.patch.object(cracker, 'randomGuess', return_value='TDD') as mock:
                assert cracker.bruteMany(0) == -1
                assert mock.call_count == 0

        def it_attempts_up_to_limit_times(cracker):
            with unittest.mock.patch.object(cracker, 'randomGuess', return_value='TDD') as mock:
                assert cracker.bruteMany(2) > 0
                assert mock.call_count == 1
