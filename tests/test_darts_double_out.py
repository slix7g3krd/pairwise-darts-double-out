import pytest
import gameplay.darts_double_out as mod

CASES = [
    ("tip_ray_board_hit", (1,)),
    ("double_out_check", (1,)),
    ("server_round_clock", (1,)),
    ("board_angle_snapshot", (1,)),
    ("slot_allocate", (1,)),
    ("landing_persist", (1,)),
    ("load_board", (1,)),
    ("throw_dart", (1,)),
    ("advance_round", (1,)),
    ("present_board", (1,)),
    ("validate_leg", (1,)),
    ("metrics_darts", (1,)),
    ("audit_darts", (1,)),
    ("fallback_darts", (1,)),
    ("determinism_darts", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
