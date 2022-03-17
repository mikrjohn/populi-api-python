from .driver import initialize, get_anonymous, get_all_anonymous


def add_address(
        person_id: str = None,
        organization_id: str = None,
        street: str = None,
        city: str = None,
        state: str = None,
        postal: str = None,
        country: str = None,
        type: str = None,
        primary: str = None,
        public: str = None):
    """
    Adds an address to a person or organization.

    :param person_id: The numeric ID of the person to whose profile you are attaching this address.
    :param organization_id: The numeric ID of the organization to whose profile you are attaching this address.
    :param street: e.g. 777 Magnolia Ln
    :param city: e.g. Moscow
    :param state: e.g. ID
    :param postal: e.g. 83843
    :param country: e.g. US
    :param type: Person addresses: HOME, WORK, BILLING, SCHOOL, SHIPPING, OTHER
    :param primary: Boolean. Use if you want to mark the address as primary or not primary. Defaults to false.
    :param public: Boolean. Use if you want to mark the address as public or not public. Defaults to true.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addAddress',
        person_id=person_id,
        organization_id=organization_id,
        street=street,
        city=city,
        state=state,
        postal=postal,
        country=country,
        type=type,
        primary=primary,
        public=public)


def add_advisor_to_student(
        advisor_person_id: str = None,
        student_person_id: str = None):
    """
    Adds an advisor to a student.

    :param advisor_person_id: The numeric person ID of the advisor you're interested in.
    :param student_person_id: The numeric person ID of the student you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addAdvisorToStudent',
        advisor_person_id=advisor_person_id,
        student_person_id=student_person_id)


def add_aid_application(
        student_id: str = None,
        aid_year_id: str = None,
        assigned_to_id: str = None,
        enrollment: str = None,
        dependency: str = None,
        student_aid_class_id: str = None,
        program_months: str = None,
        year_coa: str = None,
        program_coa: str = None,
        year_efc: str = None,
        program_efc: str = None,
        student_agi: str = None,
        parent_agi: str = None,
        legal_residence_state: str = None,
        verification: str = None,
        verification_status: str = None,
        verification_group: str = None,
        auto_zero_efc: str = None,
        status: str = None,
        housing: str = None):
    """
    Adds a new financial aid application to a particular student in a particular aid year.

    :param student_id: The numeric ID of the student.
    :param aid_year_id: The numeric ID of the aid year.
    :param assigned_to_id: The numeric ID of the person to whom this aid application is assigned.
    :param enrollment: The student's enrollment status (for financial aid purposes): FULL_TIME, THREE_QUARTER_TIME, HALF_TIME, or LESS_THAN_HALF_TIME (defaults to FULL_TIME)
    :param dependency: Whether this student is considered a dependent for aid purposes: can be blank, DEPENDENT, or INDEPENDENT
    :param student_aid_class_id: The numeric aid class ID for this student (aid classes are how Populi groups similar types of students together).
    :param program_months: The number of months this student is expected to be enrolled in your school's program.
    :param year_coa: This student's Cost of Attendance if they were attending for the entire year (this should be extrapolated out from their program_coa for shorter programs, since Pell calculates based on COA for the entire year).
    :param program_coa: This student's Cost of Attendance in this aid year.
    :param year_efc: This student's Estimated Family Contribution in this aid year (extrapolated out to a full year for shorter programs, if necessary).
    :param program_efc: This student's Estimated Family Contribution in this aid year.
    :param student_agi: This student's Adjusted Gross Income in this aid year.
    :param parent_agi: The parents' Adjusted Gross Income in this aid year.
    :param legal_residence_state: The student's state of legal residence.
    :param verification: Whether this student has been selected for verification. Must be either blank, SELECTED_BY_COLLEGE, or SELECTED_BY_GOVERNMENT.
    :param verification_status: If this student was selected for verification (see above), what's their status? If set, must be one of: IN_PROGRESS, COMPLETED, REJECTED, or EXEMPTED. Cannot be set if `verification` is blank.
    :param verification_group: If this student was selected for verification (see above), what verification group are they in? If set, must be one of: 'Standard, 'Child Support Paid', 'Custom', 'Aggregate', or 'Household Resources'. Cannot be set unless `verification` is set to SELECTED_BY_GOVERNMENT.
    :param auto_zero_efc: Whether the student's EFC was calculated using the "automatic zero" EFC formula. If set, must be: 1 or 0
    :param status: The application status: SETUP, IN_PROGRESS, COMPLETED, NEEDS_ATTENTION, or CANCELED (defaults to SETUP)
    :param housing: The student's housing situation: ON_CAMPUS, WITH_PARENT, or OFF_CAMPUS
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addAidApplication',
        student_id=student_id,
        aid_year_id=aid_year_id,
        assigned_to_id=assigned_to_id,
        enrollment=enrollment,
        dependency=dependency,
        student_aid_class_id=student_aid_class_id,
        program_months=program_months,
        year_coa=year_coa,
        program_coa=program_coa,
        year_efc=year_efc,
        program_efc=program_efc,
        student_agi=student_agi,
        parent_agi=parent_agi,
        legal_residence_state=legal_residence_state,
        verification=verification,
        verification_status=verification_status,
        verification_group=verification_group,
        auto_zero_efc=auto_zero_efc,
        status=status,
        housing=housing)


def add_application(
        application_template_id: str = None,
        person_id: str = None,
        lead_id: str = None,
        first_name: str = None,
        middle_name: str = None,
        last_name: str = None,
        fee_status: str = None,
        email_address: str = None,
        start_date: str = None,
        representative_id: str = None,
        program_id: str = None,
        academic_term_id: str = None,
        expected_enrollment: str = None,
        email_link_to_applicant: str = None,
        request_email_verification: str = None,
        street: str = None,
        city: str = None,
        state: str = None,
        postal: str = None,
        country: str = None):
    """
    Adds an admissions application.

    :param application_template_id: The numeric ID of the application template.
    :param person_id: The numeric ID of the person who is the applicant.
    :param lead_id: The numeric ID of the lead record this application should be attached to. Defaults to the person's active lead record. If no active lead record exists a new one will be created. Requires person_id.
    :param first_name: The first name of the applicant.
    :param middle_name: The middle name of the applicant.
    :param last_name: The last name of the applicant.
    :param fee_status: UNPAID, PAID, or WAIVED. Defaults to UNPAID
    :param email_address: The email address of the applicant.
    :param start_date: The date this application was started (e.g. 2014-01-15). Defaults to the current date.
    :param representative_id: The numeric ID of the admissions representative who will be assigned to this application.
    :param program_id: The numeric ID of the program the applicant is applying to.
    :param academic_term_id: The numeric ID of the academic term the applicant wishes to enroll in.
    :param expected_enrollment: FULL_TIME (default), HALF_TIME, LESS_THAN_HALF_TIME
    :param email_link_to_applicant: Boolean. A link to the application will be emailed to the applicant. Defaults to true.
    :param request_email_verification: Boolean. An verification email will be sent to the applicant. Defaults to false.
    :param street: The applicant's street address.
    :param city: The applicant's city.
    :param state: The applicant's state or province abbreviation.
    :param postal: The applicant's postal code.
    :param country: The person's country abbreviation.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addApplication',
        application_template_id=application_template_id,
        person_id=person_id,
        lead_id=lead_id,
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        fee_status=fee_status,
        email_address=email_address,
        start_date=start_date,
        representative_id=representative_id,
        program_id=program_id,
        academic_term_id=academic_term_id,
        expected_enrollment=expected_enrollment,
        email_link_to_applicant=email_link_to_applicant,
        request_email_verification=request_email_verification,
        street=street,
        city=city,
        state=state,
        postal=postal,
        country=country)


def add_application_note(
        application_id: str = None,
        content: str = None,
        public: str = None):
    """
    Adds a note to an existing application.

    :param application_id: The numeric ID of the application.
    :param content: The text content of the note.
    :param public: Boolean. Defaults to false.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addApplicationNote',
        application_id=application_id,
        content=content,
        public=public)


def add_assignment_comment(
        assignment_id: str = None,
        person_id: str = None,
        comment: str = None,
        file: str = None,
        internal: str = None):
    """
    Adds an assignment comment to a particular assignment and student.

    :param assignment_id: Numeric ID of the assignment.
    :param person_id: Numeric ID of the student.
    :param comment: The comment content.
    :param file: File uploaded the via the HTTP POST method.
    :param internal: Boolean. Use if you want the assignment comment to be an internal comment. Defaults to false.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addAssignmentComment',
        assignment_id=assignment_id,
        person_id=person_id,
        comment=comment,
        file=file,
        internal=internal)


def add_campus_to_student(person_id: str = None, campus_id: str = None):
    """
    Adds a campus to a student.

    :param person_id: The numeric ID of the person you're interested in.
    :param campus_id: The numeric ID of the campus you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addCampusToStudent',
        person_id=person_id,
        campus_id=campus_id)


def add_communication_plan_to_person(
        communication_plan_id: str = None,
        person_id: str = None,
        sender_id: str = None,
        start_date: str = None):
    """
    Adds a communication plans to a person.

    :param communication_plan_id: The numeric ID of the communication plan you're interested in.
    :param person_id: The numeric ID of the person you're interested in.
    :param sender_id: The numeric ID of the person who the email/letter will be sent from or who a to-do is assigned by.
    :param start_date: The date communication events can start on (e.g. 2018-01-18). Defaults to the current date.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addCommunicationPlanToPerson',
        communication_plan_id=communication_plan_id,
        person_id=person_id,
        sender_id=sender_id,
        start_date=start_date)


