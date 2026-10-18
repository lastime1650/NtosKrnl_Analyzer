# CmpQueryKeyDataFromNode

- RVA: `0x0084EAE0`–`0x0084F196` (길이 `1,718` bytes)
- VA: `0x000000014084EAE0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069CC8`
- 디코드: `400`개 명령, `1,718/1,718` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0084EB1A` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x0084EBFA` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0084EC4D` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0084ED05` → [CmGetVisibleMaxValueNameLenAndDataLen](../9E/CmGetVisibleMaxValueNameLenAndDataLen_function_009EB750.md) (function, `0x009EB750`)
- `0x0084ED1E` → [CmGetVisibleSubkeyCount](CmGetVisibleSubkeyCount_function_00849D74.md) (function, `0x00849D74`)
- `0x0084ED30` → [CmGetVisibleValueCount](../9F/CmGetVisibleValueCount_function_009F6B24.md) (function, `0x009F6B24`)
- `0x0084ED74` → [CmpPopulateKeyFullInformation](../A3/CmpPopulateKeyFullInformation_function_00A3C0EC.md) (function, `0x00A3C0EC`)
- `0x0084EDE4` → [CmGetKeyLastWriteTime](CmGetKeyLastWriteTime_function_0084E200.md) (function, `0x0084E200`)
- `0x0084EE0C` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0084EE9C` → [CmpCopyCompressedName](CmpCopyCompressedName_function_0084E0D0.md) (function, `0x0084E0D0`)
- `0x0084EEEA` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0084EEFF` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0084EF41` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0084EF4B` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0084EF6A` → [CmListGetNextElement](../../pagecmrc/BC/CmListGetNextElement_function_00BC9940.md) (function, `0x00BC9940`)
- `0x0084EF84` → [CmEqualTrans](CmEqualTrans_function_0084BF60.md) (function, `0x0084BF60`)
- `0x0084EFB4` → [CmpIsKeyDeleted](CmpIsKeyDeleted_function_0084BDB0.md) (function, `0x0084BDB0`)
- `0x0084EFE2` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0084F029` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0084F06E` → [CmEqualTrans](CmEqualTrans_function_0084BF60.md) (function, `0x0084BF60`)
- `0x0084F0DA` → [CmEqualTrans](CmEqualTrans_function_0084BF60.md) (function, `0x0084BF60`)
- `0x0084F142` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0084F154` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0084F166` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0084F180` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)

