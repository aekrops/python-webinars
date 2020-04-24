from multimethod import multimethod


class WithStaticAndOverload:

    worker_name = 'some name'

    @staticmethod
    def do_work():
        pass

    def sing_a_song(self):
        print(WithStaticAndOverload.worker_name)

    @multimethod
    def print_data(self, first: str, second: str):
        print(str(first) + "-" + str(second))

    @multimethod
    def print_data(self, first: int, second: int):
        """
        returns sum of two integers
        >>> print_data(10,20)
        [30]
        """
        print(str(first + second))


#if __name__ == "__main__":
 #   my_object = WithStaticAndOverload()
  #  my_object.print_data(23, 45)
   # my_object.print_data("34", "78")

# python -m doctest -v C:\Users\svyat\Desktop\webinar\python-webinars\models\another_experiment.py
if __name__ == "__main__":
    import doctest
    doctest.testmod()

def create_tuple(self, first: int, second: int):
    """
    returns sum of two integers
    >>> create_tuple(10,20)
    (10,20)
    >>> create_tuple(20,70)
    (20,70)
    >>> print("hello world")
    hello world
    """
    print(first, second)