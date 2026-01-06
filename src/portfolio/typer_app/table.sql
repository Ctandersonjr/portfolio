CREATE TABLE IF NOT EXISTS typer_table (
    UserID INT Primary Key,
    Name TEXT NOT NULL,
    Password TEXT NOT NULL
);


INSERT INTO typer_table (UserID, Name, Password)
VALUES (1, Cedric, cedspass),
       (2, Tory, toryspass);