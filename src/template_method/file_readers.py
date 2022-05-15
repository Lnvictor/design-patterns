"""
Template method design pattern applcation. It read either a JSON or csv file and 
store the key, values in a dict
"""
from typing import final, List
import json
import abc


class AbstractFileReader(abc.ABC):
	@final
	def get_dict_from_file(self, filename: str):
		lines = self.read_file(filename)
		return self.parse_file(lines)

	@abc.abstractmethod
	def parse_file(self, lines):
		pass

	def read_file(self, filename: str):
		with open(filename, 'r') as file:
			return file.read()


class JSONFileReader(AbstractFileReader):
	def parse_file(self, lines):
		return json.loads(lines)


class CsvFileReader(AbstractFileReader):
	def parse_file(self, lines):
		resp = dict()
		lines = lines.split('\n')
		headers = lines[0].split(',')
		for line in lines[1:]:
			fields = line.split(',')
			for i in range(len(fields)):
				if fields[i]:
					resp[headers[i]] = fields[i]

		return resp	


if __name__ == '__main__':
	CsvFileReader().get_dict_from_file('foo.csv')
	# JSONFileReader().get_dict_from_file('foo.json')
