import analysis.csv as csv
import analysis.xml as xml
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", help="""Type of file to analyse. Is it a CSV or an XML?""")
    #parser.add_argument("-d",  "--datafile", help="""CSV file containing pieces of information about the members of parliament""")
    return parser.parse_args()


def main():
    args = parse_arguments()
    #datafile = args.datafile
    if args.extension == "xml":
        xml.launch_analysis('SyceronBrut.xml')
    elif args.extension == "csv":
        csv.launch_analysis('current_mps.csv')
    
    
    

if __name__ == "__main__":
    main()
    