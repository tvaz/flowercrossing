from PunnetSquareMaker import get_all_combinations, make_table

def print_genotype_frequencies(table): # calculates frequencies for each genotype present in table
	frequencies = {}
	calculated = []
	genotypes = [a for b in table for a in b]
	for k, x in enumerate(genotypes):
		count = 0
		for y in genotypes:
			if sorted(x) == sorted(y):
				count += 1
		if sorted(x) not in calculated:
			frequencies[x] = str(float(count)/float((len(genotypes)))*100)
		calculated.append(sorted(x))
	return frequencies

red_tulip = "RR yy Ss"
yellow_tulip = "rr YY ss"
white_tulip = "rr yy Ss"

c1 = get_all_combinations(red_tulip.split())
c2 = get_all_combinations(yellow_tulip.split())

a = make_table(c1, c2)
result = print_genotype_frequencies(a)
print(result)
