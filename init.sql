-- ENTITIES
CREATE TABLE IF NOT EXISTS library (
    lib_id INT NOT NULL PRIMARY KEY,
    category VARCHAR(50),
    lib_name VARCHAR(50) NOT NULL,
    lib_description TEXT NOT NULL,
    license VARCHAR(50) NOT NULL,
    install_instructions TEXT NOT NULL,
    author VARCHAR(50) NOT NULL,
    doc_url VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS function (
    func_name VARCHAR(50) NOT NULL PRIMARY KEY,
    source_code TEXT,
    func_description TEXT NOT NULL,
    lib_id INT NOT NULL,
    FOREIGN KEY (lib_id) REFERENCES library(lib_id)
);

CREATE TABLE IF NOT EXISTS types (
    type_name VARCHAR(50) NOT NULL PRIMARY KEY,
    type_code TEXT,
    type_description TEXT NOT NULL,
    lib_id INT NOT NULL,
    FOREIGN KEY (lib_id) REFERENCES library(lib_id)
);

CREATE TABLE IF NOT EXISTS modules (
    mod_id INT NOT NULL PRIMARY KEY,
    mod_name VARCHAR(50) NOT NULL,
    mod_code TEXT,
    mod_description TEXT NOT NULL,
    lib_id INT NOT NULL,
    FOREIGN KEY (lib_id) REFERENCES library(lib_id)
);

CREATE TABLE IF NOT EXISTS version (
    version_id INT NOT NULL PRIMARY KEY,
    release_date DATE NOT NULL,
    change_log TEXT NOT NULL,
    lib_id INT NOT NULL,
    FOREIGN KEY (lib_id) REFERENCES library(lib_id)
);

CREATE TABLE IF NOT EXISTS contributors (
    con_id INT NOT NULL,
    con VARCHAR(50) NOT NULL,
    ver_id INT NOT NULL,
    CONSTRAINT pk_contributors PRIMARY KEY (con_id, ver_id),
    FOREIGN KEY (ver_id) REFERENCES version(version_id)
);

CREATE TABLE IF NOT EXISTS tag (
    tag_id INT NOT NULL PRIMARY KEY,
    tag_name VARCHAR(50) NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS supported_versions (
    sup_vers_id INT NOT NULL,
    version_id INT NOT NULL,
    CONSTRAINT pk_supported_versions PRIMARY KEY (sup_vers_id, version_id),
    FOREIGN KEY (version_id) REFERENCES version(version_id)
);

-- RELATIONSHIPS
CREATE TABLE IF NOT EXISTS dependency (
    lib_id INT NOT NULL,
    depend_id INT NOT NULL,
    CONSTRAINT pk_dependency PRIMARY KEY (lib_id, depend_id),
    FOREIGN KEY (lib_id) REFERENCES library(lib_id),
    FOREIGN KEY (depend_id) REFERENCES library(lib_id)
);

CREATE TABLE IF NOT EXISTS lib_tag (
    lib_id INT NOT NULL,
    tag_id INT NOT NULL,
    CONSTRAINT pk_lib_tag PRIMARY KEY (lib_id, tag_id),
    FOREIGN KEY (lib_id) REFERENCES library(lib_id),
    FOREIGN KEY (tag_id) REFERENCES tag(tag_id)
);

-- SAMPLE DATA
INSERT INTO library (lib_id, category, lib_name, lib_description, license, install_instructions, author, doc_url)
VALUES
(1, 'Data Analysis', 'Pandas', 'Powerful data structures for data analysis, time series, and statistics.', 'BSD', 'pip install pandas', 'Wes McKinney', 'https://pandas.pydata.org/docs/'),
(2, 'Numerical Computing', 'NumPy', 'Package for scientific computing with multidimensional arrays.', 'BSD', 'pip install numpy', 'Travis Oliphant', 'https://numpy.org/doc/');

INSERT INTO function (func_name, source_code, func_description, lib_id)
VALUES
('read_csv', NULL, 'Reads a comma-separated values (csv) file into a DataFrame.', 1),
('array', NULL, 'Creates an array object in NumPy.', 2);

INSERT INTO types (type_name, type_code, type_description, lib_id)
VALUES
('DataFrame', NULL, '2-dimensional labeled data structure.', 1),
('ndarray', NULL, 'Multidimensional array object.', 2);

INSERT INTO modules (mod_id, mod_name, mod_code, mod_description, lib_id)
VALUES
(1, 'pandas.io.parsers', NULL, 'Contains parsers for reading CSV and other data files.', 1),
(2, 'numpy.linalg', NULL, 'Provides linear algebra routines.', 2);

INSERT INTO version (version_id, release_date, change_log, lib_id)
VALUES
(1, '2023-01-15', 'Improved IO performance in pandas.', 1),
(2, '2023-03-22', 'Added support for GPU-based array ops.', 2);

INSERT INTO contributors (con_id, con, ver_id)
VALUES
(1, 'Wes McKinney', 1),
(2, 'Travis Oliphant', 2);

INSERT INTO tag (tag_id, tag_name, description)
VALUES
(1, 'data-science', 'Used for analyzing and processing structured data.'),
(2, 'math', 'Used for numerical operations and linear algebra.');

INSERT INTO lib_tag (lib_id, tag_id)
VALUES
(1, 1),
(2, 2);

INSERT INTO dependency (lib_id, depend_id)
VALUES
(1, 2);
