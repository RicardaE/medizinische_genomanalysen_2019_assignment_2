#! /usr/bin/env python3

import vcf

__author__ = 'Ricarda Erhart'


class Assignment2:

    def __init__(self):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)


    def get_average_quality_of_file(self):
        vcf_reader = vcf.Reader(open('chr22_new.vcf', 'r'))
        sumqual=0
        vcfs=0
        for entry in vcf_reader:
            sumqual+=entry.QUAL
            vcfs+=1
        average=sumqual/vcfs
        print('Average Quality of File: ', average)



    def get_total_number_of_variants_of_file(self):
        vcf_reader = vcf.Reader(open('chr22_new.vcf', 'r'))
        vcfs=0
        for entry in vcf_reader:
            vcfs+=1
        print('Number of Variants in File: ', vcfs)


    def get_variant_caller_of_vcf(self):
        vcf_reader = vcf.Reader(open('chr22_new.vcf', 'r'))
        callers=[]
        for entry in vcf_reader:
            c = entry.INFO['callsetnames']
            for i in c:
                if i not in callers:
                    callers.append(i)
        callers.remove('')
        print('Variant Callers: ', callers)


    def get_human_reference_version(self):
        #difficultregion=AllRepeats_lt51bp_gt95identity_merged,hg38_self_chain_withalts_gt10k
        '''
        Return the genome reference version
        :return:
        '''
        print("TODO")


    def get_number_of_indels(self):
        vcf_reader = vcf.Reader(open('chr22_new.vcf', 'r'))
        indel=0
        for entry in vcf_reader:
            if entry.is_indel == True:
                indel+=1
        print('Number of INDELs: ', indel)


    def get_number_of_snvs(self):
        vcf_reader = vcf.Reader(open('chr22_new.vcf', 'r'))
        snp=0
        for entry in vcf_reader:
            if entry.is_snp == True:
                snp+=1
        print('Number of SNVs: ', snp)

    def get_number_of_heterozygous_variants(self):
        vcf_reader = vcf.Reader(open('chr22_new.vcf', 'r'))
        het=0
        for entry in vcf_reader:
            if entry.num_het != 0:
                het+=1
        print('Number of heterozygous variants: ', het)


    def merge_chrs_into_one_vcf(self):
        '''
        Creates one VCF containing all variants of chr21 and chr22
        :return:
        '''
        print("TODO")

        print("Number of total variants")


    def print_summary(self):
        print("Print all results here")
        self.get_average_quality_of_file()
        self.get_total_number_of_variants_of_file()
        self.get_variant_caller_of_vcf()
        #self.get_human_reference_version()
        self.get_number_of_indels()
        self.get_number_of_snvs()
        self.get_number_of_heterozygous_variants()
        #self.merge_chrs_into_one_vcf()



def main():
    print("Assignment 2")
    assignment2 = Assignment2()
    assignment2.print_summary()
    print("Done with assignment 2")


if __name__ == '__main__':
    main()
