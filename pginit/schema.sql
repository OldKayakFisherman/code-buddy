
CREATE TABLE api_types
(
    id SERIAL PRIMARY KEY,
    name text NOT NULL
);

CREATE TABLE ui_types
(
    id SERIAL PRIMARY KEY,
    name text NOT NULL
);

CREATE TABLE persistence_types
(
    id SERIAL PRIMARY KEY,
    name text NOT NULL
);

CREATE TABLE data_types
(
    id SERIAL PRIMARY KEY,
    name text NOT NULL
);

CREATE TABLE relation_types
(
    id SERIAL PRIMARY KEY,
    name text NOT NULL
);


CREATE TABLE projects
(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    api_type_id BIGINT NOT NULL,
    ui_type_id BIGINT NOT NULL,
    persistence_type_id  BIGINT NOT NULL,
    description TEXT,
    CONSTRAINT project_to_api_type_fk FOREIGN KEY(api_type_id) REFERENCES api_types (id),
    CONSTRAINT project_to_ui_type_fk FOREIGN KEY(ui_type_id) REFERENCES api_types (id),
    CONSTRAINT project_to_persistence_type_fk FOREIGN KEY(persistence_type_id) REFERENCES persistence_types (id)
);


CREATE TABLE models
(
    id SERIAL PRIMARY KEY,
    project_id BIGINT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    relates_to BIGINT,
    relationship_type_id BIGINT,
    global boolean not null default false,
    CONSTRAINT fk_mdls_to_project FOREIGN KEY(project_id) REFERENCES projects(id),
    CONSTRAINT fk_mdls_relates FOREIGN KEY(relates_to) REFERENCES models(id),
    CONSTRAINT fk_mdls_relates_type FOREIGN KEY(relationship_type_id) REFERENCES relation_types(id) 
);

CREATE TABLE attributes
(
    id SERIAL PRIMARY KEY,
    data_type_id BIGINT NOT NULL,
    max_length INT,
    nullable boolean default true,
    apply_default boolean default false,
    description TEXT,
    CONSTRAINT fk_att_to_data_types FOREIGN KEY(data_type_id) REFERENCES data_types(id)

);


-- Insert our API types
INSERT INTO api_types (name) VALUES ('FastAPI');

-- Insert our UI types
INSERT INTO ui_types (name) VALUES ('Vue');

-- Insert our persistence types
INSERT INTO persistence_types (name) VALUES ('Postgresql');

-- Insert our data types
INSERT INTO data_types (name) VALUES ('String');
INSERT INTO data_types (name) VALUES ('Short');
INSERT INTO data_types (name) VALUES ('Integer');
INSERT INTO data_types (name) VALUES ('Long');
INSERT INTO data_types (name) VALUES ('Datetime');
INSERT INTO data_types (name) VALUES ('Date');
INSERT INTO data_types (name) VALUES ('Timestamp');
INSERT INTO data_types (name) VALUES ('Boolean');
INSERT INTO data_types (name) VALUES ('Block');
INSERT INTO data_types (name) VALUES ('Float');
INSERT INTO data_types (name) VALUES ('Geo Point');
INSERT INTO data_types (name) VALUES ('JSON');

-- Insert our Relationship Types
INSERT INTO relation_types (name) VALUES ('One-To-Many');
INSERT INTO relation_types (name) VALUES ('Many-To-Many');


