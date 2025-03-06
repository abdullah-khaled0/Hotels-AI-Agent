INSERT INTO Hotels (name, address, city, country, phone, email, star_rating)
VALUES
('Nile View Hotel', '25 Corniche El Nil, Cairo', 'Cairo', 'Egypt', '+20 2 25778899', 'info@nileviewhotel.com', 5),
('Red Sea Resort', '123 Beach Road, Hurghada', 'Hurghada', 'Egypt', '+20 65 3445566', 'reservations@redsearesort.com', 4),
('Luxor Palace', '10 Karnak Street, Luxor', 'Luxor', 'Egypt', '+20 95 2277889', 'contact@luxorpalace.com', 4),
('Pyramids Grand Hotel', '12 Sphinx Street, Giza', 'Giza', 'Egypt', '+20 2 33445566', 'info@pyramidsgrand.com', 5),
('Sharm El Sheikh Oasis', '45 Naama Bay, Sharm El Sheikh', 'Sharm El Sheikh', 'Egypt', '+20 69 3601234', 'reservations@sharmoasis.com', 4),
('Aswan Paradise', '8 Nile Corniche, Aswan', 'Aswan', 'Egypt', '+20 97 2314567', 'contact@aswanparadise.com', 3);

INSERT INTO Rooms (hotel_id, room_number, room_type, price_per_night, capacity, is_available)
VALUES
(1, '101', 'Standard', 1200.00, 2, TRUE),
(1, '102', 'Deluxe', 2000.00, 4, TRUE),
(1, '103', 'Suite', 3500.00, 6, FALSE),
(2, '201', 'Standard', 1000.00, 2, TRUE),
(2, '202', 'Deluxe', 1800.00, 4, TRUE),
(3, '301', 'Standard', 1100.00, 2, TRUE),
(3, '302', 'Suite', 3000.00, 6, FALSE),
(1, '104', 'Standard', 1300.00, 2, TRUE),
(1, '105', 'Deluxe', 2200.00, 4, FALSE),
(1, '106', 'Suite', 4000.00, 6, TRUE),
(2, '203', 'Standard', 1100.00, 2, TRUE),
(2, '204', 'Deluxe', 1900.00, 4, TRUE),
(2, '205', 'Suite', 3200.00, 6, FALSE),
(3, '303', 'Standard', 1200.00, 2, TRUE),
(3, '304', 'Deluxe', 2100.00, 4, TRUE),
(3, '305', 'Suite', 3800.00, 6, FALSE),
(4, '401', 'Standard', 1400.00, 2, TRUE),
(4, '402', 'Deluxe', 2300.00, 4, TRUE),
(4, '403', 'Suite', 4200.00, 6, FALSE),
(5, '501', 'Standard', 1500.00, 2, TRUE),
(5, '502', 'Deluxe', 2400.00, 4, TRUE),
(5, '503', 'Suite', 4500.00, 6, FALSE);

INSERT INTO Guests (first_name, last_name, email, phone, address, city, country)
VALUES
('Ahmed', 'Mohamed', 'ahmed.mohamed@example.com', '+20 100 123 4567', '15 Tahrir Square, Cairo', 'Cairo', 'Egypt'),
('Fatima', 'Ali', 'fatima.ali@example.com', '+20 122 987 6543', '22 Zamalek, Cairo', 'Cairo', 'Egypt'),
('Youssef', 'Hassan', 'youssef.hassan@example.com', '+20 111 555 4444', '10 Alexandria Road, Alexandria', 'Alexandria', 'Egypt'),
('Layla', 'Mahmoud', 'layla.mahmoud@example.com', '+20 102 333 2222', '5 Saad Zaghloul Street, Luxor', 'Luxor', 'Egypt'),
('Mahmoud', 'Rashad', 'mahmoud.rashad@example.com', '+20 100 111 2222', '30 Ramses Street, Cairo', 'Cairo', 'Egypt'),
('Nour', 'Samir', 'nour.samir@example.com', '+20 122 333 4444', '14 Maadi, Cairo', 'Cairo', 'Egypt'),
('Hassan', 'Kamal', 'hassan.kamal@example.com', '+20 111 555 6666', '22 El Geish Road, Alexandria', 'Alexandria', 'Egypt'),
('Sara', 'Hany', 'sara.hany@example.com', '+20 102 777 8888', '8 El Karnak Street, Luxor', 'Luxor', 'Egypt'),
('Ali', 'Fathi', 'ali.fathi@example.com', '+20 100 999 0000', '5 El Montaza, Alexandria', 'Alexandria', 'Egypt'),
('Mona', 'Adel', 'mona.adel@example.com', '+20 122 123 4567', '10 El Tahrir Street, Aswan', 'Aswan', 'Egypt');

