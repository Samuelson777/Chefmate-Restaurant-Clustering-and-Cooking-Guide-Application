import streamlit as st
import pandas as pd
import pickle
import google.generativeai as genai
from PIL import Image

# Load and preprocess data
@st.cache_data
def load_data():
    df = pd.read_csv('Zomato_cluster_data.csv')
    return df

@st.cache_resource
def load_model():
    with open('kmeans_model.pkl', 'rb') as file:
        kmeans = pickle.load(file)
    with open('onehot_encoder.pkl', 'rb') as file:
        encoder = pickle.load(file)
    return kmeans, encoder

df = load_data()
kmeans, encoder = load_model()

# Function to get response from Google Generative AI using chat
def get_gemini_response(user_question):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        chat = model.start_chat(
            history=[
                {"role": "user", "parts": "Hello"},
                {"role": "model", "parts": "Great to meet you. What would you like to know?"},
            ]
        )
        # Send the user's message to the chat
        response = chat.send_message(user_question)
        
        # Return the response text
        return response.text
    except Exception as e:
        st.error(f"An error occurred while getting the response: {e}")
        return None

# Streamlit UI
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #f0f0f0;  /* Light gray background */
        color: #333;  /* Dark text color */
        font-family: 'Arial', sans-serif;  /* Change font family */
    }
    h1 {
        color: #2c3e50;  /* Dark blue color for the title */
        text-align: center;  /* Center the title */
    }
    .recommendation {
        border: 1px solid #2980b9;  /* Blue border for recommendations */
        border-radius: 10px;  /* Rounded corners */
        padding: 10px;  /* Padding inside the box */
        margin: 10px 0;  /* Margin between boxes */
        background-color: #ffffff;  /* White background for recommendations */
    }
    .chatbot-response {
        border: 1px solid #2980b9;  /* Blue border for chatbot response */
        border-radius: 10px;  /* Rounded corners */
        padding: 10px;  /* Padding inside the box */
        background-color: #ffffff;  /* White background for chatbot response */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍽️ Restaurant Recommendation App")

# Sidebar for navigation
page = st.sidebar.selectbox("Select Page", ["Recommendations", "Map", "Chatbot"])

if page == "Recommendations":
    # Sidebar for inputs
    st.sidebar.header("Search Options")
    cuisine_input = st.sidebar.text_input("Search Cuisines (comma-separated)", placeholder="Type cuisine names...")
    location_input = st.sidebar.selectbox("Select Location", options=df['City'].unique())
    rating_input = st.sidebar.slider("Select Rating", min_value=1.0, max_value=5.0, value=(1.0, 5.0), step=0.1)

    # Button to get recommendations
    if st.sidebar.button("Get Recommendations"):
        if cuisine_input:
            # Split the input into a list of cuisines
            cuisine_list = [cuisine.strip() for cuisine in cuisine_input.split(',') if cuisine.strip()]
            
            # Filter recommendations based on the cuisine input
            recommendations = df[df['City'] == location_input]
            recommendations = recommendations[recommendations['Cuisines'].str.contains('|'.join(cuisine_list), case=False, na=False)]
            
            # Filter recommendations based on the rating input
            recommendations = recommendations[(recommendations['Aggregate_rating'] >= rating_input[0]) & (recommendations['Aggregate_rating'] <= rating_input[1])]
        else:
            recommendations = df[(df['City'] == location_input) & (df['Aggregate_rating'] >= rating_input[0]) & (df['Aggregate_rating'] <= rating_input[1 ])]

        # Reset the index and drop the old index
        recommendations = recommendations.reset_index(drop=True)

        # Count the number of recommendations
        num_recommendations = len(recommendations)

        # Display the count of recommendations
        st.write(f"Number of recommendations found: {num_recommendations}")

        # Check if recommendations DataFrame is empty or if the required columns exist
        if not recommendations.empty and all(col in recommendations.columns for col in ['Restaurant_name', 'Cuisines', 'Aggregate_rating', 'City', 'Average_Cost_for_two', 'Currency']):
            for index, row in recommendations.iterrows():
                st.markdown(f"""
                <div class="recommendation">
                    <h3>{row['Restaurant_name']} 🍴</h3>
                    <p><strong>Cuisines:</strong> {row['Cuisines']}</p>
                    <p><strong>Rating:</strong> {row['Aggregate_rating']} ⭐ 
                    <p><strong>Location:</strong> {row['City']}</p>
                    <p><strong>Average Cost for Two:</strong> {row['Average_Cost_for_two']} {row['Currency']}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.write("No recommendations found. Please try different cuisines or check the input.")

elif page == "Map":
    st.sidebar.header("Restaurant Map")
    
    # Check if latitude and longitude columns exist in the DataFrame
    if 'Latitude' in df.columns and 'Longitude' in df.columns:
        st.markdown("<h2 style='text-align: center;'>Restaurant Locations on Map</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Explore the locations of restaurants in your selected city.</p>", unsafe_allow_html=True)

        # Rename the Latitude column to 'lat' and Longitude column to 'lon'
        map_data = df[['Restaurant_name', 'Latitude', 'Longitude']].rename(columns={'Latitude': 'lat', 'Longitude': 'lon'})
        
        # Display the map with a title
        st.markdown("<h3 style='text-align: center;'>All Restaurants</h3>", unsafe_allow_html=True)
        st.map(map_data)

        # Create a selection box for restaurant names
        selected_restaurant = st.selectbox("Select a restaurant to see details:", options=df['Restaurant_name'].unique())
        
        # Display details of the selected restaurant
        if selected_restaurant:
            restaurant_info = df[df['Restaurant_name'] == selected_restaurant].iloc[0]
            st.markdown(f"""
            <div class="recommendation">
                <h3>{restaurant_info['Restaurant_name']} 🍴</h3>
                <p><strong>Cuisines:</strong> {restaurant_info['Cuisines']}</p>
                <p><strong>Rating:</strong> {restaurant_info['Aggregate_rating']} ⭐</p>
                <p><strong>Location:</strong> {restaurant_info['City']}</p>
                <p><strong>Average Cost for Two:</strong> {restaurant_info['Average_Cost_for_two']} {restaurant_info['Currency']}</p>
            </div>
            """, unsafe_allow_html=True)

            # Create a DataFrame for the selected restaurant
            selected_restaurant_data = pd.DataFrame({
                'lat': [restaurant_info['Latitude']],
                'lon': [restaurant_info['Longitude']]
            })

            # Display the map with the selected restaurant
            st.markdown("<h3 style='text-align: center;'>Selected Restaurant Location</h3>", unsafe_allow_html=True)
            st.map(selected_restaurant_data)
    else:
        st.write("Latitude and Longitude data is not available in the dataset.")

elif page == "Chatbot":
    st.sidebar.header("Chatbot")
    
    # Input for API key
    api_key = st.sidebar.text_input("Enter your Google Generative AI API Key:", type="password")
    
    user_question = st.sidebar.text_input("Ask a cooking-related question:")
    
    if st.sidebar.button("Ask "):
        # Check if API key is provided
        if not api_key:
            st.write("Please enter your API key to use the chatbot.")
        else:
            # Configure the Google Generative AI API with the user-provided API key
            genai.configure(api_key=api_key)

            # Define cooking-related keywords
            cooking_keywords = ['recipe', 'cook', 'cooking', 'ingredient', 'bake', 'fry', 'grill', 'boil', 'sauté', 'meal', 'dish', 'food', 'prepare']

            # Check if the user question contains any cooking-related keywords
            if any(keyword in user_question.lower() for keyword in cooking_keywords):
                with st.spinner("Getting response..."):
                    try:
                        response = get_gemini_response(user_question)
                        # Define a default response message
                        default_response = "I'm sorry, but I couldn't find an answer to your question. Please try asking something else related to cooking."

                        # Check if response is not empty
                        if response:  # Ensure response is not empty
                            # Display the response in a basic format with bold heading
                            st.write("**Chatbot Response:**")
                            st.write(response)
                        else:
                            # Display the default response if the response is empty
                            st.write("**No Response Found:**")
                            st.write(default_response)
                    except Exception as e:
                        st.write(f"An error occurred: {e}")
            else:
                st.write("Please ask a cooking-related question.")