### Direct callers
- [sub_0084E4B5](Unknown_function_0084E4B5.md) at `0x0084E725`
- [CmQueryKey](../85/CmQueryKey_function_00858240.md) at `0x00858518`
- [CmpQueryKeyData](../85/CmpQueryKeyData_function_00858E70.md) at `0x00858F26`
- [CmpEnumerateLayeredKey](../94/CmpEnumerateLayeredKey_function_00945E58.md) at `0x00946341`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x0084EBFA` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0084EEEA` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0084EEFF` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0084EF6A` → [CmListGetNextElement](../../pagecmrc/BC/CmListGetNextElement_function_00BC9940.md) (`PAGE` → `PAGECMRC`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0084EAE0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0084EAE5  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0084EAEA  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0084EAEF  57                              push rdi
0084EAF0  41 54                           push r12
0084EAF2  41 55                           push r13
0084EAF4  41 56                           push r14
0084EAF6  41 57                           push r15
0084EAF8  48 81 EC A0 00 00 00            sub rsp, 0xa0
0084EAFF  49 8B F1                        mov rsi, r9
0084EB02  48 8B FA                        mov rdi, rdx
0084EB05  4C 8B E9                        mov r13, rcx
0084EB08  45 33 F6                        xor r14d, r14d
0084EB0B  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
0084EB10  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
0084EB15  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0084EB1A  E8 F1 73 00 00                  call 0x140855f10
0084EB1F  0F 57 C0                        xorps xmm0, xmm0
0084EB22  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
0084EB27  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
0084EB2C  0F 11 84 24 80 00 00 00         movups xmmword ptr [rsp + 0x80], xmm0
0084EB34  41 83 F8 02                     cmp r8d, 2
0084EB38  0F 84 35 01 00 00               je 0x14084ec73
0084EB3E  45 85 C0                        test r8d, r8d
0084EB41  0F 85 83 02 00 00               jne 0x14084edca
0084EB47  45 8B E6                        mov r12d, r14d
0084EB4A  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
0084EB52  48 85 D2                        test rdx, rdx
0084EB55  0F 85 5D 02 00 00               jne 0x14084edb8
0084EB5B  48 8B 98 A8 00 00 00            mov rbx, qword ptr [rax + 0xa8]
0084EB62  4C 8B BC 24 08 01 00 00         mov r15, qword ptr [rsp + 0x108]
0084EB6A  4D 85 FF                        test r15, r15
0084EB6D  0F 85 2B 05 00 00               jne 0x14084f09e
0084EB73  0F B7 57 48                     movzx edx, word ptr [rdi + 0x48]
0084EB77  0F B7 CA                        movzx ecx, dx
0084EB7A  66 03 C9                        add cx, cx
0084EB7D  F6 47 02 20                     test byte ptr [rdi + 2], 0x20
0084EB81  66 0F 44 CA                     cmove cx, dx
0084EB85  0F B7 D1                        movzx edx, cx
0084EB88  44 8D 62 10                     lea r12d, [rdx + 0x10]
0084EB8C  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
0084EB94  44 89 20                        mov dword ptr [rax], r12d
0084EB97  44 8B BC 24 F0 00 00 00         mov r15d, dword ptr [rsp + 0xf0]
0084EB9F  41 83 FF 10                     cmp r15d, 0x10
0084EBA3  72 67                           jb 0x14084ec0c
0084EBA5  48 89 1E                        mov qword ptr [rsi], rbx
0084EBA8  44 89 76 08                     mov dword ptr [rsi + 8], r14d
0084EBAC  89 56 0C                        mov dword ptr [rsi + 0xc], edx
0084EBAF  45 8D 47 F0                     lea r8d, [r15 - 0x10]
0084EBB3  F6 47 02 20                     test byte ptr [rdi + 2], 0x20
0084EBB7  74 2F                           je 0x14084ebe8
0084EBB9  0F B7 47 48                     movzx eax, word ptr [rdi + 0x48]
0084EBBD  44 89 74 24 58                  mov dword ptr [rsp + 0x58], r14d
0084EBC2  41 D1 E8                        shr r8d, 1
0084EBC5  44 3B C0                        cmp r8d, eax
0084EBC8  44 0F 43 C0                     cmovae r8d, eax
0084EBCC  41 8B C6                        mov eax, r14d
0084EBCF  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
0084EBD3  41 3B C0                        cmp eax, r8d
0084EBD6  73 27                           jae 0x14084ebff
0084EBD8  8B D0                           mov edx, eax
0084EBDA  0F B6 4C 3A 4C                  movzx ecx, byte ptr [rdx + rdi + 0x4c]
0084EBDF  66 89 4C 56 10                  mov word ptr [rsi + rdx*2 + 0x10], cx
0084EBE4  FF C0                           inc eax
0084EBE6  EB E7                           jmp 0x14084ebcf
0084EBE8  44 3B C2                        cmp r8d, edx
0084EBEB  41 0F 46 D0                     cmovbe edx, r8d
0084EBEF  44 8B C2                        mov r8d, edx
0084EBF2  48 8D 57 4C                     lea rdx, [rdi + 0x4c]
0084EBF6  48 8D 4E 10                     lea rcx, [rsi + 0x10]
0084EBFA  E8 41 7C E7 FF                  call 0x1406c6840
0084EBFF  45 3B FC                        cmp r15d, r12d
0084EC02  73 0E                           jae 0x14084ec12
0084EC04  41 BE 05 00 00 80               mov r14d, 0x80000005
0084EC0A  EB 06                           jmp 0x14084ec12
0084EC0C  41 BE 23 00 00 C0               mov r14d, 0xc0000023
0084EC12  44 89 74 24 40                  mov dword ptr [rsp + 0x40], r14d
0084EC17  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0084EC1C  EB 14                           jmp 0x14084ec32
0084EC1E  44 8B F0                        mov r14d, eax
0084EC21  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0084EC25  4C 8B AC 24 D0 00 00 00         mov r13, qword ptr [rsp + 0xd0]
0084EC2D  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0084EC32  48 85 DB                        test rbx, rbx
0084EC35  74 1B                           je 0x14084ec52
0084EC37  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
0084EC3C  49 8B CD                        mov rcx, r13
0084EC3F  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
0084EC47  0F 85 FE 02 00 00               jne 0x14084ef4b
0084EC4D  E8 EE 72 00 00                  call 0x140855f40
0084EC52  41 8B C6                        mov eax, r14d
0084EC55  4C 8D 9C 24 A0 00 00 00         lea r11, [rsp + 0xa0]
0084EC5D  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0084EC61  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
0084EC65  49 8B E3                        mov rsp, r11
0084EC68  41 5F                           pop r15
0084EC6A  41 5E                           pop r14
0084EC6C  41 5D                           pop r13
0084EC6E  41 5C                           pop r12
0084EC70  5F                              pop rdi
0084EC71  C3                              ret
0084EC72  CC                              int3
0084EC73  49 8B C6                        mov rax, r14
0084EC76  4C 8B BC 24 00 01 00 00         mov r15, qword ptr [rsp + 0x100]
0084EC7E  48 85 FF                        test rdi, rdi
0084EC81  0F 85 17 01 00 00               jne 0x14084ed9e
0084EC87  49 8B 9F A8 00 00 00            mov rbx, qword ptr [r15 + 0xa8]
0084EC8E  4C 8B A4 24 08 01 00 00         mov r12, qword ptr [rsp + 0x108]
0084EC96  4D 85 E4                        test r12, r12
0084EC99  0F 85 94 03 00 00               jne 0x14084f033
0084EC9F  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
0084ECA4  44 89 74 24 68                  mov dword ptr [rsp + 0x68], r14d
0084ECA9  4C 89 B4 24 90 00 00 00         mov qword ptr [rsp + 0x90], r14
0084ECB1  B8 FF FF FF FF                  mov eax, 0xffffffff
0084ECB6  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0084ECBA  44 89 74 24 3C                  mov dword ptr [rsp + 0x3c], r14d
0084ECBF  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
0084ECC4  48 85 FF                        test rdi, rdi
0084ECC7  0F 85 2F 04 00 00               jne 0x14084f0fc
0084ECCD  4D 85 FF                        test r15, r15
0084ECD0  74 15                           je 0x14084ece7
0084ECD2  41 0F B7 9F B0 00 00 00         movzx ebx, word ptr [r15 + 0xb0]
0084ECDA  89 5C 24 78                     mov dword ptr [rsp + 0x78], ebx
0084ECDE  4D 85 E4                        test r12, r12
0084ECE1  0F 85 6E 02 00 00               jne 0x14084ef55
0084ECE7  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
0084ECEF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0084ECF4  4C 8D 8C 24 84 00 00 00         lea r9, [rsp + 0x84]
0084ECFC  4D 8B C4                        mov r8, r12
0084ECFF  48 8B D7                        mov rdx, rdi
0084ED02  49 8B CF                        mov rcx, r15
0084ED05  E8 46 CA 19 00                  call 0x1409eb750
0084ED0A  44 8B F0                        mov r14d, eax
0084ED0D  85 C0                           test eax, eax
0084ED0F  0F 88 0E 04 00 00               js 0x14084f123
0084ED15  4D 8B C4                        mov r8, r12
0084ED18  48 8B D7                        mov rdx, rdi
0084ED1B  49 8B CF                        mov rcx, r15
0084ED1E  E8 51 B0 FF FF                  call 0x140849d74
0084ED23  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
0084ED27  4D 8B C4                        mov r8, r12
0084ED2A  48 8B D7                        mov rdx, rdi
0084ED2D  49 8B CF                        mov rcx, r15
0084ED30  E8 EF 7D 1A 00                  call 0x1409f6b24
0084ED35  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
0084ED3C  66 83 7F 4A 00                  cmp word ptr [rdi + 0x4a], 0
0084ED41  0F 87 E6 03 00 00               ja 0x14084f12d
0084ED47  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0084ED4C  44 0F B7 47 4A                  movzx r8d, word ptr [rdi + 0x4a]
0084ED51  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
0084ED59  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0084ED5E  8B 84 24 F0 00 00 00            mov eax, dword ptr [rsp + 0xf0]
0084ED65  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0084ED69  4C 8B CE                        mov r9, rsi
0084ED6C  48 8B D3                        mov rdx, rbx
0084ED6F  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
0084ED74  E8 73 D3 1E 00                  call 0x140a3c0ec
0084ED79  44 8B F0                        mov r14d, eax
0084ED7C  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0084ED80  E9 AD FE FF FF                  jmp 0x14084ec32
0084ED85  44 8B F0                        mov r14d, eax
0084ED88  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0084ED8C  4C 8B AC 24 D0 00 00 00         mov r13, qword ptr [rsp + 0xd0]
0084ED94  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0084ED99  E9 94 FE FF FF                  jmp 0x14084ec32
0084ED9E  48 8B 5A 04                     mov rbx, qword ptr [rdx + 4]
0084EDA2  4D 85 FF                        test r15, r15
0084EDA5  0F 85 E3 FE FF FF               jne 0x14084ec8e
0084EDAB  4C 8B A4 24 08 01 00 00         mov r12, qword ptr [rsp + 0x108]
0084EDB3  E9 E7 FE FF FF                  jmp 0x14084ec9f
0084EDB8  48 8B 5A 04                     mov rbx, qword ptr [rdx + 4]
0084EDBC  48 85 C0                        test rax, rax
0084EDBF  0F 84 AE FD FF FF               je 0x14084eb73
0084EDC5  E9 98 FD FF FF                  jmp 0x14084eb62
0084EDCA  41 83 F8 01                     cmp r8d, 1
0084EDCE  0F 85 49 03 00 00               jne 0x14084f11d
0084EDD4  4C 8B 84 24 08 01 00 00         mov r8, qword ptr [rsp + 0x108]
0084EDDC  48 8B 8C 24 00 01 00 00         mov rcx, qword ptr [rsp + 0x100]
0084EDE4  E8 17 F4 FF FF                  call 0x14084e200
0084EDE9  48 8B D8                        mov rbx, rax
0084EDEC  66 44 39 77 4A                  cmp word ptr [rdi + 0x4a], r14w
0084EDF1  76 23                           jbe 0x14084ee16
0084EDF3  8B 57 30                        mov edx, dword ptr [rdi + 0x30]
0084EDF6  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
0084EDFB  49 8B CD                        mov rcx, r13
0084EDFE  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
0084EE06  0F 84 35 01 00 00               je 0x14084ef41
0084EE0C  E8 4F 5E 00 00                  call 0x140854c60
0084EE11  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0084EE16  44 0F B7 47 4A                  movzx r8d, word ptr [rdi + 0x4a]
0084EE1B  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
0084EE20  0F B7 57 48                     movzx edx, word ptr [rdi + 0x48]
0084EE24  0F B7 CA                        movzx ecx, dx
0084EE27  66 03 C9                        add cx, cx
0084EE2A  F6 47 02 20                     test byte ptr [rdi + 2], 0x20
0084EE2E  66 0F 44 CA                     cmove cx, dx
0084EE32  44 0F B7 C9                     movzx r9d, cx
0084EE36  41 8D 49 18                     lea ecx, [r9 + 0x18]
0084EE3A  89 8C 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], ecx
0084EE41  66 45 85 C0                     test r8w, r8w
0084EE45  0F 85 BB 00 00 00               jne 0x14084ef06
0084EE4B  44 8B E1                        mov r12d, ecx
0084EE4E  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
0084EE56  89 08                           mov dword ptr [rax], ecx
0084EE58  44 8B BC 24 F0 00 00 00         mov r15d, dword ptr [rsp + 0xf0]
0084EE60  41 83 FF 18                     cmp r15d, 0x18
0084EE64  72 66                           jb 0x14084eecc
0084EE66  48 89 1E                        mov qword ptr [rsi], rbx
0084EE69  44 89 76 08                     mov dword ptr [rsi + 8], r14d
0084EE6D  44 89 46 10                     mov dword ptr [rsi + 0x10], r8d
0084EE71  44 89 4E 14                     mov dword ptr [rsi + 0x14], r9d
0084EE75  B8 FF FF FF FF                  mov eax, 0xffffffff
0084EE7A  66 45 85 C0                     test r8w, r8w
0084EE7E  41 0F 45 C4                     cmovne eax, r12d
0084EE82  89 46 0C                        mov dword ptr [rsi + 0xc], eax
0084EE85  41 8D 57 E8                     lea edx, [r15 - 0x18]
0084EE89  48 8D 4E 18                     lea rcx, [rsi + 0x18]
0084EE8D  F6 47 02 20                     test byte ptr [rdi + 2], 0x20
0084EE91  74 5E                           je 0x14084eef1
0084EE93  44 0F B7 4F 48                  movzx r9d, word ptr [rdi + 0x48]
0084EE98  4C 8D 47 4C                     lea r8, [rdi + 0x4c]
0084EE9C  E8 2F F2 FF FF                  call 0x14084e0d0
0084EEA1  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0084EEA6  45 3B FC                        cmp r15d, r12d
0084EEA9  72 19                           jb 0x14084eec4
0084EEAB  41 8B C7                        mov eax, r15d
0084EEAE  41 2B C4                        sub eax, r12d
0084EEB1  8B 54 24 38                     mov edx, dword ptr [rsp + 0x38]
0084EEB5  66 85 D2                        test dx, dx
0084EEB8  75 1F                           jne 0x14084eed9
0084EEBA  44 39 BC 24 E0 00 00 00         cmp dword ptr [rsp + 0xe0], r15d
0084EEC2  76 5A                           jbe 0x14084ef1e
0084EEC4  41 BE 05 00 00 80               mov r14d, 0x80000005
0084EECA  EB 52                           jmp 0x14084ef1e
0084EECC  41 BE 23 00 00 C0               mov r14d, 0xc0000023
0084EED2  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0084EED7  EB 45                           jmp 0x14084ef1e
0084EED9  41 8B CC                        mov ecx, r12d
0084EEDC  48 03 CE                        add rcx, rsi
0084EEDF  3B C2                           cmp eax, edx
0084EEE1  0F 46 D0                        cmovbe edx, eax
0084EEE4  44 8B C2                        mov r8d, edx
0084EEE7  48 8B D3                        mov rdx, rbx
0084EEEA  E8 51 79 E7 FF                  call 0x1406c6840
0084EEEF  EB C9                           jmp 0x14084eeba
0084EEF1  41 3B D1                        cmp edx, r9d
0084EEF4  44 0F 46 CA                     cmovbe r9d, edx
0084EEF8  45 8B C1                        mov r8d, r9d
0084EEFB  48 8D 57 4C                     lea rdx, [rdi + 0x4c]
0084EEFF  E8 3C 79 E7 FF                  call 0x1406c6840
0084EF04  EB 9B                           jmp 0x14084eea1
0084EF06  83 C1 03                        add ecx, 3
0084EF09  83 E1 FC                        and ecx, 0xfffffffc
0084EF0C  44 8B E1                        mov r12d, ecx
0084EF0F  41 03 C8                        add ecx, r8d
0084EF12  89 8C 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], ecx
0084EF19  E9 30 FF FF FF                  jmp 0x14084ee4e
0084EF1E  44 89 74 24 40                  mov dword ptr [rsp + 0x40], r14d
0084EF23  E9 0A FD FF FF                  jmp 0x14084ec32
0084EF28  44 8B F0                        mov r14d, eax
0084EF2B  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0084EF2F  4C 8B AC 24 D0 00 00 00         mov r13, qword ptr [rsp + 0xd0]
0084EF37  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0084EF3C  E9 F1 FC FF FF                  jmp 0x14084ec32
0084EF41  E8 6A 5D 00 00                  call 0x140854cb0
0084EF46  E9 C6 FE FF FF                  jmp 0x14084ee11
0084EF4B  E8 D0 DC 00 00                  call 0x14085cc20
0084EF50  E9 FD FC FF FF                  jmp 0x14084ec52
0084EF55  49 8D 8F D0 00 00 00            lea rcx, [r15 + 0xd0]
0084EF5C  41 B8 20 00 00 00               mov r8d, 0x20
0084EF62  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
0084EF6A  E8 D1 A9 37 00                  call 0x140bc9940
0084EF6F  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0084EF74  48 85 C0                        test rax, rax
0084EF77  0F 84 6A FD FF FF               je 0x14084ece7
0084EF7D  49 8B D4                        mov rdx, r12
0084EF80  48 8B 48 38                     mov rcx, qword ptr [rax + 0x38]
0084EF84  E8 D7 CF FF FF                  call 0x14084bf60
0084EF89  84 C0                           test al, al
0084EF8B  49 8D 8F D0 00 00 00            lea rcx, [r15 + 0xd0]
0084EF92  74 C8                           je 0x14084ef5c
0084EF94  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0084EF99  83 78 44 01                     cmp dword ptr [rax + 0x44], 1
0084EF9D  49 8D 8F D0 00 00 00            lea rcx, [r15 + 0xd0]
0084EFA4  75 B6                           jne 0x14084ef5c
0084EFA6  48 8B 40 58                     mov rax, qword ptr [rax + 0x58]
0084EFAA  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0084EFAF  33 D2                           xor edx, edx
0084EFB1  48 8B C8                        mov rcx, rax
0084EFB4  E8 F7 CD FF FF                  call 0x14084bdb0
0084EFB9  84 C0                           test al, al
0084EFBB  49 8D 8F D0 00 00 00            lea rcx, [r15 + 0xd0]
0084EFC2  75 98                           jne 0x14084ef5c
0084EFC4  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0084EFC9  8B 50 28                        mov edx, dword ptr [rax + 0x28]
0084EFCC  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
0084EFD0  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
0084EFD5  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
0084EFDC  0F 84 84 01 00 00               je 0x14084f166
0084EFE2  E8 79 5C 00 00                  call 0x140854c60
0084EFE7  48 8B C8                        mov rcx, rax
0084EFEA  48 85 C0                        test rax, rax
0084EFED  0F 84 7D 01 00 00               je 0x14084f170
0084EFF3  8B 40 34                        mov eax, dword ptr [rax + 0x34]
0084EFF6  0F B7 C0                        movzx eax, ax
0084EFF9  3B D8                           cmp ebx, eax
0084EFFB  0F 42 D8                        cmovb ebx, eax
0084EFFE  89 5C 24 78                     mov dword ptr [rsp + 0x78], ebx
0084F002  8B 41 38                        mov eax, dword ptr [rcx + 0x38]
0084F005  44 3B F0                        cmp r14d, eax
0084F008  0F 82 7C 01 00 00               jb 0x14084f18a
0084F00E  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0084F013  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
0084F017  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
0084F01C  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
0084F023  0F 85 57 01 00 00               jne 0x14084f180
0084F029  E8 12 6F 00 00                  call 0x140855f40
0084F02E  E9 22 FF FF FF                  jmp 0x14084ef55
0084F033  49 8D 8F D0 00 00 00            lea rcx, [r15 + 0xd0]
0084F03A  48 85 C0                        test rax, rax
0084F03D  75 04                           jne 0x14084f043
0084F03F  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0084F043  48 3B C8                        cmp rcx, rax
0084F046  0F 84 53 FC FF FF               je 0x14084ec9f
0084F04C  48 8D 48 E0                     lea rcx, [rax - 0x20]
0084F050  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
0084F055  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0084F059  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0084F05E  48 85 C9                        test rcx, rcx
0084F061  0F 84 38 FC FF FF               je 0x14084ec9f
0084F067  49 8B D4                        mov rdx, r12
0084F06A  48 8B 49 38                     mov rcx, qword ptr [rcx + 0x38]
0084F06E  E8 ED CE FF FF                  call 0x14084bf60
0084F073  84 C0                           test al, al
0084F075  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0084F07A  49 8D 8F D0 00 00 00            lea rcx, [r15 + 0xd0]
0084F081  74 B7                           je 0x14084f03a
0084F083  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
0084F088  83 7A 44 08                     cmp dword ptr [rdx + 0x44], 8
0084F08C  49 8D 8F D0 00 00 00            lea rcx, [r15 + 0xd0]
0084F093  75 A5                           jne 0x14084f03a
0084F095  48 8B 5A 58                     mov rbx, qword ptr [rdx + 0x58]
0084F099  E9 01 FC FF FF                  jmp 0x14084ec9f
0084F09E  48 05 D0 00 00 00               add rax, 0xd0
0084F0A4  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0084F0A9  4D 85 E4                        test r12, r12
0084F0AC  75 04                           jne 0x14084f0b2
0084F0AE  4C 8B 60 08                     mov r12, qword ptr [rax + 8]
0084F0B2  49 3B C4                        cmp rax, r12
0084F0B5  0F 84 B8 FA FF FF               je 0x14084eb73
0084F0BB  49 8D 44 24 E0                  lea rax, [r12 - 0x20]
0084F0C0  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0084F0C5  4D 8B 64 24 08                  mov r12, qword ptr [r12 + 8]
0084F0CA  48 85 C0                        test rax, rax
0084F0CD  0F 84 A0 FA FF FF               je 0x14084eb73
0084F0D3  49 8B D7                        mov rdx, r15
0084F0D6  48 8B 48 38                     mov rcx, qword ptr [rax + 0x38]
0084F0DA  E8 81 CE FF FF                  call 0x14084bf60
0084F0DF  84 C0                           test al, al
0084F0E1  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0084F0E6  74 C1                           je 0x14084f0a9
0084F0E8  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0084F0ED  83 79 44 08                     cmp dword ptr [rcx + 0x44], 8
0084F0F1  75 B6                           jne 0x14084f0a9
0084F0F3  48 8B 59 58                     mov rbx, qword ptr [rcx + 0x58]
0084F0F7  E9 77 FA FF FF                  jmp 0x14084eb73
0084F0FC  8B 47 34                        mov eax, dword ptr [rdi + 0x34]
0084F0FF  0F B7 C8                        movzx ecx, ax
0084F102  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
0084F106  44 8B 77 38                     mov r14d, dword ptr [rdi + 0x38]
0084F10A  44 89 74 24 7C                  mov dword ptr [rsp + 0x7c], r14d
0084F10F  4D 85 FF                        test r15, r15
0084F112  0F 84 CF FB FF FF               je 0x14084ece7
0084F118  E9 B0 FB FF FF                  jmp 0x14084eccd
0084F11D  41 BE 0D 00 00 C0               mov r14d, 0xc000000d
0084F123  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0084F128  E9 05 FB FF FF                  jmp 0x14084ec32
0084F12D  8B 57 30                        mov edx, dword ptr [rdi + 0x30]
0084F130  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
0084F135  49 8B CD                        mov rcx, r13
0084F138  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
0084F140  74 12                           je 0x14084f154
0084F142  E8 19 5B 00 00                  call 0x140854c60
0084F147  48 8B D8                        mov rbx, rax
0084F14A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0084F14F  E9 F8 FB FF FF                  jmp 0x14084ed4c
0084F154  E8 57 5B 00 00                  call 0x140854cb0
0084F159  48 8B D8                        mov rbx, rax
0084F15C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0084F161  E9 E6 FB FF FF                  jmp 0x14084ed4c
0084F166  E8 45 5B 00 00                  call 0x140854cb0
0084F16B  E9 77 FE FF FF                  jmp 0x14084efe7
0084F170  41 BE 9A 00 00 C0               mov r14d, 0xc000009a
0084F176  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0084F17B  E9 B2 FA FF FF                  jmp 0x14084ec32
0084F180  E8 9B DA 00 00                  call 0x14085cc20
0084F185  E9 CB FD FF FF                  jmp 0x14084ef55
0084F18A  44 8B F0                        mov r14d, eax
0084F18D  89 44 24 7C                     mov dword ptr [rsp + 0x7c], eax
0084F191  E9 78 FE FF FF                  jmp 0x14084f00e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpQueryKeyDataFromNode(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned int a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned int v_stack_m24;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p20 = v_rsi;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (160);
    v_r14 = 0;
    v_stack_m78 = 0;
    v_stack_m98 = 0;
    result = HvpGetCellContextInitialize(v_stack_m78, a2, a3, a4);
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    if (a3 == 2) goto loc_0084EC73;
    if (a3 != 0) goto loc_0084EDCA;
    if (a2 != 0) goto loc_0084EDB8;
loc_0084EB62:
    if (a8 != 0) goto loc_0084F09E;
loc_0084EB73:
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a2 + 72))) + ((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(a2 + 72)))));
    if (((*(unsigned __int8 *)(a2 + 2)) & (32)) == 0) { a1 = (unsigned __int16)(*(unsigned __int16 *)(a2 + 72)); }
    *(unsigned int *)(a6) = (unsigned int)((unsigned __int16)(a1) + 16);
    if (((unsigned int)((unsigned int)(a5))) < 16) goto loc_0084EC0C;
    *(unsigned __int64 *)(a4) = *(unsigned __int64 *)(a7 + 168);
    *(unsigned int *)(a4 + 8) = 0;
    *(unsigned int *)(a4 + 12) = (unsigned int)((unsigned __int16)(a1));
    if (((*(unsigned __int8 *)(a2 + 2)) & (32)) == 0) goto loc_0084EBE8;
    v_stack_m70 = 0;
    a3 = (unsigned int)(((unsigned int)(a5) - 16) >> (1));
    if (a3 >= ((unsigned int)(*(unsigned __int16 *)(a2 + 72)))) { a3 = (unsigned int)(*(unsigned __int16 *)(a2 + 72)); }
