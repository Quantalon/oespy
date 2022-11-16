from sys import argv

from oespy import MdsApi


def main():
    if len(argv) != 2 or not argv[1]:
        print("Usage: python mds_strerror.py <errno>")
        return -1

    err_code = int(argv[1])
    mds_api = MdsApi()
    print(f"==> errno {err_code} is : {mds_api.MdsApi_GetErrorMsg(err_code)}")
    return 0


if __name__ == '__main__':
    main()
