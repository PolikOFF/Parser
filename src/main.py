from game import user_interaction
from src.utils import delete_everything_in_folder


def main():
    delete_everything_in_folder('user_requests')
    user_interaction()


if __name__ == '__main__':
    main()