loc_0084EBCF:
    v_stack_m70 = 0;
    if (0 >= a3) goto loc_0084EBFF;
    *(unsigned __int16 *)(a4 + 0 * 2 + 16) = (unsigned __int16)(*(unsigned __int8 *)(0 + a2 * 1 + 76));
    result = (unsigned int)((0) + 1);
    goto loc_0084EBCF;
loc_0084EBE8:
    a2 = 0;
    if (a3 <= 0) { a2 = a3; }
    result = memcpy(a4 + 16, a2 + 76, (unsigned int)((unsigned int)(a2)), a4);
loc_0084EBFF:
    if (((unsigned int)((unsigned int)(a5))) >= ((unsigned int)((unsigned __int16)(a1) + 16))) goto loc_0084EC12;
    goto loc_0084EC12;
loc_0084EC0C:
loc_0084EC12:
    v_stack_m88 = (unsigned int)((unsigned int)(0xC0000023ULL));
    goto loc_0084EC32;
loc_0084EC32:
    if (v_stack_m98 == 0) goto loc_0084EC52;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0084EF4B;
    result = HvpReleaseCellPaged(a1, v_stack_m78, (unsigned int)((unsigned int)(a2)), a4);
loc_0084EC52:
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000023ULL)));
loc_0084EC73:
    if (a2 != 0) goto loc_0084ED9E;
