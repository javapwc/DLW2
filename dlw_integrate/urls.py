"""dlw_integrate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from dlw.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_request,name='loginurl'),
    path('logout/',logout_request,name='logout'),
    path('homeadmin/',homeadmin,name='homeadmin'),
    path('createuser/',create,name='create'),
    path('dynamic/',dynamicnavbar),
    path('homeuser/', homeuser, name='homeuser'),
    path('api/chart/data/',ChartData.as_view()),
    path('password_change/done/',auth_views.PasswordChangeView.as_view(template_name='password_reset_inside_complete.html'),name='password_reset_internal_complete'),
    path('password_reset_inside/',auth_views.PasswordChangeView.as_view(template_name='password_reset_inside.html'),name='password_reset_inside'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('', include('django.contrib.auth.urls')),
    path('ajax/get_emp_info/',getEmpInfo,name='get_emp_info'),
    path('ajax/get_permission_info/',getPermissionInfo,name='get_permission_info'),
    path('ajax/get_auth_emp_info/',getauthempInfo,name='get_auth_emp_info'),
    path('ajax/get_shopemp_info/',getshopempinfo,name='get_shopemp_info'),
    path('ajax/shiftsave/',shiftsave,name='shiftsave'),
    path('delete_user/',delete_user,name='delete_user'),
    path('forget_password/', forget_password, name='forget_password'),
    path('forget_password_path/',forget_path,name='forget_password_path'),
    path('update_permission/',update_permission,name='update_permission'),
    path('update_permission_incharge/',update_permission_incharge,name='update_permission_incharge'),
    path('update_emp_shift/',update_emp_shift,name='update_emp_shift'),
    path('update_emp_shift_admin/',update_emp_shift_admin,name='update_emp_shift_admin'),
    path('test/',test,name='test'),
    path('m2view/',m2view,name='m2view'),
    path('ajax/m2getbr/',m2getbr,name='m2getbr'),
    path('ajax/m2getassly/',m2getassly,name='m2getassly'),
    path('ajax/m2getpart_no/',m2getpart_no,name='m2getpart_no'),
    path('ajax/m2getdoc_no/',m2getdoc_no,name='m2getdoc_no'),
    path('ajax/m2getwono',m2getwono,name='m2getwono'),
    path('m4view/', m4view, name='m4view'),
    path('ajax/m4getbr/',m4getbr,name='m4getbr'),
    path('ajax/m4getassly/',m4getassly,name='m4getassly'),
    path('ajax/m4getpart_no/',m4getpart_no,name='m4getpart_no'),
    path('ajax/m4getdoc_no/',m4getdoc_no,name='m4getdoc_no'),
    path('ajax/m4getwono',m4getwono,name='m4getwono'),
    path('mg9initialreportviews/',mg9initialreportviews,name='mg9initialreportviews'),
    path('mg9compreportviews/',mg9compreportviews,name='mg9compreportviews'),
    path('ajax/mg9getmw/',mg9getmw,name='mg9getmw'),
    path('ajax/mg9getstaff/',mg9getstaff,name='mg9getstaff'),
    path('m14view/', m14view, name='m14view'),
    path('ajax/m14getbr/',m14getbr,name='m14getbr'),
    path('ajax/m14getassly/',m14getassly,name='m14getassly'),
    path('ajax/m14getpart_no/',m14getpart_no,name='m14getpart_no'),
    path('ajax/m14getdoc_no/',m14getdoc_no,name='m14getdoc_no'),
    path('ajax/m14getwono',m14getwono,name='m14getwono'),
    path('ajax/get_yr_dgp/',getYrDgp,name='get_yr_dgp'),
    path('ajax/check_loco/',checkloco,name='check_loco'),
    path('ajax/check_total/',checktotal,name='check_total'),
    path('aprodplan/',bprodplan,name='aprodplan'),
    path('miscellaneous_section/',miscellaneous_section,name='miscellaneous_section'),
    path('jpo/',jpo,name='jpo'),
    path('machining_of_air_box/',insert_machining_of_air_box,name='machining_of_air_box'),
    path('dpoinput/',dpoinput,name='dpoinput'),
    path('dpo/',dpo,name='dpo'),
    path('dporeport/',dporeport,name='dporeport'),
    path('ajax/getcumino/',getcumino,name='getcumino'),
    path('m1view/',m1view,name='m1view'),
    path('ajax/m1getpano/',m1getpano,name='m1getpano'),
    path('m5view/',m5view,name='m5view'),
    path('m12view/',m12view,name='m12view'),
    path('m3view/',m3view,name='m3view'),
    path('ajax/m5getbr/',m5getbr,name='m5getbr'),
    path('ajax/submitprod/',bprodplan,name="submitprod"),
    path('ajax/m5getpart_no/',m5getpart_no,name='m5getpart_no'),
    path('ajax/m5getdoc_no/',m5getdoc_no,name='m5getdoc_no'),
    path('ajax/m5getwono',m5getwono,name='m5getwono'),
    path('ajax/m5getempname/',m5getempname,name='m5getempname'),
    path('ajax/m12getwono',m12getwono,name='m12getwono'),
    path('ajax/airbox_addbo',airbox_addbo,name='airbox_addbo'),
    path('ajax/miscell_addbo',miscell_addbo,name='miscell_addbo'),
    path('ajax/miscell_editsno',miscell_editsno,name='miscell_editsno'),
    path('m1genrept1/',m1genrept1,name='m1genrept1'),
    path('ajax/m3getbr/', m3getbr, name='m3getbr'),
    path('ajax/m3shopsec/', m3shopsec, name='m3shopsec'),
    path('ajax/m3getassly/', m3getassly, name='m3getassly'),
    path('ajax/m3getpart_no/', m3getpart_no, name='m3getpart_no'),
    path('ajax/m3getdoc_no/', m3getdoc_no, name='m3getdoc_no'),
    path('ajax/m3getwono/', m3getwono, name='m3getwono'),
    path('m3sub/', m3sub, name='m3sub'),
    path('ajax/m5getstaff_no/',m5getstaff_no,name='m5getstaff_no'),
    path('ajax/m12getstaff_no/',m12getstaff_no,name='m12getstaff_no'),
    path('m7view/', m7view, name='m7view'),
    path('ajax/m7getwono/', m7getwono, name='m7getwono'),
    path('ajax/m7getempno/', m7getempno, name='m7getempno'),
    path('ajax/m7getpart_no/', m7getpart_no, name='m7getpart_no'),
    path('ajax/airbox_editsno',airbox_editsno,name='airbox_editsno'),
    path('ajax/pinion_addbo',pinion_addbo,name='pinion_addbo'),
    path('PinionPress/',pinionpressing_section,name='PinionPress'),
    path('ajax/pinion_editsno',pinion_editsno,name='pinion_editsno'),
    path('ajax/axlepress_addbo',axlepress_addbo,name='axlepress_addbo'),
    path('axlewheelpressing_section/',axlewheelpressing_section,name='axlewheelpressing_section'),
    path('M20view/',M20view,name='M20view'),
    path('m20getstaffno/',m20getstaffno,name='m20getstaffno'),
    path('mg33getstaffno/',mg33getstaffno,name='mg33getstaffno'),
    path('m26view/',m26view,name='m26view'),
    path('m27view/',m27view,name='m27view'),
    path('ajax/m27getStaffNo/', m27getStaffNo, name='m27getStaffNo'),   
    path('ajax/m27getDetails/', m27getDetails, name='m27getDetails'),  
    path('ajax/m27getDesignation/', m27getDesignation, name='m27getDesignation'),
    path('ajax/m27getWorkOrder/', m27getWorkOrder, name='m27getWorkOrder'),
    path('ajax/m27getWorkOrderDate/', m27getWorkOrderDate, name='m27getWorkOrderDate'),
    path('ajax/m27getBatchNo/', m27getBatchNo, name='m27getBatchNo'),
    path('m18view/',m18view,name='m18view'),
    path('ajax/m26getwono/', m26getwono, name='m26getwono'),
    path('ajax/m26getStaffCatWorkHrs/', m26getStaffCatWorkHrs, name='m26getStaffCatWorkHrs'),
    path('ajax/m20getstaffName/', m20getstaffName, name='m20getstaffName'),
    path('m22view/', m22view, name='m22view'),
    path('ajax/m22getwono/',m22getwono,name='m22getwono'),
    path('ajax/m22getstaff/',m22getstaff,name='m22getstaff'),
    path('ajax/axlepress_editsno',axlepress_editsno,name="axlepress_editsno"),
    path('ajax/wheelnde',wheelnde,name='wheelnde'),
    path('logbook_delete/', logbook_delete, name='logbook_delete'),
    path('logbook_update/', logbook_update, name='logbook_update'),
    path('logbook_record/', logbook_record, name='logbook_record'),
    path('CardGeneration/',CardGeneration,name='CardGeneration'),
    path('m15view/', m15view, name='m15view'),
    path('ajax/m15getwono/', m15getwono, name='m15getwono'),
    path('ajax/m15getpart_no/', m15getpart_no, name='m15getpart_no'),
    path('ajax/m18getwono/', m18getwono, name='m18getwono'),
    path('ajax/m18getpart_no/', m18getpart_no, name='m18getpart_no'),
    path('ajax/m18getoperation_no/', m18getoperation_no, name='m18getoperation_no'),
    path('ajax/m18getoperation_desc/', m18getoperation_desc, name='m18getoperation_desc'),
    path('ajax/m13getpano/',m13getpano,name='m13getpano'),
    path('ajax/m13getwono',m13getwono,name='m13getwono'),
    path('m13view/', m13view, name='m13view'),
    path('ajax/m13getno',m13getno,name='m13getno'),
    path('ajax/m18getRef_no',m18getRef_no,name='m18getRef_no'),
    path('mg7view/', mg7view, name='mg7view'),
    path('ajax/mg7getwono/', mg7getwono, name='mg7getwono'),
    path('ajax/mg7getpartno/', mg7getpartno, name='mg7getpartno'),
    path('ajax/mg7getshop/', mg7getshop, name='mg7getshop'),
    path('ajax/mg7getjob/', mg7getjob, name='mg7getjob'),
    path('m23view/',m23view,name='m23view'),
    path('m23getempno/',m23getempno,name='m23getempno'),
    path('ajax/bogieassemb_addbo',bogieassemb_addbo,name="bogieassemb_addbo"),
    path('ajax/bogieassemb_editsno',bogieassemb_editsno,name="bogieassemb_editsno"),
    path('bogieassembly/',bogieassembly_section,name='bogieassembly'),
    path('demandreg/',wogen,name='demandreg'),
    path('MG22view/', MG22view, name='MG22view'),
    path('MG22report/', mg22report, name='MG22report'),
    path('ajax/wheelpress_inspectsno',wheelpress_inspectsno,name='wheelpress_inspectsno'),
    path('m13insert/',m13insert,name='m13insert'),
    path('mg20view/', mg20view, name='mg20view'),
    path('ajax/mg20getstaff/', mg20getstaff, name='mg20getstaff'),
    path('RoleGeneration/', RoleGeneration, name='RoleGeneration'),
    path('RoleDelete/', RoleDelete, name='RoleDelete'),
    path('maintain/', viewsPermission, name='viewsPermission'),
    path('maintain/delete/', viewsPermissiondelete, name='viewsPermissiondelete'),
    path('maintain/update/', viewsPermissionUpdate, name='viewsPermissionUpdate'),
    path('MG33view/', MG33view, name='MG33view'),
    path('m30view/', m30view, name='m30view'),
    path('mg33report/', mg33report, name='mg33report'),
    path('M13register/', M13register, name='M13register'),
    path('view_exam_data/',view_exam_data, name='view_exam_data'),
    path('ajax/m30getpartno/', m30getpartno, name='m30getpartno'),
    path('ajax/mg33getexam/', mg33getexam, name='mg33getexam'),
    path('ajax/m30getstaffno/', m30getstaffno, name='m30getstaffno'),
    path('mg15view/', mg15view, name='mg15view'),
    path('ajax/mg15getstaff/', mg15getstaff, name='mg15getstaff'),
    path('mg49view/', mg49view, name='mg49view'),
    path('mg49getstaff_no/', mg49getstaff_no, name='mg49getstaff_no'),
    path('mg49getmat_des/', mg49getmat_des, name='mg49getmat_des'),
    path('mg49report/', mg49report, name='mg49report'),
    path('ajax/m11getpart_no/',m11getpart_no,name='m11getpart_no'),
    path('ajax/m11getstaff_no/',m11getstaff_no,name='m11getstaff_no'),              
    path('ajax/m11getwono/',m11getwono,name='m11getwono'),
    path('m11view/',m11view,name='m11view'),
    path('m11report/',m11report,name='m11report'),
    path('mg18view/', mg18view, name='mg18view'),
    path('mg36view/', mg36view, name='mg36view'),
    path('ajax/mg36getempno/', mg36getempno, name='mg36getempno'),
    path('m9view/',m9view,name='m9view'),
    path('ajax/m9getwono',m9getwono,name='m9getwono'),
    path('ajax/m9getpart_no',m9getpart_no,name='m9getpart_no'),
    path('staff_auth_view/', staff_auth_view, name='staff_auth_view'),
    path('staff_auth_viewgetshop_name/', staff_auth_viewgetshop_name, name='staff_auth_viewgetshop_name'),
    path('staff_auth_viewgetstaff_name/', staff_auth_viewgetstaff_name, name='staff_auth_viewgetstaff_name'),
    path('staff_auth_viewgetemp_name/', staff_auth_viewgetemp_name, name='staff_auth_viewgetemp_name'),
    path('staff_auth_report_view/', staff_auth_report_view, name='staff_auth_report_view'),
    path('ajax/m9getopno',m9getopno,name='m9getopno'),
    path('m5hwview/', m5hwview, name='m5hwview'),
    path('partallotement/', partallotement, name='partallotement'),
    path('ajax/getpartnewdetails',getpartnewdetails,name='getpartnewdetails'),
    path('ajax/getpartnewdetails123',getpartnewdetails123,name='getpartnewdetails123'),
    path('ajax/getpartdecription',getpartdecription,name='getpartdecription'),    
    path('examdetail/',exam_detail,name='examdetail'),
    path('m23view/',m23view,name='m23view'),
    path('m23report/',m23report,name='m23report'),
    path('m23getempno/',m23getempno,name='m23getempno'),
    path('ajax/getm23date',getm23date,name='getm23date'),
    path('performaA/',performaA,name='performaA'),
    path('m3a/',m3a,name='m3a'),
    path('wheelmachining_section/',wheelmachining_section,name='wheelmachining_section'),
    path('axlemachining_section/',axlemachining_section,name='axlemachining_section'),
    path('ajax/axle_addbo',axle_addbo,name='axle_addbo'),
    path('ajax/axle_editsno',axle_editsno,name='axle_editsno'),
    path('ajax/whl_addbo',whl_addbo,name='whl_addbo'),
    path('ajax/whl_editsno',whl_editsno,name='whl_editsno'),
    path('m21view/', m21view, name='m21view'),
    path('ajax/m21getempno/', m21getempno, name='m21getempno'),
    path('ajax/m21getyymm/', m21getyymm, name='m21getyymm'),
    path('mg6views/',mg6views,name='mg6views'),
    path('ajax/mg6getmc/',mg6getmc,name='mg6getmc'),
    path('ajax/mg6getcd/',mg6getcd,name='mg6getcd'),
    path('ajax/mg6gettool/',mg6gettool,name='mg6gettool'),
    path('airboxreport/',airboxreport,name='airboxreport'),
    path('mg9initialreportviews/',mg9initialreportviews,name='mg9initialreportviews'),
    path('ajax/mg9getmw/',mg9getmw,name='mg9getmw'),
    path('ajax/mg9getstaff/',mg9getstaff,name='mg9getstaff'),
    path('miscreport/',miscreport,name='miscreport'),
    path('axlereport/',axlereport,name='axlereport'),
    path('wheelreport/',wheelreport,name='wheelreport'),
    path('bogiereport/',bogiereport,name='bogiereport'),
    path('pinionreport/',pinionreport,name='pinionreport'),
    path('axlepressreport/',axlepressreport,name='axlepressreport'),
    path('mgrview/', mgrview, name='mgrview'),
    path('ajax/mgrgetinsno/', mgrgetinsno, name='mgrgetinsno'),
    path('mgrreports/', mgrreports, name='mgrreports'),
    path('ajax/mg21getstaff/', mg21getstaff, name='mg21getstaff'),
    path('mg21view/', mg21view, name='mg21view'),
    path('mg21report/',mg21report,name='mg21report'),
    path('mg21getstaff/',mg21getstaff,name='mg21getstaff'),
    path('mg9compreportviews/',mg9compreportviews,name='mg9compreportviews'),
    path('ajax/mg9getstaff/',mg9getstaff,name='mg9getstaff'),
    path('ajax/mg9getmwno/',mg9getmwno,name='mg9getmwno'),
    path('ajax/mg9getstaffno/',mg9getstaffno,name='mg9getstaffno'),
    path('m2hwview/', m2hwview, name='m2hwview'),
    path('ajax/m2getwonohw',m2getwonohw,name='m2getwonohw'),
    path('ajax/m2getbrhw/',m2getbrhw,name='m2getbrhw'),
    path('ajax/m2getasslyhw/',m2getasslyhw,name='m2getasslyhw'),
    path('ajax/m2getpart_nohw/',m2getpart_nohw,name='m2getpart_nohw'),
    path('ajax/m2getdoc_nohw/',m2getdoc_nohw,name='m2getdoc_nohw'),
    path('m18aview/',m18aview,name='m18aview'),
    path('M24views/',M24views, name='M24views'),
    path('ajax/m24getdesgn/',m24getdesgn,name='m24getdesgn'),
    path('ajax/m24getstaff_no/',m24getstaff_no,name='m24getstaff_no'),              
    path('ajax/m24getssfo/',m24getssfo,name='m24getssfo'),
    path('ajax/m24getsuprvsr/',m24getsuprvsr,name='m24getsuprvsr'),
    path('m24report/',m24report, name='m24report'),
    path('ajax/m18getpart_no/',m18getpart_no,name='m18getpart_no'),
    path('ajax/m18getsse/',m18getsse,name='m18getsse'),
    path('ajax/m18getticket_no/',m18getticket_no,name='m18getticket_no'),
    path('ajax/m18getempname/',m18getempname,name='m18getempname'),
    path('ajax/m18getoprn_no/',m18getoprn_no,name='m18getoprn_no'),
    path('ajax/m18getwono/',m18getwono,name='m18getwono'),
    path('m4hwview/', m4hwview, name='m4hwview'),
    path('ajax/m4getbrhw/',m4getbrhw,name='m4getbrhw'),
    path('ajax/m4getasslyhw/',m4getasslyhw,name='m4getasslyhw'),
    path('ajax/m4getpart_nohw/',m4getpart_nohw,name='m4getpart_nohw'),
    path('ajax/m4getdoc_nohw/',m4getdoc_nohw,name='m4getdoc_nohw'),
    path('ajax/m4getwonohw',m4getwonohw,name='m4getwonohw'),
]
