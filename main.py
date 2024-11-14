"""Main"""
import src.logic

data = src.logic.read_file()
resulted_dict = src.logic.convert_to_dict(data)
src.logic.save_dict_to_file(resulted_dict)
