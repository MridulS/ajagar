import sys

input_file = sys.argv[1]
print(f'अजगर के साथ {input_file} चलाया जा राहा है')

eng_hindi_mapping = {
	'pass': 'जाने दो',
	'elif': 'नहीं अगर तो',
	'if': 'अगर',
	'else': 'नहीं तो',
	'or': 'या',
	'not': 'नहीं', 
	'and': 'और',
	'in': 'अंदर',
	'del': 'हटा',
	'True': 'सच',
	'False': 'झूट',
	'None': 'कुछ नहीं',
	'break': 'रुक जाओ',
	'def': 'परिभाषा',
	'return': 'अर्थ',
	'class': 'श्रेणी',
	'print': 'प्रिंट',
	'set': 'संग्रह',
	'pop': 'निकालो',
	'add': 'डालो',
	'extend': 'विस्तार',
	'while': 'जब तक',
}

hindi_eng_mapping = {hindi: eng for eng, hindi in eng_hindi_mapping.items()}


def execute_hindi_file(input_file):
	with open(input_file, 'r') as f:
		file_data = f.read()

	for hin, eng in hindi_eng_mapping.items():
		file_data = file_data.replace(hin, eng)

	exec(file_data)

def convert_to_hindi_file(input_file):
	with open(input_file, 'r') as f:
		file_data = f.read()
	for eng, hin in hindi_eng_mapping.items():
		file_data = file_data.replace(eng, hin)
	ouptut_file = input_file[:-e] + '_hindi.py'
	with open(ouptut_file, 'w') as f:
		f.write(file_data)

if __name__ == "__main__":
	execute_hindi_file(input_file)