def add_course_bulletin_board_post(
        course_offering_id: str = None,
        post: str = None):
    """
    Adds a bulletin board post to a particular course offering.

    :param course_offering_id: The numeric ID of the course offering you're interested in.
    :param post: The post content.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addCourseBulletinBoardPost',
        course_offering_id=course_offering_id,
        post=post)


def add_course_instance_assignment(
        instance_id: str = None,
        name: str = None,
        type: str = None,
        discussion_id: str = None,
        description: str = None,
        catalog_course_ids: str = None,
        points: str = None,
        extra_credit: str = None,
        group_id: str = None,
        published: str = None,
        time_due: str = None,
        visible_to_students_before_due: str = None,
        availability: str = None,
        start_window: str = None,
        end_window: str = None,
        time_limit: str = None,
        retake_policy: str = None,
        retakes: str = None,
        proctored: str = None,
        test_submit_feedback: str = None,
        test_end_feedback: str = None,
        peer_grade: str = None,
        grade_submission_points: str = None,
        grade_review_points: str = None,
        anonymous_reviews: str = None,
        review_visibility: str = None,
        allow_review_comments: str = None,
        reviews_time_due: str = None,
        reviews_closed_date_time: str = None):
    """
    Creates an assignment in a particular course instance.

    :param instance_id: The numeric ID of the course instance you're interested in.
    :param name: The name of the assignment.
    :param type: GRADE_ONLY, FILE_UPLOAD, PEER_REVIEW_FILE_UPLOAD, TEST, ATTENDANCE, DISCUSSION, ESSAY, or PEER_REVIEW_ESSAY
    :param discussion_id: Only used when the assignment type is DISCUSSION. The numeric ID of the discussion you want to use (the default is 0 which means a new discussion will be created).
    :param description: A description of the assignment.
    :param catalog_course_ids: Only used if the course is cross-listed. This would be an array of catalog course IDs that the assignment applies to. If you leave this parameter out of the request the assignment will apply to all cross-listed courses.
    :param points: The number of points that the assignment is worth (the default is 0).
    :param extra_credit: Boolean. Defaults to false.
    :param group_id: The assignment group ID this assignment belongs to (the default is 0 which is the built-in "Other" group).
    :param published: Boolean. Defaults to false.
    :param time_due: When the assignment is due (e.g. 2017-06-30 23:59:59 - must be in the course instance's timezone).
    :param visible_to_students_before_due: When the passed in type is TEST this sets whether or not the test is visible before it's available (the default is 1).
    :param availability: FROM, AFTER, BEFORE, or ALWAYS (the default is FROM). If the value is FROM and both start_window and end_window are empty then the test will not be available.
    :param start_window: When the test availability starts (e.g. 2017-06-01 00:00:00 - must be in the course instance's timezone). Only used when the availability parameter is FROM or AFTER.
    :param end_window: When the test availability ends (e.g. 2017-06-30 23:59:59 - must be in the course instance's timezone). Only used when the availability parameter is FROM or BEFORE.
    :param time_limit: The time limit in minutes (the default is 0 which is "No time limit").
    :param retake_policy: NO_RETAKES (no retakes - the default), KEEP_HIGHEST (keep highest score), KEEP_LAST (keep most recent score), AVERAGE (average all scores).
    :param retakes: The number of retakes allowed (only used when the retake_policy is not NO_RETAKES - the default is 0).
    :param proctored: Boolean. Defaults to false.
    :param test_submit_feedback: SCORE (score when available), FEEDBACK (score and response feedback - the default), ANSWERS (score, respsnse feedback, and correct answers).
    :param test_end_feedback: SCORE (score when available), FEEDBACK (score and response feedback), ANSWERS (score, respsnse feedback, and correct answers - the default).
    :param peer_grade: Boolean. Defaults to false.
    :param grade_submission_points: The number of points that submissions are worth (the default is 0).
    :param grade_review_points: The number of points that reviews are worth (the default is 0).
    :param anonymous_reviews: Boolean. Defaults to false.
    :param review_visibility: NEVER (not visible to other students - the default), AFTER_REVIEW (visible to other students after their review), ALWAYS (visible to other students).
    :param allow_review_comments: Boolean. Only used when review_visibility is not NEVER. Defaults to false.
    :param reviews_time_due: When reviews are due (e.g. 2017-06-30 23:59:59 - must be in the course instance's timezone).
    :param reviews_closed_date_time: When reviews are closed (e.g. 2017-06-30 23:59:59 - must be in the course instance's timezone).
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addCourseInstanceAssignment',
        instance_id=instance_id,
        name=name,
        type=type,
        discussion_id=discussion_id,
        description=description,
        catalog_course_ids=catalog_course_ids,
        points=points,
        extra_credit=extra_credit,
        group_id=group_id,
        published=published,
        time_due=time_due,
        visible_to_students_before_due=visible_to_students_before_due,
        availability=availability,
        start_window=start_window,
        end_window=end_window,
        time_limit=time_limit,
        retake_policy=retake_policy,
        retakes=retakes,
        proctored=proctored,
        test_submit_feedback=test_submit_feedback,
        test_end_feedback=test_end_feedback,
        peer_grade=peer_grade,
        grade_submission_points=grade_submission_points,
        grade_review_points=grade_review_points,
        anonymous_reviews=anonymous_reviews,
        review_visibility=review_visibility,
        allow_review_comments=allow_review_comments,
        reviews_time_due=reviews_time_due,
        reviews_closed_date_time=reviews_closed_date_time)


def add_course_instance_assignment_group(
        instance_id: str = None,
        name: str = None,
        weight: str = None,
        extra_credit: str = None,
        drop_lowest: str = None):
    """
    Creates an assignment group in a particular course instance.

    :param instance_id: The numeric ID of the course instance you're interested in.
    :param name: The name of the new assignment group.
    :param weight: The assignment group's weight percent (the default is 0).
    :param extra_credit: Boolean. Defaults to false.
    :param drop_lowest: The number of lowest-graded assignments to drop from this group for each student (the default is 0).
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addCourseInstanceAssignmentGroup',
        instance_id=instance_id,
        name=name,
        weight=weight,
        extra_credit=extra_credit,
        drop_lowest=drop_lowest)


def add_course_offering_link(
        course_offering_id: str = None,
        name: str = None,
        url: str = None):
    """
    Adds a link to a particular course offering.

    :param course_offering_id: The numeric ID of the course offering you're interested in.
    :param name: The name of the link.
    :param url: The URL for the link.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addCourseOfferingLink',
        course_offering_id=course_offering_id,
        name=name,
        url=url)


def add_default_tuition_schedule_to_student(
        person_id: str = None,
        tuition_schedule_id: str = None):
    """
    Adds a default tuition schedule to a student.

    :param person_id: The numeric person ID of the student you're interested in.
    :param tuition_schedule_id: The numeric ID of the tuition schedule you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addDefaultTuitionScheduleToStudent',
        person_id=person_id,
        tuition_schedule_id=tuition_schedule_id)


def add_donation(
        amount: str = None,
        posted_date: str = None,
        fund_id: str = None,
        funds: str = None,
        payment_method: str = None,
        deposit_into_account_id: str = None,
        first_name: str = None,
        last_name: str = None,
        org_name: str = None,
        person_id: str = None,
        organization_id: str = None,
        payment_reference: str = None,
        gift_in_kind_description: str = None,
        staff_comment: str = None,
        phone_number: str = None,
        email_address: str = None,
        campaign_id: str = None,
        appeal_id: str = None):
    """
    Adds a new donation.

    :param amount: The total amount of the donation.
    :param posted_date: The date the donation transaction was posted. If this parameter is not supplied, then the donation will be considered posted today.
    :param fund_id: The numeric ID of the fund the donation is applied to.
    :param funds: An array of fund_ids and amounts, in JSON format, if the donation should be split between multiple funds. (e.g. [{"fund_id":522,"amount":150.00}, {"fund_id":526, "amount":50}])
    :param payment_method: CASH, CHECK, CREDIT_CARD, ACH, MONEY_ORDER, GIFT_IN_KIND, or OTHER
    :param deposit_into_account_id: The numeric ID of the financial asset account where the donation money is deposited.
    :param first_name: The first name of the donor.
    :param last_name: The last name of the donor
    :param org_name: If the donor is an organization, provide the name here.
    :param person_id: To link this donation to an existing person as the donor, supply their numeric ID here. If this parameter is supplied, then first_name and last_name are not required.
    :param organization_id: To link this donation to an existing organization as the donor, supply their numeric ID here. If this parameter is supplied, then first_name and last_name are not required.
    :param payment_reference: Additional information about the payment, such as a check number.
    :param gift_in_kind_description: if the payment_method is GIFT_IN_KIND, use this parameter to describe what was donated.
    :param staff_comment: The comment about this donation only visible to staff.
    :param phone_number: The phone number of the donor. Typically leave blank if person_id or organization_id is included.
    :param email_address: The email address of the donor. Typically leave blank if person_id or organization_id is included.
    :param campaign_id: The numeric ID of the campaign associated with this donation.
    :param appeal_id: The numeric ID of the appeal associated with this donation.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addDonation',
        amount=amount,
        posted_date=posted_date,
        fund_id=fund_id,
        funds=funds,
        payment_method=payment_method,
        deposit_into_account_id=deposit_into_account_id,
        first_name=first_name,
        last_name=last_name,
        org_name=org_name,
        person_id=person_id,
        organization_id=organization_id,
        payment_reference=payment_reference,
        gift_in_kind_description=gift_in_kind_description,
        staff_comment=staff_comment,
        phone_number=phone_number,
        email_address=email_address,
        campaign_id=campaign_id,
        appeal_id=appeal_id)


def add_email_address(
        person_id: str = None,
        organization_id: str = None,
        email_address: str = None,
        type: str = None,
        primary: str = None,
        public: str = None):
    """
    Adds an email to a person or organization.

    :param person_id: The numeric ID of the person to whose profile you are attaching this email address.
    :param organization_id: The numeric ID of the organization to whose profile you are attaching this email address.
    :param email_address: e.g. bob@example.com
    :param type: Person email addresses: HOME, WORK, SCHOOL, OTHER
    :param primary: Boolean. Use if you want to mark the email address as primary or not primary. Defaults to false.
    :param public: Boolean. Use if you want to mark the email address as public or not public. Defaults to true.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addEmailAddress',
        person_id=person_id,
        organization_id=organization_id,
        email_address=email_address,
        type=type,
        primary=primary,
        public=public)


def add_enrollment(
        course_offering_id: str = None,
        person_id: str = None,
        status: str = None,
        status_date: str = None,
        catalog_course_id: str = None):
    """
    Adds a student to a particular course offering.

    :param course_offering_id: The numeric ID of the course offering you're interested in.
    :param person_id: The numeric ID of the student you're interested in.
    :param status: ENROLLED, AUDITOR, or WAITING (if you have access to the waiting list). The default is ENROLLED.
    :param status_date: What date Populi should recognize the student as added. This is used for financial, add/drop dates, etc. The default is the current date.
    :param catalog_course_id: This is used for cross-listed courses. The default is the primary catalog course ID.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addEnrollment',
        course_offering_id=course_offering_id,
        person_id=person_id,
        status=status,
        status_date=status_date,
        catalog_course_id=catalog_course_id)


def add_field_of_study(
        organization_id: str = None,
        person_id: str = None,
        name: str = None,
        start_date: str = None,
        end_date: str = None,
        is_private: str = None,
        can_show_on_transcript: str = None):
    """
    Adds a field of study to a person.

    :param organization_id: The numeric ID of the organization.
    :param person_id: The numeric ID of the person.
    :param name: The name of the field of study.
    :param start_date: Format should be a date. e.g. "2020-09-05".
    :param end_date: Format should be a date. e.g. "2024-05-07".
    :param is_private: Boolean. Defaults to the "Make relationships between people and organizations private by default" security setting.
    :param can_show_on_transcript: Boolean. Defaults to true.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addFieldOfStudy',
        organization_id=organization_id,
        person_id=person_id,
        name=name,
        start_date=start_date,
        end_date=end_date,
        is_private=is_private,
        can_show_on_transcript=can_show_on_transcript)


def add_financial_aid_award(
        person_id: str = None,
        aid_year_id: str = None,
        award_type_id: str = None,
        amount: str = None,
        net_amount: str = None,
        status: str = None,
        max_amount: str = None,
        disbursements: str = None,
        include_details: str = None):
    """
    Adds a new financial aid award to a student in a given aid year, and optionally add disbursements.

    :param person_id: The numeric ID of a student.
    :param aid_year_id: The numeric ID of an aid year (see getFinancialAidYears).
    :param award_type_id: The numeric ID of an award type (see getFinancialAidAwardTypes).
    :param amount: The total/gross amount of this award.
    :param net_amount: The net amount of this award.
    :param status: Possible values: SETUP, OFFERED, ACCEPTED, DECLINED, CANCELED.
    :param max_amount: The maximum amount for this award.
    :param disbursements: An array of json encoded objects, each with the following keys: date, net_amount, gross_amount, academic_term_id
    :param include_details: Boolean. Defaults to false. If true, additional details about the newly added award and disbursements will be included in the reponse.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addFinancialAidAward',
        person_id=person_id,
        aid_year_id=aid_year_id,
        award_type_id=award_type_id,
        amount=amount,
        net_amount=net_amount,
        status=status,
        max_amount=max_amount,
        disbursements=disbursements,
        include_details=include_details)


def add_financial_aid_disbursement(
        person_id: str = None,
        award_id: str = None,
        academic_term_id: str = None,
        scheduled_date: str = None,
        amount: str = None,
        gross_amount: str = None):
    """
    Adds a new disbursement to an existing financial aid award and returns the ID of the new disbursement.

    :param person_id: The numeric ID of a student.
    :param award_id: The numeric ID of an award.
    :param academic_term_id: The numeric ID of an academic term.
    :param scheduled_date: The anticipated disbursement date in the format '2012-10-10'.
    :param amount: The net amount of this disbursement.
    :param gross_amount: The gross net amount of this disbursement (defaults to the net amount).
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addFinancialAidDisbursement',
        person_id=person_id,
        award_id=award_id,
        academic_term_id=academic_term_id,
        scheduled_date=scheduled_date,
        amount=amount,
        gross_amount=gross_amount)


def add_financial_aid_refund(
        person_id: str = None,
        award_id: str = None,
        scheduled_date: str = None,
        amount: str = None,
        type: str = None,
        asset_account_id: str = None):
    """
    Adds a new refund (to source or to student) on an existing financial aid award.

    :param person_id: The numeric ID of a student.
    :param award_id: The numeric ID of an award.
    :param scheduled_date: The anticipated refund date in the format '2012-10-10'.
    :param amount: The net amount of this disbursement.
    :param type: REFUND_TO_STUDENT: The refund is being paid out to the student. This amount will remain on his or her 1098T. REFUND_TO_SOURCE: The refund is being returned to the aid source and will no longer affect the student's 1098T.
    :param asset_account_id: The ID of the asset account the money's coming from. Only applies to REFUND_TO_STUDENT type refunds.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addFinancialAidRefund',
        person_id=person_id,
        award_id=award_id,
        scheduled_date=scheduled_date,
        amount=amount,
        type=type,
        asset_account_id=asset_account_id)


def add_inquiry(
        first_name: str = None,
        middle_name: str = None,
        last_name: str = None,
        phone: str = None,
        email: str = None,
        lead_source_id: str = None,
        program_id: str = None,
        degree_id: str = None,
        specialization_id: str = None,
        academic_term_id: str = None,
        content: str = None,
        added_on: str = None,
        representative_id: str = None,
        create_response: str = None,
        street: str = None,
        city: str = None,
        state: str = None,
        postal: str = None,
        country: str = None):
    """
    Adds a new admissions inquiry.

    :param first_name: The person's first name.
    :param middle_name: The person's middle name.
    :param last_name: The person's last name.
    :param phone: The person's phone number.
    :param email: The person's email address.
    :param lead_source_id: The numeric ID of the lead source to record for this inquiry.
    :param program_id: The numeric ID of the program the person is interested in.
    :param degree_id: The numeric ID of the degree the person is interested in.
    :param specialization_id: The numeric ID of the degree specialization the person is interested in.
    :param academic_term_id: The numeric ID of the academic term the person is interested in attending.
    :param content: The text content of the person's request
    :param added_on: The date the inquiry was made in the format '2016-10-27'
    :param representative_id: The numeric ID of the person to assign this inquiry to as a representative.
    :param create_response: Boolean. Create a response thread and/or email a thank you message on create? Defaults to false.
    :param street: The person's street address.
    :param city: The person's city.
    :param state: The person's state or province abbreviation.
    :param postal: The person's postal code.
    :param country: The person's country abbreviation.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addInquiry',
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        phone=phone,
        email=email,
        lead_source_id=lead_source_id,
        program_id=program_id,
        degree_id=degree_id,
        specialization_id=specialization_id,
        academic_term_id=academic_term_id,
        content=content,
        added_on=added_on,
        representative_id=representative_id,
        create_response=create_response,
        street=street,
        city=city,
        state=state,
        postal=postal,
        country=country)


def add_organization(name: str = None, type_id: str = None):
    """
    Adds a new organization into Populi.

    :param name: The name of the organization.
    :param type_id: The numeric ID of the type.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('addOrganization', name=name, type_id=type_id)


def add_organization_to_person(
        organization_id: str = None,
        person_id: str = None,
        type: str = None,
        title: str = None,
        start_date: str = None,
        end_date: str = None,
        is_primary: str = None,
        is_private: str = None,
        occupation_id: str = None,
        full_time: str = None,
        weekly_hours: str = None,
        salary: str = None,
        can_show_on_transcript: str = None):
    """
    Adds an organization to a person.

    :param organization_id: The numeric ID of the organization.
    :param person_id: The numeric ID of the person.
    :param type: MEMBER, EMPLOYMENT, or EDUCATION.
    :param title: The person's title at the organization.
    :param start_date: Format should be a date. e.g. "2020-09-05".
    :param end_date: Format should be a date. e.g. "2024-05-07".
    :param is_primary: Boolean.
    :param is_private: Boolean. Defaults to the "Make relationships between people and organizations private by default" security setting.
    :param occupation_id: The numeric ID of the occupation. See getOccupations. Only used when type = EMPLOYMENT.
    :param full_time: Boolean. Only used when type = EMPLOYMENT.
    :param weekly_hours: Only used when full_time = 0 and type = EMPLOYMENT.
    :param salary: Only used when type = EMPLOYMENT.
    :param can_show_on_transcript: Boolean. Defaults to true. Only used when type = EDUCATION.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addOrganizationToPerson',
        organization_id=organization_id,
        person_id=person_id,
        type=type,
        title=title,
        start_date=start_date,
        end_date=end_date,
        is_primary=is_primary,
        is_private=is_private,
        occupation_id=occupation_id,
        full_time=full_time,
        weekly_hours=weekly_hours,
        salary=salary,
        can_show_on_transcript=can_show_on_transcript)


def add_payment(
        person_id: str = None,
        amount: str = None,
        asset_account_id: str = None,
        posted_date: str = None,
        automatically_apply_to_invoices: str = None,
        pay_invoices: str = None,
        paid_by_type: str = None,
        paid_by_id: str = None,
        source_type: str = None,
        reference_number: str = None,
        currency: str = None,
        exchange_rate: str = None):
    """
    Adds a payment to a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :param amount: The amount of the payment.
    :param asset_account_id: The numeric ID of the asset account.
    :param posted_date: The transaction's posted date. Defaults to the current date.
    :param automatically_apply_to_invoices: Boolean. Pass in true if you want the payment to automatically apply to invoices. Defaults to false.
    :param pay_invoices: Array. The array key(s) should be the invoice ID(s) that you want the payment to apply to. The array value(s) should be the amount that you want to apply. e.g. array(invoice_id => amount_to_apply_to_invoice, ...).
    :param paid_by_type: PERSON (default) or ORG.
    :param paid_by_id: The numeric ID of the person or org who is making the payment. Defaults to the passed in person_id (the first parameter).
    :param source_type: CASH, CHECK (default), CREDIT_CARD, ACH, MONEY_ORDER, or OTHER.
    :param reference_number: The payment's internal reference number.
    :param currency: USD, CAD, EUR, GBP, MXN, KYD, HTG, or HKD. Defaults to your organization's main currency.
    :param exchange_rate: Only used when the currency is not your organization's home currency.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addPayment',
        person_id=person_id,
        amount=amount,
        asset_account_id=asset_account_id,
        posted_date=posted_date,
        automatically_apply_to_invoices=automatically_apply_to_invoices,
        pay_invoices=pay_invoices,
        paid_by_type=paid_by_type,
        paid_by_id=paid_by_id,
        source_type=source_type,
        reference_number=reference_number,
        currency=currency,
        exchange_rate=exchange_rate)


