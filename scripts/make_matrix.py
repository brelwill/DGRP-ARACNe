#!/usr/bin/env	python

from collections import defaultdict

# female lines
header = None
header_idx = defaultdict(set)
fly_line_order = []
output = open('input/dgrp.array.exp.female.tab', 'w')

for line in open('data/dgrp.array.exp.female.csv', 'r'):
	data = line.rstrip().split(',')

	if not header:
		header = data
		# store the index of each lines 2 replicates
		for idx in range(1, len(header)):

			lline, replicate1 = header[idx].split(':')

			# store the index of this line for all replicates
			header_idx[lline].add(idx)

		fly_line_order = header_idx.keys()
		output.write('gene\t'+'\t'.join(fly_line_order)+'\n')
		continue


	# average values for each replicate
	gene = data[0]

	mean_values = []
	for fly_line in fly_line_order:
		mean_values.append(str(sum([float(data[replicate_idx]) for replicate_idx in header_idx[fly_line]])/2.0))

	output.write(gene+'\t'+'\t'.join(mean_values)+'\n')
	
output.close()	


# male lines
header = None
header_idx = defaultdict(set)
fly_line_order = []
output = open('input/dgrp.array.exp.male.tab', 'w')

for line in open('data/dgrp.array.exp.male.csv', 'r'):
	data = line.rstrip().split(',')

	if not header:
		header = data
		# store the index of each lines 2 replicates
		for idx in range(1, len(header)):

			lline, replicate1 = header[idx].split(':')

			# store the index of this line for all replicates
			header_idx[lline].add(idx)

		fly_line_order = header_idx.keys()
		output.write('gene\t'+'\t'.join(fly_line_order)+'\n')
		continue


	# average values for each replicate
	gene = data[0]

	mean_values = []
	for fly_line in fly_line_order:
		mean_values.append(str(sum([float(data[replicate_idx]) for replicate_idx in header_idx[fly_line]])/2.0))

	output.write(gene+'\t'+'\t'.join(mean_values)+'\n')
	
output.close()	


