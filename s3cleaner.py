import boto3
import argparse


def get_client(access_key_id):
	


def main(access_key_id, secret_access_key):
	if access_key_id:
		print(f'ACCESS KEY ID: {access_key_id}')

	if secret_access_key:
		print(f'SECRET ACCESS KEY: {secret_access_key}')


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='')
	parser.add_argument('--access-key-id', default=None, type=str, required=False, help='(optional) Access Key ID for the AWS profile.')
	parser.add_argument('--secret-access-key', default=None, type=str, required=False, help='(optional) Secret Access Key for the AWS profile.')
	args = parser.parse_args()

	main(args.access_key_id, args.secret_access_key)