def add_pending_charge(
        person_id: str = None,
        amount: str = None,
        item_type: str = None,
        item_id: str = None,
        academic_term_id: str = None,
        description: str = None):
    """
    Adds a pending charge to a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :param amount: The amount of the pending charge.
    :param item_type: TUITION, FEE, ROOM_PLAN, or MEAL_PLAN.
    :param item_id: Depending on what item_type is passed in this would be a tution bracket ID, a fee ID, a room plan ID, or a meal plan ID.
    :param academic_term_id: A pending charge with item_type FEE does not have to be attached to a particular academic term. All other item_types must be attached to a particular academic term.
    :param description: A description for the pending charge.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addPendingCharge',
        person_id=person_id,
        amount=amount,
        item_type=item_type,
        item_id=item_id,
        academic_term_id=academic_term_id,
        description=description)


def add_person(
        first_name: str = None,
        last_name: str = None,
        gender: str = None,
        birth_date: str = None):
    """
    Adds a new person into Populi. To avoid duplicate records, we strongly recommend calling getPossibleDuplicatePeople before calling addPerson.

    :param first_name: The official/legal first name for this person (you can set preferred name later).
    :param last_name: The last name for the person.
    :param gender: MALE, FEMALE, or UNKNOWN (default).
    :param birth_date: e.g. 1979-10-02
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addPerson',
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        birth_date=birth_date)


def add_phone_number(
        person_id: str = None,
        organization_id: str = None,
        phone_number: str = None,
        type: str = None,
        primary: str = None,
        public: str = None):
    """
    Adds a phone number to a person or organization.

    :param person_id: The numeric ID of the person to whose profile you are attaching this phone number.
    :param organization_id: The numeric ID of the organization to whose profile you are attaching this phone number.
    :param phone_number: e.g. 1-800-888-8888
    :param type: Person phone numbers: HOME, WORK, MOBILE, SCHOOL, FAX, OTHER
    :param primary: Boolean. Use if you want to mark the phone number as primary or not primary. Defaults to false.
    :param public: Boolean. Use if you want to mark the phone number as public or not public. Defaults to true.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addPhoneNumber',
        person_id=person_id,
        organization_id=organization_id,
        phone_number=phone_number,
        type=type,
        primary=primary,
        public=public)


def add_profile_picture(person_id: str = None, image: str = None):
    """
    Adds a profile picture to Populi. The ideal dimensions are 600 wide x 750 tall.

    :param person_id: The numeric ID of the person.
    :param image: A base 64 encoded string of the image.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('addProfilePicture', person_id=person_id, image=image)


def add_role(person_id: str = None, role_id: str = None):
    """
    Adds a role to a person.

    :param person_id: The numeric ID of the person you're interested in.
    :param role_id: The numeric ID of the role you want to add.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('addRole', person_id=person_id, role_id=role_id)


def add_student_degree(
        person_id: str = None,
        degree_id: str = None,
        active_date: str = None,
        catalog_year_id: str = None,
        anticipated_completion_date: str = None,
        show_on_transcript: str = None):
    """
    Add a degree to a particular student.

    :param person_id: The numeric ID of the person you're interested in.
    :param degree_id: The numeric ID of the degree you're interested in.
    :param active_date: The active date in the format '2012-10-10'.
    :param catalog_year_id: The numeric ID of the catalog year you're interested in.
    :param anticipated_completion_date: The anticipated completion date in the format '2012-10-10'.
    :param show_on_transcript: Possible values: 1 (default) or 0. Whether the degree should show on the transcript.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addStudentDegree',
        person_id=person_id,
        degree_id=degree_id,
        active_date=active_date,
        catalog_year_id=catalog_year_id,
        anticipated_completion_date=anticipated_completion_date,
        show_on_transcript=show_on_transcript)


def add_student_degree_specialization(
        person_id: str = None,
        degree_student_id: str = None,
        specialization_id: str = None,
        granted_date: str = None,
        show_on_transcript: str = None):
    """
    Adds a specialization to student's existing degree.

    :param person_id: The numeric ID of the person you're interested in.
    :param degree_student_id: The numeric ID of the degree_student object in question.
    :param specialization_id: The numeric ID of the specialization you wish to add.
    :param granted_date: The granted date in the format '2012-10-10'.
    :param show_on_transcript: Possible values: 1 (default) or 0. Whether the specialization should show on the transcript.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addStudentDegreeSpecialization',
        person_id=person_id,
        degree_student_id=degree_student_id,
        specialization_id=specialization_id,
        granted_date=granted_date,
        show_on_transcript=show_on_transcript)


def add_student_program(
        person_id: str = None,
        program_id: str = None,
        start_date: str = None):
    """
    Add a program to a particular student.

    :param person_id: The numeric ID of the person you're interested in.
    :param program_id: The numeric ID of the program you're interested in.
    :param start_date: The start date of the program in the format '2018-06-05'. Defaults to the current date.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addStudentProgram',
        person_id=person_id,
        program_id=program_id,
        start_date=start_date)


def add_tag(
        person_id: str = None,
        organization_id: str = None,
        tag_id: str = None,
        tag: str = None):
    """
    Adds a tag to a particular person.

    :param person_id: The numeric ID of the person who should be tagged.
    :param organization_id: The numeric ID of the organization that should be tagged.
    :param tag_id: The numeric ID of the tag.
    :param tag: The actual tag you want to be attached (e.g. "Do not call", or "Good reference").
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addTag',
        person_id=person_id,
        organization_id=organization_id,
        tag_id=tag_id,
        tag=tag)


def add_term_tuition_schedule_to_student(
        person_id: str = None,
        academic_term_id: str = None,
        tuition_schedule_id: str = None,
        tuition_schedule_bracket_id: str = None):
    """
    Adds a term tuition schedule to a student.

    :param person_id: The numeric person ID of the student you're interested in.
    :param academic_term_id: The numeric ID of the academic term you're interested in.
    :param tuition_schedule_id: The numeric ID of the tuition schedule you're interested in.
    :param tuition_schedule_bracket_id: The numeric ID of the tuition schedule bracket you're interested in, or "AUTOMATIC" (defaults to "AUTOMATIC").
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addTermTuitionScheduleToStudent',
        person_id=person_id,
        academic_term_id=academic_term_id,
        tuition_schedule_id=tuition_schedule_id,
        tuition_schedule_bracket_id=tuition_schedule_bracket_id)


def add_todo(
        content: str = None,
        due: str = None,
        assigned_to: str = None,
        attached_to_type: str = None,
        attached_to: str = None):
    """
    Adds a new todo (the Added By of this new todo will show the currently logged-in user).

    :param content: What the todo should say (e.g. "Remember the milk on the way home from work")
    :param due: The due date for this todo (e.g. 2011-06-24)
    :param assigned_to: The person responsible for completing this todo. Defaults to the currently logged-in user.
    :param attached_to_type: If you'd like to attach this todo onto someone's profile, set this to PERSON.
    :param attached_to: If you'd like to attach this todo onto someone's profile, put that person's numeric ID here (and you MUST have attached_to_type set to PERSON).
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addTodo',
        content=content,
        due=due,
        assigned_to=assigned_to,
        attached_to_type=attached_to_type,
        attached_to=attached_to)


def add_transfer_credit(
        organization_id: str = None,
        person_id: str = None,
        course_number: str = None,
        course_name: str = None,
        credits: str = None,
        hours: str = None,
        clinical_hours: str = None,
        attendance_hours: str = None,
        fulfills_program_requirements: str = None,
        pass_affects_gpa: str = None,
        fail_affects_gpa: str = None,
        pass_fail_pass_affects_gpa: str = None,
        pass_fail_fail_affects_gpa: str = None,
        affects_standing: str = None,
        catalog_course_id: str = None,
        course_group_id: str = None,
        description: str = None,
        status: str = None,
        effective_date: str = None,
        applies_to_all_programs: str = None):
    """
    Adds a transfer credit to a person.

    :param organization_id: The numeric ID of the organization. Transfer Instutitions are Organizations.
    :param person_id: The numeric ID of the person.
    :param course_number:  
    :param course_name:  
    :param credits:  
    :param hours:  
    :param clinical_hours:  
    :param attendance_hours:  
    :param fulfills_program_requirements: Boolean. Defaults to true.
    :param pass_affects_gpa: Boolean. Defaults to true.
    :param fail_affects_gpa: Boolean. Defaults to true.
    :param pass_fail_pass_affects_gpa: Boolean. Defaults to false.
    :param pass_fail_fail_affects_gpa: Boolean. Defaults to true.
    :param affects_standing: Boolean. Defaults to true.
    :param catalog_course_id: The numeric ID of the catalog course.
    :param course_group_id: The numeric ID of the course group.
    :param description:  
    :param status: PENDING (default), APPROVED, or REJECTED
    :param effective_date: Format should be a date. e.g. "2020-09-05".
    :param applies_to_all_programs: Boolean. Defaults to true.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addTransferCredit',
        organization_id=organization_id,
        person_id=person_id,
        course_number=course_number,
        course_name=course_name,
        credits=credits,
        hours=hours,
        clinical_hours=clinical_hours,
        attendance_hours=attendance_hours,
        fulfills_program_requirements=fulfills_program_requirements,
        pass_affects_gpa=pass_affects_gpa,
        fail_affects_gpa=fail_affects_gpa,
        pass_fail_pass_affects_gpa=pass_fail_pass_affects_gpa,
        pass_fail_fail_affects_gpa=pass_fail_fail_affects_gpa,
        affects_standing=affects_standing,
        catalog_course_id=catalog_course_id,
        course_group_id=course_group_id,
        description=description,
        status=status,
        effective_date=effective_date,
        applies_to_all_programs=applies_to_all_programs)


def add_transfer_credit_program(
        transfer_credit_id: str = None,
        program_id: str = None,
        grade: str = None,
        pass_fail: str = None,
        show_on_transcript: str = None,
        is_transfer_student: str = None):
    """
    Adds a program to a transfer credit.

    :param transfer_credit_id: The numeric ID of the transfer credit you're interested in.
    :param program_id: The numeric ID of the program you're interested in.
    :param grade: Mixed. See getTransferCreditProgramGradeOptions for a list of values.
    :param pass_fail: Boolean. Whether or not this the grade is a pass/fail grade. Defaults to false.
    :param show_on_transcript: Boolean. Defaults to true. Whether or not the transfer credit should show up on the transcript. Only used when the transfer credit's status = APPROVED.
    :param is_transfer_student: Boolean. Defaults to true. Whether or not the student is considered a transfer student in the particular program. Only used when the transfer credit's status = APPROVED.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addTransferCreditProgram',
        transfer_credit_id=transfer_credit_id,
        program_id=program_id,
        grade=grade,
        pass_fail=pass_fail,
        show_on_transcript=show_on_transcript,
        is_transfer_student=is_transfer_student)


def add_user(
        person_id: str = None,
        username: str = None,
        send_welcome_email: str = None):
    """
    Grants user access to a person.

    :param person_id: The numeric ID of the person whose user account will be created.
    :param username: A username for the person. Allowed characters are letters, numbers, period and underscore. If no username is passed in Populi will autogenerate one.
    :param send_welcome_email: Boolean. Send a welcome email to the person's primary email address. Defaults to true.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'addUser',
        person_id=person_id,
        username=username,
        send_welcome_email=send_welcome_email)


def block_user(person_id: str = None, reason: str = None):
    """
    Used to block a particular user account.

    :param person_id: The numeric ID of the person whose user account will be blocked.
    :param reason: The reason the user account is being blocked.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('blockUser', person_id=person_id, reason=reason)


def create_course_instance_meeting(
        instanceID: str = None,
        startMonth: str = None,
        startDay: str = None,
        startYear: str = None,
        startHour: str = None,
        startMinute: str = None,
        endMonth: str = None,
        endDay: str = None,
        endYear: str = None,
        endHour: str = None,
        endMinute: str = None,
        roomID: str = None,
        counts_toward_attendance_hours: str = None,
        counts_toward_clinical_hours: str = None,
        initial_student_attendance_status: str = None):
    """
    Creates a meeting for a particular course instance.

    :param instanceID: The numeric ID of the course instance you're interested in.
    :param startMonth: e.g. 01
    :param startDay: e.g. 01
    :param startYear: e.g. 2016
    :param startHour: Hours should be 0 based. e.g. 0-23
    :param startMinute: Minutes should be 0 based. e.g. 0-59
    :param endMonth: e.g. 01
    :param endDay: e.g. 01
    :param endYear: e.g. 2016
    :param endHour: Hours should be 0 based. e.g. 0-23
    :param endMinute: Minutes should be 0 based. e.g. 0-59
    :param roomID: The numeric ID of the room where the meeting will take place.
    :param counts_toward_attendance_hours: Boolean. Defaults to true.
    :param counts_toward_clinical_hours: Boolean. Defaults to true.
    :param initial_student_attendance_status: PRESENT (default), ABSENT, TARDY, EXCUSED, or NONE
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'createCourseInstanceMeeting',
        instanceID=instanceID,
        startMonth=startMonth,
        startDay=startDay,
        startYear=startYear,
        startHour=startHour,
        startMinute=startMinute,
        endMonth=endMonth,
        endDay=endDay,
        endYear=endYear,
        endHour=endHour,
        endMinute=endMinute,
        roomID=roomID,
        counts_toward_attendance_hours=counts_toward_attendance_hours,
        counts_toward_clinical_hours=counts_toward_clinical_hours,
        initial_student_attendance_status=initial_student_attendance_status)


def create_financial_aid_disbursement_batch(
        batch_type: str = None,
        disbursement_ids: str = None):
    """
    Creates a new financial aid disbursement batch and returns the ID of the new batch.

    :param batch_type: Must be DISBURSEMENT, REFUND_TO_STUDENT, or REFUND_TO_SOURCE
    :param disbursement_ids: An array of disbursement IDs - see
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'createFinancialAidDisbursementBatch',
        batch_type=batch_type,
        disbursement_ids=disbursement_ids)


def delete_address(addressid: str = None):
    """
    Deletes an address.

    :param addressid: The numeric ID of the address.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('deleteAddress', addressid=addressid)


def delete_application(application_id: str = None):
    """
    Deletes an application from an applicant.

    :param application_id: Numeric ID of the application.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('deleteApplication', application_id=application_id)


def delete_campus_from_student(person_id: str = None, campus_id: str = None):
    """
    Deletes a campus from a student.

    :param person_id: The numeric ID of the person you're interested in.
    :param campus_id: The numeric ID of the campus you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'deleteCampusFromStudent',
        person_id=person_id,
        campus_id=campus_id)


def delete_communication_plan_from_person(
        communication_plan_instance_id: str = None,
        person_id: str = None):
    """
    Deletes a communication plans from a person.

    :param communication_plan_instance_id: The numeric ID of the communication plan instance you're interested in.
    :param person_id: The numeric ID of the person you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'deleteCommunicationPlanFromPerson',
        communication_plan_instance_id=communication_plan_instance_id,
        person_id=person_id)


def delete_course_instance_assignment(
        instance_id: str = None,
        assignment_id: str = None):
    """
    Deletes an assignment in a particular course instance.

    :param instance_id: The numeric ID of the course instance you're interested in.
    :param assignment_id: The numeric ID of the assignment you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'deleteCourseInstanceAssignment',
        instance_id=instance_id,
        assignment_id=assignment_id)


def delete_course_instance_assignment_group(
        instance_id: str = None,
        group_id: str = None):
    """
    Deletes an assignment group in a particular course instance.

    :param instance_id: The numeric ID of the course instance you're interested in.
    :param group_id: The numeric ID of the assignment group you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'deleteCourseInstanceAssignmentGroup',
        instance_id=instance_id,
        group_id=group_id)


def delete_course_offering_link(
        course_offering_id: str = None,
        link_id: str = None):
    """
    Deletes a link attached to a particular course offering.

    :param course_offering_id: The numeric ID of the course offering you're interested in.
    :param link_id: The numeric ID of the link you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'deleteCourseOfferingLink',
        course_offering_id=course_offering_id,
        link_id=link_id)


