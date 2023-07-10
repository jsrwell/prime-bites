import React from "react";
import Header from "../../components/header/Header";
import "./Home.css";

const Home = () => {
  return (
    <div>
      <Header />
      <main>
        <div className="pt-1 flex bg-m-red first-content">
          <div className="mx-2 pb-3 w-full flex justify-center get-started-bg">
            <div className="get-started flex justify-center items-center">
              <div className="w-4/5 h-4/5 welcome-bg">
                <h1 className="welcome-title">Lorem-ipsum</h1>
                <p className="text-m-white hyphens-auto text-sm sm:text-base md:text-lg overflow-hidden">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                  Mauris sagittis quam non mauris fermentum molestie. Proin
                  dapibus massa ligula, et vestibulum nulla vulputate sit amet.
                </p>
                <div className="flex justify-center items-center st-button-div">
                  <button
                    type="button"
                    className="bg-m-white hover:bg-m-gray rounded-3xl text-m-green font-semibold st-button text-base md:text-xl"
                  >
                    Get started
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="bg-m-white w-full promotions-area">
          <h1 className="ml-10 mt-5 text-3xl font-semibold">Promotions</h1>
          <div className="w-full h-5/6 flex justify-center items-center">
            <div className="bg-m-gray rounded-lg promotion-box w-3/4 h-5/6 flex items-center justify-center">
              <div className="h-2/3 w-4/6 mx-10 flex justify-start space-x-5 overflow-x-auto relative">
                <div className="bg-white">
                  <div className="w-52">card</div>
                </div>
                <div className="bg-white">
                  <div className="w-52">card</div>
                </div>
                <div className=" bg-white">
                  <div className="w-52">card</div>
                </div>
                <div className=" bg-white">
                  <div className="w-52">card</div>
                </div>
                <div className="bg-white">
                  <div className="w-52">card</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Home;
