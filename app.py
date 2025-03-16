import streamlit as st
import password_strength


st.title("🔐Password Strength Checker 👀")

#Ask user to enter password
password  = st.text_input("Enter your Password: ")
# score, messages = password_strength.check_password_strength(password)

if password:
    score, feedback = password_strength.check_password_strength(password)

    if score == 5:
        st.success("✅ Strong Password!")
        st.write("Your password meets all criteria for a strong password.")
        st.write("A strong password should:")
        st.write("✅ Be at least 8 characters long")
        st.write("✅ Contain uppercase & lowercase letters")
        st.write("✅ Include at least one digit (0-9)")
        st.write("✅ Have one special character (!@#$%^&*)")
        
    elif score == 4:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
        st.write("Ensure you meet all criteria for a strong password.")
    else:
        st.error("❌ Weak Password! Improve it using these tips:")
        for msg in feedback:
            st.write(msg)
        st.subheader("Generate a strong Password: ")
        # length = st.number_input("Enter the length of password: ", min_value=8)
        if st.button("Generate"):
                result = password_strength.password_generator(12)  
                st.success(f"Here is your strong Password {result}") 
           
        
        