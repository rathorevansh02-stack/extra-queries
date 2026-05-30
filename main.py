from db_connection import get_connection
from sql_setup import build_database
import queries

def execute_pipeline():
    conn = get_connection()
    if conn is None: 
        return

    # Build schema and inject starter records
    build_database(conn)

    print("\n==================================================")
    print("RUNNING EXERCISE SUITE: 12 CORE WORKSPACE QUERIES")
    print("==================================================")

    # --- Query 1 ---
    print("\n[QUERY 1] List All Registered Companies:")
    for row in queries.query_1_all_companies(conn):
        print(f"ID: {row[0]} | Company: {row[1]:<12} | Country: {row[2]:<10} | Industry: {row[3]}")

    # --- Query 2 ---
    print("\n[QUERY 2] Students Older Than 21:")
    for row in queries.query_2_students_older_than_21(conn):
        print(f"Student Name: {row[0]:<10} | Age: {row[1]}")

    # --- Query 3 ---
    print("\n[QUERY 3] Job Listings with Salary > $80,000:")
    for row in queries.query_3_high_salary_jobs(conn):
        print(f"Title: {row[0]:<20} | Salary: ${row[1]}")

    # --- Query 4 ---
    print("\n[QUERY 4] Applications with Status Matching 'Offered':")
    for row in queries.query_4_offered_applications(conn):
        print(f"Application ID: {row[0]} | Current Status: {row[1]}")

    # --- Query 5 ---
    print("\n[QUERY 5] INNER JOIN - Mapping Student Profiles to Applications:")
    for row in queries.query_5_inner_join_student_apps(conn):
        print(f"Student: {row[0]:<10} -> Application Status: {row[1]}")

    print("\n[QUERY 6] INNER JOIN - Mapping Job Openings to Hosting Companies:")
    for row in queries.query_6_join_jobs_and_companies(conn):
        print(f"Role: {row[0]:<20} | Company: {row[1]}")

    print("\n[QUERY 7] 3-TABLE INNER JOIN - Complete Application Pipeline Grid:")
    for row in queries.query_7_three_table_master_join(conn):
        print(f"Applicant: {row[0]:<10} | Targeted Role: {row[1]:<20} | Stage: {row[2]}")

    print("\n[QUERY 8] LEFT OUTER JOIN - Comprehensive Company Job Deployment List:")
    for row in queries.query_8_left_join_all_companies(conn):
        role_listing = row[1] if row[1] else "No active job listings posted"
        print(f"Company Node: {row[0]:<12} | Opening: {role_listing}")

    print("\n[QUERY 9] ADVANCED CURSOR LOOP - Sequential Row Fetch Stream:")
    for row in queries.query_9_cursor_fetchone_stream(conn):
        print(f"Streaming Row Data -> Node Name: {row[0]:<12} | Field: {row[1]}")

    print("\n[QUERY 10] ADVANCED CURSOR BATCH - Segmented Fetchmany Blocks:")
    for row in queries.query_10_cursor_fetchmany_batch(conn):
        print(f"Batch Row Extraction -> Student: {row[0]:<10} | Origin: {row[1]}")

    print("\n[QUERY 11] TRIGGER STAGE A - Dispatching Raw Mutation Insert Query...")
    status_msg = queries.query_11_insert_trigger_test(conn)
    print(status_msg)

    print("\n[QUERY 12] TRIGGER STAGE B - Verifying Capitilization Auto-Formatting:")
    for row in queries.query_12_verify_trigger_modification(conn):
        print(f"Student ID Reference: {row[0]} | Job Reference: {row[1]}")
        print(f"Notice Status Result conversion: '{row[2]}' (Auto-capitalized from 'interviewing')")

    print("\n==================================================")
    conn.close()
    print("Database session ended. Data tunnel closed cleanly.")

if __name__ == "__main__":
    execute_pipeline()