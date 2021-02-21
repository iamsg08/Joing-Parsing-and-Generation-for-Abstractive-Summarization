from pyrouge import Rouge155

r = Rouge155()
r.system_dir = './Desktop/summar_research/paper_1'
r.model_dir = './Desktop/summar_research/paper_1'
r.system_filename_pattern = 'summary.txt'
r.model_filename_pattern = 'gold.txt'

output = r.convert_and_evaluate()
print(output)
output_dict = r.output_to_dict(output)