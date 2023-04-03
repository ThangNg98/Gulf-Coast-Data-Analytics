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
      const response = await axios.get(`http://127.0.0.1:5000/check_most_recent/${volunteerId}`)
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
      const response = await axios.get('http://127.0.0.1:5000/read_events');
      console.log('response from getEventsAPI:', response)
      return response
    } catch (error) {
      console.log(error);
      throw error;
    }
}

export async function getOrgsAPI() {
    try {
        const response = await axios.get('http://127.0.0.1:5000/read_orgs');
        console.log('response from getOrgsAPI:', response)
        return response
    } catch (error) {
        console.log(error);
        throw error;
    }
};

export async function createSessionAPI(session) {
    try {
        await axios.post('http://127.0.0.1:5000/create_session', session)
    } catch (error) {
        console.log(error);
        throw error;
    }
};

export async function checkOutAPI(session) {
    try {
        await axios.post('http://127.0.0.1:5000/check_out', session);
    } catch (error) {
        console.log(error);
        throw error;
    }
};