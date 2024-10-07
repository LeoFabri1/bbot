from bbot.modules.output.postgres_save import PostgresModule, Scan

scan = Scan(scan_id=1, scan_data={'example': 'data'})

if __name__ == "__main__":
    postgres_module = PostgresModule(scan=scan)

    # Sample results
    results = [
        {'data': 'Sample data 1'},
        {'data': 'Sample data 2'}
    ]

    postgres_module.save_results(results)
