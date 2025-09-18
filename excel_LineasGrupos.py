import pandas as pd
from DB_LineasGrupos import LineasGrupos
from tkinter import messagebox

def import_excel_data(db_params, excel_file_path):
    """
    Import data from Excel file to database using LineasGrupos class
    
    Args:
        db_params (dict): Database connection parameters
        excel_file_path (str): Path to the Excel file
    """
    try:
        # Read the Excel file
        df = pd.read_excel(excel_file_path, sheet_name='TABLAS', header=None)
        
        # Create database connection
        db = LineasGrupos(**db_params)
        
        current_line_code = None
        current_line_name = None
        imported_lines = 0
        imported_groups = 0
        
        print("Starting data import...")
        
        # First, let's check if the default line "1" exists and update it if needed
        try:
            with db.conn.cursor() as cur:
                # Check if default line exists and has the wrong name
                cur.execute("SELECT nombre FROM lineas WHERE codigo = %s;", ("1",))
                result = cur.fetchone()
                if result and result[0] == "Linea 1":
                    # Update the default line name to match Excel
                    cur.execute("UPDATE lineas SET nombre = %s WHERE codigo = %s;", ("ESTOPERAS", "1"))
                    db.conn.commit()
                    print("✓ Updated default line name from 'Linea 1' to 'ESTOPERAS'")
                
                # Check if default group exists and has the wrong name
                cur.execute("SELECT nombre FROM grupos WHERE codigo = %s;", ("1.1",))
                result = cur.fetchone()
                if result and result[0] == "Grupo 1":
                    # Update the default group name to match Excel
                    cur.execute("UPDATE grupos SET nombre = %s WHERE codigo = %s;", ("ESTOPERAS", "1.1"))
                    db.conn.commit()
                    print("✓ Updated default group name from 'Grupo 1' to 'ESTOPERAS'")
        except Exception as e:
            print(f"Warning: Could not check/update default items: {e}")
            db.conn.rollback()
        
        # Iterate through each row in the Excel file
        for index, row in df.iterrows():
            # Skip empty rows
            if pd.isna(row[0]):
                continue
                
            # Convert to appropriate types
            line_code = str(int(row[0]))  # Column A
            group_code = str(int(row[1])) if not pd.isna(row[1]) else None  # Column B
            name = str(row[2]) if not pd.isna(row[2]) else ""  # Column C
            
            # Check if this is a line (group_code = 0)
            if group_code == '0':
                current_line_code = line_code
                current_line_name = name
                
                # For line "1", we might already have it from default initialization
                if current_line_code == "1":
                    # Just update the name if it's different
                    try:
                        with db.conn.cursor() as cur:
                            cur.execute("SELECT nombre FROM lineas WHERE codigo = %s;", (current_line_code,))
                            result = cur.fetchone()
                            if result and result[0] != current_line_name:
                                cur.execute("UPDATE lineas SET nombre = %s WHERE codigo = %s;", 
                                           (current_line_name, current_line_code))
                                db.conn.commit()
                                print(f"✓ Updated line: {current_line_code} - {current_line_name}")
                    except:
                        pass
                    continue
                
                # For other lines, check if they exist
                if not db.CheckLineNM(current_line_code):
                    # Add the new line without groups
                    if db.Add_LineNM(current_line_code, current_line_name):
                        imported_lines += 1
                        print(f"✓ Added line: {current_line_code} - {current_line_name}")
                else:
                    print(f"→ Line exists: {current_line_code} - {current_line_name}")
            
            # Otherwise, it's a group for the current line
            elif current_line_code is not None and group_code is not None:
                # Get percentages (handle possible NaN values)
                p1 = float(row[3]) if not pd.isna(row[3]) else 0.0
                p2 = float(row[4]) if not pd.isna(row[4]) else 0.0
                p3 = float(row[5]) if not pd.isna(row[5]) else 0.0
                
                # Create full group code (line_code.group_code)
                full_group_code = f"{current_line_code}.{group_code}"
                
                # For group "1.1", we might already have it from default initialization
                if full_group_code == "1.1":
                    # Update the group if it exists with default values
                    try:
                        with db.conn.cursor() as cur:
                            cur.execute("""
                                UPDATE grupos SET 
                                    nombre = %s, 
                                    porcentaje1 = %s, 
                                    porcentaje2 = %s, 
                                    porcentaje3 = %s 
                                WHERE codigo = %s;
                            """, (name, p1, p2, p3, full_group_code))
                            db.conn.commit()
                            print(f"✓ Updated group: {full_group_code} - {name}")
                    except:
                        pass
                    continue
                
                # Check if group already exists
                if not db.CheckGrupoNM(current_line_code, full_group_code):
                    # Add the new group
                    if db.Add_GroupNM(current_line_code, group_code, name, p1, p2, p3):
                        imported_groups += 1
                        print(f"✓ Added group: {full_group_code} - {name}")
                else:
                    # Update existing group with new percentages if needed
                    try:
                        with db.conn.cursor() as cur:
                            cur.execute("""
                                UPDATE grupos SET 
                                    porcentaje1 = %s, 
                                    porcentaje2 = %s, 
                                    porcentaje3 = %s 
                                WHERE codigo = %s;
                            """, (p1, p2, p3, full_group_code))
                            db.conn.commit()
                            print(f"✓ Updated percentages for group: {full_group_code}")
                    except:
                        pass
                    print(f"→ Group exists: {full_group_code} - {name}")
        
        # Show summary
        summary = (
            f"Import completed successfully!\n\n"
            f"Lines imported: {imported_lines}\n"
            f"Groups imported: {imported_groups}\n"
            f"Total items: {imported_lines + imported_groups}"
        )
        
        print(f"\n{summary}")
        messagebox.showinfo("Import Complete", summary)
        
    except Exception as e:
        error_msg = f"Error during import: {str(e)}"
        print(f"ERROR: {error_msg}")
        messagebox.showerror("Import Error", error_msg)

# Database connection parameters - UPDATE THESE WITH YOUR ACTUAL CREDENTIALS
db_params = {
    'dbname': 'AppDatabase',
    'user': 'postgres',
    'password': 'admin1234',
    'host': 'localhost',
    'port': '5432'
}

# Path to your Excel file - UPDATE THIS WITH YOUR ACTUAL FILE PATH
excel_file_path = 'Tabla_LineasGrupos.xls'

# Run the import
if __name__ == "__main__":
    print("Excel Data Import Tool")
    print("=" * 50)
    
    # Run the import function
    import_excel_data(db_params, excel_file_path)