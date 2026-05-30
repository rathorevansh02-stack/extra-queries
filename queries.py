
def query_1_all_companies(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM companies;")
    results = cursor.fetchall()
    cursor.close()
    return results

def query_2_students_older_than_21(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name, age FROM students WHERE age > 21;")
    results = cursor.fetchall()
    cursor.close()
    return results

def query_3_high_salary_jobs(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT title, salary FROM jobs WHERE salary > 80000;")
    results = cursor.fetchall()
    cursor.close()
    return results

def query_4_offered_applications(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, status FROM applications WHERE status = 'Offered';")
    results = cursor.fetchall()
    cursor.close()
    return results


def query_5_inner_join_student_apps(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT students.name, applications.status 
        FROM students
        INNER JOIN applications ON students.id = applications.student_id;
    """)
    results = cursor.fetchall()
    cursor.close()
    return results

def query_6_join_jobs_and_companies(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT jobs.title, companies.company_name 
        FROM jobs
        INNER JOIN companies ON jobs.company_id = companies.id;
    """)
    results = cursor.fetchall()
    cursor.close()
    return results

def query_7_three_table_master_join(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT students.name, jobs.title, applications.status
        FROM applications
        INNER JOIN students ON applications.student_id = students.id
        INNER JOIN jobs ON applications.job_id = jobs.id;
    """)
    results = cursor.fetchall()
    cursor.close()
    return results

def query_8_left_join_all_companies(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT companies.company_name, jobs.title 
        FROM companies
        LEFT JOIN jobs ON companies.id = jobs.company_id;
    """)
    results = cursor.fetchall()
    cursor.close()
    return results


def query_9_cursor_fetchone_stream(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT company_name, industry FROM companies;")
    
    output_rows = []
    row = cursor.fetchone()
    while row is not None:
        output_rows.append(row)
        row = cursor.fetchone()
        
    cursor.close()
    return output_rows

def query_10_cursor_fetchmany_batch(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name, country FROM students;")
    
    output_rows = []
    # Fetch batches of 4 records at a time
    batch = cursor.fetchmany(4)
    while batch:
        for row in batch:
            output_rows.append(row)
        batch = cursor.fetchmany(4)
        
    cursor.close()
    return output_rows


def query_11_insert_trigger_test(conn):
    
    cursor = conn.cursor()
    # We type 'interviewing' in all lowercase to test the trigger formatting
    cursor.execute("""
        INSERT INTO applications (student_id, job_id, status) 
        VALUES (10, 4, 'interviewing');
    """)
    conn.commit()
    cursor.close()
    return "New application record submitted with uncleaned lowercase data."

def query_12_verify_trigger_modification(conn):
    
    cursor = conn.cursor()
    cursor.execute("""
        SELECT student_id, job_id, status 
        FROM applications 
        WHERE student_id = 10 AND job_id = 4;
    """)
    results = cursor.fetchall()
    cursor.close()
    return results