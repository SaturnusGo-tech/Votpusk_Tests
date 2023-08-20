from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.BaseMethods.object_methods import BaseMethods
from selenium.webdriver.common.by import By


class FiltersTrainLocator(BaseMethods):
    FILTERS_CONTAINER = (By.CSS_SELECTOR, '[class="wg-filter__inner"]')
    COST_FIELD_FROM = (By.CSS_SELECTOR, '[class="wg-textinput ga_search_filters_price_min"]')
    COST_FIELD_TO = (By.CSS_SELECTOR, '[class="wg-textinput ga_search_filters_price_max"]')
    ROAD_SCROLLER = (By.CSS_SELECTOR, '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div['
                                      '2]/div[2]/div/div[3]')
    ROAD_SCROLLER_TIME = (
        By.XPATH, '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]')
    ROAD_SCROLLER_ARRIVE = (
        By.XPATH, '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]')

    # Checkboxes
    PLATS_CARD = (By.XPATH,
                  '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div/div[1]/div[2]/label/span[1]')
    COUPE = (By.XPATH,
             '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div/div[1]/div[3]/label/span[1]')
    SEAT_RESERVED = (By.XPATH,
                     '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div/div[1]/div[4]/label/span[1]')
    PUBLIC = (By.XPATH,
              '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div/div[1]/div[5]/label/span[1]')
    PRIORITY = (By.XPATH,
                '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div/div[1]/div[6]/label/span[1]')
    LUX = (By.XPATH,
           '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div/div[1]/div[7]/label/span[1]')

    # Wagon place
    ASIDE_SOFAS = (By.XPATH,
                   '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]/label/span[1]')
    MEN_SOFAS = (By.XPATH,
                 '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div/div[2]/div[3]/label/span[1]')
    DOWN_SOFAS = (By.XPATH,
                  '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div/div[2]/div[4]/label/span[1]')
    FEMAIL_SOFAS = (By.XPATH,
                    '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div/div[2]/div[5]/label/span[1]')
    DOWNSIDE_SOFAS = (By.XPATH,
                      '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div/div[2]/div[6]/label/span[1]')
    PUBLIC_COUPES_SOFAS = (By.XPATH,
                           '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div/div[7]/div[2]/label/span[1]')

    # Rating
    PERFECT = (By.XPATH,
               '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[4]/div[2]/div/div[1]/label/span[1]')
    EXCELLENT = (By.XPATH,
                 '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[4]/div[2]/div/div[2]/label/span[1]')
    GOOD = (By.XPATH,
            '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[4]/div[2]/div/div[3]/label/span[1]')

    # Services
    FOOD_STAFF = (By.XPATH,
                  '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[5]/div[2]/div/div[1]/div[1]/label/span[1]')
    F_P_W_K = (By.XPATH,
               '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[5]/div[2]/div/div[1]/div[2]/label/span[1]')  # Для пассажиров с детьми
    AIR_CONDITIONER = (By.XPATH,
                       '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[5]/div[2]/div/div[1]/div[3]/label/span[1]')
    TV_MEDIA = (By.XPATH,
                '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[5]/div[2]/div/div[1]/div[4]/label/span[1]')
    TV = (By.XPATH,
          '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[5]/div[2]/div/div[1]/div[5]/label/span[1]')
    SANITARY_KIT = (By.XPATH,
                    '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[5]/div[2]/div/div[1]/div[6]/label/span[1]')
    BED_SET = (By.XPATH,
               '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[5]/div[2]/div/div[1]/div[7]/label/span[1]')
    BIO_TOILET = (By.XPATH,
                  '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[5]/div[2]/div/div[2]/div[1]/label/span[1]')
    TRANSFER = (By.XPATH,
                '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[5]/div[2]/div/div[2]/div[2]/label/span[1]')
    PRESS = (By.XPATH,
             '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[5]/div[2]/div/div[2]/div[3]/label/span[1]')
    SPECIAL_SEATS = (By.XPATH,
                     '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[5]/div[2]/div/div[2]/div[4]/label/span[1]')
    PET_TRANSFER = (By.XPATH,
                    '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[5]/div[2]/div/div[2]/div[5]/label/span[1]')
    NO_PET = (By.XPATH,
              '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[5]/div[2]/div/div[2]/div[6]/label/span[1]')
    GUARANTY_CASH_BACK = (By.XPATH,
                          '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[5]/div[2]/div/div[2]/div[7]/label/span[1]')
    NON_REFUNDABLE_TICKET = (By.XPATH,
                             '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[5]/div[2]/div/div[2]/div[8]/label/span[1]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_page_loaded(self, s=2):
        self.page_loaded(FiltersTrainLocator.FILTERS_CONTAINER)
        self.sleep(s)

    def scroll_into_filters_view(self, s=2):
        self.window_scroll_by(0, 700)
        self.sleep(s)

    def assert_filters_container(self, s=2):
        self.is_element_present(FiltersTrainLocator.FILTERS_CONTAINER)
        self.sleep(s)

    def assert_cost_filed_from(self, s=2):
        self.is_element_present(FiltersTrainLocator.COST_FIELD_FROM)
        self.sleep(s)

    def assert_cost_field_to(self, s=2):
        self.is_element_present(FiltersTrainLocator.COST_FIELD_TO)
        self.sleep(s)

    def assert_road_scroller(self, s=2):
        self.is_element_present(FiltersTrainLocator.ROAD_SCROLLER)  # Заменить на скролл
        self.sleep(s)

    def assert_time_scroller(self, s=2):
        self.is_element_present(FiltersTrainLocator.ROAD_SCROLLER_TIME)  # Заменить на скролл
        self.sleep(s)

    def assert_arrive_scroller(self, s=2):
        self.is_element_present(FiltersTrainLocator.ROAD_SCROLLER_ARRIVE)  # Заменить на скролл
        self.sleep(s)

    # CheckBoxes
    def assert_checkboxes_plats_card(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.PLATS_CARD)
        self.sleep(s)

    def assert_checkboxes_coupe(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.COUPE)
        self.sleep(s)

    def assert_checkboxes_seat_reserved(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.SEAT_RESERVED)
        self.sleep(s)

    def assert_checkboxes_public(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.PUBLIC)
        self.sleep(s)

    def assert_checkboxes_priority(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.PRIORITY)
        self.sleep(s)

    def assert_checkboxes_lux(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.LUX)
        self.sleep(s)

    # Places
    def assert_checkboxes_aside(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.ASIDE_SOFAS)
        self.sleep(s)

    def assert_checkboxes_men_coupe(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.MEN_SOFAS)
        self.sleep(s)

    def assert_checkboxes_down_seats(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.DOWN_SOFAS)
        self.sleep(s)

    def assert_checkboxes_female_seats(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.FEMAIL_SOFAS)
        self.sleep(s)

    def assert_checkboxes_upside_side(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.PUBLIC_COUPES_SOFAS)
        self.sleep(s)
        # Rating

    def assert_checkboxes_perfect(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.PERFECT)
        self.sleep(s)

    def assert_checkboxes_excellent(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.EXCELLENT)
        self.sleep(s)

    def assert_checkboxes_good(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.GOOD)
        self.sleep(s)

    # Services
    def assert_checkboxes_food_staff(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.F_P_W_K)
        self.sleep(s)

    def assert_checkboxes_fpwk(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.AIR_CONDITIONER)
        self.sleep(s)

    def assert_checkboxes_air_conditioner(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.TV_MEDIA)
        self.sleep(s)

    def assert_checkboxes_tvmedia(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.TV)
        self.sleep(s)

    def assert_checkboxes_tv(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.SANITARY_KIT)
        self.sleep(s)

    def assert_checkboxes_sanitary_kit(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.BED_SET)
        self.sleep(s)

    def assert_checkboxes_bed_set(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.BIO_TOILET)
        self.sleep(s)

    def assert_checkboxes_bio_toilet(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.TRANSFER)
        self.sleep(s)

    def assert_checkboxes_transfer(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.PRESS)
        self.sleep(s)

    def assert_checkboxes_press(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.SPECIAL_SEATS)
        self.sleep(s)

    def assert_checkboxes_pet_transfer(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.PET_TRANSFER)
        self.sleep(s)

    def assert_checkboxes_no_pets(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.NO_PET)
        self.sleep(s)

    def assert_checkboxes_refundable_ticket(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.GUARANTY_CASH_BACK)
        self.sleep(s)

    def assert_checkboxes_non_refundable_ticket(self, s=2):
        self.assert_element_to_be_clickable(FiltersTrainLocator.NON_REFUNDABLE_TICKET)
        self.sleep(s)
