SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema financeDB
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema financeDB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS financeDB ;
USE financeDB ;

-- -----------------------------------------------------
-- Table financeDB.Countries
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS financeDB.Countries (
  CountryId TINYINT NOT NULL AUTO_INCREMENT,
  CountryName VARCHAR(255) NULL,
  PRIMARY KEY (CountryId))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table financeDB.Cities
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS financeDB.Cities (
  CityId SMALLINT NOT NULL AUTO_INCREMENT,
  CountryId TINYINT NULL,
  CityName VARCHAR(255) NULL,
  PRIMARY KEY (CityId),
  CONSTRAINT FK_Country_Cities
    FOREIGN KEY (CountryId)
    REFERENCES financeDB.Countries (CountryId)
    )
ENGINE = InnoDB;

CREATE INDEX IF NOT EXISTS FK_Country_Cities_idx ON Cities (CountryId ASC);
-- -----------------------------------------------------
-- Table financeDB.States
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS financeDB.States (
  StateId SMALLINT NOT NULL AUTO_INCREMENT,
  CountryId TINYINT NULL,
  StateName VARCHAR(255) NULL,
  PRIMARY KEY (StateId),
  INDEX fk_States_Countries_idx (CountryId ASC),
  CONSTRAINT fk_States_Countries
    FOREIGN KEY (CountryId)
    REFERENCES financeDB.Countries (CountryId))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table financeDB.Industries
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS financeDB.Industries (
  IndustryId SMALLINT NOT NULL AUTO_INCREMENT,
  IndustryName VARCHAR(255) NOT NULL,
  PRIMARY KEY (IndustryId))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table financeDB.Sectors
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS financeDB.Sectors (
  SectorId SMALLINT NOT NULL AUTO_INCREMENT,
  SectorName VARCHAR(255) NULL,
  PRIMARY KEY (SectorId))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table financeDB.Currencies
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS financeDB.Currencies (
  CurrencyId TINYINT NOT NULL AUTO_INCREMENT,
  CurrencyCode CHAR(3) NOT NULL,
  CurrencyName VARCHAR(255) NOT NULL,
  PRIMARY KEY (CurrencyId))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table financeDB.Companies
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS financeDB.Companies (
  CompanyId SMALLINT NOT NULL AUTO_INCREMENT,
  Ticker CHAR(4) NOT NULL,
  CityId SMALLINT NOT NULL,
  StateId SMALLINT NULL,
  IndustryId SMALLINT NULL,
  BusinessSummary LONGTEXT NULL,
  EmployeeCount INT NULL,
  SectorId SMALLINT NULL,
  AuditRisk TINYINT NULL,
  BoardRisk TINYINT NULL,
  CompensationRisk TINYINT NULL,
  ShareholderRisk TINYINT NULL,
  OverallRisk TINYINT NULL,
  GovernanceEpochDate DATE NULL,
  CurrencyId TINYINT NULL,
  HeldPercentInsiders FLOAT NULL,
  HeldPercentInstitutions FLOAT NULL,
  TotalShares BIGINT NULL,
  PublicShares BIGINT NULL,
  BookValue DECIMAL(8,2) NULL,
  PRIMARY KEY (CompanyId),
  INDEX fk_Companies_Cities_idx (CityId ASC),
  INDEX fk_Companies_States_idx (StateId ASC),
  INDEX fk_Companies_Industries_idx (IndustryId ASC),
  INDEX fk_Companies_Sectors_idx (SectorId ASC),
  INDEX fk_Companies_Currencies_idx (CurrencyId ASC),
  CONSTRAINT fk_Companies_Cities FOREIGN KEY (CityId) REFERENCES financeDB.Cities (CityId),
  CONSTRAINT fk_Companies_States FOREIGN KEY (StateId) REFERENCES financeDB.States (StateId),
  CONSTRAINT fk_Companies_Industries FOREIGN KEY (IndustryId) REFERENCES financeDB.Industries (IndustryId),
  CONSTRAINT fk_Companies_Sectors FOREIGN KEY (SectorId) REFERENCES financeDB.Sectors (SectorId),
  CONSTRAINT fk_Companies_Currencies FOREIGN KEY (CurrencyId) REFERENCES financeDB.Currencies (CurrencyId))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