INSERT INTO Reservations (guest_id, room_id, check_in_date, check_out_date, total_price, status)
VALUES
(1, 1, '2023-11-01', '2023-11-05', 4800.00, 'Confirmed'),
(2, 2, '2023-11-10', '2023-11-15', 10000.00, 'Confirmed'),
(3, 5, '2023-12-20', '2023-12-25', 9000.00, 'Pending'),
(4, 7, '2023-11-15', '2023-11-20', 15000.00, 'Confirmed'),
(5, 4, '2023-11-12', '2023-11-17', 6500.00, 'Confirmed'),
(6, 8, '2023-12-01', '2023-12-05', 4400.00, 'Pending'),
(7, 10, '2023-11-20', '2023-11-25', 11500.00, 'Confirmed'),
(8, 12, '2023-12-10', '2023-12-15', 12600.00, 'Confirmed'),
(9, 14, '2023-11-18', '2023-11-22', 9600.00, 'Pending'),
(10, 15, '2023-12-05', '2023-12-10', 22500.00, 'Confirmed');

INSERT INTO Staff (hotel_id, first_name, last_name, role, phone, email, hire_date)
VALUES
(1, 'Omar', 'Sayed', 'Receptionist', '+20 100 222 3333', 'omar.sayed@nileviewhotel.com', '2020-05-01'),
(1, 'Mona', 'Ibrahim', 'Housekeeping Manager', '+20 122 444 5555', 'mona.ibrahim@nileviewhotel.com', '2019-08-15'),
(2, 'Karim', 'Adel', 'Chef', '+20 111 666 7777', 'karim.adel@redsearesort.com', '2021-03-10'),
(3, 'Nadia', 'Fawzy', 'Concierge', '+20 102 888 9999', 'nadia.fawzy@luxorpalace.com', '2022-07-20'),
(2, 'Samir', 'Fouad', 'Receptionist', '+20 100 222 3333', 'samir.fouad@redsearesort.com', '2021-06-01'),
(3, 'Lina', 'Magdy', 'Housekeeping Manager', '+20 122 444 5555', 'lina.magdy@luxorpalace.com', '2020-09-15'),
(4, 'Tarek', 'Nabil', 'Chef', '+20 111 666 7777', 'tarek.nabil@pyramidsgrand.com', '2022-04-10'),
(5, 'Dina', 'Youssef', 'Concierge', '+20 102 888 9999', 'dina.youssef@sharmoasis.com', '2023-01-20');

INSERT INTO Payments (reservation_id, payment_date, amount, payment_method, status)
VALUES
(1, '2023-10-25 14:30:00', 4800.00, 'Credit Card', 'Completed'),
(2, '2023-10-28 10:15:00', 10000.00, 'Bank Transfer', 'Completed'),
(4, '2023-11-01 09:00:00', 15000.00, 'Cash', 'Completed'),
(5, '2023-11-10 12:00:00', 6500.00, 'Credit Card', 'Completed'),
(7, '2023-11-18 09:30:00', 11500.00, 'Bank Transfer', 'Completed'),
(8, '2023-12-05 14:45:00', 12600.00, 'Cash', 'Completed'),
(10, '2023-12-01 10:15:00', 22500.00, 'Credit Card', 'Completed');

INSERT INTO Services (name, description, price)
VALUES
('Breakfast Buffet', 'Daily breakfast buffet with Egyptian and international cuisine', 150.00),
('Spa Access', 'Full-day access to the spa and wellness center', 300.00),
('Airport Transfer', 'Round-trip airport transfer service', 200.00),
('Dinner Cruise', 'Nile River dinner cruise with entertainment', 500.00),
('Fitness Center', '24/7 access to the fitness center with modern equipment', 100.00),
('Private Tour Guide', 'Private guided tours to local attractions', 400.00),
('Laundry Service', 'Daily laundry and dry-cleaning service', 50.00),
('Private Dinner', 'Private dinner setup with a personal chef', 800.00);

INSERT INTO RoomServices (room_id, service_id)
VALUES
(1, 1), -- Room 101 has Breakfast Buffet
(2, 1), -- Room 102 has Breakfast Buffet
(2, 2), -- Room 102 has Spa Access
(7, 4), -- Room 302 has Dinner Cruise
(4, 5), -- Room 104 has Fitness Center
(5, 6), -- Room 105 has Private Tour Guide
(6, 7), -- Room 106 has Laundry Service
(8, 5), -- Room 203 has Fitness Center
(10, 8), -- Room 303 has Private Dinner
(12, 6); -- Room 403 has Private Tour Guide