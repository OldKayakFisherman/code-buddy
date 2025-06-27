
from sqlmodel import Field, SQLModel

class APIType(SQLModel, table=True):

    __tablename__ = "api_types"

    id: int | None = Field(default=None, primary_key=True)
    name: str | None

class UIType(SQLModel, table=True):

    __tablename__ = "ui_types"

    id: int | None = Field(default=None, primary_key=True)
    name: str | None


"""

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


"""