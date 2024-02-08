import streamlit as st
import random

class DebitCard:
    def __init__(self, card_number, pin, balance=0):
        self.card_number = card_number
        self.pin = pin
        self.balance = balance

def main():
    if 'debit_card' not in st.session_state:
        st.session_state.debit_card = None

    st.title("Debit Card System")

    if st.session_state.debit_card is None:
        card_number = st.text_input("Enter your debit card number (16 digits):")
        while not card_number.isdigit() or len(card_number) != 16:
            card_number = st.text_input("Invalid input. Please enter 16-digit debit card number:")

        pin = st.text_input("Set your card PIN (6 digits):", type="password")
        while not pin.isdigit() or len(pin) != 6:
            pin = st.text_input("Invalid input. Please enter 6-digit PIN:", type="password")

        st.session_state.debit_card = DebitCard(card_number, pin)

    forget_details = st.button('Forget Details')
    if forget_details:
        st.session_state.debit_card = None

    if st.session_state.debit_card:
        for _ in range(3):
            entered_pin = st.text_input("Verify your card PIN:", type="password")
            if entered_pin == st.session_state.debit_card.pin:
                st.success("PIN accepted.")
                break
            else:
                st.error("Invalid PIN.")

        else:
            st.error("Your card is blocked. Please contact your card provider.")
            st.session_state.debit_card = None
            return

        initial_money = random.randint(10, 100) * 1000  # Random amount between Rs. 10,000 and Rs. 100,000
        st.session_state.debit_card.balance += initial_money

        st.write(f"Your current balance is: Rs. {st.session_state.debit_card.balance}")

        for _ in range(3):
            amount = st.number_input("Enter the amount you want to withdraw:", min_value=0.01)
            if amount > st.session_state.debit_card.balance:
                st.error("Insufficient funds. Please try again with a lower amount.")
                continue

            st.session_state.debit_card.balance -= amount
            st.success(f"You withdrew Rs. {amount}. Your new balance is: Rs. {st.session_state.debit_card.balance}")
            break

if __name__ == "__main__":
    main()
