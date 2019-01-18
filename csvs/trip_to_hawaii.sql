# database
#CREATE DATABASE trip_to_hawaii;
USE trip_to_hawaii;

-- Create Two Tables
CREATE TABLE hotel (
  id INT PRIMARY KEY,
  hotel_name TEXT,
  price_per_night TEXT
);

CREATE TABLE rentals (
  id INT PRIMARY KEY,
  rental_name TEXT,
  price_per_night TEXT
);

CREATE TABLE restaurants (
  id INT PRIMARY KEY,
  res_name TEXT,
  rating TEXT
);