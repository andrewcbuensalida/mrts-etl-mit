USE mrts;
CREATE TABLE naics_code (
        id INT AUTO_INCREMENT PRIMARY KEY,
        naics_code VARCHAR(255)
    );

CREATE TABLE kind_of_business (
        id INT AUTO_INCREMENT PRIMARY KEY,
        kind_of_business VARCHAR(255)
    );

CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sales_amount DECIMAL(10, 2),
    month INT,
    year INT,
    kind_of_business_id INT,
    FOREIGN KEY (kind_of_business_id) REFERENCES kind_of_business(id)
);

CREATE TABLE naics_kind_of_business_association (
    naics_code_id INT,
    kind_of_business_id INT,
    FOREIGN KEY (naics_code_id) REFERENCES naics_code(id),
    FOREIGN KEY (kind_of_business_id) REFERENCES kind_of_business(id)
);