loc_0084EC8E:
    if (a8 != 0) goto loc_0084F033;
loc_0084EC9F:
    v_stack_m40 = *(unsigned __int64 *)(a7 + 168);
    v_stack_m38 = (unsigned int)((unsigned int)(0xC0000023ULL));
    v_stack_m10 = (unsigned int)(0xC0000023ULL);
    v_stack_m68 = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    v_stack_m64 = (unsigned int)((unsigned int)(0xC0000023ULL));
    v_stack_m28 = (unsigned int)(0xC0000023ULL);
    if (a2 != 0) goto loc_0084F0FC;
loc_0084ECCD:
    if (a7 == 0) goto loc_0084ECE7;
    v_stack_m28 = (unsigned int)(*(unsigned __int16 *)(a7 + 176));
    if (a8 != 0) goto loc_0084EF55;
loc_0084ECE7:
    v_stack_m80 = v_stack_m18;
    result = CmGetVisibleMaxValueNameLenAndDataLen(a7, a2, a8, v_stack_m1C);
    if (sign_flag) goto loc_0084F123;
    result = CmGetVisibleSubkeyCount(a7, a2, a8, v_stack_m1C);
    v_stack_m2C = (unsigned int)(result);
    result = CmGetVisibleValueCount(a7, a2, a8, v_stack_m1C);
    v_stack_m20 = (unsigned int)(result);
    if ((*(unsigned __int16 *)(a2 + 74)) > 0) goto loc_0084F12D;
