
# рекурсивний виклик функції sum(*args)
def sum(*args):
        """
        Returns sum of the args.
        >>> sum(1)
        1
        >>> sum(2, 2)
        4
        >>> sum(1, 2, (3, 4))
        10
        >>> sum(1, ())
        1
        >>> sum(-1, 1.0)
        0.0
        """
        result = 0
        for arg in args:
            if hasattr(arg, '__len__'):
                result += sum(*arg)
            else:
                result += arg

        return result