def delete_custom_field(
        person_id: str = None,
        owner_id: str = None,
        custom_field_id: str = None,
        term_id: str = None):
    """
    Deletes a custom field attached a particular person, organization, or donation.

    :param person_id: The numeric ID of the person you're interested in.
    :param owner_id: The numeric ID of the object you're interested in.
    :param custom_field_id: The numeric ID of the custom field you're interested in.
    :param term_id: The numeric ID of the term you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'deleteCustomField',
        person_id=person_id,
        owner_id=owner_id,
        custom_field_id=custom_field_id,
        term_id=term_id)


def delete_email_address(emailid: str = None):
    """
    Deletes an email address.

    :param emailid: The numeric ID of the email address.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('deleteEmailAddress', emailid=emailid)


def delete_financial_aid_award(award_id: str = None):
    """
    Deletes an existing financial aid award (must not have any posted disbursements).

    :param award_id: The numeric ID of an award with no posted disbursements.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('deleteFinancialAidAward', award_id=award_id)


def delete_financial_aid_disbursement(disbursement_id: str = None):
    """
    Deletes an existing disbursement which has not yet been posted.

    :param disbursement_id: The numeric ID of a disbursement with a status of SETUP or SCHEDULED (but not POSTED, DELETED or VOID)
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'deleteFinancialAidDisbursement',
        disbursement_id=disbursement_id)


def delete_financial_aid_refund(refund_id: str = None):
    """
    Deletes an existing refund (REFUND_TO_STUDENT, REFUND_TO_SOURCE) which has not yet been posted.

    :param refund_id: The numeric ID of a refund with a status of SETUP or SCHEDULED (but not POSTED, DELETED or VOID)
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('deleteFinancialAidRefund', refund_id=refund_id)


def delete_license_plate(person_id: str = None):
    """
    Delete a person's license plate.

    :param person_id: The numeric ID of the person.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('deleteLicensePlate', person_id=person_id)


def delete_person_birth_date(person_id: str = None):
    """
    Deletes the birth date for a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('deletePersonBirthDate', person_id=person_id)


def delete_person_citizenship(person_id: str = None):
    """
    Deletes the citizenship for a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('deletePersonCitizenship', person_id=person_id)


def delete_person_hometown(person_id: str = None):
    """
    Deletes the hometown for a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('deletePersonHometown', person_id=person_id)


def delete_person_organization(id: str = None):
    """
    Deletes a person organization record.

    :param id: The numeric ID of the person_organization record. See getPersonOrganization.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('deletePersonOrganization', id=id)


def delete_person_race_ethnicity(person_id: str = None):
    """
    Deletes the race/ethnicity for a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('deletePersonRaceEthnicity', person_id=person_id)


def delete_person_s_i_n(person_id: str = None):
    """
    Deletes the social insurance number for a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('deletePersonSIN', person_id=person_id)


def delete_person_s_s_n(person_id: str = None):
    """
    Deletes the social security number for a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('deletePersonSSN', person_id=person_id)


def delete_phone_number(phoneid: str = None):
    """
    Deletes a phone number.

    :param phoneid: The numeric ID of the phone number.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('deletePhoneNumber', phoneid=phoneid)


def delete_student_degree_specialization(
        person_id: str = None,
        degree_student_id: str = None,
        specialization_id: str = None):
    """
    Deletes a specialization attached to a student's degree.

    :param person_id: The numeric ID of the person you're interested in.
    :param degree_student_id: The numeric ID of the degree_student object in question.
    :param specialization_id: The numeric ID of the specialization you wish to remove.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'deleteStudentDegreeSpecialization',
        person_id=person_id,
        degree_student_id=degree_student_id,
        specialization_id=specialization_id)


def delete_student_meal_plan(
        person_id: str = None,
        academic_term_id: str = None):
    """
    Removes a meal plan from a student.

    :param person_id: The numeric ID of the person.
    :param academic_term_id: The numeric ID of the academic term you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'deleteStudentMealPlan',
        person_id=person_id,
        academic_term_id=academic_term_id)


def delete_student_room_plan(
        person_id: str = None,
        academic_term_id: str = None):
    """
    Removes a room plan from a student.

    :param person_id: The numeric ID of the person.
    :param academic_term_id: The numeric ID of the academic term you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'deleteStudentRoomPlan',
        person_id=person_id,
        academic_term_id=academic_term_id)


def delete_todo(todo_id: str = None):
    """
    Deletes a todo.

    :param todo_id: The numeric ID of the todo you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('deleteTodo', todo_id=todo_id)


def download_backup(backup_id: str = None):
    """
    Once a backup is ready for download, you can download it (as a ZIP file named backup_YEAR_MO_DY.zip) using this task.

    :param backup_id: The numeric ID of the backup you'd like to download.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('downloadBackup', raw_data=True, backup_id=backup_id)


def download_file(file_id: str = None):
    """
    Downloads the contents of a file.

    :param file_id: The numeric ID of the file you'd like to download.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('downloadFile', raw_data=True, file_id=file_id)


def download_student_schedule(person_id: str = None, term_id: str = None):
    """
    Returns a PDF version of a student's schedule in a term.

    :param person_id: The numeric ID of the person you're interested in.
    :param term_id: The numeric ID of the academic term you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'downloadStudentSchedule',
        raw_data=True,
        person_id=person_id,
        term_id=term_id)


def edit_aid_application(
        aid_application_id: str = None,
        assigned_to_id: str = None,
        enrollment: str = None,
        dependency: str = None,
        student_aid_class_id: str = None,
        program_months: str = None,
        year_coa: str = None,
        program_coa: str = None,
        year_efc: str = None,
        program_efc: str = None,
        student_agi: str = None,
        parent_agi: str = None,
        legal_residence_state: str = None,
        verification: str = None,
        verification_status: str = None,
        verification_group: str = None,
        auto_zero_efc: str = None,
        status: str = None,
        housing: str = None):
    """
    Edits an existing financial aid application.

    :param aid_application_id: The numeric ID of the aid application.
    :param assigned_to_id: The numeric ID of the person to whom this aid application is assigned.
    :param enrollment: The student's enrollment status (for financial aid purposes): FULL_TIME, THREE_QUARTER_TIME, HALF_TIME, or LESS_THAN_HALF_TIME
    :param dependency: Whether this student is considered a dependent for aid purposes: can be blank, DEPENDENT, or INDEPENDENT
    :param student_aid_class_id: The numeric aid class ID for this student (aid classes are how Populi groups similar types of students together).
    :param program_months: The number of months this student is expected to be enrolled in your school's program.
    :param year_coa: This student's Cost of Attendance if they were attending for the entire year (this should be extrapolated out from their program_coa for shorter programs, since Pell calculates based on COA for the entire year).
    :param program_coa: This student's Cost of Attendance in this aid year.
    :param year_efc: This student's Estimated Family Contribution in this aid year (extrapolated out to a full year for shorter programs, if necessary).
    :param program_efc: This student's Estimated Family Contribution in this aid year.
    :param student_agi: This student's Adjusted Gross Income in this aid year.
    :param parent_agi: The parents' Adjusted Gross Income in this aid year.
    :param legal_residence_state: The student's state of legal residence.
    :param verification: Whether this student has been selected for verification. Must be either blank, SELECTED_BY_COLLEGE, or SELECTED_BY_GOVERNMENT.
    :param verification_status: If this student was selected for verification (see above), what's their status? If set, must be one of: IN_PROGRESS, COMPLETED, REJECTED, or EXEMPTED. Cannot be set if `verification` is blank.
    :param verification_group: If this student was selected for verification (see above), what verification group are they in? If set, must be one of: 'Standard, 'Child Support Paid', 'Custom', 'Aggregate', or 'Household Resources'. Cannot be set unless `verification` is set to SELECTED_BY_GOVERNMENT.
    :param auto_zero_efc: Whether the student's EFC was calculated using the "automatic zero" EFC formula. If set, must be: 1 or 0
    :param status: The application status: SETUP, IN_PROGRESS, COMPLETED, NEEDS_ATTENTION, or CANCELED
    :param housing: The student's housing situation: ON_CAMPUS, WITH_PARENT, or OFF_CAMPUS
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'editAidApplication',
        aid_application_id=aid_application_id,
        assigned_to_id=assigned_to_id,
        enrollment=enrollment,
        dependency=dependency,
        student_aid_class_id=student_aid_class_id,
        program_months=program_months,
        year_coa=year_coa,
        program_coa=program_coa,
        year_efc=year_efc,
        program_efc=program_efc,
        student_agi=student_agi,
        parent_agi=parent_agi,
        legal_residence_state=legal_residence_state,
        verification=verification,
        verification_status=verification_status,
        verification_group=verification_group,
        auto_zero_efc=auto_zero_efc,
        status=status,
        housing=housing)


def edit_donation(
        donation_id: str = None,
        staff_comment: str = None,
        campaign_id: str = None,
        appeal_id: str = None,
        acknowledged_at: str = None,
        acknowledged_by: str = None):
    """
    Edits an existing donation.

    :param donation_id: The numeric ID of the donation
    :param staff_comment: The comment about this donation only visible to staff.
    :param campaign_id: The numeric ID of the campaign associated with this donation.
    :param appeal_id: The numeric ID of the appeal associated with this donation.
    :param acknowledged_at: The date and time the donation was acknowledged. (e.g. 2019-05-02 14:00:00). Set this to blank to mark a donation as unacknowledged.
    :param acknowledged_by: The numeric ID of the person who acknowledged the donation.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'editDonation',
        donation_id=donation_id,
        staff_comment=staff_comment,
        campaign_id=campaign_id,
        appeal_id=appeal_id,
        acknowledged_at=acknowledged_at,
        acknowledged_by=acknowledged_by)


def edit_financial_aid_award(
        award_id: str = None,
        amount: str = None,
        net_amount: str = None,
        status: str = None,
        max_amount: str = None):
    """
    Edits an existing financial aid award.

    :param award_id: The numeric ID of an award.
    :param amount: The total/gross amount of this award.
    :param net_amount: The net amount of this award.
    :param status: Possible values: SETUP, OFFERED, ACCEPTED, DECLINED, CANCELED.
    :param max_amount: The maximum amount for this award.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'editFinancialAidAward',
        award_id=award_id,
        amount=amount,
        net_amount=net_amount,
        status=status,
        max_amount=max_amount)


def edit_financial_aid_disbursement(
        disbursement_id: str = None,
        scheduled_date: str = None,
        amount: str = None,
        gross_amount: str = None):
    """
    Edits an existing disbursement (only possible before it's posted).

    :param disbursement_id: The numeric ID of a disbursement.
    :param scheduled_date: The anticipated disbursement date in the format '2012-10-10'.
    :param amount: The net amount of this disbursement.
    :param gross_amount: The gross net amount of this disbursement.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'editFinancialAidDisbursement',
        disbursement_id=disbursement_id,
        scheduled_date=scheduled_date,
        amount=amount,
        gross_amount=gross_amount)


def edit_financial_aid_refund(
        refund_id: str = None,
        scheduled_date: str = None,
        amount: str = None,
        type: str = None,
        asset_account_id: str = None):
    """
    Edits an existing refund (only possible before it's posted).

    :param refund_id: The numeric ID of a refund.
    :param scheduled_date: The anticipated disbursement date in the format '2012-10-10'.
    :param amount: The net amount of this refund.
    :param type: Possible options: REFUND_TO_STUDENT, REFUND_TO_SOURCE
    :param asset_account_id: The ID of the asset account the money's coming from. Only applies to REFUND_TO_STUDENT type refunds.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'editFinancialAidRefund',
        refund_id=refund_id,
        scheduled_date=scheduled_date,
        amount=amount,
        type=type,
        asset_account_id=asset_account_id)


def edit_transfer_credit_program(
        transfer_credit_id: str = None,
        program_id: str = None,
        grade: str = None,
        pass_fail: str = None,
        show_on_transcript: str = None,
        is_transfer_student: str = None):
    """
    Used to edit a transfer credit's program data.

    :param transfer_credit_id: The numeric ID of the transfer credit you're interested in.
    :param program_id: The numeric ID of the program you're interested in.
    :param grade: Mixed. See getTransferCreditProgramGradeOptions for a list of values.
    :param pass_fail: Boolean. Whether or not this the grade is a pass/fail grade. Defaults to false.
    :param show_on_transcript: Boolean. Defaults to true. Whether or not the transfer credit should show up on the transcript. Only used when the transfer credit's status = APPROVED.
    :param is_transfer_student: Boolean. Defaults to true. Whether or not the student is considered a transfer student in the particular program. Only used when the transfer credit's status = APPROVED.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'editTransferCreditProgram',
        transfer_credit_id=transfer_credit_id,
        program_id=program_id,
        grade=grade,
        pass_fail=pass_fail,
        show_on_transcript=show_on_transcript,
        is_transfer_student=is_transfer_student)


def finalize_course_instance(instance_id: str = None):
    """
    Finalizes a course instance.

    :param instance_id: The numeric ID of the course instance you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('finalizeCourseInstance', instance_id=instance_id)


def get_academic_terms():
    """
    Returns all academic terms.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getAcademicTerms')


def get_academic_years():
    """
    Returns all academic years.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getAcademicYears')


def get_aid_application(aid_application_id: str = None):
    """
    Returns a particular financial aid application (each student can have one per aid year).

    :param aid_application_id: The numeric ID of the aid application.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getAidApplication',
        aid_application_id=aid_application_id)


def get_aid_application_for_student_aid_year(
        student_id: str = None,
        aid_year_id: str = None):
    """
    Returns a particular financial aid application (each student can have one per aid year).

    :param student_id: The numeric ID of the student.
    :param aid_year_id: The numeric ID of the aid year.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getAidApplicationForStudentAidYear',
        student_id=student_id,
        aid_year_id=aid_year_id)


def get_all_custom_fields(type: str = None):
    """
    Returns all custom fields your college has defined.

    :param type: ALL (default), PERSON, STUDENT, TERM_STUDENT, ADMISSIONS, CAMPUS_LIFE, FINANCIAL, or FINANCIAL_AID, DONATION, ORGANIZATION
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getAllCustomFields', type=type)


def get_appeals():
    """
    Returns all information related to donation appeals configured for your institution.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getAppeals')


def get_application(application_id: str = None):
    """
    Returns an application.

    :param application_id: The numeric ID of the application you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getApplication', application_id=application_id)


def get_application_components(application_id: str = None):
    """
    Returns all application components for a particular application.

    :param application_id: The numeric ID of the application you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getApplicationComponents',
        application_id=application_id)


def get_application_field_options(
        application_field_id: str = None,
        country: str = None,
        degree_id: str = None):
    """
    Returns the options for an application field.

    :param application_field_id: The numeric ID of the application field you're interested in.
    :param country: US, CA
    :param degree_id: Numeric ID of a degree.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getApplicationFieldOptions',
        application_field_id=application_field_id,
        country=country,
        degree_id=degree_id)


def get_application_templates(show_online_only: str = None):
    """
    Returns all application templates.

    :param show_online_only: Boolean. If true only application templates that are set to show online will be returned. Defaults to false.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getApplicationTemplates',
        show_online_only=show_online_only)


