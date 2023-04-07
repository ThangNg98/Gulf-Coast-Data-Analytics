import moment from 'moment';


function fillMissingDatesInData(groupedData, startDate, endDate, grouping) {
    const result = [];
    const currentDate = moment(startDate).startOf(grouping);
    const lastDate = moment(endDate).startOf(grouping);
  
    while (currentDate.isSameOrBefore(lastDate)) {
      let key;
  
      switch (grouping) {
        case 'day':
          key = currentDate.format('MM-DD-YYYY');
          break;
        case 'week':
          key = currentDate.startOf('isoWeek').format('MM-DD-YYYY');
          break;
        case 'month':
          key = currentDate.startOf('month').format('YYYY-MM');
          break;
        case 'quarter':
          key = currentDate.startOf('quarter').format('YYYY-[Q]Q');
          break;
        case 'year':
          key = currentDate.startOf('year').format('YYYY');
          break;
        default:
          key = currentDate.format('YYYY-MM-DD');
      }
  
      const foundData = groupedData.find(data => data.session_date === key);
      if (foundData) {
        result.push(foundData);
      } else {
        result.push({ session_date: key, total_hours: 0 });
      }
  
      currentDate.add(1, grouping);
    }
  
    return result;
  }

  

export function filterAndGroupData(data, startDate, endDate, grouping, fillMissingDates) {
    const adjustedStartDate = new Date(startDate);
    const adjustedEndDate = new Date(endDate);
    
    adjustedStartDate.setDate(adjustedStartDate.getDate() + 1);
    adjustedEndDate.setDate(adjustedEndDate.getDate() + 1);
  
    const filteredData = data.filter(
      item => new Date(item.session_date) >= adjustedStartDate && new Date(item.session_date) <= adjustedEndDate
    );

  const grouped = {};

  filteredData.forEach(item => {
    const date = moment(item.session_date);
    let key;

    switch (grouping) {
      case 'day':
        key = date.format('MM-DD-YYYY');
        break;
      case 'week':
        key = date.startOf('isoWeek').format('MM-DD-YYYY');
        break;
      case 'month':
        key = date.startOf('month').format('YYYY-MM');
        break;
      case 'quarter':
        key = date.startOf('quarter').format('YYYY-[Q]Q');
        break;
      case 'year':
        key = date.startOf('year').format('YYYY');
        break;
      default:
        key = item.session_date;
    }

    if (!grouped[key]) {
      grouped[key] = 0;
    }

    grouped[key] += item.total_hours;
  });

  const groupedData = Object.entries(grouped).map(([session_date, total_hours]) => ({ session_date, total_hours }));

  if (fillMissingDates) {
    return fillMissingDatesInData(groupedData, adjustedStartDate, adjustedEndDate, grouping);
  }

  return groupedData;


}
