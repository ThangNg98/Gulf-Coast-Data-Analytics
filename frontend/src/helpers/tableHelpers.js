import moment from 'moment';

function getDateFormat(grouping) {
  switch (grouping) {
    case 'day':
      return 'MM-DD-YYYY';
    case 'week':
      return 'MM-DD-YYYY';
    case 'month':
      return 'YYYY-MM';
    case 'quarter':
      return 'YYYY-[Q]Q';
    case 'year':
      return 'YYYY';
    default:
      return 'YYYY-MM-DD';
  }
}


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

    result.sort((a, b) => {
      const dateA = moment(a.session_date, getDateFormat(grouping));
      const dateB = moment(b.session_date, getDateFormat(grouping));
      return dateB.isBefore(dateA) ? -1 : 1;
    });
    
  
    return result;
  }

  

export function filterAndGroupData(data, startDate, endDate, grouping, fillMissingDates) {
    const adjustedStartDate = new Date(startDate);
    const adjustedEndDate = new Date(endDate);
    adjustedStartDate.setHours(0, 0, 0, 0);
    adjustedEndDate.setHours(0, 0, 0, 0);

    console.log('original adjustedStartDate', adjustedStartDate)
    console.log('original adjustedEndDate', adjustedEndDate)
    adjustedStartDate.setDate(adjustedStartDate.getDate() + 1);
    adjustedEndDate.setDate(adjustedEndDate.getDate() + 2);
    
    // Add a 1-month offset when the user searches by month
    if (grouping === 'month') {
      adjustedStartDate.setDate(1);
      const now = new Date();
      const year = now.getUTCFullYear();
      const month = now.getUTCMonth() + 1; // Note that months are zero-indexed, so we add 1 to get the correct month
      const lastDayOfMonth = new Date(Date.UTC(year, month, 0)).getUTCDate();
      adjustedEndDate.setUTCDate(lastDayOfMonth);
      adjustedEndDate.setDate(adjustedEndDate.getDate() + 2); 
    } else if (grouping === 'quarter') {
      const startQuarter = Math.floor(adjustedStartDate.getUTCMonth() / 3);
      const endQuarter = Math.floor(adjustedEndDate.getUTCMonth() / 3);
    
      const firstDayOfStartQuarter = new Date(Date.UTC(adjustedStartDate.getUTCFullYear(), startQuarter * 3, 1));
      const lastDayOfEndQuarter = new Date(Date.UTC(adjustedEndDate.getUTCFullYear(), (endQuarter + 1) * 3, 0));
    
      adjustedStartDate.setTime(firstDayOfStartQuarter.getTime());
      adjustedEndDate.setTime(lastDayOfEndQuarter.getTime());
      adjustedEndDate.setDate(adjustedEndDate.getDate() + 1);
      adjustedStartDate.setDate(adjustedStartDate.getDate() + 1);
    } else if (grouping === 'year') {
      const firstDayOfStartYear = new Date(Date.UTC(adjustedStartDate.getUTCFullYear(), 0, 1));
      const lastDayOfEndYear = new Date(Date.UTC(adjustedEndDate.getUTCFullYear(), 11, 31));
    
      adjustedStartDate.setTime(firstDayOfStartYear.getTime());
      adjustedEndDate.setTime(lastDayOfEndYear.getTime());
      adjustedEndDate.setDate(adjustedEndDate.getDate() + 2);
    } else if (grouping === 'week') {
      const startWeek = moment.utc(adjustedStartDate).startOf('week').toDate();
      const endWeek = moment.utc(adjustedEndDate).endOf('week').toDate();
    
      adjustedStartDate.setTime(startWeek.getTime());
      adjustedEndDate.setTime(endWeek.getTime());
      adjustedEndDate.setDate(adjustedEndDate.getDate() + 2);
      adjustedStartDate.setDate(adjustedStartDate.getDate() + 2);
    };
    
    console.log('new adjustedStartDate', adjustedStartDate)
    console.log('new adjustedEndDate', adjustedEndDate)
  
    const filteredData = data.filter(item => {
      const itemDate = new Date(item.session_date);
      itemDate.setDate(itemDate.getDate() + 1);
    
      return itemDate >= adjustedStartDate && itemDate <= adjustedEndDate;
    });
    
    console.log('filteredData', filteredData)

  const grouped = {};

  filteredData.forEach(item => {
    const date = moment.utc(item.session_date);
    console.log('date', date)
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

  console.log('groupedData', groupedData)

  return groupedData;


}