def get_applications(
        status: str = None,
        date_field: str = None,
        start_date: str = None,
        end_date: str = None,
        term_id: str = None,
        program_id: str = None,
        degree_id: str = None,
        specialization_id: str = None,
        lead_active: str = None,
        offset: str = None):
    """
    Returns applications based on the filter conditions.

    :param status: Possible values: IN_PROGRESS, SUBMITTED, PENDING_DECISION, ACCEPTED, DECLINED, WITHDRAWN, DEFERRED, or WAITLISTED.
    :param date_field: The name of the date field you want to filter by (e.g. APPLIED, DECISION, SUBMITTED, or WITHDRAWN).
    :param start_date: The start date used to filter the "date_field" parameter.
    :param end_date: The end date used to filter the "date_field" parameter.
    :param term_id: The numeric ID of the academic term you're interested in.
    :param program_id: The numeric ID of the program you're interested in.
    :param degree_id: The numeric ID of the degree you're interested in.
    :param specialization_id: The numeric ID of the specialization you're interested in.
    :param lead_active: Boolean. 1 or 0.
    :param offset: The numeric value you want to offset the results by.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getApplications',
        status=status,
        date_field=date_field,
        start_date=start_date,
        end_date=end_date,
        term_id=term_id,
        program_id=program_id,
        degree_id=degree_id,
        specialization_id=specialization_id,
        lead_active=lead_active,
        offset=offset)


def get_assignment_comments(assignment_id: str = None, person_id: str = None):
    """
    Returns assignment comments for a particular assignment and person.

    :param assignment_id: Numeric ID of the assignment.
    :param person_id: Numeric ID of the person.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getAssignmentComments',
        assignment_id=assignment_id,
        person_id=person_id)


def get_available_roles():
    """
    Returns all the roles in Populi (Student, Staff, Admissions, etc).

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getAvailableRoles')


def get_campaigns():
    """
    Returns all information related to donation campaigns configured for your institution.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getCampaigns')


def get_campus_life_rooms(academic_term_id: str = None):
    """
    Returns campus life rooms.

    :param academic_term_id: The numeric ID of the academic term you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getCampusLifeRooms',
        academic_term_id=academic_term_id)


def get_campuses():
    """
    Returns all campuses.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getCampuses')


def get_communication_plans():
    """
    Returns all available communication plans.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getCommunicationPlans')


def get_countries():
    """
    Returns a list of countries and their respective abbreviations.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getCountries')


def get_course_catalog(include_retired: str = None):
    """
    Returns courses from your catalog (only active courses are returned by default).

    :param include_retired: If set to 1, retired courses will be returned as well.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getCourseCatalog', include_retired=include_retired)


def get_course_group_info(
        course_group_id: str = None,
        academic_year_id: str = None):
    """
    Returns information about a course group.

    :param course_group_id: The numeric ID of the course group you're interested in.
    :param academic_year_id: The numeric ID of the academic year you're interested in. Defaults to the current academic year ID.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getCourseGroupInfo',
        course_group_id=course_group_id,
        academic_year_id=academic_year_id)


def get_course_groups():
    """
    Returns a list of course groups.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getCourseGroups')


def get_course_instance(instance_id: str = None):
    """
    A course instance is created each time a course from the catalog is offered in a particular term. If the same catalog course is offered multiple times in the same term, each instance will have a unique section number.

    :param instance_id: The numeric ID of the course instance you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getCourseInstance', instance_id=instance_id)


def get_course_instance_assignment_groups(instance_id: str = None):
    """
    Assignment groups are worth a fixed percentage of the course (e.g. Quizzes are worth 10% of each student's final grade), and you can then add as many assignments within the Quizzes group as you like, or even add new assignments to the group part-way through the term, and be guaranteed that the value of all those assignments together will still equal 10% of the course.

    :param instance_id: The numeric ID of the course instance you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getCourseInstanceAssignmentGroups',
        instance_id=instance_id)


def get_course_instance_assignments(instance_id: str = None):
    """
    Returns information about each assignment in a course - including which Assignment Group it belongs to.

    :param instance_id: The numeric ID of the course instance you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getCourseInstanceAssignments',
        instance_id=instance_id)


def get_course_instance_files(instance_id: str = None):
    """
    Returns the files attached to a course instance.

    :param instance_id: The numeric ID of the course instance you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getCourseInstanceFiles', instance_id=instance_id)


def get_course_instance_lessons(instance_id: str = None):
    """
    Returns the lessons attached to a course instance.

    :param instance_id: The numeric ID of the course instance you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getCourseInstanceLessons', instance_id=instance_id)


def get_course_instance_meeting_attendance(
        instanceID: str = None,
        meetingID: str = None,
        return_students_with_no_attendance_taken: str = None):
    """
    Gets attendance for a course instance meeting.

    :param instanceID: The numeric ID of the course instance you're interested in.
    :param meetingID: The numeric ID of the meeting.
    :param return_students_with_no_attendance_taken: Boolean. Defaults to false.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getCourseInstanceMeetingAttendance',
        instanceID=instanceID,
        meetingID=meetingID,
        return_students_with_no_attendance_taken=return_students_with_no_attendance_taken)


def get_course_instance_meetings(instanceID: str = None):
    """
    Returns the meetings attached to a course instance.

    :param instanceID: The numeric ID of the course instance you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getCourseInstanceMeetings', instanceID=instanceID)


def get_course_instance_student(
        instance_id: str = None,
        person_id: str = None):
    """
    Returns a single student from a course instance.

    :param instance_id: The numeric ID of the course instance you're interested in.
    :param person_id: The numeric ID of the student you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getCourseInstanceStudent',
        instance_id=instance_id,
        person_id=person_id)


def get_course_instance_student_attendance(
        instanceID: str = None,
        person_id: str = None):
    """
    Gets attendance for all course instance meetings for a particular student.

    :param instanceID: The numeric ID of the course instance you're interested in.
    :param person_id: The numeric ID of the person whose attendance you wish to look up.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getCourseInstanceStudentAttendance',
        instanceID=instanceID,
        person_id=person_id)


def get_course_instance_students(instance_id: str = None):
    """
    Returns all students enrolled, auditing, incomoplete, or withdrawn in a course instance.

    :param instance_id: The numeric ID of the course instance you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getCourseInstanceStudents', instance_id=instance_id)


def get_course_offering_links(course_offering_id: str = None):
    """
    Returns links attached to a particular course offering.

    :param course_offering_id: The numeric ID of the course offering you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getCourseOfferingLinks',
        course_offering_id=course_offering_id)


def get_current_academic_term():
    """
    Returns the current academic term.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getCurrentAcademicTerm')


def get_current_academic_year():
    """
    Returns the current academic year.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getCurrentAcademicYear')


def get_custom_field_options(custom_field_id: str = None):
    """
    Returns available options for RADIO, CHECKBOX, and SELECT input type custom fields.

    :param custom_field_id: The numeric ID of the custom field you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getCustomFieldOptions',
        custom_field_id=custom_field_id)


def get_custom_fields(
        person_id: str = None,
        organization_id: str = None,
        donation_id: str = None,
        type: str = None):
    """
    Returns custom fields attached to a particular person or organization.

    :param person_id: The numeric ID of the person you're interested in.
    :param organization_id: The numeric ID of the organization you're interested in.
    :param donation_id: The numeric ID of the donation you're interested in.
    :param type: ALL (default), PERSON, STUDENT, TERM_STUDENT, ADMISSIONS, CAMPUS_LIFE, FINANCIAL, or FINANCIAL_AID, DONATION, ORGANIZATION
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getCustomFields',
        person_id=person_id,
        organization_id=organization_id,
        donation_id=donation_id,
        type=type)


def get_data_slicer_report(report_id: str = None, export_format: str = None):
    """
    Produces and returns a data slicer report in CSV or XLS format.

    :param report_id: The numeric ID of the data slicer report.
    :param export_format: The file format of the report to be produced, either XLS or CSV.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getDataSlicerReport',
        report_id=report_id,
        export_format=export_format)


def get_data_slicer_reports():
    """
    Returns a list of data slicer reports available for use.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getDataSlicerReports')


def get_degree_audit(
        person_id: str = None,
        degree_id: str = None,
        academic_year_id: str = None,
        specialization_id: str = None):
    """
    Returns the degree audit for a particular student.

    :param person_id: The numeric ID of the person you're interested in.
    :param degree_id: The numeric ID of the degree you're interested in.
    :param academic_year_id: The numeric ID of the academic year you're interested in.
    :param specialization_id: The numeric ID of the specialization you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getDegreeAudit',
        person_id=person_id,
        degree_id=degree_id,
        academic_year_id=academic_year_id,
        specialization_id=specialization_id)


def get_degrees():
    """
    Returns information about each degree configured at the school.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getDegrees')


def get_donation(donation_id: str = None):
    """
    Returns information about a specific donation.

    :param donation_id: The numeric ID of the donation
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getDonation', donation_id=donation_id)


def get_donor(
        donor_id: str = None,
        person_id: str = None,
        organization_id: str = None):
    """
    Returns information about a donor, including a history of their donations.

    :param donor_id: The numeric ID of the donor.
    :param person_id: Numeric ID of a person who is a donor.
    :param organization_id: Numeric ID of an organization that is a donor.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getDonor',
        donor_id=donor_id,
        person_id=person_id,
        organization_id=organization_id)


def get_education_levels():
    """
    Returns all education levels (e.g. High School Diploma, Some College, etc).

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getEducationLevels')


def get_entries_for_account(
        account_id: str = None,
        start_date: str = None,
        end_date: str = None):
    """
    Returns ledger transactions for a particular account.

    :param account_id: The numeric ID of the account.
    :param start_date: The start date of the posted date filter (e.g. 2010-01-15).
    :param end_date: The end date of the posted date filter (e.g. 2012-12-30).
    :returns: String containing xml or an lxml element.
    """

    return get_all_anonymous(
        'getEntriesForAccount',
        root_element='ledger_entry',
        account_id=account_id,
        start_date=start_date,
        end_date=end_date)


def get_event(eventID: str = None, recurrence: str = None):
    """
    Returns data for a particular event.

    :param eventID: The numeric ID of the event you're interested in.
    :param recurrence: If you want a particular occurrence of a reoccurring event. By default the first occurrence will be returned. Example: 2017-01-26.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getEvent', eventID=eventID, recurrence=recurrence)


def get_events(
        startDate: str = None,
        endDate: str = None,
        calendars: str = None):
    """
    Returns calendar events.

    :param startDate: Format like MM/DD/YYYY or YYYY-MM-DD. Defaults to the current date.
    :param endDate: Format like MM/DD/YYYY or YYYY-MM-DD. Defaults to 1 month in the future.
    :param calendars: An array of specific calendars to return events from. Defaults to returning events from the current user's calendars.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getEvents',
        startDate=startDate,
        endDate=endDate,
        calendars=calendars)


def get_fees():
    """
    Returns all information related to fees configured for the institution.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getFees')


def get_file_download_u_r_l(file_id: str = None):
    """
    Returns a URL that can be used to download a file (valid for 10 minutes).

    :param file_id: The numeric ID of the file you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getFileDownloadURL', file_id=file_id)


def get_financial_aid_award_types():
    """
    Returns all available financial aid award types (both active and retired)

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getFinancialAidAwardTypes')


def get_financial_aid_awards(
        aid_year_id: str = None,
        award_type_id: str = None,
        person_id: str = None):
    """
    Returns all aid awards for a particular aid year (see getFinancialAidYears).

    :param aid_year_id: The numeric ID of an aid year.
    :param award_type_id: The numeric ID of an award type (see getFinancialAidAwardTypes).
    :param person_id: The numeric ID of a student.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getFinancialAidAwards',
        aid_year_id=aid_year_id,
        award_type_id=award_type_id,
        person_id=person_id)


def get_financial_aid_disbursements(
        aid_year_id: str = None,
        type: str = None,
        award_type_id: str = None,
        academic_term_id: str = None,
        person_id: str = None):
    """
    Returns all disbursements (whether original, to source, or to student) for a particular aid year (see getFinancialAidYears).

    :param aid_year_id: The numeric ID of an aid year
    :param type: Possible values: DISBURSEMENT, REFUND_TO_SOURCE, REFUND_TO_STUDENT
    :param award_type_id: The numeric ID of an award type (see getFinancialAidAwardTypes).
    :param academic_term_id: The numeric ID of an academic term.
    :param person_id: The numeric ID of a student.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getFinancialAidDisbursements',
        aid_year_id=aid_year_id,
        type=type,
        award_type_id=award_type_id,
        academic_term_id=academic_term_id,
        person_id=person_id)


def get_financial_aid_years():
    """
    Returns all financial aid years - note that these are different than calendar years, and each award must be attached to a financial aid year.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getFinancialAidYears')


def get_funds():
    """
    Returns all information related to donation funds configured for your institution.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getFunds')


def get_grade_report(
        person_id: str = None,
        term_id: str = None,
        program_id: str = None,
        include_locked_grades: str = None):
    """
    Returns the grade report for a particular student and term.

    :param person_id: The numeric ID of the person you're interested in.
    :param term_id: The numeric ID of the term you're interested in.
    :param program_id: The numeric ID of the program you're interested in. Default to all programs (program_id 0).
    :param include_locked_grades: Boolean. Defaults to true.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getGradeReport',
        person_id=person_id,
        term_id=term_id,
        program_id=program_id,
        include_locked_grades=include_locked_grades)


def get_inquiries(
        start_date: str = None,
        end_date: str = None,
        status: str = None,
        program_id: str = None,
        representative_id: str = None):
    """
    Returns all admissions inquiries matching the specified criteria.

    :param start_date: The start date after which inquiries were received.
    :param end_date: The end date before which inquiries were received.
    :param status: The current status of the inquiries (e.g. WAITING_ON_US, WAITING_ON_THEM, CLOSED).
    :param program_id: The numeric ID of the academic program associated with the inquiries.
    :param representative_id: The numeric ID of the representative associated with the inquiries.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getInquiries',
        start_date=start_date,
        end_date=end_date,
        status=status,
        program_id=program_id,
        representative_id=representative_id)


def get_inquiry(inquiry_id: str = None):
    """
    Returns a particular admissions inquiry.

    :param inquiry_id: The numeric ID of the inquiry.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getInquiry', inquiry_id=inquiry_id)


def get_invoice(invoice_id: str = None):
    """
    Returns all basic and associated information about an invoice. This could includes charges, payments, credits, financial aid payments, deadlines, credited invoices, and credit refunds.

    :param invoice_id: The numeric ID of the invoice you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getInvoice', invoice_id=invoice_id)


def get_invoices(
        academic_term_id: str = None,
        student_id: str = None,
        type: str = None,
        status: str = None):
    """
    Returns invoices and associated information. This could includes charges, payments, credits, financial aid payments, deadlines, credited invoices, and credit refunds.

    :param academic_term_id: The numeric ID of the academic term you're interested in.
    :param student_id: The numeric ID of the person you're interested in.
    :param type: ALL (default), INVOICE, or CREDIT.
    :param status: ALL (default), UNPAID, PAID, or UNCOLLECTIBLE.
    :returns: String containing xml or an lxml element.
    """

    return get_all_anonymous(
        'getInvoices',
        root_element='invoice',
        academic_term_id=academic_term_id,
        student_id=student_id,
        type=type,
        status=status)


def get_lead_sources():
    """
    Returns all the lead sources you've set up in the Admissions settings.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getLeadSources')


def get_ledger_accounts():
    """
    Returns all ledger accounts.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getLedgerAccounts')


def get_meal_plans():
    """
    Returns all information related to meal plans configured for the institution.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getMealPlans')


def get_my_courses(person_id: str = None, term_id: str = None):
    """
    Returns all courses taken or taught for the current user for a particular term (or all terms currently in progress).

    :param person_id: The numeric ID of the person you're interested in.  To call this task for anyone other than yourself, you must have the Registrar or Academic Admin role.  If not set, uses the person_id of the currently logged-in user.
    :param term_id: The numeric ID of the term you're interested in.  If not specified, all terms currently in progress will be checked.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getMyCourses', person_id=person_id, term_id=term_id)


