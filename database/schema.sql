CREATE TABLE teams (
  team_id INT AUTO_INCREMENT PRIMARY KEY,
  team_name VARCHAR(100) NOT NULL,
  manager_name VARCHAR(100) NOT NULL
);

CREATE TABLE users (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(150) NOT NULL UNIQUE,
  role VARCHAR(50) NOT NULL,
  team_id INT,
  FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

CREATE TABLE mood_entries (
  entry_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  mood_value VARCHAR(20) NOT NULL,
  comment VARCHAR(255),
  entry_date DATE NOT NULL,
  entry_time TIME NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);