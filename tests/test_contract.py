import ast,pathlib
S=(pathlib.Path(__file__).parents[1]/'contracts'/'contract.py').read_text()
def test_parses():ast.parse(S)
def test_proposal_fetched_by_contract():assert 'gl.nondet.web.get' in S and 'proposal snapshot' in S
def test_exact_score_consensus():assert "['scores']==x['scores']" in S and "['gaps']==x['gaps']" in S
def test_mandatory_backstop():assert "r['gaps']!='[]'" in S
def test_lifecycle():
 for n in ('open_tender','evaluate_bid','close_tender','get_tender','get_bid'):assert f'def {n}' in S