def get_news(offset: str = None, limit: str = None):
    """
    Returns the Populi news feed, ordered most recent to least recent (with pinned articles at the top).

    :param offset: The numeric value you want to offset the results by.
    :param limit: The maximum number of matches you'd like returned - defaults to 200, maximum is 200.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getNews', offset=offset, limit=limit)


def get_occupations():
    """
    Returns a list of occupations and their respective SOC codes.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getOccupations')


def get_online_payment_url(person_id: str = None):
    """
    Gets a special url for students to pay online. This link is good for 30 days.

    :param person_id: The numeric ID of the person you're interested in.
    :returns: String containing xml or lxml element.
    """

    return get_anonymous('getOnlinePaymentUrl', person_id=person_id)


def get_organization(organization_id: str = None):
    """
    Returns basic profile data about an organization: name, type, tags, and contact information (address, phone, email).

    :param organization_id: The numeric ID of the organization.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getOrganization', organization_id=organization_id)


def get_organization_types():
    """
    Returns organization types.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getOrganizationTypes')


def get_organizations():
    """
    Returns all organizations.

    :returns: String containing xml or an lxml element.
    """

    return get_all_anonymous('getOrganizations', root_element='organization')


def get_payment(payment_id: str = None):
    """
    Returns all basic and associated information about a payment. This could include credit card information, electronic check information, invoice payments, and payment refunds.

    :param payment_id: The numeric ID of the payment you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getPayment', payment_id=payment_id)


def get_payment_plans():
    """
    Returns all financial payment plans.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getPaymentPlans')


def get_pending_charges(
        term_id: str = None,
        person_id: str = None,
        campus_id: str = None,
        type: str = None):
    """
    Returns all financial pending charges.

    :param term_id: Possible values: ALL (default), 0 (None), or any numeric term_id.
    :param person_id: Numeric ID of the person you're interested in.
    :param campus_id: Possible values: ALL (default), 0 (None), or any numeric campus_id.
    :param type: Possible values: ALL (default), TUITION, FEE, ROOM_PLAN, MEAL_PLAN, or BOOKSTORE.
    :returns: String containing xml or an lxml element.
    """

    return get_all_anonymous(
        'getPendingCharges',
        root_element='pending_charge',
        term_id=term_id,
        person_id=person_id,
        campus_id=campus_id,
        type=type)


def get_person(
        person_id: str = None,
        student_id: str = None,
        return_image_data: str = None):
    """
    Returns basic profile data about a person: name, age, gender, tags, and contact information (address, phone, email).

    :param person_id: The numeric ID of the person.
    :param student_id: The student ID of the person.
    :param return_image_data: Boolean. Returning binary image data will result in slower response times. Defaults to false.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getPerson',
        person_id=person_id,
        student_id=student_id,
        return_image_data=return_image_data)


def get_person_applications(person_id: str = None):
    """
    Returns all applications for a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getPersonApplications', person_id=person_id)


def get_person_communication_plans(person_id: str = None):
    """
    Returns all active communication plans attached to a person.

    :param person_id: The numeric ID of the person you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getPersonCommunicationPlans', person_id=person_id)


def get_person_leads(person_id: str = None):
    """
    Returns all leads attached to a person.

    :param person_id: The numeric ID of the person you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getPersonLeads', person_id=person_id)


def get_person_locks(person_id: str = None):
    """
    Returns locks for a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getPersonLocks', person_id=person_id)


def get_person_organizations(person_id: str = None):
    """
    Returns organization records associated with a person.

    :param person_id: The numeric ID of the person.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getPersonOrganizations', person_id=person_id)


def get_person_relationships(person_id: str = None):
    """
    Returns relationships for a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getPersonRelationships', person_id=person_id)


def get_person_s_i_n(person_id: str = None):
    """
    Gets the social insurance number for a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getPersonSIN', person_id=person_id)


def get_person_s_s_n(person_id: str = None):
    """
    Gets the social security number for a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getPersonSSN', person_id=person_id)


def get_possible_duplicate_people(
        first_name: str = None,
        last_name: str = None,
        gender: str = None,
        birth_date: str = None,
        email_address: str = None,
        phone_number: str = None):
    """
    Called before you add a new person into Populi, this task returns similar people already in the system. You can then present the results to the user of your application and confirm they're not about to add a duplicate person.

    :param first_name: e.g. Bob
    :param last_name: e.g. McProspect
    :param gender: MALE or FEMALE
    :param birth_date: e.g. 1979-10-02
    :param email_address: e.g. bob@gmail.com
    :param phone_number: e.g. 777-888-9999
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getPossibleDuplicatePeople',
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        birth_date=birth_date,
        email_address=email_address,
        phone_number=phone_number)


def get_print_layouts():
    """
    Returns all information related to built-in and custom Open Office ODT print layout templates.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getPrintLayouts')


def get_programs():
    """
    Returns information about each program configured at the school.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getPrograms')


def get_provinces():
    """
    Returns a list of provinces and their respective abbreviations.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getProvinces')


def get_races():
    """
    Returns a list of race ids and their respective names.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getRaces')


def get_refund(refund_id: str = None):
    """
    Returns all basic and associated information about a refund. This could include reduced payments and reduced credits.

    :param refund_id: The numeric ID of the refund you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getRefund', refund_id=refund_id)


def get_role_members(
        roleID: str = None,
        roleName: str = None,
        status: str = None):
    """
    Returns members of a particular role.

    :param roleID: The numeric ID of the role.
    :param roleName: Name of the role.
    :param status: Possible values: ACTIVE (default), INACTIVE, and ALL.
    :returns: String containing xml or an lxml element.
    """

    return get_all_anonymous(
        'getRoleMembers',
        root_element='person',
        roleID=roleID,
        roleName=roleName,
        status=status)


def get_roles(person_id: str = None):
    """
    Returns all active roles for a particular person (or the current users if no person_id is specified).

    :param person_id: The numeric ID of the person whose roles you wish to retrieve.  If not specified, the roles for the logged-in user will be returned.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getRoles', person_id=person_id)


def get_room_plans():
    """
    Returns all information related to room plans configured for the institution.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getRoomPlans')


def get_states():
    """
    Returns a list of states and their respective abbreviations.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getStates')


def get_student_assignment_submissions(
        assignment_id: str = None,
        person_id: str = None):
    """
    Returns assignment submissions for a particular assignment and person.

    :param assignment_id: The numeric ID of the assignment.
    :param person_id: The numeric ID of the person.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getStudentAssignmentSubmissions',
        assignment_id=assignment_id,
        person_id=person_id)


def get_student_balances():
    """
    Returns all non-zero balances.

    :returns: String containing xml or an lxml element.
    """

    return get_all_anonymous(
        'getStudentBalances',
        root_element='student_balance')


def get_student_default_tuition_schedules(person_id: str = None):
    """
    Returns a student's default tuition schedules.

    :param person_id: The numeric person ID of the student you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getStudentDefaultTuitionSchedules',
        person_id=person_id)


def get_student_discipline(person_id: str = None):
    """
    Returns student discipline information for a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getStudentDiscipline', person_id=person_id)


def get_student_info(person_id: str = None, return_image_data: str = None):
    """
    Returns student information for a particular person.

    :param person_id: The numeric ID of the person you're interested in.  To call this task for anyone other than yourself, you must have the Registrar role, Academic Admin role, or be an advisor of the person.  If not set, uses the person_id of the currently logged-in user.
    :param return_image_data: Boolean. Returning binary image data will result in slower response times. Defaults to false.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getStudentInfo',
        person_id=person_id,
        return_image_data=return_image_data)


def get_student_meal_plan(person_id: str = None, academic_term_id: str = None):
    """
    Returns a student's meal plan information.

    :param person_id: The numeric ID of the person.
    :param academic_term_id: The numeric ID of the academic term you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getStudentMealPlan',
        person_id=person_id,
        academic_term_id=academic_term_id)


def get_student_programs(person_id: str = None):
    """
    Returns the programs, degrees, and specializations for a particular student.

    :param person_id: The numeric ID of the person you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getStudentPrograms', person_id=person_id)


def get_student_room_plan(person_id: str = None, academic_term_id: str = None):
    """
    Returns a student's room plan information.

    :param person_id: The numeric ID of the person.
    :param academic_term_id: The numeric ID of the academic term you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getStudentRoomPlan',
        person_id=person_id,
        academic_term_id=academic_term_id)


def get_student_term_tuition_schedules(
        person_id: str = None,
        academic_term_id: str = None):
    """
    Returns a student's term tuition schedules.

    :param person_id: The numeric person ID of the student you're interested in.
    :param academic_term_id: The numeric ID of the academic term you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getStudentTermTuitionSchedules',
        person_id=person_id,
        academic_term_id=academic_term_id)


def get_tagged_people(tagID: str = None, tagName: str = None):
    """
    Returns people tagged with a particular tag.

    :param tagID: The numeric ID of the tag.
    :param tagName: The name of the tag.
    :returns: String containing xml or an lxml element.
    """

    return get_all_anonymous(
        'getTaggedPeople',
        root_element='person',
        tagID=tagID,
        tagName=tagName)


def get_tags():
    """
    Returns a list of available tags.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getTags')


def get_term_billing_info(academic_term_id: str = None):
    """
    Returns the students billing information for a particular academic term.

    :param academic_term_id: The numeric ID of the academic term you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getTermBillingInfo',
        academic_term_id=academic_term_id)


def get_term_course_instances(term_id: str = None, finalized: str = None):
    """
    Returns course instances for a given term.

    :param term_id: The numeric ID of the term you're interested in.
    :param finalized: Boolean. All course instances are returned by default.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getTermCourseInstances',
        term_id=term_id,
        finalized=finalized)


def get_term_enrollment(term_id: str = None, person_id: str = None):
    """
    Returns term enrollment for a particular academic term.

    :param term_id: The numeric ID of the academic term.
    :param person_id: Numeric ID of the person you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getTermEnrollment',
        term_id=term_id,
        person_id=person_id)


def get_term_students(
        term_id: str = None,
        program_id: str = None,
        campus_id: str = None,
        return_image_data: str = None):
    """
    Returns term students.

    :param term_id: The numeric ID of the term you're interested in. Defaults to the current academic term_id.
    :param program_id: Possible values: ALL (default), NONE, or any numeric program_id.
    :param campus_id: Possible values: ALL (default), 0 (None), or any numeric campus_id.
    :param return_image_data: Boolean. Returning binary image data will result in slower response times. Defaults to false.
    :returns: String containing xml or an lxml element.
    """

    return get_all_anonymous(
        'getTermStudents',
        root_element='student',
        term_id=term_id,
        program_id=program_id,
        campus_id=campus_id,
        return_image_data=return_image_data)


def get_todos(completed: str = None):
    """
    Returns todos for the current user.

    :param completed: Possible values: NO (default), YES, or BOTH. Whether you'd like to see completed todos, uncompleted todos, or all todos.
    :returns: String containing xml or an lxml element.
    """

    return get_all_anonymous(
        'getTodos',
        root_element='todo',
        completed=completed)


def get_transactions(
        start_date: str = None,
        end_date: str = None,
        primary_actor_id: str = None):
    """
    Returns all financial transactions within a specified date range and the associated ledger entries.

    :param start_date: The start date used to filter the transactions. (e.g. 2016-01-01) Default is 30 days ago if not specified.
    :param end_date: The end date used to filter the transactions. (e.g. 2016-12-31) Default is today if not specified.
    :param primary_actor_id: The numeric ID of the primary actor you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_all_anonymous(
        'getTransactions',
        root_element='transaction',
        start_date=start_date,
        end_date=end_date,
        primary_actor_id=primary_actor_id)


def get_transcript(
        person_id: str = None,
        pdf: str = None,
        layout_id: str = None,
        program_id: str = None,
        official: str = None,
        recipient: str = None,
        include_course_descriptions: str = None):
    """
    Returns the transcript for a particular student.

    :param person_id: The numeric ID of the person you're interested in.
    :param pdf: Boolean. If set to true, pdf content will be returned instead of xml. Defaults to false.
    :param layout_id: The numeric ID of the custom transcript layout you want to use. If not specified, the built-in default layout will be used.
    :param program_id: The numeric ID of the student's program you wish to export a transcript for. When using a custom layout, this parameter is required.
    :param official: (Requires the "pdf" parameter to be set to true) Boolean. If set to true, the official transcript pdf content will be returned. Defaults to false.
    :param recipient: (Requires the "pdf" parameter to be set to true) String. The recipient who will be receiving this transcript.
    :param include_course_descriptions: (Requires the "pdf" parameter to be set to true) Boolean. If set to true, course descriptions will be returned in the pdf content. Note: course descriptions will always be returned in the xml. The parameter has no effect on custom layouts. Defaults to false.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getTranscript',
        person_id=person_id,
        pdf=pdf,
        layout_id=layout_id,
        program_id=program_id,
        official=official,
        recipient=recipient,
        include_course_descriptions=include_course_descriptions)


def get_transfer_credit_program_grade_options(program_id: str = None):
    """
    Returns transfer credit program grade options.

    :param program_id: The numeric ID of the program you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getTransferCreditProgramGradeOptions',
        program_id=program_id)


def get_tuition_schedules():
    """
    Returns all information related to tuition schedules and brackets configured for the institution.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getTuitionSchedules')


def get_updated_enrollment(start_date: str = None, offset: str = None):
    """
    Returns updated enrollment for a particular time.

    :param start_date: Format should be a date like "2010-11-06".
    :param offset: The numeric value you want to offset the results by.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getUpdatedEnrollment',
        start_date=start_date,
        offset=offset)


def get_updated_people(start_time: str = None, offset: str = None):
    """
    Returns all people who have had information changed since start_time. This is useful if you want to sync Populi users to a directory service, etc.

    :param start_time: Return all people with updated info since this second. Format should be a local timestamp like "2010-11-06 13:27:10".
    :param offset: The numeric value you want to offset the results by.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'getUpdatedPeople',
        start_time=start_time,
        offset=offset)


def get_users():
    """
    Returns all users.

    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('getUsers')


def get_voided_transactions(
        start_time: str = None,
        end_date: str = None,
        primary_actor_id: str = None):
    """
    Returns all voided financial transactions within a specified time period and the associated ledger entries.

    :param start_time: The start time used to filter the voided transactions. (e.g. 2016-01-01 14:00:00) Default is 30 days ago if not specified.
    :param end_date: The end date used to filter the voided transactions. (e.g. 2016-12-31 14:00:00) Default is now if not specified.
    :param primary_actor_id: The numeric ID of the primary actor you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_all_anonymous(
        'getVoidedTransactions',
        root_element='transaction',
        start_time=start_time,
        end_date=end_date,
        primary_actor_id=primary_actor_id)


def invoice_pending_charges(
        person_id: str = None,
        academic_term_id: str = None,
        due_date: str = None,
        posted_date: str = None,
        fee_id: str = None):
    """
    Creates an invoice based from pending charges associate with a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :param academic_term_id: The academic term ID that the pending charges are attached to. This is optional because some pending charges may not be attached to an academic term.
    :param due_date: The date that the invoice is due. Defaults to your specified due date setting (if set), otherwise the defaults to the academic term start date (if an academic_term_id is passed in and the academic term's start date is in the future), otherwise the default is 30 days in the future.
    :param posted_date: The transaction's posted date. Defaults to the current date.
    :param fee_id: The numeric ID of a particular fee you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'invoicePendingCharges',
        person_id=person_id,
        academic_term_id=academic_term_id,
        due_date=due_date,
        posted_date=posted_date,
        fee_id=fee_id)


def link_application_to_person(
        application_id: str = None,
        person_id: str = None):
    """
    Links an application to a person.

    :param application_id: Numeric ID of the application.
    :param person_id: Numeric ID of the person.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'linkApplicationToPerson',
        application_id=application_id,
        person_id=person_id)


