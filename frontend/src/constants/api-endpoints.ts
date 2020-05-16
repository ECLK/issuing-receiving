export const apiEndpoints = {
    partOne: {
        beforeElection: "report-to-work/before-election/",
        onElectionDay: "report-to-work/on-election-day/"
    },
    me: {
        me: "staffs/ir-aro/get-my-details/",
        storageInCharge: "staffs/pd-storage-in-charge/storage-in-charge-my-polling-division/",
        countingCentre: (election: number) => `units/election/${election}/counting-centre/counting-centre-of-my-pd`,
        pollingStation: (election: number) =>
            `units/election/${election}/polling-station/polling-stations-under-my-control`
    },
    staffs: {
        changePassword: "staffs/change-password/",
        iRAroPollingDistricts: "staffs/ir-aro-polling-districts/",
        iRAro: "staffs/ir-aro/",
        pDStorageInCharge: "staffs/pd-storage-in-charge/",
        staffs: "staffs/staffs/",
        getMyDetails:"staffs/ir-aro/get-my-details"
    },
    units: {
        administrativeDistrict: "units/administrative-district/",
        electoralDistrict: "units/electoral-district/",
        pollingDistrict: "units/polling-district/",
        pollingDivision: "units/polling-division/",
        countingCentre: (election: number) => `units/election/${election}/counting-centre/`,
        pollingStation: (election: number) => `units/election/${election}/polling-station`
    },
    partTwo: {
        issuedBallotBoxes: "part-two/issued-ballot-boxes-to-spo/",
        issuedToSpo: "part-two/issued-to-spo/",
        receivedBallotBoxes: "part-two/received-ballot-boxes-from-spo/",
        receivedFromSpo: "part-two/received-from-spo/"
    },
    partThree: {
        receivedFromSpo: "part-three/received-from-spo/"
    },
    partFour: {
        issuedBallotBoxes: "​part-four​/issued-ballot-boxes-to-cco​/",
        issuedToCCO: "part-four/issued-to-cco/"
    },
    partFive: {
        cover5: "part-five/cover-5/",
        cover6: "part-five/cover-6/",
        issuedToAroCC: "part-five/issued-to-aro-cc/",
        issuedToPD: "part-five/issued-to-pd/"
    },
    election: {
        election: "election/",
        activeElection: "election/get_active_elections/"
    },
    auth: "auth/"
};
