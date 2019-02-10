import subprocess


#
# Tests for RulesGenerator.py
#
class TestRulesGeneratorClass:

    #
    # Make sure that RulesGenerator does not crash with --help
    #
    def test_rulesgenerator_help(self):
        command = './Scout.py ruleset --help'
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        process.wait()
        assert process.returncode == 0
