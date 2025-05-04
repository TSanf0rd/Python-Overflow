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

CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    message TEXT,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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

-- Add new libraries
INSERT INTO library (lib_id, category, lib_name, lib_description, license, install_instructions, author, doc_url)
VALUES
(3, 'Visualization', 'Matplotlib', 'Comprehensive library for creating static, animated, and interactive plots.', 'PSF', 'pip install matplotlib', 'John Hunter', 'https://matplotlib.org/stable/contents.html'),
(4, 'Machine Learning', 'Scikit-learn', 'Simple and efficient tools for predictive data analysis and modeling.', 'BSD', 'pip install scikit-learn', 'INRIA', 'https://scikit-learn.org/stable/'),
(5, 'Networking', 'Requests', 'Elegant and simple HTTP library for Python, built for human beings.', 'Apache 2.0', 'pip install requests', 'Kenneth Reitz', 'https://requests.readthedocs.io/en/latest/');

-- Add functions
INSERT INTO function (func_name, source_code, func_description, lib_id)
VALUES
('plot', NULL, 'Plots y vs. x as lines and/or markers.', 3),
('fit', NULL, 'Fits the model to training data.', 4),
('get', NULL, 'Sends a GET request to the specified URL.', 5);

-- Add types
INSERT INTO types (type_name, type_code, type_description, lib_id)
VALUES
('Figure', NULL, 'Top-level container for all plot elements.', 3),
('Estimator', NULL, 'Base class for all estimators in scikit-learn.', 4),
('Response', NULL, 'The response object returned by requests.', 5);

-- Add modules
INSERT INTO modules (mod_id, mod_name, mod_code, mod_description, lib_id)
VALUES
(3, 'matplotlib.pyplot', NULL, 'Provides a MATLAB-like plotting framework.', 3),
(4, 'sklearn.linear_model', NULL, 'Implements linear regression models.', 4),
(5, 'requests.api', NULL, 'Core HTTP methods for Requests.', 5);

-- Add versions
INSERT INTO version (version_id, release_date, change_log, lib_id)
VALUES
(3, '2023-02-01', 'Added support for interactive figures.', 3),
(4, '2023-04-10', 'Improved accuracy of classifiers.', 4),
(5, '2023-05-12', 'Added support for HTTP/2.', 5);

-- Add contributors
INSERT INTO contributors (con_id, con, ver_id)
VALUES
(3, 'Michael Droettboom', 3),
(4, 'Gaël Varoquaux', 4),
(5, 'Kenneth Reitz', 5);

-- Add tags
INSERT INTO tag (tag_id, tag_name, description)
VALUES
(3, 'visualization', 'Used for rendering plots and charts.'),
(4, 'ml', 'Used for training and evaluating predictive models.'),
(5, 'http', 'Used for making web requests and handling responses.');

-- Map tags to libraries
INSERT INTO lib_tag (lib_id, tag_id)
VALUES
(3, 3),
(4, 4),
(5, 5);

-- Add dependencies
INSERT INTO dependency (lib_id, depend_id)
VALUES
(4, 2);  -- Scikit-learn depends on NumPy