loc_0084ED4C:
    v_stack_m78 = a6;
    v_stack_m80 = (unsigned int)((unsigned int)(a5));
    result = CmpPopulateKeyFullInformation(v_stack_m40, v_stack_m70, *(unsigned __int16 *)(a2 + 74), *(unsigned __int64 *)(v_stack_m28 + 72));
    v_stack_m60 = (unsigned int)(result);
    goto loc_0084EC32;
loc_0084ED9E:
    if (a7 != 0) goto loc_0084EC8E;
    goto loc_0084EC9F;
loc_0084EDB8:
    if (result == 0) goto loc_0084EB73;
    goto loc_0084EB62;
loc_0084EDCA:
    if (((unsigned int)(*(unsigned __int16 *)(a2 + 74))) != 1) goto loc_0084F11D;
    result = CmGetKeyLastWriteTime(a7, v_stack_m70, a8, *(unsigned __int64 *)(v_stack_m28 + 72));
    if ((*(unsigned __int16 *)(a2 + 74)) <= ((unsigned __int16)((unsigned int)((unsigned int)(result))))) goto loc_0084EE16;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0084EF41;
    result = HvpGetCellFlat(a1, (unsigned int)(*(unsigned int *)(a2 + 48)), v_stack_m50, *(unsigned __int64 *)(v_stack_m28 + 72));
loc_0084EE11:
    v_stack_m70 = result;
loc_0084EE16:
    v_stack_m68 = (unsigned int)(*(unsigned __int16 *)(a2 + 74));
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a2 + 72))) + ((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(a2 + 72)))));
    if (((*(unsigned __int8 *)(a2 + 2)) & (32)) == 0) { a1 = (unsigned __int16)(*(unsigned __int16 *)(a2 + 72)); }
    v_stack_p40 = (unsigned int)((unsigned __int16)(a1) + 24);
    if ((unsigned __int16)(*(unsigned __int16 *)(a2 + 74)) != 0) goto loc_0084EF06;
loc_0084EE4E:
    *(unsigned int *)(a6) = (unsigned int)((unsigned __int16)(a1) + 24);
    if (((unsigned int)((unsigned int)(a5))) < 24) goto loc_0084EECC;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72)) = result;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8) = (unsigned int)((unsigned int)((unsigned int)(result)));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16) = (unsigned int)(*(unsigned __int16 *)(a2 + 74));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 20) = (unsigned int)((unsigned __int16)(a1));
    result = (unsigned int)(0xFFFFFFFFULL);
    if ((unsigned __int16)(*(unsigned __int16 *)(a2 + 74)) != 0) { result = (unsigned int)((unsigned int)((unsigned int)((unsigned __int16)(a1) + 24))); }
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 12) = (unsigned int)(result);
    if (((*(unsigned __int8 *)(a2 + 2)) & (32)) == 0) goto loc_0084EEF1;
    result = CmpCopyCompressedName(*(unsigned __int64 *)(v_stack_m28 + 72) + 24, (unsigned int)(a5) - 24, a2 + 76, *(unsigned __int16 *)(a2 + 72));
loc_0084EEA1:
    if (((unsigned int)((unsigned int)(a5))) < ((unsigned int)((unsigned int)((unsigned int)((unsigned __int16)(a1) + 24))))) goto loc_0084EEC4;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) - ((unsigned int)((unsigned int)((unsigned int)((unsigned __int16)(a1) + 24)))));
    if ((unsigned __int16)((unsigned int)(v_stack_m68)) != 0) goto loc_0084EED9;
loc_0084EEBA:
    if (v_stack_p40 <= ((unsigned int)((unsigned int)(a5)))) goto loc_0084EF1E;
loc_0084EEC4:
    goto loc_0084EF1E;
loc_0084EECC:
    goto loc_0084EF1E;
loc_0084EED9:
    a1 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned __int16)(a1) + 24))))) + (*(unsigned __int64 *)(v_stack_m28 + 72));
    a2 = (unsigned int)(v_stack_m68);
    if (((unsigned int)(result)) <= ((unsigned int)((unsigned int)(v_stack_m68)))) { a2 = (unsigned int)(result); }
    result = memcpy(a1, v_stack_m70, (unsigned int)((unsigned int)(a2)), *(unsigned __int16 *)(a2 + 72));
    goto loc_0084EEBA;
