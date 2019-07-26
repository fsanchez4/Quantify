"""
Main :: Quantify
Quantifying the health of a small business
By Frankie Sanchez :: 900942699
"""

from SBHealth import SBHealth


def main():
    # Create new business for analysis
    frankie = SBHealth()
    frankie.add_business()
    frankie.final_results()
    print()

    # Reporting #1 - Print results & create DB
    frankie.print_results()
    frankie.create_report()
    frankie.create_db()
    print()
    #
    # # Add data to existing DB
    # frankie.add_new_data_db()
    # frankie.final_results()
    # print()
    #
    # # Reporting #2 - Print results
    # frankie.print_results()
    # frankie.create_report()
    # print()


if __name__ == '__main__':
    main()

