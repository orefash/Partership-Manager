from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from flask_login import current_user
from flask import request, jsonify
from forms import StaffForm

from . import staff_mgmt
from .. import db
from ..models import Staff, Staff_Role

from datetime import datetime

from data_helper import get_staff_details

@staff_mgmt.route('/staff', methods=['GET', 'POST'])
@login_required
def manage_staff():

    staff = get_staff_details()

    return render_template('manage_staff.html', staff=staff, title="Manage Staff")

@staff_mgmt.route('/delete-staff/<s_id>')
@login_required
def remove_staff(s_id):

    status = Staff.query.filter_by(id=s_id).delete()
    db.session.commit()

    print("Del status: ",status)

    return redirect(url_for('staff_mgmt.manage_staff'))

@staff_mgmt.route('/add-staff', methods=['GET', 'POST'])
@login_required
def add_staff():
    form = StaffForm()
    roles = Staff_Role.query.with_entities(Staff_Role.id, Staff_Role.role).all()
    print("Role:", roles)

    if request.method == 'POST':
        surname = request.form['surname']
        fname = request.form['fname']
        phone = request.form['phone']
        email = request.form['email']
        role = request.form['role']

        # print("Details: "+surname+" "+fname+" "+phone+" "+email+" "+role)
        staff = Staff(
        role_id=role,
        email=email,
        f_name=fname,
        l_name=surname,
        phone=phone,
        entry_date = datetime.today().strftime('%Y-%m-%d'),
        password_hash='password')
        db.session.add(staff)
        db.session.commit()
        # flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('staff_mgmt.manage_staff'))

    # staff = get_staff_details()

    return render_template('add_staff.html', form = form, title="Add Staff")

@staff_mgmt.route('/update-staff', methods=['GET', 'POST'])
@login_required
def update_staff():
    print("In update")

    result = {
        "status" : -1
    }

    if request.method == 'POST':

        print("In update 2")
        print("SNAME: ",request.form['fname'])
        print("SNAME: ",request.form['phone'])
        print("SNAME: ",request.form['email'])
        surname = request.form['surname']
        fname = request.form['fname']
        phone = request.form['phone']
        email = request.form['email']


        print("CU:",current_user)
        sid = current_user.id
        print("sid:",sid)

        staff = Staff.query.filter_by(id=sid).first()
        print("Staff: ",staff)
        staff.email = email
        staff.phone = phone
        staff.f_name = fname
        staff.l_name = surname

        db.session.commit()
        result["status"] = 0
        # flash('You have successfully registered! You may now login.')
        return jsonify(result)

    return jsonify(result)

@staff_mgmt.route('/update-password', methods=['GET', 'POST'])
@login_required
def update_password():
    print("In update pass")

    result = {
        "status" : -1
    }

    if request.method == 'POST':

        print("In update 2")
        print("OLD PASS: ",request.form['old_pass'])
        print("NEW PASS: ",request.form['new_pass'])
        old_pass = request.form['old_pass']
        new_pass = request.form['new_pass']


        print("CU:",current_user)
        sid = current_user.id
        print("sid:",sid)

        staff = Staff.query.filter_by(id=sid).first()
        print("Staff: ",staff)
        staff.email = email
        staff.phone = phone
        staff.f_name = fname
        staff.l_name = surname

        db.session.commit()
        result["status"] = 0
        # flash('You have successfully registered! You may now login.')
        return jsonify(result)

    return jsonify(result)