loc_0084EEF1:
    a4 = *(unsigned __int16 *)(a2 + 72);
    if (((unsigned int)(v_stack_m70)) <= ((unsigned int)(*(unsigned __int16 *)(a2 + 72)))) { a4 = (unsigned int)(v_stack_m70); }
    result = memcpy(a1, a2 + 76, (unsigned int)((unsigned int)(a4)), a4);
    goto loc_0084EEA1;
loc_0084EF06:
    a1 = (unsigned int)((a1) + (3));
    a1 = (unsigned int)((a1) & (0xFFFFFFFCULL));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned int)((unsigned int)(a4)))));
    v_stack_p40 = (unsigned int)(a1);
    goto loc_0084EE4E;
loc_0084EF1E:
    v_stack_m60 = (unsigned int)((unsigned int)(0xC0000023ULL));
    goto loc_0084EC32;
loc_0084EF41:
    result = HvpGetCellPaged(a1, a2 + 76, (unsigned int)((unsigned int)(a4)), a4);
    goto loc_0084EE11;
loc_0084EF4B:
    result = HvpReleaseCellFlat(a1, a2 + 76, (unsigned int)((unsigned int)(a4)), a4);
    goto loc_0084EC52;
loc_0084EF55:
loc_0084EF5C:
    result = CmListGetNextElement((unsigned int)(a5) + 208, v_stack_m10, 32, a4);
    v_stack_m58 = result;
    if (result == 0) goto loc_0084ECE7;
    result = CmEqualTrans(*(unsigned __int64 *)(result + 56), (unsigned int)((unsigned int)(a1)), 32, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0084EF5C;
    if ((*(unsigned int *)(v_stack_m58 + 68)) != 1) goto loc_0084EF5C;
    v_stack_m58 = *(unsigned __int64 *)(v_stack_m58 + 88);
    a2 = 0;
    result = CmpIsKeyDeleted(*(unsigned __int64 *)(v_stack_m58 + 88), a2, 32, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0084EF5C;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m58 + 32) + 140)) & (1)) == 0) goto loc_0084F166;
    result = HvpGetCellFlat(*(unsigned __int64 *)(v_stack_m58 + 32), (unsigned int)(*(unsigned int *)(v_stack_m58 + 40)), v_stack_m68, a4);
loc_0084EFE7:
    if (result == 0) goto loc_0084F170;
    v_rbx = v_stack_m70;
    if (((unsigned int)(v_stack_m70)) < ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(result + 52)))))) { v_rbx = (unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(result + 52)))); }
    v_stack_m28 = (unsigned int)(v_rbx);
    if (((unsigned int)((unsigned int)(0xC0000023ULL))) < ((unsigned int)((unsigned int)(*(unsigned int *)(result + 56))))) goto loc_0084F18A;
loc_0084F00E:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m58 + 32) + 140)) & (1)) != 0) goto loc_0084F180;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_stack_m58 + 32), v_stack_m68, v_stack_m68, a4);
    goto loc_0084EF55;
loc_0084F033:
loc_0084F03A:
    if (result == 0) {
        result = *(unsigned __int64 *)((unsigned int)(a5) + 208 + 8);
    }
    if (((unsigned int)(a5) + 208) == result) goto loc_0084EC9F;
    v_stack_m58 = result - 32;
    v_stack_m68 = *(unsigned __int64 *)(result + 8);
    if (result - 32 == 0) goto loc_0084EC9F;
    result = CmEqualTrans(*(unsigned __int64 *)(result - 32 + 56), (unsigned int)((unsigned int)(a1)), v_stack_m68, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0084F03A;
    if ((*(unsigned int *)(v_stack_m58 + 68)) != 8) goto loc_0084F03A;
    goto loc_0084EC9F;
loc_0084F09E:
    result = (v_stack_m68) + (208);
    v_stack_m68 = result;
loc_0084F0A9:
    v_r12 = (unsigned int)((unsigned int)(a1));
    if ((unsigned int)((unsigned int)(a1)) == 0) {
        v_r12 = *(unsigned __int64 *)(result + 8);
    }
    if (result == v_r12) goto loc_0084EB73;
    v_stack_m58 = v_r12 - 32;
    if (v_r12 - 32 == 0) goto loc_0084EB73;
    result = CmEqualTrans(*(unsigned __int64 *)(v_r12 - 32 + 56), (unsigned int)(a5), v_stack_m68, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0084F0A9;
    if ((*(unsigned int *)(v_stack_m58 + 68)) != 8) goto loc_0084F0A9;
    goto loc_0084EB73;
loc_0084F0FC:
    v_stack_m28 = (unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(a2 + 52))));
    v_stack_m24 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 56)));
    if ((unsigned int)(a5) == 0) goto loc_0084ECE7;
    goto loc_0084ECCD;
loc_0084F11D:
loc_0084F123:
    goto loc_0084EC32;
loc_0084F12D:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0084F154;
    result = HvpGetCellFlat(a1, (unsigned int)(*(unsigned int *)(a2 + 48)), v_stack_m50, a4);
    v_stack_m70 = result;
    goto loc_0084ED4C;
loc_0084F154:
    result = HvpGetCellPaged(a1, (unsigned int)(*(unsigned int *)(a2 + 48)), v_stack_m50, a4);
    v_stack_m70 = result;
    goto loc_0084ED4C;
loc_0084F166:
    result = HvpGetCellPaged(a1, (unsigned int)(*(unsigned int *)(a2 + 48)), v_stack_m50, a4);
    goto loc_0084EFE7;
loc_0084F170:
    goto loc_0084EC32;
loc_0084F180:
    result = HvpReleaseCellFlat(a1, (unsigned int)(*(unsigned int *)(a2 + 48)), v_stack_m50, a4);
    goto loc_0084EF55;
loc_0084F18A:
    v_stack_m24 = (unsigned int)(result);
    goto loc_0084F00E;
}
```

## 5. (Beta) C Style

```c
int64_t CmpQueryKeyDataFromNode(void *Arg1, void *Arg2, int32_t Arg3, void *Arg4, uint32_t Arg5, void *Arg6, void *Arg7, int64_t Arg8)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint32_t v_stack_m24;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint32_t v_stack_p40;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p20 = local_rsi;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (160);
    local_r14 = 0;
    v_stack_m78 = 0;
    v_stack_m98 = 0;
    result = HvpGetCellContextInitialize(v_stack_m78, Arg2, Arg3, Arg4);
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    if (Arg3 == 2) goto loc_0084EC73;
    if (Arg3 != 0) goto loc_0084EDCA;
    if (Arg2 != NULL) goto loc_0084EDB8;
loc_0084EB62:
    if (Arg8 != 0) goto loc_0084F09E;
loc_0084EB73:
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(arg2 + 0x48))) + ((uint16_t)((uint16_t)(*(uint16_t *)(arg2 + 0x48)))));
    if (((*(uint8_t *)(arg2 + 0x2)) & (32)) == 0) { Arg1 = (uint16_t)(*(uint16_t *)(arg2 + 0x48)); }
    *(uint32_t *)(arg6) = (uint32_t)((uint16_t)(Arg1) + 16);
    if (((uint32_t)((uint32_t)(Arg5))) < 16) goto loc_0084EC0C;
    *(uint64_t *)(arg4) = *(uint64_t *)(arg7 + 0xA8);
    *(uint32_t *)(arg4 + 0x8) = 0;
    *(uint32_t *)(arg4 + 0xC) = (uint32_t)((uint16_t)(Arg1));
    if (((*(uint8_t *)(arg2 + 0x2)) & (32)) == 0) goto loc_0084EBE8;
    v_stack_m70 = 0;
    Arg3 = (uint32_t)(((uint32_t)(Arg5) - 16) >> (1));
    if (Arg3 >= ((uint32_t)(*(uint16_t *)(arg2 + 0x48)))) { Arg3 = (uint32_t)(*(uint16_t *)(arg2 + 0x48)); }
