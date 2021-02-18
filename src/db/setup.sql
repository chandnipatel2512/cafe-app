-- Product table
CREATE TABLE product(
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price FLOAT NOT NULL
);

-- Courier table
CREATE TABLE courier(
    id VARCHAR(255) NOT NULL PRIMARY KEY, 
    name VARCHAR(255) NOT NULL, 
    phone VARCHAR(255) NOT NULL
);

-- Transaction table
CREATE TABLE transaction(
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    customer_address VARCHAR(500) NOT NULL,
    customer_phone VARCHAR(255) NOT NULL,
    courier_id VARCHAR(255) NULL,
    order_status VARCHAR(255) DEFAULT 'Preparing',
    FOREIGN KEY (courier_id) REFERENCES courier(id) ON DELETE SET NULL
);

-- Basket table
CREATE TABLE basket(
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    transaction_id VARCHAR(255) NOT NULL,
    product_id VARCHAR(255) NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    FOREIGN KEY (transaction_id) REFERENCES transaction(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE
);