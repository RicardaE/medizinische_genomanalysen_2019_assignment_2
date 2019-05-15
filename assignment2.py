#! /usr/bin/env python3

import vcf

__author__ = 'Ricarda Erhart'


class Assignment2:

    def __init__(self):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)


    def get_average_quality_of_file(self):
        vcf_reader = vcf.Reader(open('chr22_new.vcf', 'r'))
        SumQuality = 0
        vcfs = 0
        for entry in vcf_reader:
            SumQuality += entry.QUAL
            vcfs += 1
        AverageQuality = SumQuality / vcfs
        print('Average Quality of File: ', "{:.2f}".format(AverageQuality))



    def get_total_number_of_variants_of_file(self):
        vcf_reader = vcf.Reader(open('chr22_new.vcf', 'r'))
        vcfs = 0
        for entry in vcf_reader:
            vcfs += 1
        print('Number of Variants in File: ', vcfs)


    def get_variant_caller_of_vcf(self):
        vcf_reader = vcf.Reader(open('chr22_new.vcf', 'r'))
        callers = []
        for entry in vcf_reader:
            caller = entry.INFO['callsetnames']
            for i in caller:
                if i not in callers:
                    callers.append(i)
        callers.remove('')
        print('Variant Callers: ', callers)


    def get_human_reference_version(self):
        vcf_reader = vcf.Reader(open('chr22_new.vcf', 'r'))
        HumanReferenceVersion = []
        for entry in vcf_reader:
            if 'difficultregion' in entry.INFO.keys():
                for i in entry.INFO['difficultregion']:
                    if i not in HumanReferenceVersion:
                        HumanReferenceVersion.append(i)
        print('Human Reference Version: ', HumanReferenceVersion)


    def get_number_of_indels(self):
        vcf_reader = vcf.Reader(open('chr22_new.vcf', 'r'))
        indel = 0
        for entry in vcf_reader:
            if entry.is_indel == True:
                indel += 1
        print('Number of INDELs: ', indel)


    def get_number_of_snvs(self):
        vcf_reader = vcf.Reader(open('chr22_new.vcf', 'r'))
        snp = 0
        for entry in vcf_reader:
            if entry.is_snp == True:
                snp += 1
        print('Number of SNVs: ', snp)

    def get_number_of_heterozygous_variants(self):
        vcf_reader = vcf.Reader(open('chr22_new.vcf', 'r'))
        HeterozygousVariants = 0
        for entry in vcf_reader:
            if entry.num_het != 0:
                HeterozygousVariants += 1
        print('Number of heterozygous variants: ', HeterozygousVariants)


    def merge_chrs_into_one_vcf(self):
        File1=open('chr21_new.vcf', 'r')
        File2=open('chr22_new.vcf', 'r')
        File12=open('chr2122_new.vcf', 'w')
        LinesInFile2=File2.readlines()
        LineNumberOfFile2=0
        NumberOfEntrys=0
        MergeHeaderSuccess = True
        for LineInFile1 in File1:
            if LineInFile1[0] == '#':
                if LineInFile1 == LinesInFile2[LineNumberOfFile2]:
                    File12.write(LineInFile1)
                    LineNumberOfFile2 += 1
                else:
                    MergeHeaderSuccess == False
                    print("headers not the same, can not merge vcfs")
                    break
            else:
                File12.write(LineInFile1)
                NumberOfEntrys += 1
        if MergeHeaderSuccess == True:
            for LineInFile2 in LinesInFile2:
                if LineInFile2[0] != '#':
                    File12.write(LineInFile2)
                    NumberOfEntrys += 1
        if MergeHeaderSuccess == True:
            print("Files merged. Total number of variants: ", NumberOfEntrys)
        File1.close()
        File2.close()
        File12.close()

    def print_summary(self):
        print("Print all results here")
        self.get_average_quality_of_file()
        self.get_total_number_of_variants_of_file()
        self.get_variant_caller_of_vcf()
        self.get_human_reference_version()
        self.get_number_of_indels()
        self.get_number_of_snvs()
        self.get_number_of_heterozygous_variants()
        self.merge_chrs_into_one_vcf()



def main():
    print("Assignment 2")
    assignment2 = Assignment2()
    assignment2.print_summary()
    print("Done with assignment 2")


if __name__ == '__main__':
    main()
