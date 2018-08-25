from base import Base

class S3(Base):
    def __init__(self):
        pass

if __name__ == '__main__':
    s3 = S3()
    print("hello %s" % s3.conf()['aws_key'])