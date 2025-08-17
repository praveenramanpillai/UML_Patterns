# onlinePotholeTrackingSystem.py

diagram_info = {
    "title": "Online Pothole Tracking & Repair System (PHTRS)",
    "author": "Praveen Perumal Ramanpillai",
    "date": "2025-08-17",
    "brief_description": (
        "Citizens report potholes and track status on the Online Pothole Tracking & Repair System (PHTRS). "
        "Public Work Employees triage reports, create/assign work orders, and update statuses based on severity and crew capacity. "
        "Repair Crews view assigned work orders, perform repairs, and log hours/materials. "
        "The system also supports damage claims submitted by citizens and processed by staff."
    )
}

actors = [
    "Citizens",
    "Public Work Employee",
    "Repair Crews"
]

actor_usecase_map = {
    "Citizens": [
        "Login and Report Pothole",
        "Check Pothole Status",
        "Submit Damage Claim"
    ],
    "Public Work Employee": [
        "View Reported Pot Hole",
        "Assign work order based on size and crew member",
        "Update pothole status",
        "New/Process Damage Claims"
    ],
    "Repair Crews": [
        "View Assigned work orders",
        "Perform required repairs",
        "Log Repair Details",
        "Update pothole status"
    ]
}

def show_overview():
    print(f"Project : {diagram_info['title']}")
    print(f"Author : {diagram_info['author']}")
    print(f"Date   : {diagram_info['date']}\n")
    print("\033[1;4mBrief description:\033[0m")
    print(f"{diagram_info['brief_description']}\n")

def show_actors():
    print("\033[1;4mActors:\033[0m")
    for a in actors:
        print(f"\t{a}")
    print()

def show_actor_to_use_cases():
    print("\033[1;4mUse Cases:\033[0m")
    for actor, ucs in actor_usecase_map.items():
        print(f"\t{actor}:")
        for uc in ucs:
            print(f"\t\t- {uc}")
    print()

if __name__ == "__main__":
    show_overview()
    show_actors()
    show_actor_to_use_cases()
