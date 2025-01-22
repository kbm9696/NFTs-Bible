import streamlit as st



def about():
    # About Section
    st.title("🎨 Real-Time NFT Analytics")
    st.subheader("With Next Prediction Values, API Subscriptions, and Alerts")
    st.markdown("""
    Welcome to Real-Time NFT Analytics! This platform leverages **UnleashNFTs V2 APIs** to provide real-time insights and predictions for the NFT ecosystem.  
    Receive **15m, 30m, and 24h analytics**, tailored insights, and instant alerts via WhatsApp.  
    """)

    # Section Tabs
    tabs = st.tabs(["Blockchains", "Collections", "NFTs", "Marketplaces"])

    # Blockchains Section
    with tabs[0]:
        st.header("🌐 Blockchains")
        st.markdown("""
        Explore performance metrics and predictions for multiple blockchains:
        - **15m**, **30m**, and **24h analytics** for granular data.
        - Real-time **next prediction values** for key blockchain trends.
        """)
        st.write("🚀 **Coming Soon:** More L2 chains!")

    # Collections Section
    with tabs[1]:
        st.header("📂 Collections")
        st.markdown("""
        Dive deep into NFT collections with:
        - **Real-time analytics** tailored to your preferences.
        - Personalized **predictions** for your favorite collections.
        """)
        st.write("🎯 **Coming Soon:** Collection-specific more metrics.")

    # NFTs Section
    with tabs[2]:
        st.header("🖼️ NFTs")
        st.markdown("""
        Stay updated on individual NFTs that matter to you:
        - Performance metrics like trading history and ownership data.
        - **Alerts** for significant market movements.
        """)
        st.write("✨ **Coming Soon:** Real-time NFT data for more metrics")

    # Marketplaces Section
    with tabs[3]:
        st.header("🏪 Marketplaces")
        st.markdown("""
        Analyze top NFT marketplaces with:
        - **Real-time metrics** such as transaction volumes and active users.
        - **Predictions** for marketplace dominance and activity trends.
        """)
        st.write("📈 **Coming Soon:** Comparative insights for OpenSea, Blur, and more!")

    # Footer and Acknowledgment
    st.markdown("---")
    st.markdown("""
    **Acknowledgment**  
    We extend our thanks to **UnleashNFTs V2 APIs** for powering this platform with real-time analytics and predictive capabilities.  
    """)
    st.markdown("**Stay tuned for updates as we unleash the full potential of NFT analytics!**")
