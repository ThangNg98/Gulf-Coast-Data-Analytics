<template>
    <div class="container1 table-wrapper"> 
      <div class="table-responsive-md">
        <table class="table table-hover" style="width: 100%; table-layout: fixed;">
          <colgroup>
            <col style="width: 25%;">
            <col style="width: 25%;">
            <col style="width: 25%;">
            <col style="width: 25%;">
          </colgroup>
          <thead class="theadsticky">
            <tr>
              <th scope="col" style="width: 25%;"><div class="responsive-text">Date</div></th>
              <th scope="col" style="width: 25%;"><div class="responsive-text">Event</div></th>
              <th scope="col" style="width: 25%;"><div class="responsive-text">Organization</div></th>
              <th scope="col" style="width: 25%;"><div class="responsive-text">Total Hours</div></th>
            </tr>
          </thead>
          <tbody>
            <!-- for each session, print event name, org name, hours, and formatted date-->
            <tr v-for="session in processedSessionsData">
              <td style="width: 25%;"><div class="responsive-text">{{session.dateval}}</div></td>
              <td style="width: 25%;"><div class="responsive-text">{{session.eventName}}</div></td>
              <td style="width: 25%;"><div class="responsive-text">{{session.orgName}}</div></td>
              <td style="width: 25%;"><div class="responsive-text">{{session.hours}}</div></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </template>
  

<script>
export default {
  props: {
    sessions: Object
  },
  data() {
    return {
      processedSessionsData: [],
    }
  },
  computed: {
    formattedSessionsData() {
      return this.processedSessionsData.map(session => {
        const formattedDate = this.formattedDate(session.dateval);
        return {
          ...session,
          eventName: this.truncatedEventName(session.eventName),
          orgName: this.truncatedOrgName(session.orgName),
          hours: this.truncatedHours(session.hours),
          dateval: formattedDate,
        };
      });
    }
  },
  mounted() {
    console.log('mounted Sessions Table')
    this.processSessions();
  },
  methods: {
        processSessions() {
        this.processedSessionsData = this.sessions.map(session => {
            const formattedDate = this.formattedDate(session.dateval);
            const processedSession = {
            ...session,
            eventName: this.truncatedEventName(session.eventName),
            orgName: this.truncatedOrgName(session.orgName),
            hours: this.truncatedHours(session.hours),
            dateval: formattedDate,
            };
            return processedSession;
        });
        },
        formattedDate(current) {
        const options = { month: '2-digit', day: '2-digit', year: 'numeric' };
        const date = new Date(current);
        return date.toLocaleDateString('en-US', options);
        },
        truncatedEventName(text, maxLength = 22) {
        if (text && text.length > maxLength) {
            return text.slice(0, maxLength) + '...';
        } else {
            return text;
        }
        },
        truncatedOrgName(text, maxLength = 22) {
        if (text && text.length > maxLength) {
            return text.slice(0, maxLength) + '...';
        } else {
            return text;
        }
        },
        truncatedHours(text, maxLength = 22) {
        if (text && text.length > maxLength) {
            return text.slice(0, maxLength) + '...';
        } else {
            return text;
        }
        },
    }

}
</script>




<style scoped>

.table-wrapper {
  max-height: 400px;
  overflow: auto;
  display:inline-block;
  width: 90%;
}

.container1 {
  margin: auto;
  padding-left: auto;
  padding-right: auto
}

.responsive-text {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    font-size: 16px;
}

@media (max-width: 576px) {
    .responsive-text {
        font-size: 14px;
    }
}

.theadsticky {
  position: sticky;
  top: 0;
  background-color: #e6e7eb !important;
}
</style>