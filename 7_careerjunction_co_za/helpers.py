from bs4 import BeautifulSoup


html = """

<div class="cjun-main-profile job-details ">
                            <div class="main-profile">
                                <div class="main-profile-info">
                                    <div class="profile-info">
                                        <div class="job-description">
                                            <div class="logo-mob">
                                                <img src="https://careerjunction-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/27464-240x120.png?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPPL4T7PMH/20240109/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20240109T120613Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=bf8bb7252190c7f1fae59fee9b6998d741de08b54790b73382e125a95783f22b" alt="Reverside Professional Services" onerror="smallLogoNotFound(this)">
                                            </div>

                                            <div class="name-wrapper">
                                                <h1>Senior SQL Developer at Reverside</h1>
                                                    <h2>Reverside Professional Services</h2>
                                                <span id="lastViewed" class="viewed-label" style="visibility: hidden"></span>
                                            </div>

                                            <ul class="job-overview ov-item">
                                                <li class="salary">Commission Only</li>

                                                    <li class="position">Permanent Senior position</li>

                                                <li class="location">
                                                    Johannesburg
                                                </li>


                                                    <li class="updated-time">Posted 09 Jan 2024 by Reverside Professional Services</li>
                                                                                                    <li class="expires">Expires in 34 days</li>
                                                <li class="cjun-job-ref">
                                                    Job 2550148 
                                                </li>

                                            </ul>

                                            <div class="cta-desc">
                                                <div class="apply-btn-wrapper">
                                                    <span id="overlayTrigger"></span>

                                                    <div class="favorite" jobid="2550148">
                                                        <a class="btn-save-job" rel="nofollow"><i class="far fa-star"></i> <span class="save-dk">Save</span> </a>
                                                    </div>

                <a href="/application/apply-link/2550148" class="btn-apply data_btn_track" rel="nofollow">Apply Now</a>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <div class="job-desc-on-expired job-details-description">
                                    <div class="job-details">
                                        <h2>About the position</h2>
                                        <p><span></span></p><p>Reverside is an IT services provider; we are always looking for professional candidates to join our team in Software Development, providing opportunities to work on exciting projects, within our well-established client base. We are looking for a Senior SQL Developer Professional with 5- 8 who is responsible for batch processing development as well as backend capability to support the application. SQL developers translate software requirements into workable programming code and maintain and develop programs for use in business.<br><br>The role usually involves writing technical specifications and designing, building, testing, implementing and sometimes supporting applications using programming languages and development tools.<br><br>The SQL Developer contributes to the development of software to support web, and multi-media applications that facilitates the achievement of business outcomes and improves business efficiencies and processes through leveraging technology.<br><br>Key Area of Responsibility<br><br></p><ul><li>Work as part of a project team, reporting to an IT Manager.</li><li>Work closely with business staff to ensure solutions adhere to client standards and fit their strategic enterprise architecture.</li><li>Definition and management of non-functional requirements, including working with others to ensure these requirements have been met.</li><li>Definition and organization of development tasks and accurate estimation of these tasks.</li><li>Work closely with members of the development team to ensure that the software design and implementation meets the architectural goals and quality standards.</li><li> Provide support to the business analysts, and other project team members, during functional requirements definition to ensure that functionality is both technically achievable and feasible within the project constraints.</li><li> Identification and ownership of technical project risks and issues, including owning mitigation activities and resolution of issues.</li><li> Undertake other duties as directed by line managers commensurate with the post.</li><li>Actively seeking opportunities to contribute improvements to Client's applications.</li><li>Mentoring junior members of the development team including training.</li><li>Acting as a focal point of expertise on key technologies or skills.</li></ul><strong>Qualification and Skill Requirements</strong><br><br><ul><li>Computer Science or other relevant technical degree, diploma, or certification.</li><li>At least 8+ years Development experience.</li><li>Experience of the full software development lifecycle.</li><li>Experience within an agile environment, with Scrum/KANBAN as methodology.</li><li>Advanced working knowledge of SQL (DDL, DML, JSON, XML).</li><li>Extensive experience in dealing with large datasets and managing incremental batch loading methodologies.</li><li>Advanced understanding of relational data structures including keys, constraints, and triggers.</li><li>Performance tuning and optimization of RDBMS.</li><li>Highly skilled and experienced in using relational database technologies in an environment with high data volumes and many transactional systems.</li><li>Understand how to design and implement a conceptual, logical, and physical data model that supports the needs of the organization.</li><li>Solid understanding and experience in data modelling, data management and governance methodologies.</li><li>Ability to develop unit testing of code components.</li><li>Advantageous – Microsoft stack SSIS, SSRS, SSAS, Power BI, SQL Server.</li><li>Experience building DevOps automation is beneficial.</li><li>Previous experience in the Insurance Industry is beneficial.</li></ul>Behavioral Competencies<br><br><ul><li>Good planning, organizational skills, task/project driven, deadline oriented.</li><li>Good collaboration, communication, and interpersonal skills.</li><li>Good people management skills.</li><li>Good problem solving and decision-making ability.</li><li>Ability to prioritize and work under pressure.</li><li>High attention to quality and detail.</li><li>Process and practices orientated.</li><li>Analytical and problem-solving skills.</li></ul><br><br><p></p><img src="https://recruiter.careerjunction.co.za//_service/p/RecruiterSiteTypePlugin_1_0/recruiter/logpixeltrackingjobview?id=8a2937c2-aedb-11ee-b7b9-06012153df26" width="0px" height="0px" style="display:none">

<p><span><strong>Desired Skills: </strong></span></p>
<ul>
<li>Scrum/KANBAN as methodolo</li>
<li>SQL (DDL</li>
<li> DML</li>
<li> JSON</li>
<li> XML)</li>
<li>Microsoft stack SSIS</li>
<li> SSRS</li>
</ul>


<p><span><strong>About The Employer: </strong></span></p>
<p><span>Reverside is a Global ICT company focusing on Digital Engineering, Integration, Cyber-Security, Cloud and Digital Transformation services with delivery centres in Johannesburg and Cape Town, South Africa and Gurgaon, India. Reverside has its Global Headquarter in South Africa and is a B-BBEE Level 1 IT consulting &amp; services organization. Reverside was founded in 2006 and has since grown to a strong team of over 300+ consultants, serving more than 40+ active clients [URL Removed] - [URL Removed] - [URL Removed]</span></p>


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                <p></p>
                                    </div>
                                </div>

                                <div class="expires expires-button cta-desc-above">

                <a href="/application/apply-link/2550148" class="btn-apply data_btn_track" rel="nofollow">Apply Now</a>

                                </div>
                            </div>

                            <div class="aside-profile">
                                <div class="profile-container">
                                    <div class="profile-image">
                                        <div class="cjun-logo-wrap">
                                            <a href="/companies/27464/reverside-professional-services">
                                                <img class="cjun-logo-company" src="https://careerjunction-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/27464-240x120.png?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPPL4T7PMH/20240109/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20240109T120613Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=bf8bb7252190c7f1fae59fee9b6998d741de08b54790b73382e125a95783f22b" alt="" onerror="smallLogoNotFound(this)">
                                            </a>
                                        </div>
                                            <h2>Reverside Professional Services</h2>
                                                <div class="company-links">
                                                    <a href="/companies/27464/reverside-professional-services">
                                                            <p>View agency profile</p>
                                                        <i class="fas fa-arrow-right"></i>
                                                    </a>
                                                    <a href="/companies/27464/reverside-professional-services#jobs">
                                                        <p>See all Reverside Professional Services jobs</p>
                                                        <i class="fas fa-arrow-right"></i>
                                                    </a>
                                                </div>
                                                <div class="about-the-agency">
                                                    <h2>About the agency</h2>
                                                    <p style="display: block; overflow: visible; height: auto;" id="about-the-agency-text">Reverside is a consulting company that serves mainly but not limited to the Financial Industry. We are constantly looking for Top Talent – people who are passionate about their careers and interested in building long term professional relationships.

Overview of RPS:
• Professional recruitment services in the IT, Finance, Management, Engineering &amp; Mining sectors.
• Legally compliant / APSO member
• Black empowered entity: awarded AA rating from Emp...</p>
                                                    <div>
                                                        <a id="read-more" href="#">read more</a>
                                                        <a id="read-less" href="#" style="display: none;">read less</a>
                                                    </div>
                                                </div>

                                        <div id="jobalertfeedbackSimilar" class="similar-jobs-email">
                                            <p class="receive-email">Receive a daily digest of all new jobs matching this job. Your information is safe with us and you can cancel any time.</p>
                                            <a id="create-job-alert-btn" class="apply-now email-me-jobs-btn">
                                                EMAIL ME JOBS LIKE THIS
                                            </a>
                                        </div>
                                        <div class="clear"></div>
                                        <div class="add-job-alert-container job-description-job-alert">

                                            


<script type="text/javascript" src="/Common/js/smartRegistration.js?v=1"></script>
<script type="text/javascript">
    if (!saon.Api.AjaxWS) saon.Api.AjaxWS = {};
    saon.Api.AjaxWS.ValidateEmailDomain = '/validate-cv-domain';
    function createJobAlertSimilar() {

        var email = "";
        //TO DO: Unify JS code of new job alerts partial views
                
                email = $("#Email-similar").val();
                

        if (email != "") {
            if (validateEmailDomain(email)) {
                $("#createjobalertSimilar").css("visibility", "hidden");
                $("#addjobalertdivSimilar").append("<img src='/img/icons/AjaxLoader.gif' />");
                $.ajax({
                    type : 'POST',
                    data: { jobAlertName: "Senior SQL Developer at Reverside", email: email, requestURL: "https://www.careerjunction.co.za/JobDesc.aspx?ID=2550148",isJobDescription:'True'},
                    dataType: 'json',
                    url: "/CreateJobAlert",
                    success: function (data) {
                        if (data.Success) {
                            var message = "";

                        if (data.NewJobSeeker) {
                            message += "<p class='confirm'><svg version='1.1' id='Layer_1' xmlns='https://www.w3.org/2000/svg' xmlns:xlink='https://www.w3.org/1999/xlink' x='0px' y='0px' viewBox='0 0 21 21' style='width: 19px;vertical-align: bottom;enable-background:new 0 0 21 21;' xml:space='preserve'><style type='text/css'>.st0{fill:none;}.st1{fill:#31C104;}</style><g><path class='st0' d='M10.5,20C5.3,20,1,15.7,1,10.5C1,5.3,5.3,1,10.5,1c5.2,0,9.5,4.2,9.5,9.5C20,15.7,15.7,20,10.5,20z'></path><path class='st1' d='M10.5,2c4.7,0,8.5,3.8,8.5,8.5S15.2,19,10.5,19S2,15.2,2,10.5S5.8,2,10.5,2 M10.5,0C4.7,0,0,4.7,0,10.5S4.7,21,10.5,21S21,16.3,21,10.5S16.3,0,10.5,0L10.5,0z'></path></g><g><path class='st0' d='M8.7,14.8c0,0-0.1,0-0.2,0l-3-3c-0.1-0.1-0.1-0.1-0.1-0.2s0-0.1,0.1-0.2c0.1-0.1,0.1-0.1,0.2-0.1c0,0,0.1,0,0.2,0.1l2.8,2.8l6.5-6.5c0.1-0.1,0.1-0.1,0.2-0.1s0.1,0,0.2,0.1c0.1,0.1,0.1,0.1,0.1,0.2c0,0,0,0.1-0.1,0.2l-6.7,6.7C8.8,14.8,8.8,14.8,8.7,14.8z'></path><path class='st1' d='M15.4,6.6c-0.3,0-0.6,0.1-0.9,0.4l-5.8,5.8l-2.1-2.1c-0.2-0.2-0.6-0.4-0.9-0.4c-0.3,0-0.6,0.1-0.9,0.4c-0.5,0.5-0.5,1.3,0,1.8l2.9,2.9c0,0,0,0,0,0c0.2,0.2,0.6,0.4,0.9,0.4s0.6-0.1,0.9-0.4l6.7-6.7c0.5-0.5,0.5-1.3,0-1.8C16.1,6.7,15.7,6.6,15.4,6.6L15.4,6.6z'></path></g></svg>&nbsp; Your job alert email has been created.<br>"
                            message += "An email has been sent to " + email + ".<br>";
                            message += "Please click the link in the email to create your account and start receiving your Job Alerts emails.<br>";
                            message += "The link will expire in 24 hours.</p>"
                        } else {
                            message += "<p class='confirm'><svg version='1.1' id='Layer_1' xmlns='https://www.w3.org/2000/svg' xmlns:xlink='https://www.w3.org/1999/xlink' x='0px' y='0px' viewBox='0 0 21 21' style='width: 19px;vertical-align: bottom;enable-background:new 0 0 21 21;' xml:space='preserve'><style type='text/css'>.st0{fill:none;}.st1{fill:#31C104;}</style><g><path class='st0' d='M10.5,20C5.3,20,1,15.7,1,10.5C1,5.3,5.3,1,10.5,1c5.2,0,9.5,4.2,9.5,9.5C20,15.7,15.7,20,10.5,20z'></path><path class='st1' d='M10.5,2c4.7,0,8.5,3.8,8.5,8.5S15.2,19,10.5,19S2,15.2,2,10.5S5.8,2,10.5,2 M10.5,0C4.7,0,0,4.7,0,10.5S4.7,21,10.5,21S21,16.3,21,10.5S16.3,0,10.5,0L10.5,0z'></path></g><g><path class='st0' d='M8.7,14.8c0,0-0.1,0-0.2,0l-3-3c-0.1-0.1-0.1-0.1-0.1-0.2s0-0.1,0.1-0.2c0.1-0.1,0.1-0.1,0.2-0.1c0,0,0.1,0,0.2,0.1l2.8,2.8l6.5-6.5c0.1-0.1,0.1-0.1,0.2-0.1s0.1,0,0.2,0.1c0.1,0.1,0.1,0.1,0.1,0.2c0,0,0,0.1-0.1,0.2l-6.7,6.7C8.8,14.8,8.8,14.8,8.7,14.8z'></path><path class='st1' d='M15.4,6.6c-0.3,0-0.6,0.1-0.9,0.4l-5.8,5.8l-2.1-2.1c-0.2-0.2-0.6-0.4-0.9-0.4c-0.3,0-0.6,0.1-0.9,0.4c-0.5,0.5-0.5,1.3,0,1.8l2.9,2.9c0,0,0,0,0,0c0.2,0.2,0.6,0.4,0.9,0.4s0.6-0.1,0.9-0.4l6.7-6.7c0.5-0.5,0.5-1.3,0-1.8C16.1,6.7,15.7,6.6,15.4,6.6L15.4,6.6z'></path></g></svg>&nbsp; Your job alert email has been created.</p>"
                        }

                            //DTM direct call for jaсreated condition
                            if (data.JaId > 0) {
                                window.digitalData["jobalert__id"] = data.JaId;
                                try {
                                    _satellite.track("jacreated");
                                } catch (e) {}
                            }
                        $("#addjobalertdivSimilar").hide();
                        $("#jobalertfeedbackSimilar").html("");
                        $("#jobalertfeedbackSimilar").html(message);
                    } else {
                        $("#addjobalertdivSimilar").hide();
                        $("#jobalertfeedbackSimilar").html("");
                        $("#jobalertfeedbackSimilar").html("<p class='error'><?xml version='1.0' encoding='utf-8'?><!-- Generator: Adobe Illustrator 20.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  --><svg version='1.1' id='Layer_1' xmlns='https://www.w3.org/2000/svg' xmlns:xlink='https://www.w3.org/1999/xlink' x='0px' y='0px' viewBox='0 0 21 21' style='enable-background:new 0 0 21 21;width: 19px;vertical-align: bottom;' xml:space='preserve'><style type='text/css'>.st0{fill:none;}.stRed{fill:#FF9595;}</style><g><path class='st0' d='M10.5,20C5.3,20,1,15.7,1,10.5C1,5.3,5.3,1,10.5,1c5.2,0,9.5,4.2,9.5,9.5C20,15.7,15.7,20,10.5,20z'/><path class='stRed' d='M10.5,2c4.7,0,8.5,3.8,8.5,8.5S15.2,19,10.5,19S2,15.2,2,10.5S5.8,2,10.5,2 M10.5,0C4.7,0,0,4.7,0,10.5S4.7,21,10.5,21S21,16.3,21,10.5S16.3,0,10.5,0L10.5,0z'/></g><g><path class='stRed' d='M12.4,14.9C11.1,16.4,9.7,17,9.1,17c-0.5,0-0.9-0.4-0.6-1.9l1.1-4.8c0.1-0.5,0.1-0.6,0-0.6c-0.2,0-0.8,0.4-1.1,0.7L8.2,9.9c1.3-1.3,2.7-2.1,3.4-2.1c0.6,0,0.7,0.7,0.4,2l-1.1,4.7c-0.1,0.6-0.1,0.7,0.1,0.7c0.2,0,0.6-0.3,1.1-0.7L12.4,14.9z M12.8,5.1c0,0.8-0.6,1.5-1.4,1.5c-0.6,0-1-0.5-1-1.1c0-0.8,0.5-1.5,1.4-1.5C12.4,4,12.8,4.5,12.8,5.1z'/></g></svg>&nbsp; You have reached your limit of 5 job alert emails.<br>To save a new job alert email you must delete at least 1 previously <a href='/myprofile/jobalerts'>saved job alert</a>.</p>");
                    }
                },
            });
        } else {
            $("#jobalerterror-msgEmail").css("display", "inline-block");
            $('.name-alert').click(function(){
                $('#jobalerterror-msgEmail').hide();
            });
        }
    } else {
            $("#jobalerterror-msgSimilar").css("display", "inline-block");
    $('.name-alert').click(function(){
        $('#jobalerterror-msgSimilar').hide();
    });
    }
   }

</script>

<div id="addjobalertdivSimilar" style="display: none;">
    <div class="email-address" data-hj-masked="">
            <input class="name-alert" id="Email-similar" maxlength="255" name="Email-similar" placeholder="EMAIL" type="email" value="" tabindex="11">
    </div>
    <div id="jobalerterror-msgSimilar" style="display: none;">
        <p>Please enter your email address</p>
    </div>
    <div id="jobalerterror-msgEmail" style="display: none;">
        <p>Please enter a valid email address</p>
    </div>
    <input id="createjobalertSimilar" type="button" value="EMAIL ME JOBS" onclick="createJobAlertSimilar();" class="create-alert data_btn_track" tabindex="12">

</div>

                                        </div>
                                        <div class="date-bottom">
                                            <div>
                                                <i class="fas fa-hourglass-half"></i>
                                                    <p>Expires in 33 days</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
"""

