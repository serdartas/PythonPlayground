from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, BigInteger, DECIMAL, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import json

def getDBConfig(env):
    with open('config.json') as configFile:
        configData = json.load(configFile)
    
    for config in configData:
        if config["env"] == env:
            dbConfig = config["config"]
            return dbConfig
    
    raise ValueError(f"Can't find the '{env}' environment in configuration")

cfg = getDBConfig("tascloud")
DB_URL = 'mysql+mysqlconnector://' + cfg["user"] + ':' + cfg["password"] + '@' + cfg["server"] + ':' + str(cfg["port"]) + '/' + cfg["database"]


# Create a SQLAlchemy engine
engine = create_engine(DB_URL)

# Create a base class for declarative class definitions
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Define your table classes
class Country(Base):
    __tablename__ = 'Countries'

    CountryId = Column(Integer, primary_key=True, autoincrement=True)
    CountryName = Column(String(255))

    # Define the relationship with the City class
    cities = relationship("City", back_populates="country")
    states = relationship("State", back_populates="country")

    def save(self, session):
        # Check if the country already exists in the database
        existing_country = session.query(Country).filter_by(CountryName=self.CountryName).first()

        if existing_country:
            self.CountryId = existing_country.CountryId
        else:
            session.add(self)
        session.commit()
        return self

class City(Base):
    __tablename__ = 'Cities'

    CityId = Column(Integer, primary_key=True, autoincrement=True)
    CountryId = Column(Integer, ForeignKey('Countries.CountryId'))
    CityName = Column(String(255))

    country = relationship("Country", back_populates="cities")

    def save(self, session):
        # Check if the country already exists in the database
        existing_city = session.query(City).filter_by(CityName=self.CityName, CountryId = self.CountryId).first()

        if existing_city:
            self.CityId = existing_city.CityId
        else:
            session.add(self)
        session.commit()
        return self

class State(Base):
    __tablename__ = 'States'

    StateId = Column(Integer, primary_key=True, autoincrement=True)
    CountryId = Column(Integer, ForeignKey('Countries.CountryId'))
    StateName = Column(String(255))

    country = relationship("Country", back_populates="states")

    def save(self, session):
        # Check if the state already exists in the database
        existing_state = session.query(State).filter_by(StateName=self.StateName, CountryId = self.CountryId).first()

        if existing_state:
            self.StateId = existing_state.StateId
        else:
            session.add(self)
        session.commit()
        return self

class Industry(Base):
    __tablename__ = 'Industries'

    IndustryId = Column(Integer, primary_key=True, autoincrement=True)
    IndustryName = Column(String(255))

    def save(self, session):
        # Check if the state already exists in the database
        existing_industry = session.query(Industry).filter_by(IndustryName=self.IndustryName).first()

        if existing_industry:
            self.IndustryId = existing_industry.IndustryId
        else:
            session.add(self)
        session.commit()
        return self

class Sector(Base):
    __tablename__ = 'Sectors'

    SectorId = Column(Integer, primary_key=True, autoincrement=True)
    SectorName = Column(String(255))

    def save(self, session):
        # Check if the state already exists in the database
        existing_sector = session.query(Sector).filter_by(SectorName=self.SectorName).first()

        if existing_sector:
            self.SectorId = existing_sector.SectorId
        else:
            session.add(self)
        session.commit()
        return self

class Currency(Base):
    __tablename__ = 'Currencies'

    CurrencyId = Column(Integer, primary_key=True, autoincrement=True)
    CurrencyCode = Column(String(3))
    CurrencyName = Column(String(255))

    def save(self, session):
        # Check if the state already exists in the database
        existing_currencuy = session.query(Currency).filter_by(CurrencyName=self.CurrencyName, CurrencyCode=self.CurrencyCode).first()

        if existing_currencuy:
            self.CurrencyId = existing_currencuy.CurrencyId
        else:
            session.add(self)
        session.commit()
        return self

