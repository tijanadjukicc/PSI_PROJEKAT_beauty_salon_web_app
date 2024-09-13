function generateTimeSlots() {
    const selectedDate = document.getElementById('selectedDate').value;
    const timeSlotsDiv = document.getElementById('time-slots');

    // Clear previous time slots
    timeSlotsDiv.innerHTML = '';

    if (selectedDate) {
      const timeSlots = Array.from({ length: 5 }, (_, index) => (index * 2 + 9) + ":00"); // 9 AM to 5 PM with 2-hour difference

      // Generate time slot buttons
      timeSlots.forEach(time => {
        const timeSlotButton = document.createElement('div');
        timeSlotButton.classList.add('time-slot');
        timeSlotButton.textContent = time;

        // Check if the time slot is reserved
        const isReserved = isTimeSlotReserved(selectedDate, time);
        if (isReserved) {
          timeSlotButton.classList.add('selected');
        }

        timeSlotButton.onclick = () => toggleOccupancy(selectedDate, timeSlotButton);
        timeSlotsDiv.appendChild(timeSlotButton);
      });
    }
  }

  function toggleOccupancy(selectedDate, timeSlotButton) {
    timeSlotButton.classList.toggle('selected');
    updateLocalStorage(selectedDate, timeSlotButton.textContent);
  }

  function isTimeSlotReserved(selectedDate, time) {
    const reservedTimeSlots = getReservedTimeSlots(selectedDate);
    return reservedTimeSlots.includes(time);
  }

  function getReservedTimeSlots(selectedDate) {
    const reservedTimeSlotsKey = `reservedTimeSlots_${selectedDate}`;
    const reservedTimeSlotsString = localStorage.getItem(reservedTimeSlotsKey);
    return reservedTimeSlotsString ? JSON.parse(reservedTimeSlotsString) : [];
  }

  function updateLocalStorage(selectedDate, time) {
    const reservedTimeSlots = getReservedTimeSlots(selectedDate);
    const index = reservedTimeSlots.indexOf(time);

    if (index !== -1) {
      // Remove the time slot if it's already reserved
      reservedTimeSlots.splice(index, 1);
    } else {
      // Add the time slot if it's not reserved
      reservedTimeSlots.push(time);
    }

    const reservedTimeSlotsKey = `reservedTimeSlots_${selectedDate}`;
    localStorage.setItem(reservedTimeSlotsKey, JSON.stringify(reservedTimeSlots));
  }

  function reserveTime() {
    const selectedDate = document.getElementById('selectedDate').value;
    const selectedTimeSlots = document.querySelectorAll('.time-slot.selected');

    if (selectedTimeSlots.length > 0) {
      selectedTimeSlots.forEach(slot => slot.remove());
      alert('Termin je rezervisan!');
    } else {
      alert('Molimo vas da izaberete termin pre nego što rezervišete.');
    }
  }