def build_database(conn):
    """Drops old components and creates the 4-table schema with a trigger."""
    cursor = conn.cursor()
    
    print("Cleaning up any old database components...")
    cursor.execute("DROP TABLE IF EXISTS applications CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS jobs CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS students CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS companies CASCADE;")
    
    # Drop trigger and function if they existed before
    cursor.execute("DROP TRIGGER IF EXISTS trg_clean_status ON applications;")
    cursor.execute("DROP FUNCTION IF EXISTS t_clean_application_status();")
    
    print("Creating fresh relational practice tables...")
    
    cursor.execute("""
    CREATE TABLE companies (
        id SERIAL PRIMARY KEY,
        company_name VARCHAR(100) NOT NULL,
        country VARCHAR(50) NOT NULL,
        industry VARCHAR(100) NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        country VARCHAR(50) NOT NULL,
        age INT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE jobs (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        salary INT NOT NULL,
        location VARCHAR(50) NOT NULL,
        company_id INT REFERENCES companies(id) ON DELETE CASCADE
    );
    """)

    cursor.execute("""
    CREATE TABLE applications (
        id SERIAL PRIMARY KEY,
        student_id INT REFERENCES students(id) ON DELETE CASCADE,
        job_id INT REFERENCES jobs(id) ON DELETE CASCADE,
        application_date DATE DEFAULT CURRENT_DATE,
        status VARCHAR(50) DEFAULT 'Applied'
    );
    """)
    
    print("Creating automated database trigger mechanics...")
    
    # 1. Create the Trigger Function
    cursor.execute("""
    CREATE OR REPLACE FUNCTION t_clean_application_status()
    RETURNS TRIGGER AS $$
    BEGIN
       
        NEW.status = INITCAP(NEW.status);
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    """)
    
    # 2. Bind the Function to the Applications Table
    cursor.execute("""
    CREATE TRIGGER trg_clean_status
    BEFORE INSERT ON applications
    FOR EACH ROW
    EXECUTE FUNCTION t_clean_application_status();
    """)
    
    print("Seeding 10 complete baseline rows into each table...")
    
    # Insert Companies
    cursor.execute("""
    INSERT INTO companies (company_name, country, industry) VALUES 
    ('Google', 'USA', 'Technology'),
    ('TCS', 'India', 'IT Services'),
    ('Microsoft', 'USA', 'Technology'),
    ('Infosys', 'India', 'IT Services'),
    ('Amazon', 'USA', 'E-commerce'),
    ('Accenture', 'Ireland', 'Consulting'),
    ('Meta', 'USA', 'Social Media'),
    ('Wipro', 'India', 'IT Services'),
    ('Netflix', 'USA', 'Entertainment'),
    ('Capgemini', 'France', 'Consulting');
    """)

    # Insert Students
    cursor.execute("""
    INSERT INTO students (name, country, age) VALUES 
    ('Rudra', 'India', 20),
    ('Vishu', 'India', 23),
    ('raju', 'India', 21),
    ('Jetha lal', 'USA', 22),
    ('Pappu', 'India', 19),
    ('modi', 'UK', 24),
    ('Rahul', 'India', 22),
    ('rajesh', 'Germany', 21),
    ('daa', 'India', 20),
    ('lallu', 'Canada', 23);
    """)

    # Insert Jobs
    cursor.execute("""
    INSERT INTO jobs (title, salary, location, company_id) VALUES 
    ('Software Engineer', 120000, 'Remote', 1),   
    ('Data Analyst', 80000, 'Pune', 1),          
    ('System Engineer', 45000, 'Mumbai', 2),     
    ('Cloud Architect', 140000, 'Seattle', 3),    
    ('Java Developer', 50000, 'Bangalore', 4),   
    ('Web Developer', 95000, 'Remote', 5),       
    ('IT Consultant', 70000, 'Delhi', 6),        
    ('Data Scientist', 130000, 'New York', 7),   
    ('DevOps Engineer', 55000, 'Hyderabad', 8),  
    ('QA Automation', 110000, 'Los Angeles', 9); 
    """)

    # Insert Applications
    cursor.execute("""
    INSERT INTO applications (student_id, job_id, application_date, status) VALUES 
    (1, 1, '2026-05-20', 'Interviewing'), 
    (1, 2, '2026-05-21', 'Applied'),      
    (2, 3, '2026-05-22', 'Applied'),      
    (3, 2, '2026-05-22', 'Rejected'),     
    (4, 4, '2026-05-23', 'Offered'),      
    (5, 5, '2026-05-24', 'Applied'),      
    (6, 8, '2026-05-25', 'Interviewing'), 
    (7, 3, '2026-05-25', 'Applied'),      
    (8, 10, '2026-05-26', 'Applied'),     
    (9, 7, '2026-05-27', 'Offered');      
    """)
    
    conn.commit()
    cursor.close()
    print("Database setup initialization completed successfully.")  