loc_0084EBCF:
    v_stack_m70 = 0;
    if (0 >= Arg3) goto loc_0084EBFF;
    *(uint16_t *)(arg4 + 0x0 * 2 + 0x10) = (uint16_t)(*(uint8_t *)(0 + arg2 * 1 + 0x4C));
    result = (uint32_t)((0) + 1);
    goto loc_0084EBCF;
loc_0084EBE8:
    Arg2 = 0;
    if (Arg3 <= 0) { Arg2 = Arg3; }
    result = memcpy(Arg4 + 16, Arg2 + 76, (uint32_t)((uint32_t)(Arg2)), Arg4);
loc_0084EBFF:
    if (((uint32_t)((uint32_t)(Arg5))) >= ((uint32_t)((uint16_t)(Arg1) + 16))) goto loc_0084EC12;
    goto loc_0084EC12;
loc_0084EC0C:
loc_0084EC12:
    v_stack_m88 = (uint32_t)((uint32_t)(0xC0000023ULL));
    goto loc_0084EC32;
loc_0084EC32:
    if (v_stack_m98 == 0) goto loc_0084EC52;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0084EF4B;
    result = HvpReleaseCellPaged(Arg1, v_stack_m78, (uint32_t)((uint32_t)(Arg2)), Arg4);
loc_0084EC52:
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000023ULL)));
loc_0084EC73:
    if (Arg2 != NULL) goto loc_0084ED9E;
loc_0084EC8E:
    if (Arg8 != 0) goto loc_0084F033;
loc_0084EC9F:
    v_stack_m40 = *(uint64_t *)(arg7 + 0xA8);
    v_stack_m38 = (uint32_t)((uint32_t)(0xC0000023ULL));
    v_stack_m10 = (uint32_t)(0xC0000023ULL);
    v_stack_m68 = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    v_stack_m64 = (uint32_t)((uint32_t)(0xC0000023ULL));
    v_stack_m28 = (uint32_t)(0xC0000023ULL);
    if (Arg2 != NULL) goto loc_0084F0FC;
loc_0084ECCD:
    if (Arg7 == NULL) goto loc_0084ECE7;
    v_stack_m28 = (uint32_t)(*(uint16_t *)(arg7 + 0xB0));
    if (Arg8 != 0) goto loc_0084EF55;
loc_0084ECE7:
    v_stack_m80 = v_stack_m18;
    result = CmGetVisibleMaxValueNameLenAndDataLen(Arg7, Arg2, Arg8, v_stack_m1C);
    if (sign_flag) goto loc_0084F123;
    result = CmGetVisibleSubkeyCount(Arg7, Arg2, Arg8, v_stack_m1C);
    v_stack_m2C = (uint32_t)(result);
    result = CmGetVisibleValueCount(Arg7, Arg2, Arg8, v_stack_m1C);
    v_stack_m20 = (uint32_t)(result);
    if ((*(uint16_t *)(arg2 + 0x4A)) > 0) goto loc_0084F12D;
loc_0084ED4C:
    v_stack_m78 = Arg6;
    v_stack_m80 = (uint32_t)((uint32_t)(Arg5));
    result = CmpPopulateKeyFullInformation(v_stack_m40, v_stack_m70, *(uint16_t *)(arg2 + 0x4A), *(uint64_t *)(v_stack_m28 + 0x48));
    v_stack_m60 = (uint32_t)(result);
    goto loc_0084EC32;
loc_0084ED9E:
    if (Arg7 != NULL) goto loc_0084EC8E;
    goto loc_0084EC9F;
loc_0084EDB8:
    if (result == 0) goto loc_0084EB73;
    goto loc_0084EB62;
loc_0084EDCA:
    if (((uint32_t)(*(uint16_t *)(arg2 + 0x4A))) != 1) goto loc_0084F11D;
    result = CmGetKeyLastWriteTime(Arg7, v_stack_m70, Arg8, *(uint64_t *)(v_stack_m28 + 0x48));
    if ((*(uint16_t *)(arg2 + 0x4A)) <= ((uint16_t)((uint32_t)((uint32_t)(result))))) goto loc_0084EE16;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0084EF41;
    result = HvpGetCellFlat(Arg1, (uint32_t)(*(uint32_t *)(arg2 + 0x30)), v_stack_m50, *(uint64_t *)(v_stack_m28 + 0x48));
loc_0084EE11:
    v_stack_m70 = result;
loc_0084EE16:
    v_stack_m68 = (uint32_t)(*(uint16_t *)(arg2 + 0x4A));
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(arg2 + 0x48))) + ((uint16_t)((uint16_t)(*(uint16_t *)(arg2 + 0x48)))));
    if (((*(uint8_t *)(arg2 + 0x2)) & (32)) == 0) { Arg1 = (uint16_t)(*(uint16_t *)(arg2 + 0x48)); }
    v_stack_p40 = (uint32_t)((uint16_t)(Arg1) + 24);
    if ((uint16_t)(*(uint16_t *)(arg2 + 0x4A)) != 0) goto loc_0084EF06;
loc_0084EE4E:
    *(uint32_t *)(arg6) = (uint32_t)((uint16_t)(Arg1) + 24);
    if (((uint32_t)((uint32_t)(Arg5))) < 24) goto loc_0084EECC;
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48)) = result;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8) = (uint32_t)((uint32_t)((uint32_t)(result)));
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10) = (uint32_t)(*(uint16_t *)(arg2 + 0x4A));
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x14) = (uint32_t)((uint16_t)(Arg1));
    result = (uint32_t)(0xFFFFFFFFULL);
    if ((uint16_t)(*(uint16_t *)(arg2 + 0x4A)) != 0) { result = (uint32_t)((uint32_t)((uint32_t)((uint16_t)(Arg1) + 24))); }
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xC) = (uint32_t)(result);
    if (((*(uint8_t *)(arg2 + 0x2)) & (32)) == 0) goto loc_0084EEF1;
    result = CmpCopyCompressedName(*(uint64_t *)(v_stack_m28 + 0x48) + 24, (uint32_t)(Arg5) - 24, Arg2 + 76, *(uint16_t *)(arg2 + 0x48));
loc_0084EEA1:
    if (((uint32_t)((uint32_t)(Arg5))) < ((uint32_t)((uint32_t)((uint32_t)((uint16_t)(Arg1) + 24))))) goto loc_0084EEC4;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) - ((uint32_t)((uint32_t)((uint32_t)((uint16_t)(Arg1) + 24)))));
    if ((uint16_t)((uint32_t)(v_stack_m68)) != 0) goto loc_0084EED9;
loc_0084EEBA:
    if (v_stack_p40 <= ((uint32_t)((uint32_t)(Arg5)))) goto loc_0084EF1E;
loc_0084EEC4:
    goto loc_0084EF1E;
loc_0084EECC:
    goto loc_0084EF1E;
