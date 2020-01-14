
# Description: This program tests the countability of rational numbers based on the algorithm found at
# https://www.cut-the-knot.org/do_you_know/countRats.shtml. It looks to be based on Cantor's enumeration of a countable
# collection of countable sets. It creates a 1 to 1 function that maps any integer to any rational number and vice
# versa, as a proof that there is a countably infinite number of rational numbers.
import math


def main():
    exit_program = False
    print("----------------------------------------")
    print("-----INTEGER/RATIONAL NUMBER MAPPER-----")
    print("----------------------------------------")
    print(
        "Enter an integer to find the corresponding rational number. Or enter a fraction to find the corresponding",
        "integer. Enter \"n\" to exit program.")
    while not exit_program:

        user_input = input("\nEnter your value: ")

        if user_input.lower() in ["n", "N", "exit"]:
            exit_program = True
        elif "/" not in user_input:
            n = int(user_input)

            # Get prime factorization of the integer
            factors = get_prime_factors(n)

            # Create set containing each unique prime factor
            factor_set = set()
            factor_set.update(factors)

            # Create a list of tuples, each tuple holds a prime factor and it's exponent
            factor_tuples = list()
            for x in factor_set:
                factor_tuples.append((x, factors.count(x)))

            # This block finds the rational number that corresponds with the integer
            m_total = 1
            n_total = 1

            for x in factor_tuples:
                if x[1] % 2 == 0:  # Checks if the exponent for this tuple is even
                    m_total *= (x[0]) ** (x[1] // 2)
                else:  # If the exponent is odd
                    n_total *= (x[0]) ** ((x[1] + 1) // 2)

            print(n, " corresponds to the rational number ", m_total, "/", n_total, sep="")

        elif "/" in user_input:

            fraction = [int(s) for s in user_input.split("/")]
            gcd = math.gcd(fraction[0], fraction[1])

            # Checks if the fraction is simplified, and if it is not will reduce it
            if (fraction[0] % gcd == 0 or fraction[1] % gcd == 0) and gcd != 1:
                fraction[0] //= gcd
                fraction[1] //= gcd
                print("Your fraction was reduced to ", fraction[0], "/", fraction[1], sep="")

            # Get prime factorization of numerator and denominator
            m = get_prime_factors(fraction[0])
            n = get_prime_factors(fraction[1])

            # create sets containing each unique prime factor
            m_set = set()
            m_set.update(m)
            n_set = set()
            n_set.update(n)

            # Creates a list of tuples, each tuple holds a prime factor and its exponent
            m_tuples = list()
            n_tuples = list()

            for x in m_set:
                m_tuples.append((x, m.count(x)))
            for y in n_set:
                n_tuples.append((y, n.count(y)))

            # This block finds the integer that corresponds to the rational number
            m_total = 1
            n_total = 1

            for x in m_tuples:
                m_total *= (x[0]) ** (2 * x[1])
            for y in n_tuples:
                n_total *= (y[0]) ** ((2 * y[1]) - 1)

            print(fraction[0], "/", fraction[1], ' corresponds to ', m_total * n_total, sep="")

    print("Program exiting.")


# from https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/, modified to store values to a list
def get_prime_factors(num):
    my_list = list()
    # Print the number of two's that divide n
    while num % 2 == 0:
        my_list.append(2)
        num = num / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(num)) + 1, 2):

        # while i divides n , print i and divide n
        while num % i == 0:
            my_list.append(int(i))

            num = num / i

    # Condition if n is a prime number greater than 2
    if num > 2:
        my_list.append(int(num))

    return my_list


if __name__ == "__main__":
    main()
