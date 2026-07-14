#app_data for storing all variables
#i got this from internet search.  This has prefilled data which i don't want.
#employee address should already be what they entered on the 1040.

w2_data={}


app_data = {
    "personal_info":{
        "name":"",
        "address":"",
        "spouse":""
    },
    "filing_status":{
        "single":"",
        "married_joint":"",
        "married_separate":"",
        "spouse_ssn":"",
        "head_household":"",
        "qual_surviving_spouse":"",
        "child_name":"",
        "alien_a_spouse":"",
        "alien_spouse_name":""
    },
    "dependents":[
        {
            "name":"", 
            "ssn":"", 
            "relationship":"", 
            "live_with_filer":"",
            "live_in_US":"",
            "full_time_student":"",
            "disabled":"",
            "child_tax_credit":"",
            "credit_for_other_dep":""
        },
         {
            "name":"", 
            "ssn":"", 
            "relationship":"", 
            "live_with_filer":"",
            "live_in_US":"",
            "full_time_student":"",
            "disabled":"",
            "child_tax_credit":"",
            "credit_for_other_dep":""
        },
         {
            "name":"", 
            "ssn":"", 
            "relationship":"", 
            "live_with_filer":"",
            "live_in_US":"",
            "full_time_student":"",
            "disabled":"",
            "child_tax_credit":"",
            "credit_for_other_dep":""
        },
         {
            "name":"", 
            "ssn":"", 
            "relationship":"", 
            "live_with_filer":"",
            "live_in_US":"",
            "full_time_student":"",
            "disabled":"",
            "child_tax_credit":"",
            "credit_for_other_dep":""
        }

    ],
    "1a_total_amount_w2_line_1":{
        "w2_1" :w2_data,
        "w2_2": w2_data,
        "w2_3": w2_data,
        "w2_4": w2_data
    },
    "1b_household_employee_wages":"",
    "1c_tip_income":"",
    "1d_medicaid_waiver_payments":"",
    "1e_taxable_dependent_care_benefits":"",
    "1f_adoption_benefits":"",
    "1g_wages_form_8919":"",
    "1h_other_earned_income_type":"",
    "1h_other_earned_income_amount":"",
    "1i_nontaxable_combat_pay":"",
    "2a_tax_exempt_interest":"",
    "2b_taxable_interest":"",
    "3a_qualified_dividends":"",
    "3b_ordinary_dividends":"",
    "3c1_child_dividends_in_3a":"",
    "3c2_child_dividends_in_3b":"",
    "4a_ira_distributions":"",
    "4b_taxable_amount_of_4a":"",
    "4c1_is_rollover":"",
    "4c2_is_QCD":"",
    "4c3":"",
    "5a_pensions_annuities":"",
    "5b_taxable_amount_5a":"",
    "5c1_is_rollover":"",
    "5c2_is_PSO":"",
    "5c3":"",
    "6a_social_security_benefits":"",
    "6b_taxable_amont_6a":"",
    "6c_lump_sum_method":"",
    "6d_married_filing_separately_lived_apart":"",
    "7a_capital_gain_or_loss":"",
    "7b1_scheduleD_not_required":"",
    "7b2_includes_child_capital_gain_or_loss":"",  
    "8_additional_income_schedule_1_Line_10":"",
    "9_total_income":"", 
    "10_adjustments_to_income_schedule_1_Line_26":"",
    "11a_adjusted_gross_income":"",
    "11b_same_as_11a":"",
    "12a1_someone_can_claim_you_as_dependent":"",
    "12a2_someone_can_claim_spouse_as_dependent":"",
    "12b_spouse_itemizes_separate_return":"",
    "12c_you_dual_status_alien":"",
    "12d1_you_born_after_Jan_2_1961":"",
    "12d2_you_are_blind":"",
    "12d3_spouse_born_after_Jan_2_1961":"",
    "12d4_spouse_is_blind":"",
    "13a_qualified_business_income_deduction":"",
    "13b_additional_deductions_schedule_1A":"",
    "14":"",
    "15":"",
    "16_tax":"",
    "16_1_form_8814":"",
    "16_2_form_4972":"",
    "16_3_form_other":"",
    "17_schedule_2_line_3":"",
    "18":"",
    "19_child_tax_credit_schedule_8812":"",
    "20_schedule_3_line_8":"",
    "21":"",
    "22":"",
    "23_other_taxes_schedule_2_line_21":"",
    "24_total_tax":"",
    "25a_income_tax_witheld_from_W2":"",
    "25b_forms_1099":"",
    "25c_other_forms":"",
    "25d":"",
    "26_estimated_tax_payments_and_amount_from_prior_year":"",
    "26_made_estimated_payment_with_former_spouse":"",
    "27a_earned_income_credit":"",
    "27b_clergy_filing_schedule_SE":"",
    "27c_do_not_want_to_claim_EIC":"",
    "28_entry_value_additional_child_tax_credit_form_8812":"",
    "28_check_if_you_dont_want_to_claim":"",
    "29_american_oppportunity_credit":"",
    "30_refundable_adoption_credit":"",
    "31_schedule_3_line_15":"",
    "32_total_other_payments_refundable_credits":"",
    "33_total_payments":"",
    "34_amount_overpaid":"",
    "35a_amount_of_overpayment_refund":"",
    "35b_bank_routing_number":"",
    "35c_bank_type_of_account":"",
    "35d_bank_account_number":"",
    "36_amount_to_apply_to_next_year_estimated_tax":"",
    "37_amount_you_owe":"",
    "38_estimated_tax_penalty":""





}



w2_data = {
    "employee": {
        "ssn": "",
        "first_name": "",
        "middle_initial": "",
        "last_name": "",
        "address": ""
    },
    "employer": {
        "ein": "",
        "name": "",
        "address": "",
        "control_number": ""
    },
    "federal": {
        "box_1_wages": "",
        "box_2_federal_tax_withheld": "",
        "box_3_social_security_wages": "",
        "box_4_social_security_tax_withheld": "",
        "box_5_medicare_wages_and_tips": "",
        "box_6_medicare_tax_withheld": "",
        "box_7_social_security_tips": "",
        "box_8_allocated_tips": "",
        "box_10_dependent_care_benefits": "",
        "box_11_nonqualified_plans": "",
        "box_13_statutory_employee": "",
        "box_13_retirement_plan": "",
        "box_13_third_party_sick_pay": "",
    },
    "box_12_codes": [
        {"code": "", "amount": ""},
        {"code": "", "amount": ""},
        {"code": "", "amount":""},
        {"code": "", "amount":""},
        {"code": "", "amount": ""}
    ],
    "box_14_other": [
        {"description": "", "amount": ""},
        {"description": "", "amount": ""},
        {"description": "", "amount": ""},
        {"description": "", "amount": ""}
    ],
    "state_and_local": [
        {
            "box_15_state": "",
            "box_15_employer_state_id": "",
            "box_16_state_wages": "",
            "box_17_state_tax_withheld": "",
            "box_18_local_wages": "",
            "box_19_local_tax_withheld": "",
            "box_20_locality_name": ""
        }
    ]
}