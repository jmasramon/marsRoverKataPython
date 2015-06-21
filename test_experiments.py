__author__ = 'jmasramon'

from pyspecs import given, when, then, and_, the, this, that, it


with given.two_operands:
    a = 2
    b = 3

    with when.supplied_to_the_add_function:
        total = a + b

        with then.the_total_should_be_mathmatically_correct:
            the(total).should.equal(5)

        with and_.the_total_should_be_greater_than_either_operand:
            the(total).should.be_greater_than(a)
            the(total).should.be_greater_than(b)

    with when.supplied_to_the_subtract_function:
        difference = b - a

        with then.the_difference_should_be_mathmatically_correct:
            the(difference).should.equal(1)

            this(42).should.equal(42) # this passes

            this([1, 2, 3]).should.contain(2) # this also passes

            the(list()).should.be_empty() # passes

            it(1).should_NOT.be_greater_than(100) # passes

            # raises AssertionError, caught by framework, logged as failure
            that(20).should.be_less_than(200)

    # cleanup is just based on scope
    del a, b, total, difference