class Exchange(Base):
    __tablename__ = 'Exchanges'

    ExchangeId = Column(Integer, primary_key=True, autoincrement=True)
    CurrencyId = Column(Integer, ForeignKey('Currencies.CurrencyId'))
    ExchangeName = Column(String(50))

    currency = relationship("Currency", back_populates="exchanges")
    companies = relationship("Company", back_populates="exchange")

    def save(self, session):
        # Check if the exchange already exists in the database
        existing_exchange = session.query(Exchange).filter_by(ExchangeName=self.ExchangeName, CurrencyId = self.CurrencyId).first()

        if existing_exchange:
            self.ExchangeId = existing_exchange.ExchangeId
        else:
            session.add(self)
        session.commit()
        return self
    


class Company(Base):
    __tablename__ = 'Companies'

    CompanyId = Column(Integer, primary_key=True, autoincrement=True)
    Ticker = Column(String(4))
    CityId = Column(Integer, ForeignKey('Cities.CityId'))
    StateId = Column(Integer, ForeignKey('States.StateId'))
    IndustryId = Column(Integer, ForeignKey('Industries.IndustryId'))
    BusinessSummary = Column(Text)
    EmployeeCount = Column(Integer)
    SectorId = Column(Integer, ForeignKey('Sectors.SectorId'))
    AuditRisk = Column(Integer)
    BoardRisk = Column(Integer)
    CompensationRisk = Column(Integer)
    ShareholderRisk = Column(Integer)
    OverallRisk = Column(Integer)
    GovernanceEpochDate = Column(Date)
    CurrencyId = Column(Integer, ForeignKey('Currencies.CurrencyId'))
    ExchangeId = Column(Integer, ForeignKey('Exchanges.ExchangeId'))
    HeldPercentInsiders = Column(Float)
    HeldPercentInstitutions = Column(Float)
    TotalShares = Column(BigInteger)
    PublicShares = Column(BigInteger)
    BookValue = Column(DECIMAL(8,2))

    city = relationship("City", back_populates="companies")
    state = relationship("State", back_populates="companies")
    industry = relationship("Industry", back_populates="companies")
    sector = relationship("Sector", back_populates="companies")
    currency = relationship("Currency", back_populates="companies")
    exchange = relationship("Exchange", back_populates="companies")

    def save(self, session):
        # Check if the company already exists in the database
        existing_company = session.query(Company).filter_by(Ticker=self.Ticker, ExchangeId = self.ExchangeId).first()

        if existing_company:
            self.CompanyId = existing_company.CompanyId
        else:
            session.add(self)
        session.commit()
        return self


# Define relationships
## Companies
City.companies = relationship("Company", order_by=Company.CompanyId, back_populates="city")
State.companies = relationship("Company", order_by=Company.CompanyId, back_populates="state")
Industry.companies = relationship("Company", order_by=Company.CompanyId, back_populates="industry")
Sector.companies = relationship("Company", order_by=Company.CompanyId, back_populates="sector")
Currency.companies = relationship("Company", order_by=Company.CompanyId, back_populates="currency")
Exchange.companies = relationship("Company", order_by=Company.CompanyId, back_populates="exchange")
## Exchanges
Currency.exchanges = relationship("Exchange", order_by=Exchange.ExchangeId, back_populates="currency")


# Create the tables in the database (if they don't exist already)
Base.metadata.create_all(engine)

# Helper Functions
def create_city(city_name, country_name):
    country = Country()
    country.CountryName = country_name
    country.save(session)

    city = City()
    city.CityName = city_name
    city.CountryId = country.CountryId
    city.save(session)

    return city

def create_currency(currency_code, currency_name):
    currency = Currency()
    currency.CurrencyName = currency_name
    currency.CurrencyCode = currency_code
    currency.save(session)

    return currency

def create_state(state_name, country_name):
    country = Country()
    country.CountryName = country_name
    country.save(session)

    state = State()
    state.StateName = state_name
    state.CountryId = country.CountryId
    state.save(session)

    return state

def create_exchange(exchange_name, currency_code, currency_name):
    CurrencyId = create_currency(currency_code, currency_name).CurrencyId

    exchange = Exchange()
    exchange.ExchangeName = exchange_name
    exchange.CurrencyId
    exchange.save(session)

    return exchange

def create_industry(industry_name):
    industry = Industry()
    industry.IndustryName = industry_name
    industry.save(session)

    return industry

def create_sector(sector_name):
    sector = Sector()
    sector.SectorName = sector_name
    sector.save(session)

    return sector

