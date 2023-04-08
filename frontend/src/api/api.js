import axios from 'axios';
import { useLoadingStore } from '../stores/LoadingStore.js'

axios.interceptors.request.use((config) => {
    useLoadingStore().setLoading(true);
    return config;
  }, (error) => {
    useLoadingStore().setLoading(false);
    return Promise.reject(error);
  });
  
axios.interceptors.response.use((response) => {
    useLoadingStore().setLoading(false);
    return response;
}, (error) => {
    useLoadingStore().setLoading(false);
    return Promise.reject(error);
});

// api.js

export async function checkMostRecentAPI(volunteerId) {
    try {
      const response = await axios.get(`https://llc.onrender.com/check_most_recent/${volunteerId}`)
      const result = {
        alreadyCheckedIn: false,
        session: null
      };
      if (response.data[0]) {
        const temp_checkedIn = response.data[0].time_out;
        if (temp_checkedIn == '1') {
          result.session = {
            session_id: response.data[0].session_id,
            org_id: response.data[0].org_id,
            event_id: response.data[0].event_id,
            time_in: response.data[0].time_in,
            session_comment: response.data[0].session_comment
          };
          result.alreadyCheckedIn = true;
        } else if (temp_checkedIn == '2') {
          result.alreadyCheckedIn = false;
        }
      }
      return result;
    } catch (error) {
      throw error;
    }
};

export async function getEventsAPI() {
    try {
      const response = await axios.get('https://llc.onrender.com/read_events');
      console.log('response from getEventsAPI:', response)
      return response
    } catch (error) {
      console.log(error);
      throw error;
    }
}

export async function getOrgsAPI() {
    try {
        const response = await axios.get('https://llc.onrender.com/read_orgs');
        console.log('response from getOrgsAPI:', response)
        return response
    } catch (error) {
        console.log(error);
        throw error;
    }
};

export async function createSessionAPI(session) {
    try {
        await axios.post('https://llc.onrender.com/create_session', session)
    } catch (error) {
        console.log(error);
        throw error;
    }
};

export async function checkOutAPI(session) {
    try {
        await axios.post('https://llc.onrender.com/check_out', session);
    } catch (error) {
        console.log(error);
        throw error;
    }
};

export async function getPhoneListAPI() {
    try {
        const response = await axios.get('https://llc.onrender.com/volunteer_phone/');
        return response
    } catch (error) {
      console.log(error);
      throw (error);
    }
};

export async function getVolunteerIDAPI(phone) {
  try {
      const response = await axios.get(`https://llc.onrender.com/get_volunteer_id/${phone}`);
      return response;
  } catch (error) {
    console.log(error);
    throw (error);
  }
};

export async function getVolunteerAPI(id) {
  try {
    const response = await axios.get(`https://llc.onrender.com/get_volunteer/${id}`);
    return response;
  } catch (error) {
    console.log(error);
    throw (error);
  }
};

export async function updateVolunteerAPI(volunteer_info) {
  try {
    await axios.post('https://llc.onrender.com/update_volunteer', volunteer_info)
  } catch (error) {
    console.log(error);
    throw (error);
  }
};

export async function createEventAPI(event_info) {
  try {
    await axios.post('https://llc.onrender.com/create_event', event_info)
  } catch (error) {
    console.log(error);
    throw (error);
  }
};

export async function getEventAPI(event_id) {
  try {
    const response = await axios.get(`https://llc.onrender.com/get_event/${event_id}`);
    return response
  } catch (error) {
    console.log(error);
    throw (error);
  }
};

export async function updateEventAPI(events) {
  try {
    await axios.post('https://llc.onrender.com/update_event', events)
  } catch (error) {
    console.log(error);
    throw (error);
  }
};

export async function deleteEventAPI(events) {
  try {
    await axios.post('https://llc.onrender.com/delete_event', events)
  } catch (error) {
    console.log(error);
    throw (error);
  }
};

export async function createOrgAPI(org_info) {
  try {
    await axios.post('https://llc.onrender.com/create_organization', org_info)
  } catch (error) {
    console.log(error);
    throw (error);
  }
};

export async function getOrgAPI(org_id) {
  try {
    const response = await axios.get(`https://llc.onrender.com/get_org/${org_id}`);
    return response;
  } catch (error) {
    console.log(error);
    throw (error);
  }
};

export async function updateOrgAPI(organization) {
  try {
    await axios.post('https://llc.onrender.com/update_organization', organization);
  } catch (error) {
    console.log(error);
    throw (error);
  }
};

export async function deleteOrgAPI(organization) {
  try {
    await axios.post('https://llc.onrender.com/delete_organization', organization)
  } catch (error) {
    console.log(error);
    throw (error);
  }
};

export async function getVolunteersAPI() {
  try {
    const response = await axios.get('https://llc.onrender.com/read_volunteers');
    return response;
  } catch (error) {
    console.log(error);
    throw (error);
  }
};

export async function getVolunteerHoursAPI(id) {
  try {
    const response = await axios.get(`https://llc.onrender.com/read_volunteer_hours/${id}`);
    return response;
  } catch (error) {
    console.log(error);
    throw (error);
  }
};

export async function adminUpdateVolunteerAPI(volunteer_info) {
  try {
    await axios.post('https://llc.onrender.com/admin_update_volunteer', volunteer_info);
  } catch (error) {
    console.log(error);
    throw (error);
  }
};

export async function adminDeleteVolunteerAPI(volunteer_info) {
  try {
    await axios.post('https://llc.onrender.com/delete_volunteer', volunteer_info);
  } catch (error) {
    console.log(error);
    throw (error);
  }
};

export async function getOrgsHoursAPI() {
  try {
    const response = await axios.get('https://llc.onrender.com/getOrgsHours');
    return response
  } catch (error) {
    console.log(error);
    throw (error);
  }
};

export async function getOrgsVolunteersAPI() {
  try {
    const response = await axios.get('https://llc.onrender.com/getOrgsVolunteers');
    return response
  } catch (error) {
    console.log(error);
    throw (error);
  }
};

export async function getOrgsHoursVolunteersAPI() {
  try {
    const response = await axios.get('https://llc.onrender.com/getOrgsHoursVolunteers');
    return response
  } catch (error) {
    console.log(error);
    throw (error);
  }
};

export async function getEventsHoursAPI() {
  try {
    const response = await axios.get('https://llc.onrender.com/getEventsHours');
    return response
  } catch (error) {
    console.log(error);
    throw (error);
  }
};

export async function getEventsVolunteersAPI() {
  try {
    const response = await axios.get('https://llc.onrender.com/getEventsVolunteers');
    return response
  } catch (error) {
    console.log(error);
    throw (error);
  }
};

export async function getEventsHoursVolunteersAPI() {
  try {
    const response = await axios.get('https://llc.onrender.com/getEventsHoursVolunteers');
    return response
  } catch (error) {
    console.log(error);
    throw (error);
  }
};

export async function getDatesHoursAPI() {
  try {
    const response = await axios.get('https://llc.onrender.com/getDatesHours');
    return response
  } catch (error) {
    console.log(error);
    throw (error);
  }
};