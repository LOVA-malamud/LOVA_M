DROP TABLE IF EXISTS support_tickets;
CREATE TABLE support_tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    priority TEXT,
    issue_score INTEGER
);
INSERT INTO support_tickets (customer_name, priority, issue_score) VALUES 
('Dana', 'high', 95),
('Omar', 'medium', 74),
('Noa', 'high', 88);

SELECT * FROM support_tickets 
WHERE priority = 'medium';

DELETE FROM support_tickets WHERE id = 3;

INSERT INTO support_tickets (customer_name, priority, issue_score) VALUES 
('LOVA', 'HIGH', 60);

SELECT * FROM support_tickets;