import json

def scrap_data(html):
    data = {
        'jobName': '',
        'companyName': '',
        'salary': '',
        'position': '',
        'location': '',
        'posted_on': '',
        'expires': '',
        'jobRef': ''
    }

    soup= BeautifulSoup(html, 'html.parser')
    target_div = soup.find('div', class_= 'cjun-main-profile job-details')
    if target_div:
        name_ele = target_div.find('div', class_='name-wrapper') 
        data['jobName'] = name_ele.find('h1').get_text(strip= True) if name_ele and name_ele.find('h1') else ''
        data['companyName'] = name_ele.find('h2').get_text(strip= True) if name_ele and name_ele.find('h2') else ''

        target_ul = target_div.find('ul', class_='job-overview')
        li_tags = target_ul.find_all('li') if target_ul else None
        if li_tags:
            for litag in li_tags:
                if 'salary' in litag.get('class',[]):
                    data['salary'] = litag.get_text(strip=True)
                elif 'position' in litag.get('class',[]):
                    data['position'] = litag.get_text(strip=True)
                elif 'location' in litag.get('class', []):
                    data['location'] = litag.get_text(strip=True)
                elif 'updated-time' in litag.get('class', []):
                    data['posted_on'] = litag.get_text(strip = True)
                elif 'expires' in litag.get('class', []):
                    data['expires'] = litag.get_text(strip=True)
                elif 'cjun-job-ref' in litag.get('class', []):
                    data['jobRef'] = litag.get_text(strip=True)

    return data




print(json.dumps(scrap_data(html)))



