with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
    input_data = input_file.read()
    data_rows = input_data.split('\n')
    header_line = data_rows[0]
    header_line += ',NumberOfYears\n'
    output_file.write(header_line)
    
    i = 1
    while i < len(data_rows):
        data_row = data_rows[i]
        if not data_row.strip():
            i += 1
            continue
        i += 1
        
        columns = data_row.split(',')
        if len(columns) < 4:
            continue
        
        start_date = columns[1]
        start_date_year = start_date.split("-")
        end_date = columns[2]
        end_date_year = end_date.split("-")
        study_mode = columns[3]
        duration = int(end_date_year[1]) - int(start_date_year[1])

        if study_mode == 'Full-Time':
            if duration > 4:
                columns.append(str(duration))
                for idx, col in enumerate(columns):
                    output_file.write(col)
                    if idx != len(columns) - 1: 
                        output_file.write(',')
                output_file.write('\n')  
        elif study_mode == 'Part-Time':
            if duration > 7:
                columns.append(str(duration))
                for idx, col in enumerate(columns):
                    output_file.write(col)
                    if idx != len(columns) - 1:
                        output_file.write(',')
                output_file.write('\n')   