def link_donation(
        donation_id: str = None,
        link_type: str = None,
        person_id: str = None,
        organization_id: str = None):
    """
    Links a donation to a person or organization as that donation's donor or soft credit.

    :param donation_id: The numeric ID of the donation
    :param link_type: DONOR or SOFT_CREDIT
    :param person_id: The numeric ID of the person you wish to link to this donation
    :param organization_id: The numeric ID of the organization you wish to link to this donation
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'linkDonation',
        donation_id=donation_id,
        link_type=link_type,
        person_id=person_id,
        organization_id=organization_id)


def post_financial_aid_disbursement(
        disbursement_id: str = None,
        posted_date: str = None,
        notify_student: str = None):
    """
    Posts an existing scheduled disbursement.

    :param disbursement_id: The numeric ID of a disbursement with a status of SCHEDULED (but not SETUP, POSTED, DELETED or VOID)
    :param posted_date: Format should be a date like "2010-11-06". Defaults to the current date.
    :param notify_student: Boolean. Send a notification email to the student's primary email address. Defaults to true.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'postFinancialAidDisbursement',
        disbursement_id=disbursement_id,
        posted_date=posted_date,
        notify_student=notify_student)


def remove_advisor_from_student(
        advisor_person_id: str = None,
        student_person_id: str = None):
    """
    Removes an advisor from a student.

    :param advisor_person_id: The numeric person ID of the advisor you're interested in.
    :param student_person_id: The numeric person ID of the student you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'removeAdvisorFromStudent',
        advisor_person_id=advisor_person_id,
        student_person_id=student_person_id)


def remove_default_tuition_schedule_from_student(
        person_id: str = None,
        tuition_schedule_id: str = None):
    """
    Removes a default tuition schedule from a student.

    :param person_id: The numeric person ID of the student you're interested in.
    :param tuition_schedule_id: The numeric ID of the tuition schedule you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'removeDefaultTuitionScheduleFromStudent',
        person_id=person_id,
        tuition_schedule_id=tuition_schedule_id)


def remove_role(person_id: str = None, role_id: str = None):
    """
    Removes a role from a person.

    :param person_id: The numeric ID of the person you're interested in.
    :param role_id: The numeric ID of the role you want to remove.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('removeRole', person_id=person_id, role_id=role_id)


def remove_tag(
        person_id: str = None,
        organization_id: str = None,
        tag_id: str = None,
        tag: str = None):
    """
    Removes a tag from a particular person.

    :param person_id: The numeric ID of the person whose tag should be removed.
    :param organization_id: The numeric ID of the organization whose tag should be removed.
    :param tag_id: The numeric ID of the tag.
    :param tag: The actual tag you want to be removed (e.g. "Do not call", or "Good reference").
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'removeTag',
        person_id=person_id,
        organization_id=organization_id,
        tag_id=tag_id,
        tag=tag)


def remove_term_tuition_schedule_from_student(
        person_id: str = None,
        academic_term_id: str = None,
        tuition_schedule_id: str = None):
    """
    Removes a term tuition schedule from a student.

    :param person_id: The numeric person ID of the student you're interested in.
    :param academic_term_id: The numeric ID of the academic term you're interested in.
    :param tuition_schedule_id: The numeric ID of the tuition schedule you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'removeTermTuitionScheduleFromStudent',
        person_id=person_id,
        academic_term_id=academic_term_id,
        tuition_schedule_id=tuition_schedule_id)


def remove_user(person_id: str = None):
    """
    Removes the user account from a person.

    :param person_id: The numeric ID of the person whose user account will be removed.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('removeUser', person_id=person_id)


def request_backup(on_complete_email: str = None, on_complete_url: str = None):
    """
    Requests a backup of your Populi data, delivered as a ZIP file in CSV format. You can be notified by email when it's ready for download, or have an HTTP request made to another web application.

    :param on_complete_email: Where to send the "Backup Ready for Download" email.
    :param on_complete_url: If set, when the backup is ready for download we'll make an HTTP request to this URL, including the backup_id as a POST variable.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'requestBackup',
        on_complete_email=on_complete_email,
        on_complete_url=on_complete_url)


def resubscribe_email_address(email_address: str = None):
    """
    Resubscribes a particular email address to emails.

    :param email_address: The email address you want to resubscribe to emails. (e.g. bob@example.com)
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'resubscribeEmailAddress',
        email_address=email_address)


def search_organizations(search_term: str = None, limit: str = None):
    """
    Looks up organizations by name & location.

    :param search_term: e.g. "College of Nursing" or "Chicago, IL".
    :param limit: The maximum number of matches you'd like returned - defaults to 10, maximum is 50.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'searchOrganizations',
        search_term=search_term,
        limit=limit)


def search_people(search_term: str = None, limit: str = None):
    """
    Looks up people by name, email, phone number, etc.

    :param search_term: e.g. "Joe McStudent" or "208-111-2222" or "joe@mcstudent.edu"
    :param limit: The maximum number of matches you'd like returned - defaults to 10, maximum is 50.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('searchPeople', search_term=search_term, limit=limit)


def set_application_field(
        application_field_id: str = None,
        value: str = None,
        reference_email: str = None,
        reference_message: str = None,
        street: str = None,
        city: str = None,
        state: str = None,
        zip: str = None,
        country: str = None,
        hispanic_latino: str = None,
        race_ids: str = None,
        date_taken: str = None,
        total_score: str = None):
    """
    Sets a value for a particular application field.

    :param application_field_id: The numeric ID of the application field you're interested in.
    :param value: The value for this field.
    :param reference_email: The email address that should receive an online reference invitation.
    :param reference_message: A personal message to the recipient of the online reference invitation.
    :param street: The street portion of an address.
    :param city: The city portion of an address.
    :param state: A state or province abbreviation.
    :param zip: The zip/postal code portion of an address.
    :param country: A country abbreviation.
    :param hispanic_latino: Boolean.
    :param race_ids: An array of race IDs.
    :param date_taken: The date a standardized test was taken.
    :param total_score: The total score for a standardized test.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'setApplicationField',
        application_field_id=application_field_id,
        value=value,
        reference_email=reference_email,
        reference_message=reference_message,
        street=street,
        city=city,
        state=state,
        zip=zip,
        country=country,
        hispanic_latino=hispanic_latino,
        race_ids=race_ids,
        date_taken=date_taken,
        total_score=total_score)


def set_custom_field(
        custom_field_id: str = None,
        person_id: str = None,
        owner_id: str = None,
        term_id: str = None,
        value: str = None,
        option_index: str = None):
    """
    Sets a custom field value for a particular person, organization, or donation.

    :param custom_field_id: The numeric ID of the custom field you're interested in.
    :param person_id: The numeric ID of the person you're interested in.
    :param owner_id: The numeric ID of object you're interested in, if they are not a person.
    :param term_id: The numeric ID of the term you're interested in.
    :param value: The value for this field.
    :param option_index: For RADIOs and SELECTs, you can pass in the index of the selected option.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'setCustomField',
        custom_field_id=custom_field_id,
        person_id=person_id,
        owner_id=owner_id,
        term_id=term_id,
        value=value,
        option_index=option_index)


def set_lead_info(
        person_id: str = None,
        status: str = None,
        term_id: str = None,
        source_id: str = None,
        source_comment: str = None,
        ed_level_id: str = None,
        admissions_officer_id: str = None,
        high_school_grad_date: str = None):
    """
    Sets information about an admissions lead.

    :param person_id: The numeric ID of the person whose lead information you'd like to change.
    :param status: PROSPECT, INQUIRY, APPLICATION_STARTED, APPLICATION_COMPLETED, ACCEPTED, CONFIRMED, ENROLLED
    :param term_id: The numeric ID of the term the school hopes the lead will attend.
    :param source_id: The numeric ID of the source this lead to which this lead should be attributed.
    :param source_comment: A short comment describing this lead's source (i.e. "Where did this lead come from?").
    :param ed_level_id: The numeric education level ID associated with this lead (e.g. High School, Some College, etc).
    :param admissions_officer_id: The numeric person ID of the main admissions officer responsible for this lead (he or she should have the Admissions role).
    :param high_school_grad_date: The date this lead graduated from High School (e.g. 2010-06-15)
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'setLeadInfo',
        person_id=person_id,
        status=status,
        term_id=term_id,
        source_id=source_id,
        source_comment=source_comment,
        ed_level_id=ed_level_id,
        admissions_officer_id=admissions_officer_id,
        high_school_grad_date=high_school_grad_date)


def set_person_birth_date(person_id: str = None, birth_date: str = None):
    """
    Sets the birth date for a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :param birth_date: e.g. 1979-10-02
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'setPersonBirthDate',
        person_id=person_id,
        birth_date=birth_date)


def set_person_citizenship(
        person_id: str = None,
        citizenship: list = [],
        resident_alien: str = None):
    """
    Sets the citizenship for a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :param citizenship: The citizenship country abbreviation(s) for the person.
    :param resident_alien: Boolean. Defaults to false.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'setPersonCitizenship',
        person_id=person_id,
        citizenship=citizenship,
        resident_alien=resident_alien)


def set_person_gender(person_id: str = None, gender: str = None):
    """
    Sets the gender for a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :param gender: MALE, FEMALE, or UNKNOWN
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('setPersonGender', person_id=person_id, gender=gender)


def set_person_hometown(
        person_id: str = None,
        city: str = None,
        state: str = None,
        country: str = None):
    """
    Sets the hometown for a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :param city: The hometown city for the person.
    :param state: The hometown state abbreviation for the person.
    :param country: The hometown country abbreviation for the person.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'setPersonHometown',
        person_id=person_id,
        city=city,
        state=state,
        country=country)


def set_person_name(
        person_id: str = None,
        prefix: str = None,
        first_name: str = None,
        preferred_name: str = None,
        middle_name: str = None,
        last_name: str = None,
        suffix: str = None,
        former_name: str = None,
        maiden_name: str = None):
    """
    Sets the name a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :param prefix:  
    :param first_name:  
    :param preferred_name:  
    :param middle_name:  
    :param last_name:  
    :param suffix:  
    :param former_name:  
    :param maiden_name:  
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'setPersonName',
        person_id=person_id,
        prefix=prefix,
        first_name=first_name,
        preferred_name=preferred_name,
        middle_name=middle_name,
        last_name=last_name,
        suffix=suffix,
        former_name=former_name,
        maiden_name=maiden_name)


def set_person_race_ethnicity(
        person_id: str = None,
        hispanic_or_latino: str = None,
        race_ids: str = None):
    """
    Sets the race/ethnicity for a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :param hispanic_or_latino: Boolean. Defaults to false.
    :param race_ids: An array of race IDs.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'setPersonRaceEthnicity',
        person_id=person_id,
        hispanic_or_latino=hispanic_or_latino,
        race_ids=race_ids)


def set_person_s_i_n(person_id: str = None, sin: str = None):
    """
    Sets the social insurance number for a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :param sin: The social insurance number for the person.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('setPersonSIN', person_id=person_id, sin=sin)


def set_person_s_s_n(person_id: str = None, ssn: str = None):
    """
    Sets the social security number for a particular person.

    :param person_id: The numeric ID of the person you're interested in.
    :param ssn: The social security number for the person.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('setPersonSSN', person_id=person_id, ssn=ssn)


def set_student_assignment_grade(
        course_offering_id: str = None,
        assignment_id: str = None,
        person_id: str = None,
        grade: str = None,
        recalculate_final_grade: str = None):
    """
    Sets an assignment grade for a particular student.

    :param course_offering_id: The numeric ID of the course offering you're interested in.
    :param assignment_id: The numeric ID of the assignment you're interested in.
    :param person_id: The numeric ID of the person you're interested in.
    :param grade: The assignment grade for the student.
    :param recalculate_final_grade: Boolean. Defaults to true.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'setStudentAssignmentGrade',
        course_offering_id=course_offering_id,
        assignment_id=assignment_id,
        person_id=person_id,
        grade=grade,
        recalculate_final_grade=recalculate_final_grade)


def set_student_entrance_term(
        person_id: str = None,
        term_id: str = None,
        student_program_id: str = None):
    """
    Sets the entrance term for a particular student.

    :param person_id: The numeric ID of the person you're interested in.
    :param term_id: The numeric ID of the term you're interested in.
    :param student_program_id: The numeric ID of the student's program you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'setStudentEntranceTerm',
        person_id=person_id,
        term_id=term_id,
        student_program_id=student_program_id)


def set_student_final_grade(
        course_offering_id: str = None,
        person_id: str = None,
        grade: str = None):
    """
    Sets the final grade for a particular student in a particular course instance.

    :param course_offering_id: The numeric ID of the course offering you're interested in.
    :param person_id: The numeric ID of the person you're interested in.
    :param grade: The final grade for the student.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'setStudentFinalGrade',
        course_offering_id=course_offering_id,
        person_id=person_id,
        grade=grade)


def set_student_i_d(person_id: str = None, student_id: str = None):
    """
    Sets a student's ID

    :param person_id: The numeric ID of the person whose student ID you'd like to change.
    :param student_id: The new student ID
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'setStudentID',
        person_id=person_id,
        student_id=student_id)


def set_student_meal_plan(
        person_id: str = None,
        academic_term_id: str = None,
        meal_plan_id: str = None):
    """
    Sets a student's meal plan information.

    :param person_id: The numeric ID of the person.
    :param academic_term_id: The numeric ID of the academic term you're interested in.
    :param meal_plan_id: The numeric ID of the meal plan you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'setStudentMealPlan',
        person_id=person_id,
        academic_term_id=academic_term_id,
        meal_plan_id=meal_plan_id)


def set_student_room_plan(
        person_id: str = None,
        academic_term_id: str = None,
        room_plan_id: str = None,
        room_id: str = None,
        capacity_used: str = None):
    """
    Sets a student's room plan information.

    :param person_id: The numeric ID of the person.
    :param academic_term_id: The numeric ID of the academic term you're interested in.
    :param room_plan_id: The numeric ID of the room plan you're interested in.
    :param room_id: The numeric ID of the room you're interested in.
    :param capacity_used:  
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'setStudentRoomPlan',
        person_id=person_id,
        academic_term_id=academic_term_id,
        room_plan_id=room_plan_id,
        room_id=room_id,
        capacity_used=capacity_used)


def set_todo_completed(todo_id: str = None, completed: str = None):
    """
    Marks a todo completed or not completed.

    :param todo_id: The numeric ID of the todo you're interested in.
    :param completed: Possible values: 1 (default) or 0. Whether the todo should be marked completed.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'setTodoCompleted',
        todo_id=todo_id,
        completed=completed)


def submit_application(application_id: str = None):
    """
    Submits an application.

    :param application_id: The numeric ID of the application you're interested in.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('submitApplication', application_id=application_id)


def unblock_user(person_id: str = None):
    """
    Used to unblock a particular user account.

    :param person_id: The numeric ID of the person whose user account will be unblocked.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('unblockUser', person_id=person_id)