loc_0084EED9:
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint16_t)(Arg1) + 24))))) + (*(uint64_t *)(v_stack_m28 + 0x48));
    Arg2 = (uint32_t)(v_stack_m68);
    if (((uint32_t)(result)) <= ((uint32_t)((uint32_t)(v_stack_m68)))) { Arg2 = (uint32_t)(result); }
    result = memcpy(Arg1, v_stack_m70, (uint32_t)((uint32_t)(Arg2)), *(uint16_t *)(arg2 + 0x48));
    goto loc_0084EEBA;
loc_0084EEF1:
    Arg4 = *(uint16_t *)(arg2 + 0x48);
    if (((uint32_t)(v_stack_m70)) <= ((uint32_t)(*(uint16_t *)(arg2 + 0x48)))) { Arg4 = (uint32_t)(v_stack_m70); }
    result = memcpy(Arg1, Arg2 + 76, (uint32_t)((uint32_t)(Arg4)), Arg4);
    goto loc_0084EEA1;
loc_0084EF06:
    Arg1 = (uint32_t)((Arg1) + (3));
    Arg1 = (uint32_t)((Arg1) & (0xFFFFFFFCULL));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint32_t)((uint32_t)(Arg4)))));
    v_stack_p40 = (uint32_t)(Arg1);
    goto loc_0084EE4E;
loc_0084EF1E:
    v_stack_m60 = (uint32_t)((uint32_t)(0xC0000023ULL));
    goto loc_0084EC32;
loc_0084EF41:
    result = HvpGetCellPaged(Arg1, Arg2 + 76, (uint32_t)((uint32_t)(Arg4)), Arg4);
    goto loc_0084EE11;
loc_0084EF4B:
    result = HvpReleaseCellFlat(Arg1, Arg2 + 76, (uint32_t)((uint32_t)(Arg4)), Arg4);
    goto loc_0084EC52;
loc_0084EF55:
loc_0084EF5C:
    result = CmListGetNextElement((uint32_t)(Arg5) + 208, v_stack_m10, 32, Arg4);
    v_stack_m58 = result;
    if (result == 0) goto loc_0084ECE7;
    result = CmEqualTrans(*(uint64_t *)(result + 0x38), (uint32_t)((uint32_t)(Arg1)), 32, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0084EF5C;
    if ((*(uint32_t *)(v_stack_m58 + 0x44)) != 1) goto loc_0084EF5C;
    v_stack_m58 = *(uint64_t *)(v_stack_m58 + 0x58);
    Arg2 = 0;
    result = CmpIsKeyDeleted(*(uint64_t *)(v_stack_m58 + 0x58), Arg2, 32, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0084EF5C;
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m58 + 0x20) + 0x8C)) & (1)) == 0) goto loc_0084F166;
    result = HvpGetCellFlat(*(uint64_t *)(v_stack_m58 + 0x20), (uint32_t)(*(uint32_t *)(v_stack_m58 + 0x28)), v_stack_m68, Arg4);
loc_0084EFE7:
    if (result == 0) goto loc_0084F170;
    local_rbx = v_stack_m70;
    if (((uint32_t)(v_stack_m70)) < ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(result + 0x34)))))) { local_rbx = (uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(result + 0x34)))); }
    v_stack_m28 = (uint32_t)(local_rbx);
    if (((uint32_t)((uint32_t)(0xC0000023ULL))) < ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x38))))) goto loc_0084F18A;
loc_0084F00E:
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m58 + 0x20) + 0x8C)) & (1)) != 0) goto loc_0084F180;
    result = HvpReleaseCellPaged(*(uint64_t *)(v_stack_m58 + 0x20), v_stack_m68, v_stack_m68, Arg4);
    goto loc_0084EF55;
loc_0084F033:
loc_0084F03A:
    if (result == 0) {
        result = *(uint64_t *)((uint32_t)(Arg5) + 0xD0 + 0x8);
    }
    if (((uint32_t)(Arg5) + 208) == result) goto loc_0084EC9F;
    v_stack_m58 = result - 32;
    v_stack_m68 = *(uint64_t *)(result + 0x8);
    if (result - 32 == 0) goto loc_0084EC9F;
    result = CmEqualTrans(*(uint64_t *)(result - 0x20 + 0x38), (uint32_t)((uint32_t)(Arg1)), v_stack_m68, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0084F03A;
    if ((*(uint32_t *)(v_stack_m58 + 0x44)) != 8) goto loc_0084F03A;
    goto loc_0084EC9F;
loc_0084F09E:
    result = (v_stack_m68) + (208);
    v_stack_m68 = result;
loc_0084F0A9:
    local_r12 = (uint32_t)((uint32_t)(Arg1));
    if ((uint32_t)((uint32_t)(Arg1)) == 0) {
        local_r12 = *(uint64_t *)(result + 0x8);
    }
    if (result == local_r12) goto loc_0084EB73;
    v_stack_m58 = local_r12 - 32;
    if (local_r12 - 32 == 0) goto loc_0084EB73;
    result = CmEqualTrans(*(uint64_t *)(local_r12 - 0x20 + 0x38), (uint32_t)(Arg5), v_stack_m68, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0084F0A9;
    if ((*(uint32_t *)(v_stack_m58 + 0x44)) != 8) goto loc_0084F0A9;
    goto loc_0084EB73;
loc_0084F0FC:
    v_stack_m28 = (uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(arg2 + 0x34))));
    v_stack_m24 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x38)));
    if ((uint32_t)(Arg5) == 0) goto loc_0084ECE7;
    goto loc_0084ECCD;
loc_0084F11D:
loc_0084F123:
    goto loc_0084EC32;
loc_0084F12D:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0084F154;
    result = HvpGetCellFlat(Arg1, (uint32_t)(*(uint32_t *)(arg2 + 0x30)), v_stack_m50, Arg4);
    v_stack_m70 = result;
    goto loc_0084ED4C;
loc_0084F154:
    result = HvpGetCellPaged(Arg1, (uint32_t)(*(uint32_t *)(arg2 + 0x30)), v_stack_m50, Arg4);
    v_stack_m70 = result;
    goto loc_0084ED4C;
loc_0084F166:
    result = HvpGetCellPaged(Arg1, (uint32_t)(*(uint32_t *)(arg2 + 0x30)), v_stack_m50, Arg4);
    goto loc_0084EFE7;
loc_0084F170:
    goto loc_0084EC32;
loc_0084F180:
    result = HvpReleaseCellFlat(Arg1, (uint32_t)(*(uint32_t *)(arg2 + 0x30)), v_stack_m50, Arg4);
    goto loc_0084EF55;
loc_0084F18A:
    v_stack_m24 = (uint32_t)(result);
    goto loc_0084F00E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8C` | `8` | `R` |
| `Arg2` | `+ 0x2` | `8` | `R` |
| `Arg2` | `+ 0x30` | `32` | `R` |
| `Arg2` | `+ 0x48` | `16` | `R` |
| `Arg2` | `+ 0x4A` | `16` | `R` |
| `Arg2` | `+ 0x4C` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |
| `Arg4` | `+ 0x8` | `32` | `W` |
| `Arg4` | `+ 0xC` | `32` | `W` |
| `Arg4` | `+ 0x10` | `32` | `W` |
| `Arg4` | `+ 0x10` | `64` | `R` |
| `Arg4` | `+ 0x10 + rdx*2` | `16` | `W` |
| `Arg4` | `+ 0x14` | `32` | `W` |
| `Arg4` | `+ 0x18` | `64` | `R` |
| `Arg6` | `+ 0x0` | `32` | `W` |
| `Arg7` | `+ 0xA8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0084EAE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
