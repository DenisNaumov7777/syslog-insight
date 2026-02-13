import argparse
import sys
from src.analyzer import LogAnalyzer

def main():
    # Initialize argument parser for CLI usage
    parser = argparse.ArgumentParser(
        description="Syslog Insight: A tool to analyze system logs and generate error reports."
    )
    
    parser.add_argument(
        "--input", "-i", 
        type=str, 
        default="data/syslog.log", 
        help="Path to the input log file (default: data/syslog.log)"
    )
    parser.add_argument(
        "--output", "-o", 
        type=str, 
        default="error_report.csv", 
        help="Path to the output CSV report (default: error_report.csv)"
    )

    args = parser.parse_args()

    print(f"Starting analysis on file: {args.input}...")

    try:
        # Initialize the analyzer
        analyzer = LogAnalyzer(args.input)
        
        # Run analysis
        analyzer.analyze()
        
        # Output summary to console
        print("\n--- Top Errors Found ---")
        top_errors = analyzer.get_top_errors(5)
        
        if not top_errors:
            print("No errors found.")
        else:
            for error, count in top_errors:
                print(f"Count: {count:<4} | Error: {error}")
        print("------------------------\n")

        # Export full report
        analyzer.export_to_csv(args.output)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()