def unlink_application(application_id: str = None):
    """
    Unlinks a person from an application.

    :param application_id: Numeric ID of the application.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous('unlinkApplication', application_id=application_id)


def unlink_donation(
        donation_id: str = None,
        link_type: str = None,
        soft_credit_donor_id: str = None):
    """
    Removes the donor link or soft credits from a donation.

    :param donation_id: The numeric ID of the donation
    :param link_type: DONOR or SOFT_CREDIT
    :param soft_credit_donor_id: Numeric donor ID of the soft credit you wish to remove from this donation
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'unlinkDonation',
        donation_id=donation_id,
        link_type=link_type,
        soft_credit_donor_id=soft_credit_donor_id)


def unsubscribe_email_address(email_address: str = None):
    """
    Unsubscribes a particular email address from emails.

    :param email_address: The email address you want to unsubscribe from emails. (e.g. bob@example.com)
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'unsubscribeEmailAddress',
        email_address=email_address)


def update_address(
        addressid: str = None,
        street: str = None,
        city: str = None,
        state: str = None,
        postal: str = None,
        country: str = None,
        type: str = None,
        primary: str = None,
        old: str = None,
        public: str = None):
    """
    Updates an address.

    :param addressid: The numeric ID of the address.
    :param street: e.g. 777 Magnolia Ln
    :param city: e.g. Moscow
    :param state: e.g. ID
    :param postal: e.g. 83843
    :param country: e.g. US, CA, etc.
    :param type: Person addresses: HOME, WORK, BILLING, SCHOOL, SHIPPING, OTHER
    :param primary: Boolean. Use if you want to mark the address as primary or not primary.
    :param old: Boolean. Use if you want to mark the address as old or not old.
    :param public: Boolean. Use if you want to mark the address as public or not public.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'updateAddress',
        addressid=addressid,
        street=street,
        city=city,
        state=state,
        postal=postal,
        country=country,
        type=type,
        primary=primary,
        old=old,
        public=public)


def update_application_field_status(
        application_field_id: str = None,
        status: str = None):
    """
    Updates an application field's status.

    :param application_field_id: The numeric ID of the application field you're interested in.
    :param status: IN_PROGRESS, SUBMITTED, ACCEPTED, or REJECTED
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'updateApplicationFieldStatus',
        application_field_id=application_field_id,
        status=status)


def update_application_status(
        application_id: str = None,
        status: str = None,
        fee_status: str = None,
        provisional: str = None,
        provisional_comment: str = None,
        add_student_role: str = None,
        import_course_of_study: str = None):
    """
    Updates an application's status.

    :param application_id: The numeric ID of the application you're interested in.
    :param status: IN_PROGRESS, SUBMITTED, PENDING_DECISION, ACCEPTED, DECLINED, WITHDRAWN, DEFERRED, or WAITLISTED.
    :param fee_status: UNPAID, PAID, or WAIVED.
    :param provisional: Boolean. Only applies when the status=ACCEPTED. Defaults to false.
    :param provisional_comment: Only applies when the status=ACCEPTED.
    :param add_student_role: Boolean. Only applies when the status=ACCEPTED. Defaults to true.
    :param import_course_of_study: Boolean. Only applies when the applicant has the student role and status=ACCEPTED. Defaults to true.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'updateApplicationStatus',
        application_id=application_id,
        status=status,
        fee_status=fee_status,
        provisional=provisional,
        provisional_comment=provisional_comment,
        add_student_role=add_student_role,
        import_course_of_study=import_course_of_study)


def update_course_instance_assignment(
        instance_id: str = None,
        assignment_id: str = None,
        name: str = None,
        type: str = None,
        discussion_id: str = None,
        description: str = None,
        catalog_course_ids: str = None,
        points: str = None,
        extra_credit: str = None,
        group_id: str = None,
        published: str = None,
        time_due: str = None,
        visible_to_students_before_due: str = None,
        availability: str = None,
        start_window: str = None,
        end_window: str = None,
        time_limit: str = None,
        retake_policy: str = None,
        retakes: str = None,
        proctored: str = None,
        test_submit_feedback: str = None,
        test_end_feedback: str = None,
        peer_grade: str = None,
        grade_submission_points: str = None,
        grade_review_points: str = None,
        anonymous_reviews: str = None,
        review_visibility: str = None,
        allow_review_comments: str = None,
        reviews_time_due: str = None,
        reviews_closed_date_time: str = None):
    """
    Updates an assignment in a particular course instance.

    :param instance_id: The numeric ID of the course instance you're interested in.
    :param assignment_id: The numeric ID of the assignment you're interested in.
    :param name: The name of the assignment.
    :param type: GRADE_ONLY, FILE_UPLOAD, PEER_REVIEW_FILE_UPLOAD, TEST, ATTENDANCE, DISCUSSION, ESSAY, or PEER_REVIEW_ESSAY
    :param discussion_id: Only used when the assignment type is DISCUSSION. The numeric ID of the discussion you want to use (the default is 0 which means a new discussion will be created).
    :param description: A description of the assignment.
    :param catalog_course_ids: Only used if the course is cross-listed. This would be an array of catalog course IDs that the assignment applies to. If you leave this parameter out of the request the assignment will apply to all cross-listed courses.
    :param points: The number of points that the assignment is worth.
    :param extra_credit: Boolean.
    :param group_id: The assignment group ID this assignment belongs to (group_id 0 is the built-in "Other" group).
    :param published: Boolean.
    :param time_due: When the assignment is due (e.g. 2017-06-30 23:59:59 - must be in the course instance's timezone).
    :param visible_to_students_before_due: When the passed in type is TEST this sets whether or not the test is visible before it's available.
    :param availability: FROM, AFTER, BEFORE, or ALWAYS. If the value is FROM and both start_window and end_window are empty then the test will not be available.
    :param start_window: When the test availability starts (e.g. 2017-06-01 00:00:00 - must be in the course instance's timezone). Only used when the availability parameter is FROM or AFTER.
    :param end_window: When the test availability ends (e.g. 2017-06-30 23:59:59 - must be in the course instance's timezone). Only used when the availability parameter is FROM or BEFORE.
    :param time_limit: The time limit in minutes (time_limit 0 means "No time limit").
    :param retake_policy: NO_RETAKES (no retakes), KEEP_HIGHEST (keep highest score), KEEP_LAST (keep most recent score), AVERAGE (average all scores).
    :param retakes: The number of retakes allowed (only used when the retake_policy is not NO_RETAKES).
    :param proctored: Boolean.
    :param test_submit_feedback: SCORE (score when available), FEEDBACK (score and response feedback - the default), ANSWERS (score, respsnse feedback, and correct answers).
    :param test_end_feedback: SCORE (score when available), FEEDBACK (score and response feedback), ANSWERS (score, respsnse feedback, and correct answers - the default).
    :param peer_grade: Boolean.
    :param grade_submission_points: The number of points that submissions are worth.
    :param grade_review_points: The number of points that reviews are worth.
    :param anonymous_reviews: Boolean.
    :param review_visibility: NEVER (not visible to other students), AFTER_REVIEW (visible to other students after their review), ALWAYS (visible to other students).
    :param allow_review_comments: Boolean. Only used when review_visibility is not NEVER.
    :param reviews_time_due: When reviews are due (e.g. 2017-06-30 23:59:59 - must be in the course instance's timezone).
    :param reviews_closed_date_time: When reviews are closed (e.g. 2017-06-30 23:59:59 - must be in the course instance's timezone).
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'updateCourseInstanceAssignment',
        instance_id=instance_id,
        assignment_id=assignment_id,
        name=name,
        type=type,
        discussion_id=discussion_id,
        description=description,
        catalog_course_ids=catalog_course_ids,
        points=points,
        extra_credit=extra_credit,
        group_id=group_id,
        published=published,
        time_due=time_due,
        visible_to_students_before_due=visible_to_students_before_due,
        availability=availability,
        start_window=start_window,
        end_window=end_window,
        time_limit=time_limit,
        retake_policy=retake_policy,
        retakes=retakes,
        proctored=proctored,
        test_submit_feedback=test_submit_feedback,
        test_end_feedback=test_end_feedback,
        peer_grade=peer_grade,
        grade_submission_points=grade_submission_points,
        grade_review_points=grade_review_points,
        anonymous_reviews=anonymous_reviews,
        review_visibility=review_visibility,
        allow_review_comments=allow_review_comments,
        reviews_time_due=reviews_time_due,
        reviews_closed_date_time=reviews_closed_date_time)


def update_course_instance_assignment_group(
        instance_id: str = None,
        group_id: str = None,
        name: str = None,
        weight: str = None,
        extra_credit: str = None,
        drop_lowest: str = None):
    """
    Updates an assignment group in a particular course instance.

    :param instance_id: The numeric ID of the course instance you're interested in.
    :param group_id: The numeric ID of the assignment group you're interested in.
    :param name: The name of the assignment group.
    :param weight: The assignment group's weight percent (the default is 0).
    :param extra_credit: Boolean.
    :param drop_lowest: The number of lowest-graded assignments to drop from this group for each student (the default is 0).
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'updateCourseInstanceAssignmentGroup',
        instance_id=instance_id,
        group_id=group_id,
        name=name,
        weight=weight,
        extra_credit=extra_credit,
        drop_lowest=drop_lowest)


def update_course_offering_link(
        course_offering_id: str = None,
        link_id: str = None,
        name: str = None,
        url: str = None):
    """
    Updates a link attached to a particular course offering.

    :param course_offering_id: The numeric ID of the course offering you're interested in.
    :param link_id: The numeric ID of the link you're interested in.
    :param name: The name of the link.
    :param url: The URL for the link.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'updateCourseOfferingLink',
        course_offering_id=course_offering_id,
        link_id=link_id,
        name=name,
        url=url)


def update_email_address(
        emailid: str = None,
        email_address: str = None,
        type: str = None,
        primary: str = None,
        old: str = None,
        public: str = None):
    """
    Updates an email address.

    :param emailid: The numeric ID of the email address.
    :param email_address: e.g. bob@example.com
    :param type: Person email addresses: HOME, WORK, SCHOOL, OTHER
    :param primary: Boolean. Use if you want to mark the email address as primary or not primary.
    :param old: Boolean. Use if you want to mark the email address as old or not old.
    :param public: Boolean. Use if you want to mark the email address as public or not public.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'updateEmailAddress',
        emailid=emailid,
        email_address=email_address,
        type=type,
        primary=primary,
        old=old,
        public=public)


def update_license_plate(person_id: str = None, license_plate: str = None):
    """
    Updates a person's license plate.

    :param person_id: The numeric ID of the person.
    :param license_plate: The person's license plate.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'updateLicensePlate',
        person_id=person_id,
        license_plate=license_plate)


def update_person_organization(
        id: str = None,
        type: str = None,
        title: str = None,
        start_date: str = None,
        end_date: str = None,
        is_primary: str = None,
        is_private: str = None,
        occupation_id: str = None,
        full_time: str = None,
        weekly_hours: str = None,
        salary: str = None,
        can_show_on_transcript: str = None):
    """
    Updates a person organization record.

    :param id: The numeric ID of the person_organization record. See getPersonOrganization.
    :param type: MEMBER, EMPLOYMENT, or EDUCATION.
    :param title: The person's title at the organization.
    :param start_date: Format should be a date. e.g. "2020-09-05".
    :param end_date: Format should be a date. e.g. "2024-05-07".
    :param is_primary: Boolean.
    :param is_private: Boolean. Defaults to the "Make relationships between people and organizations private by default" security setting.
    :param occupation_id: The numeric ID of the occupation. See getOccupations. Only used when type = EMPLOYMENT.
    :param full_time: Boolean. Only used when type = EMPLOYMENT.
    :param weekly_hours: Only used when full_time = 0 and type = EMPLOYMENT.
    :param salary: Only used when type = EMPLOYMENT.
    :param can_show_on_transcript: Boolean. Defaults to true. Only used when type = EDUCATION.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'updatePersonOrganization',
        id=id,
        type=type,
        title=title,
        start_date=start_date,
        end_date=end_date,
        is_primary=is_primary,
        is_private=is_private,
        occupation_id=occupation_id,
        full_time=full_time,
        weekly_hours=weekly_hours,
        salary=salary,
        can_show_on_transcript=can_show_on_transcript)


def update_phone_number(
        phoneid: str = None,
        phone_number: str = None,
        type: str = None,
        primary: str = None,
        old: str = None,
        public: str = None):
    """
    Updates a phone number.

    :param phoneid: The numeric ID of the phone number.
    :param phone_number: e.g. 1-800-888-8888
    :param type: Person phone numbers: HOME, WORK, MOBILE, SCHOOL, FAX, OTHER
    :param primary: Boolean. Use if you want to mark the phone number as primary or not primary.
    :param old: Boolean. Use if you want to mark the phone number as old or not old.
    :param public: Boolean. Use if you want to mark the phone number as public or not public.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'updatePhoneNumber',
        phoneid=phoneid,
        phone_number=phone_number,
        type=type,
        primary=primary,
        old=old,
        public=public)


def update_student_attendance(
        instanceID: str = None,
        meetingID: str = None,
        personID: str = None,
        status: str = None,
        note: str = None,
        keep_best_status: str = None):
    """
    Update a student's attendance.

    :param instanceID: The numeric ID of the course instance you're interested in.
    :param meetingID: The numeric ID of the meeting.
    :param personID: The numeric ID of the person whose attendance will be updated.
    :param status: PRESENT, ABSENT, TARDY, or EXCUSED
    :param note: The text content of the note.
    :param keep_best_status: Boolean. Defaults to false.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'updateStudentAttendance',
        instanceID=instanceID,
        meetingID=meetingID,
        personID=personID,
        status=status,
        note=note,
        keep_best_status=keep_best_status)


def update_student_term_tuition_schedule_bracket(
        person_id: str = None,
        academic_term_id: str = None,
        tuition_schedule_id: str = None,
        tuition_schedule_bracket_id: str = None):
    """
    Updates a student's term tuition schedule bracket.

    :param person_id: The numeric person ID of the student you're interested in.
    :param academic_term_id: The numeric ID of the academic term you're interested in.
    :param tuition_schedule_id: The numeric ID of the tuition schedule you're interested in.
    :param tuition_schedule_bracket_id: The numeric ID of the tuition schedule bracket you're interested in, or "AUTOMATIC".
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'updateStudentTermTuitionScheduleBracket',
        person_id=person_id,
        academic_term_id=academic_term_id,
        tuition_schedule_id=tuition_schedule_id,
        tuition_schedule_bracket_id=tuition_schedule_bracket_id)


def upload_assignment_submission(assignment_id: str = None, file: str = None):
    """
    Uploads a file to an assignment for the current user.

    :param assignment_id: The numeric ID of the assignment.
    :param file: File uploaded the via the HTTP POST method.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'uploadAssignmentSubmission',
        assignment_id=assignment_id,
        file=file)


def upload_file(
        person_id: str = None,
        file: str = None,
        custom_field_id: str = None,
        term_id: str = None,
        role_ids: str = None):
    """
    Uploads a file for a particular person.

    :param person_id: The numeric ID of the person.
    :param file: File uploaded the via the HTTP POST method.
    :param custom_field_id: If passed in, the file will be uploaded to the given custom info field.
    :param term_id: The numeric ID of the term you're interested in.
    :param role_ids: An array of role IDs - the file will be visible to people with these role IDs.
    :returns: String containing xml or an lxml element.
    """

    return get_anonymous(
        'uploadFile',
        person_id=person_id,
        file=file,
        custom_field_id=custom_field_id,
        term_id=term_id,
        role_ids=role_ids)
