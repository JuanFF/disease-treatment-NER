import run_ner
import sys

result = run_ner.run_ner(sys.argv[1])

print(
	'Treatment: ' + result['treatment'] + '\n'
	+ 'Disease: ' + result['disease']
	)