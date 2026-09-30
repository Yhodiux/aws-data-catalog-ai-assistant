### 1. Concise Description of the Dataset

The dataset `nyc_311_sample` contains 5,000 records of complaints submitted to New York City's 311 service. The dataset includes details about the complaint, such as timestamps, location information, the agency responsible, complaint type, status, and resolution details. It also contains geographic coordinates and various identifiers related to the complaint's location and administrative divisions.

### 2. Technical Explanation of Each Column

| Column Name                        | Data Type  | Null Count | Null Percentage | Distinct Count | Description / Inference                                                                 |
|------------------------------------|------------|------------|-----------------|----------------|-----------------------------------------------------------------------------------------|
| `unique_key`                       | int64      | 0          | 0.0%            | 5000           | Unique identifier for each complaint record.                                             |
| `created_date`                     | str        | 0          | 0.0%            | 4322           | Date and time when the complaint was created. Format: `YYYY-MM-DDTHH:MM:SS.000`.        |
| `closed_date`                      | str        | 2807       | 56.14%          | 1399           | Date and time when the complaint was closed. Format: `YYYY-MM-DDTHH:MM:SS.000`.          |
| `agency`                           | str        | 0          | 0.0%            | 12             | Agency responsible for handling the complaint.                                            |
| `agency_name`                      | str        | 0          | 0.0%            | 12             | Full name of the agency responsible for handling the complaint.                           |
| `complaint_type`                   | str        | 0          | 0.0%            | 112            | Type of complaint submitted.                                                             |
| `descriptor`                       | str        | 53         | 1.06%           | 316            | Additional descriptor for the complaint type.                                             |
| `descriptor_2`                     | str        | 3144       | 62.88%          | 211            | Secondary descriptor for the complaint type.                                             |
| `location_type`                    | str        | 338        | 6.76%           | 50             | Type of location where the complaint occurred (e.g., street, sidewalk, subway).          |
| `incident_zip`                     | float64    | 54         | 1.08%           | 183            | ZIP code of the incident location.                                                       |
| `incident_address`                 | str        | 184        | 3.68%           | 3461           | Full address of the incident.                                                            |
| `street_name`                      | str        | 184        | 3.68%           | 1776           | Name of the street where the incident occurred.                                          |
| `cross_street_1`                   | str        | 1299       | 25.98%          | 1402           | First cross street of the incident location.                                             |
| `cross_street_2`                   | str        | 1299       | 25.98%          | 1423           | Second cross street of the incident location.                                            |
| `intersection_street_1`            | str        | 1217       | 24.34%          | 1404           | First street of the intersection where the incident occurred.                            |
| `intersection_street_2`            | str        | 1217       | 24.34%          | 1424           | Second street of the intersection where the incident occurred.                           |
| `address_type`                     | str        | 39         | 0.78%           | 5              | Type of address (e.g., ADDRESS, INTERSECTION, PLACE).                                    |
| `city`                             | str        | 238        | 4.76%           | 46             | City where the incident occurred.                                                        |
| `landmark`                         | str        | 1519       | 30.38%          | 1446           | Landmark near the incident location.                                                     |
| `facility_type`                    | str        | 4999       | 99.98%          | 1              | Type of facility related to the complaint. Mostly null, with one value: "DSNY Garage".   |
| `status`                           | str        | 0          | 0.0%            | 4              | Current status of the complaint (e.g., Open, Closed, In Progress).                       |
| `due_date`                         | str        | 4994       | 99.88%          | 6              | Date and time by which the complaint was due to be resolved. Format: `YYYY-MM-DDTHH:MM:SS.000`. |
| `resolution_description`           | str        | 1706       | 34.12%          | 57             | Description of the resolution actions taken for the complaint.                           |
| `resolution_action_updated_date`   | str        | 1699       | 33.98%          | 1472           | Date and time when the resolution action was last updated. Format: `YYYY-MM-DDTHH:MM:SS.000`. |
| `community_board`                  | str        | 0          | 0.0%            | 71             | Community board responsible for the area where the complaint occurred.                   |
| `council_district`                 | float64    | 95         | 1.9%            | 51             | City council district where the incident occurred.                                       |
| `police_precinct`                  | str        | 0          | 0.0%            | 78             | Police precinct responsible for the area where the complaint occurred.                    |
| `bbl`                              | float64    | 491        | 9.82%           | 3127           | Borough, Block, and Lot (BBL) number of the property related to the complaint.           |
| `borough`                          | str        | 0          | 0.0%            | 6              | Borough where the incident occurred.                                                     |
| `x_coordinate_state_plane`         | float64    | 72         | 1.44%           | 3409           | X-coordinate of the incident location in the State Plane coordinate system.              |
| `y_coordinate_state_plane`         | float64    | 71         | 1.42%           | 3466           | Y-coordinate of the incident location in the State Plane coordinate system.              |
| `open_data_channel_type`           | str        | 0          | 0.0%            | 4              | Channel through which the complaint was submitted (e.g., ONLINE, PHONE, MOBILE).         |
| `park_facility_name`               | str        | 0          | 0.0%            | 1              | Name of the park facility related to the complaint. Value is always "Unspecified".       |
| `park_borough`                     | str        | 0          | 0.0%            | 6