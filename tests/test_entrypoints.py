def test_hyp3_fire_tracking(script_runner):
    ret = script_runner.run(['python', '-m', 'hyp3_fire_tracking', '-h'])
    assert ret.success
