import boto3
import argparse


def get_s3_client(access_key_id=None, secret_access_key=None):
	if access_key_id and secret_access_key:
		return boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
	else:
		return boto3.client('s3')


def main(access_key_id=None, secret_access_key=None):
	client = get_s3_client(access_key_id, secret_access_key)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='')
	parser.add_argument('--access-key-id', default=None, type=str, required=False, help='(optional) Access Key ID for the AWS profile.')
	parser.add_argument('--secret-access-key', default=None, type=str, required=False, help='(optional) Secret Access Key for the AWS profile.')
	args = parser.parse_args()

	access_key_id = args.access_key_id
	secret_access_key = args.secret_access_key

	if access_key_id and secret_access_key:
		main(access_key_id, secret_access_key)
	elif not access_key_id and not secret_access_key:
		main()
	else:
		print('You must provide both the Access Key ID and Secret Access Key, or neither to use system credentials.')