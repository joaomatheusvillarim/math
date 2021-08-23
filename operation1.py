for r in [True, False]:
	for p in [True, False]:
		for q in [True, False]:
			print(p or (q and r) == (p or q) and (p or r))