import analyzer_pkg.text_analyzer

def run_ner (string):

	language_data = analyzer_pkg.text_analyzer.language_data_loader('./analyzer_pkg/language_data/grammar.txt', './analyzer_pkg/language_data/counter_grammar.txt', './analyzer_pkg/language_data/start_words.txt', './analyzer_pkg/language_data/stop_words.txt')

	
	result = analyzer_pkg.text_analyzer.analyzer(
		string,
		language_data['start_words'], 
		language_data['grammar'], 
		language_data['counter_grammar'], 
		language_data['stop_words'], 
		language_data['magic_bullet_grammar']
	)

	return {'treatment': result[0], 'disease': result[1]}