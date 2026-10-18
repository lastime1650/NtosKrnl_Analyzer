# sub_006F033D

- RVA: `0x006F033D`–`0x006F0AA0` (길이 `1,891` bytes)
- VA: `0x00000001406F033D`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A6140`
- 디코드: `463`개 명령, `1,891/1,891` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x006F0366` → [SepGetLearningModeObjectInformation](../60/SepGetLearningModeObjectInformation_function_00608F74.md) (function, `0x00608F74`)
- `0x006F054C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x006F0581` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x006F067D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x006F06DB` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x006F0944` → [SepFlattenAcl](../60/SepFlattenAcl_function_00608E1C.md) (function, `0x00608E1C`)
- `0x006F09C8` → [SepFlattenAcl](../60/SepFlattenAcl_function_00608E1C.md) (function, `0x00608E1C`)
- `0x006F0A8A` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006F0372` → RVA `0x006C8EC0` (` ?? ::FNODOBFM::`string'`; read)
- `0x006F0816` → RVA `0x00FD9B78` (`PAGEDATA`; read)
- `0x006F0A63` → RVA `0x00EFFA28` (`.data`; read)
- `0x006F0A6A` → RVA `0x000222F0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x006F054C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x006F067D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006F0A9E` → [sub_006F0AA0 + 0xA](Unknown_function_006F0AA0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F033D  48 89 BC 24 F8 02 00 00         mov qword ptr [rsp + 0x2f8], rdi
006F0345  48 0F 45 C1                     cmovne rax, rcx
006F0349  44 89 6D BC                     mov dword ptr [rbp - 0x44], r13d
006F034D  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006F0351  B9 16 00 00 00                  mov ecx, 0x16
006F0356  B8 0E 00 00 00                  mov eax, 0xe
006F035B  0F 45 C1                        cmovne eax, ecx
006F035E  48 8D 4C 24 41                  lea rcx, [rsp + 0x41]
006F0363  89 45 B8                        mov dword ptr [rbp - 0x48], eax
006F0366  E8 09 8C F1 FF                  call 0x140608f74
006F036B  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
006F036F  48 8B D0                        mov rdx, rax
006F0372  4C 8D 1D 47 8B FD FF            lea r11, [rip - 0x274b9]
006F0379  48 85 C0                        test rax, rax
006F037C  74 39                           je 0x1406f03b7
006F037E  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
006F0382  48 85 C0                        test rax, rax
006F0385  74 30                           je 0x1406f03b7
006F0387  44 0F B7 08                     movzx r9d, word ptr [rax]
006F038B  44 0F B7 40 02                  movzx r8d, word ptr [rax + 2]
006F0390  49 8D 49 02                     lea rcx, [r9 + 2]
006F0394  49 3B C8                        cmp rcx, r8
006F0397  41 8D 49 02                     lea ecx, [r9 + 2]
006F039B  72 03                           jb 0x1406f03a0
006F039D  41 8B C8                        mov ecx, r8d
006F03A0  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006F03A4  41 BA 02 00 00 00               mov r10d, 2
006F03AA  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
006F03AE  89 4D C8                        mov dword ptr [rbp - 0x38], ecx
006F03B1  44 89 6D CC                     mov dword ptr [rbp - 0x34], r13d
006F03B5  EB 17                           jmp 0x1406f03ce
006F03B7  4C 89 5D C0                     mov qword ptr [rbp - 0x40], r11
006F03BB  41 BA 02 00 00 00               mov r10d, 2
006F03C1  48 C7 45 C8 02 00 00 00         mov qword ptr [rbp - 0x38], 2
006F03C9  48 85 D2                        test rdx, rdx
006F03CC  74 39                           je 0x1406f0407
006F03CE  4C 8B 42 18                     mov r8, qword ptr [rdx + 0x18]
006F03D2  4D 85 C0                        test r8, r8
006F03D5  74 30                           je 0x1406f0407
006F03D7  4C 39 6A 20                     cmp qword ptr [rdx + 0x20], r13
006F03DB  74 0F                           je 0x1406f03ec
006F03DD  4C 8B 4A 30                     mov r9, qword ptr [rdx + 0x30]
006F03E1  4D 85 C9                        test r9, r9
006F03E4  74 06                           je 0x1406f03ec
006F03E6  0F B7 4A 2A                     movzx ecx, word ptr [rdx + 0x2a]
006F03EA  EB 23                           jmp 0x1406f040f
006F03EC  41 0F B7 10                     movzx edx, word ptr [r8]
006F03F0  41 0F B7 48 02                  movzx ecx, word ptr [r8 + 2]
006F03F5  48 8D 42 02                     lea rax, [rdx + 2]
006F03F9  48 3B C1                        cmp rax, rcx
006F03FC  73 03                           jae 0x1406f0401
006F03FE  8D 4A 02                        lea ecx, [rdx + 2]
006F0401  4D 8B 48 08                     mov r9, qword ptr [r8 + 8]
006F0405  EB 08                           jmp 0x1406f040f
006F0407  B9 02 00 00 00                  mov ecx, 2
006F040C  4D 8B CB                        mov r9, r11
006F040F  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
006F0413  41 FF C2                        inc r10d
006F0416  44 89 6D DC                     mov dword ptr [rbp - 0x24], r13d
006F041A  4C 8D 4D B0                     lea r9, [rbp - 0x50]
006F041E  89 4D D8                        mov dword ptr [rbp - 0x28], ecx
006F0421  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
006F042A  48 8B 88 20 02 00 00            mov rcx, qword ptr [rax + 0x220]
006F0431  41 8B C2                        mov eax, r10d
006F0434  48 C1 E0 04                     shl rax, 4
006F0438  4C 03 C8                        add r9, rax
006F043B  41 8B C5                        mov eax, r13d
006F043E  48 8B 91 50 03 00 00            mov rdx, qword ptr [rcx + 0x350]
006F0445  41 FF C2                        inc r10d
006F0448  48 85 D2                        test rdx, rdx
006F044B  74 0A                           je 0x1406f0457
006F044D  0F B7 4A 02                     movzx ecx, word ptr [rdx + 2]
006F0451  4C 8B 42 08                     mov r8, qword ptr [rdx + 8]
006F0455  EB 08                           jmp 0x1406f045f
006F0457  B9 02 00 00 00                  mov ecx, 2
006F045C  4D 8B C3                        mov r8, r11
006F045F  4D 89 01                        mov qword ptr [r9], r8
006F0462  41 8D 52 01                     lea edx, [r10 + 1]
006F0466  41 89 49 08                     mov dword ptr [r9 + 8], ecx
006F046A  48 8D 8D 18 02 00 00            lea rcx, [rbp + 0x218]
006F0471  41 89 41 0C                     mov dword ptr [r9 + 0xc], eax
006F0475  41 8B C2                        mov eax, r10d
006F0478  48 03 C0                        add rax, rax
006F047B  4C 89 5C C5 B0                  mov qword ptr [rbp + rax*8 - 0x50], r11
006F0480  48 C7 44 C5 B8 02 00 00 00      mov qword ptr [rbp + rax*8 - 0x48], 2
006F0489  8B C2                           mov eax, edx
006F048B  FF C2                           inc edx
006F048D  48 03 C0                        add rax, rax
006F0490  48 89 4C C5 B0                  mov qword ptr [rbp + rax*8 - 0x50], rcx
006F0495  48 8D 4C 24 5C                  lea rcx, [rsp + 0x5c]
006F049A  48 C7 44 C5 B8 04 00 00 00      mov qword ptr [rbp + rax*8 - 0x48], 4
006F04A3  8B C2                           mov eax, edx
006F04A5  FF C2                           inc edx
006F04A7  48 03 C0                        add rax, rax
006F04AA  48 89 4C C5 B0                  mov qword ptr [rbp + rax*8 - 0x50], rcx
006F04AF  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
006F04B4  48 C7 44 C5 B8 04 00 00 00      mov qword ptr [rbp + rax*8 - 0x48], 4
006F04BD  8B C2                           mov eax, edx
006F04BF  FF C2                           inc edx
006F04C1  48 03 C0                        add rax, rax
006F04C4  48 89 4C C5 B0                  mov qword ptr [rbp + rax*8 - 0x50], rcx
006F04C9  48 8D 4D B0                     lea rcx, [rbp - 0x50]
006F04CD  48 C7 44 C5 B8 04 00 00 00      mov qword ptr [rbp + rax*8 - 0x48], 4
006F04D6  8B C2                           mov eax, edx
006F04D8  48 C1 E0 04                     shl rax, 4
006F04DC  48 03 C8                        add rcx, rax
006F04DF  48 8D 43 78                     lea rax, [rbx + 0x78]
006F04E3  48 89 01                        mov qword ptr [rcx], rax
006F04E6  48 C7 41 08 04 00 00 00         mov qword ptr [rcx + 8], 4
006F04EE  8D 4A 01                        lea ecx, [rdx + 1]
006F04F1  4C 8B 83 38 04 00 00            mov r8, qword ptr [rbx + 0x438]
006F04F8  48 8D 55 B0                     lea rdx, [rbp - 0x50]
006F04FC  8B C1                           mov eax, ecx
006F04FE  8D 79 01                        lea edi, [rcx + 1]
006F0501  48 C1 E0 04                     shl rax, 4
006F0505  48 03 D0                        add rdx, rax
006F0508  49 8D 40 28                     lea rax, [r8 + 0x28]
006F050C  4D 85 C0                        test r8, r8
006F050F  75 05                           jne 0x1406f0516
006F0511  48 8D 44 24 50                  lea rax, [rsp + 0x50]
006F0516  48 89 02                        mov qword ptr [rdx], rax
006F0519  41 B8 53 65 53 69               mov r8d, 0x69536553
006F051F  48 C7 42 08 04 00 00 00         mov qword ptr [rdx + 8], 4
006F0527  C7 45 88 01 00 00 00            mov dword ptr [rbp - 0x78], 1
006F052E  48 8B 83 98 00 00 00            mov rax, qword ptr [rbx + 0x98]
006F0535  48 8B 08                        mov rcx, qword ptr [rax]
006F0538  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
006F053C  B9 00 01 00 00                  mov ecx, 0x100
006F0541  44 8D 2C 85 0C 00 00 00         lea r13d, [rax*4 + 0xc]
006F0549  41 8B D5                        mov edx, r13d
006F054C  E8 9F 1B 49 00                  call 0x140b820f0
006F0551  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
006F0555  48 85 C0                        test rax, rax
006F0558  74 5A                           je 0x1406f05b4
006F055A  48 8B 8B 98 00 00 00            mov rcx, qword ptr [rbx + 0x98]
006F0561  8B 51 08                        mov edx, dword ptr [rcx + 8]
006F0564  89 10                           mov dword ptr [rax], edx
006F0566  48 8B 8B 98 00 00 00            mov rcx, qword ptr [rbx + 0x98]
006F056D  48 8B 11                        mov rdx, qword ptr [rcx]
006F0570  48 8D 48 04                     lea rcx, [rax + 4]
006F0574  44 0F B6 42 01                  movzx r8d, byte ptr [rdx + 1]
006F0579  4E 8D 04 85 08 00 00 00         lea r8, [r8*4 + 8]
006F0581  E8 BA 62 FD FF                  call 0x1406c6840
006F0586  8B CF                           mov ecx, edi
006F0588  48 8D 45 88                     lea rax, [rbp - 0x78]
006F058C  48 03 C9                        add rcx, rcx
006F058F  FF C7                           inc edi
006F0591  48 89 44 CD B0                  mov qword ptr [rbp + rcx*8 - 0x50], rax
006F0596  48 C7 44 CD B8 04 00 00 00      mov qword ptr [rbp + rcx*8 - 0x48], 4
006F059F  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
006F05A3  8B C7                           mov eax, edi
006F05A5  48 03 C0                        add rax, rax
006F05A8  44 89 6C C5 B8                  mov dword ptr [rbp + rax*8 - 0x48], r13d
006F05AD  44 89 7C C5 BC                  mov dword ptr [rbp + rax*8 - 0x44], r15d
006F05B2  EB 13                           jmp 0x1406f05c7
006F05B4  8B C7                           mov eax, edi
006F05B6  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
006F05BB  48 03 C0                        add rax, rax
006F05BE  48 C7 44 C5 B8 04 00 00 00      mov qword ptr [rbp + rax*8 - 0x48], 4
006F05C7  48 89 4C C5 B0                  mov qword ptr [rbp + rax*8 - 0x50], rcx
006F05CC  4C 8D 45 B0                     lea r8, [rbp - 0x50]
006F05D0  48 8B 93 10 03 00 00            mov rdx, qword ptr [rbx + 0x310]
006F05D7  8D 4F 01                        lea ecx, [rdi + 1]
006F05DA  8B C1                           mov eax, ecx
006F05DC  44 8D 69 01                     lea r13d, [rcx + 1]
006F05E0  48 C1 E0 04                     shl rax, 4
006F05E4  4C 03 C0                        add r8, rax
006F05E7  49 C7 40 08 04 00 00 00         mov qword ptr [r8 + 8], 4
006F05EF  48 85 D2                        test rdx, rdx
006F05F2  74 37                           je 0x1406f062b
006F05F4  48 8D 44 24 68                  lea rax, [rsp + 0x68]
006F05F9  49 89 00                        mov qword ptr [r8], rax
006F05FC  48 8D 55 B0                     lea rdx, [rbp - 0x50]
006F0600  48 8B 8B 10 03 00 00            mov rcx, qword ptr [rbx + 0x310]
006F0607  41 8B C5                        mov eax, r13d
006F060A  48 C1 E0 04                     shl rax, 4
006F060E  48 03 D0                        add rdx, rax
006F0611  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
006F0615  41 FF C5                        inc r13d
006F0618  48 89 0A                        mov qword ptr [rdx], rcx
006F061B  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
006F0622  44 89 7A 0C                     mov dword ptr [rdx + 0xc], r15d
006F0626  89 42 08                        mov dword ptr [rdx + 8], eax
006F0629  EB 08                           jmp 0x1406f0633
006F062B  48 8D 44 24 50                  lea rax, [rsp + 0x50]
006F0630  49 89 00                        mov qword ptr [r8], rax
006F0633  44 89 6C 24 64                  mov dword ptr [rsp + 0x64], r13d
006F0638  44 39 BB 20 03 00 00            cmp dword ptr [rbx + 0x320], r15d
006F063F  0F 86 0B 01 00 00               jbe 0x1406f0750
006F0645  44 8B 93 20 03 00 00            mov r10d, dword ptr [rbx + 0x320]
006F064C  33 FF                           xor edi, edi
006F064E  4C 8B 8B 18 03 00 00            mov r9, qword ptr [rbx + 0x318]
006F0655  49 8B 01                        mov rax, qword ptr [r9]
006F0658  4D 8D 49 10                     lea r9, [r9 + 0x10]
006F065C  0F B6 50 01                     movzx edx, byte ptr [rax + 1]
006F0660  8D 3C 97                        lea edi, [rdi + rdx*4]
006F0663  83 C7 0C                        add edi, 0xc
006F0666  49 83 EA 01                     sub r10, 1
006F066A  75 E9                           jne 0x1406f0655
006F066C  8B D7                           mov edx, edi
006F066E  B9 00 01 00 00                  mov ecx, 0x100
006F0673  41 B8 53 65 53 69               mov r8d, 0x69536553
006F0679  89 7C 24 74                     mov dword ptr [rsp + 0x74], edi
006F067D  E8 6E 1A 49 00                  call 0x140b820f0
006F0682  4C 8B F8                        mov r15, rax
006F0685  48 85 C0                        test rax, rax
006F0688  0F 84 85 00 00 00               je 0x1406f0713
006F068E  8B 8B 20 03 00 00               mov ecx, dword ptr [rbx + 0x320]
006F0694  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
006F0698  C7 45 8C 00 00 00 00            mov dword ptr [rbp - 0x74], 0
006F069F  85 C9                           test ecx, ecx
006F06A1  74 74                           je 0x1406f0717
006F06A3  44 8B 75 8C                     mov r14d, dword ptr [rbp - 0x74]
006F06A7  4C 8B E8                        mov r13, rax
006F06AA  48 8B 83 18 03 00 00            mov rax, qword ptr [rbx + 0x318]
006F06B1  41 8B FE                        mov edi, r14d
006F06B4  48 03 FF                        add rdi, rdi
006F06B7  8B 4C F8 08                     mov ecx, dword ptr [rax + rdi*8 + 8]
006F06BB  41 89 4D 00                     mov dword ptr [r13], ecx
006F06BF  49 8D 4D 04                     lea rcx, [r13 + 4]
006F06C3  48 8B 83 18 03 00 00            mov rax, qword ptr [rbx + 0x318]
006F06CA  48 8B 14 F8                     mov rdx, qword ptr [rax + rdi*8]
006F06CE  44 0F B6 42 01                  movzx r8d, byte ptr [rdx + 1]
006F06D3  4E 8D 04 85 08 00 00 00         lea r8, [r8*4 + 8]
006F06DB  E8 60 61 FD FF                  call 0x1406c6840
006F06E0  48 8B 83 18 03 00 00            mov rax, qword ptr [rbx + 0x318]
006F06E7  41 FF C6                        inc r14d
006F06EA  48 8B 0C F8                     mov rcx, qword ptr [rax + rdi*8]
006F06EE  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
006F06F2  8B 4C 24 54                     mov ecx, dword ptr [rsp + 0x54]
006F06F6  4D 8D 6C 85 00                  lea r13, [r13 + rax*4]
006F06FB  4D 8D 6D 0C                     lea r13, [r13 + 0xc]
006F06FF  44 3B F1                        cmp r14d, ecx
006F0702  72 A6                           jb 0x1406f06aa
006F0704  4C 8B 75 98                     mov r14, qword ptr [rbp - 0x68]
006F0708  44 8B 6C 24 64                  mov r13d, dword ptr [rsp + 0x64]
006F070D  8B 7C 24 74                     mov edi, dword ptr [rsp + 0x74]
006F0711  EB 04                           jmp 0x1406f0717
006F0713  8B 4C 24 54                     mov ecx, dword ptr [rsp + 0x54]
006F0717  41 8B C5                        mov eax, r13d
006F071A  48 8D 54 24 54                  lea rdx, [rsp + 0x54]
006F071F  48 03 C0                        add rax, rax
006F0722  41 FF C5                        inc r13d
006F0725  48 89 54 C5 B0                  mov qword ptr [rbp + rax*8 - 0x50], rdx
006F072A  48 C7 44 C5 B8 04 00 00 00      mov qword ptr [rbp + rax*8 - 0x48], 4
006F0733  85 C9                           test ecx, ecx
006F0735  74 35                           je 0x1406f076c
006F0737  41 8B C5                        mov eax, r13d
006F073A  48 03 C0                        add rax, rax
006F073D  4C 89 7C C5 B0                  mov qword ptr [rbp + rax*8 - 0x50], r15
006F0742  89 7C C5 B8                     mov dword ptr [rbp + rax*8 - 0x48], edi
006F0746  C7 44 C5 BC 00 00 00 00         mov dword ptr [rbp + rax*8 - 0x44], 0
006F074E  EB 19                           jmp 0x1406f0769
006F0750  41 8B C5                        mov eax, r13d
006F0753  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
006F0758  48 03 C0                        add rax, rax
006F075B  48 89 4C C5 B0                  mov qword ptr [rbp + rax*8 - 0x50], rcx
006F0760  48 C7 44 C5 B8 04 00 00 00      mov qword ptr [rbp + rax*8 - 0x48], 4
006F0769  41 FF C5                        inc r13d
006F076C  41 8B C5                        mov eax, r13d
006F076F  48 8D 4D B0                     lea rcx, [rbp - 0x50]
006F0773  48 C1 E0 04                     shl rax, 4
006F0777  41 8D 55 01                     lea edx, [r13 + 1]
006F077B  48 03 C8                        add rcx, rax
006F077E  48 C7 41 08 04 00 00 00         mov qword ptr [rcx + 8], 4
006F0786  4D 85 E4                        test r12, r12
006F0789  74 33                           je 0x1406f07be
006F078B  48 8D 44 24 68                  lea rax, [rsp + 0x68]
006F0790  48 89 01                        mov qword ptr [rcx], rax
006F0793  48 8D 4D B0                     lea rcx, [rbp - 0x50]
006F0797  8B C2                           mov eax, edx
006F0799  48 C1 E0 04                     shl rax, 4
006F079D  48 03 C8                        add rcx, rax
006F07A0  41 0F B6 44 24 01               movzx eax, byte ptr [r12 + 1]
006F07A6  FF C2                           inc edx
006F07A8  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
006F07AF  4C 89 21                        mov qword ptr [rcx], r12
006F07B2  89 41 08                        mov dword ptr [rcx + 8], eax
006F07B5  C7 41 0C 00 00 00 00            mov dword ptr [rcx + 0xc], 0
006F07BC  EB 08                           jmp 0x1406f07c6
006F07BE  48 8D 44 24 50                  lea rax, [rsp + 0x50]
006F07C3  48 89 01                        mov qword ptr [rcx], rax
006F07C6  45 0F B7 4E 02                  movzx r9d, word ptr [r14 + 2]
006F07CB  49 8D 4E 02                     lea rcx, [r14 + 2]
006F07CF  8B C2                           mov eax, edx
006F07D1  FF C2                           inc edx
006F07D3  48 03 C0                        add rax, rax
006F07D6  4C 89 74 C5 B0                  mov qword ptr [rbp + rax*8 - 0x50], r14
006F07DB  48 C7 44 C5 B8 01 00 00 00      mov qword ptr [rbp + rax*8 - 0x48], 1
006F07E4  8B C2                           mov eax, edx
006F07E6  FF C2                           inc edx
006F07E8  48 03 C0                        add rax, rax
006F07EB  48 89 4C C5 B0                  mov qword ptr [rbp + rax*8 - 0x50], rcx
006F07F0  48 C7 44 C5 B8 02 00 00 00      mov qword ptr [rbp + rax*8 - 0x48], 2
006F07F9  66 45 85 C9                     test r9w, r9w
006F07FD  79 0E                           jns 0x1406f080d
006F07FF  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
006F0803  85 C0                           test eax, eax
006F0805  74 0F                           je 0x1406f0816
006F0807  4D 8D 04 06                     lea r8, [r14 + rax]
006F080B  EB 04                           jmp 0x1406f0811
006F080D  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
006F0811  4D 85 C0                        test r8, r8
006F0814  75 07                           jne 0x1406f081d
006F0816  4C 8B 05 5B 93 8E 00            mov r8, qword ptr [rip + 0x8e935b]
006F081D  8B C2                           mov eax, edx
006F081F  48 8D 4D B0                     lea rcx, [rbp - 0x50]
006F0823  48 C1 E0 04                     shl rax, 4
006F0827  FF C2                           inc edx
006F0829  48 03 C8                        add rcx, rax
006F082C  41 0F B6 40 01                  movzx eax, byte ptr [r8 + 1]
006F0831  4C 89 01                        mov qword ptr [rcx], r8
006F0834  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
006F083B  89 41 08                        mov dword ptr [rcx + 8], eax
006F083E  C7 41 0C 00 00 00 00            mov dword ptr [rcx + 0xc], 0
006F0845  66 45 85 C9                     test r9w, r9w
006F0849  79 0E                           jns 0x1406f0859
006F084B  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
006F084F  85 C0                           test eax, eax
006F0851  74 0F                           je 0x1406f0862
006F0853  4D 8D 04 06                     lea r8, [r14 + rax]
006F0857  EB 04                           jmp 0x1406f085d
006F0859  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
006F085D  4D 85 C0                        test r8, r8
006F0860  75 07                           jne 0x1406f0869
006F0862  4C 8B 05 0F 93 8E 00            mov r8, qword ptr [rip + 0x8e930f]
006F0869  8B C2                           mov eax, edx
006F086B  48 8D 4D B0                     lea rcx, [rbp - 0x50]
006F086F  48 C1 E0 04                     shl rax, 4
006F0873  48 03 C8                        add rcx, rax
006F0876  41 0F B6 40 01                  movzx eax, byte ptr [r8 + 1]
006F087B  FF C2                           inc edx
006F087D  4C 89 01                        mov qword ptr [rcx], r8
006F0880  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
006F0887  89 41 08                        mov dword ptr [rcx + 8], eax
006F088A  C7 41 0C 00 00 00 00            mov dword ptr [rcx + 0xc], 0
006F0891  41 F6 C1 04                     test r9b, 4
006F0895  74 14                           je 0x1406f08ab
006F0897  66 45 85 C9                     test r9w, r9w
006F089B  79 7C                           jns 0x1406f0919
006F089D  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
006F08A1  85 C0                           test eax, eax
006F08A3  74 06                           je 0x1406f08ab
006F08A5  4D 8D 2C 06                     lea r13, [r14 + rax]
006F08A9  EB 72                           jmp 0x1406f091d
006F08AB  8B C2                           mov eax, edx
006F08AD  4C 8D 65 B0                     lea r12, [rbp - 0x50]
006F08B1  48 C1 E0 04                     shl rax, 4
006F08B5  8D 7A 01                        lea edi, [rdx + 1]
006F08B8  4C 03 E0                        add r12, rax
006F08BB  49 C7 44 24 08 01 00 00 00      mov qword ptr [r12 + 8], 1
006F08C4  4C 8B 6C 24 78                  mov r13, qword ptr [rsp + 0x78]
006F08C9  48 8D 44 24 40                  lea rax, [rsp + 0x40]
006F08CE  49 89 04 24                     mov qword ptr [r12], rax
006F08D2  48 8D 4C 24 44                  lea rcx, [rsp + 0x44]
006F08D7  8B C7                           mov eax, edi
006F08D9  48 03 C0                        add rax, rax
006F08DC  48 C7 44 C5 B8 02 00 00 00      mov qword ptr [rbp + rax*8 - 0x48], 2
006F08E5  48 89 4C C5 B0                  mov qword ptr [rbp + rax*8 - 0x50], rcx
006F08EA  41 0F B7 4E 02                  movzx ecx, word ptr [r14 + 2]
006F08EF  8D 47 01                        lea eax, [rdi + 1]
006F08F2  F6 C1 10                        test cl, 0x10
006F08F5  0F 84 1F 01 00 00               je 0x1406f0a1a
006F08FB  66 85 C9                        test cx, cx
006F08FE  0F 89 9C 00 00 00               jns 0x1406f09a0
006F0904  41 8B 4E 0C                     mov ecx, dword ptr [r14 + 0xc]
006F0908  85 C9                           test ecx, ecx
006F090A  0F 84 0A 01 00 00               je 0x1406f0a1a
006F0910  4D 8D 24 0E                     lea r12, [r14 + rcx]
006F0914  E9 8B 00 00 00                  jmp 0x1406f09a4
006F0919  4D 8B 6E 20                     mov r13, qword ptr [r14 + 0x20]
006F091D  8B C2                           mov eax, edx
006F091F  4C 8D 65 B0                     lea r12, [rbp - 0x50]
006F0923  48 C1 E0 04                     shl rax, 4
006F0927  8D 7A 01                        lea edi, [rdx + 1]
006F092A  4C 03 E0                        add r12, rax
006F092D  4D 85 ED                        test r13, r13
006F0930  74 89                           je 0x1406f08bb
006F0932  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
006F0937  49 8B CD                        mov rcx, r13
006F093A  4C 8D 44 24 6C                  lea r8, [rsp + 0x6c]
006F093F  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
006F0944  E8 D3 84 F1 FF                  call 0x140608e1c
006F0949  49 C7 44 24 08 01 00 00 00      mov qword ptr [r12 + 8], 1
006F0952  85 C0                           test eax, eax
006F0954  0F 88 6A FF FF FF               js 0x1406f08c4
006F095A  4D 89 2C 24                     mov qword ptr [r12], r13
006F095E  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
006F0963  4C 8B 6C 24 78                  mov r13, qword ptr [rsp + 0x78]
006F0968  8B C7                           mov eax, edi
006F096A  FF C7                           inc edi
006F096C  48 03 C0                        add rax, rax
006F096F  48 89 4C C5 B0                  mov qword ptr [rbp + rax*8 - 0x50], rcx
006F0974  48 8D 4D B0                     lea rcx, [rbp - 0x50]
006F0978  48 C7 44 C5 B8 02 00 00 00      mov qword ptr [rbp + rax*8 - 0x48], 2
006F0981  8B C7                           mov eax, edi
006F0983  48 C1 E0 04                     shl rax, 4
006F0987  48 03 C8                        add rcx, rax
006F098A  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
006F098E  4C 89 29                        mov qword ptr [rcx], r13
006F0991  89 41 08                        mov dword ptr [rcx + 8], eax
006F0994  C7 41 0C 00 00 00 00            mov dword ptr [rcx + 0xc], 0
006F099B  E9 4A FF FF FF                  jmp 0x1406f08ea
006F09A0  4D 8B 66 18                     mov r12, qword ptr [r14 + 0x18]
006F09A4  8D 78 01                        lea edi, [rax + 1]
006F09A7  48 C1 E0 04                     shl rax, 4
006F09AB  4C 8D 75 B0                     lea r14, [rbp - 0x50]
006F09AF  4C 03 F0                        add r14, rax
006F09B2  4D 85 E4                        test r12, r12
006F09B5  74 71                           je 0x1406f0a28
006F09B7  4C 8D 4C 24 4C                  lea r9, [rsp + 0x4c]
006F09BC  49 8B CC                        mov rcx, r12
006F09BF  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
006F09C4  48 8D 55 80                     lea rdx, [rbp - 0x80]
006F09C8  E8 4F 84 F1 FF                  call 0x140608e1c
006F09CD  49 C7 46 08 01 00 00 00         mov qword ptr [r14 + 8], 1
006F09D5  85 C0                           test eax, eax
006F09D7  78 57                           js 0x1406f0a30
006F09D9  4D 89 26                        mov qword ptr [r14], r12
006F09DC  48 8D 4C 24 4C                  lea rcx, [rsp + 0x4c]
006F09E1  4C 8B 75 80                     mov r14, qword ptr [rbp - 0x80]
006F09E5  8B C7                           mov eax, edi
006F09E7  FF C7                           inc edi
006F09E9  48 03 C0                        add rax, rax
006F09EC  48 89 4C C5 B0                  mov qword ptr [rbp + rax*8 - 0x50], rcx
006F09F1  48 8D 4D B0                     lea rcx, [rbp - 0x50]
006F09F5  48 C7 44 C5 B8 02 00 00 00      mov qword ptr [rbp + rax*8 - 0x48], 2
006F09FE  8B C7                           mov eax, edi
006F0A00  48 C1 E0 04                     shl rax, 4
006F0A04  48 03 C8                        add rcx, rax
006F0A07  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
006F0A0B  4C 89 31                        mov qword ptr [rcx], r14
006F0A0E  89 41 08                        mov dword ptr [rcx + 8], eax
006F0A11  C7 41 0C 00 00 00 00            mov dword ptr [rcx + 0xc], 0
006F0A18  EB 3A                           jmp 0x1406f0a54
006F0A1A  8D 78 01                        lea edi, [rax + 1]
006F0A1D  48 C1 E0 04                     shl rax, 4
006F0A21  4C 8D 75 B0                     lea r14, [rbp - 0x50]
006F0A25  4C 03 F0                        add r14, rax
006F0A28  49 C7 46 08 01 00 00 00         mov qword ptr [r14 + 8], 1
006F0A30  48 8D 44 24 40                  lea rax, [rsp + 0x40]
006F0A35  49 89 06                        mov qword ptr [r14], rax
006F0A38  48 8D 4C 24 44                  lea rcx, [rsp + 0x44]
006F0A3D  4C 8B 75 80                     mov r14, qword ptr [rbp - 0x80]
006F0A41  8B C7                           mov eax, edi
006F0A43  48 03 C0                        add rax, rax
006F0A46  48 C7 44 C5 B8 02 00 00 00      mov qword ptr [rbp + rax*8 - 0x48], 2
006F0A4F  48 89 4C C5 B0                  mov qword ptr [rbp + rax*8 - 0x50], rcx
006F0A54  48 8D 4D B0                     lea rcx, [rbp - 0x50]
006F0A58  45 33 C9                        xor r9d, r9d
006F0A5B  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
006F0A60  8D 47 01                        lea eax, [rdi + 1]
006F0A63  48 8B 0D BE EF 80 00            mov rcx, qword ptr [rip + 0x80efbe]
006F0A6A  48 8D 15 7F 18 93 FF            lea rdx, [rip - 0x6ce781]
006F0A71  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
006F0A75  45 33 C0                        xor r8d, r8d
006F0A78  48 C7 44 24 28 00 00 00 00      mov qword ptr [rsp + 0x28], 0
006F0A81  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
006F0A8A  E8 41 E6 B6 FF                  call 0x14025f0d0
006F0A8F  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
006F0A93  48 8B BC 24 F8 02 00 00         mov rdi, qword ptr [rsp + 0x2f8]
006F0A9B  48 85 C0                        test rax, rax
006F0A9E  74 0A                           je 0x1406f0aaa
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006F033D(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, unsigned int a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27, __int64 a28, __int64 a29, __int64 a30, __int64 a31, __int64 a32, __int64 a33, __int64 a34, __int64 a35, __int64 a36, __int64 a37, __int64 a38, __int64 a39, __int64 a40, __int64 a41, __int64 a42, __int64 a43, __int64 a44, __int64 a45, __int64 a46, __int64 a47, __int64 a48, __int64 a49, __int64 a50, __int64 a51, __int64 a52, __int64 a53, __int64 a54, __int64 a55, __int64 a56, __int64 a57, __int64 a58, __int64 a59, __int64 a60, __int64 a61, __int64 a62, __int64 a63, __int64 a64, __int64 a65, __int64 a66, __int64 a67, __int64 a68, __int64 a69, __int64 a70, __int64 a71, __int64 a72, __int64 a73, __int64 a74, __int64 a75, __int64 a76, __int64 a77, __int64 a78, __int64 a79, __int64 a80, __int64 a81, __int64 a82, __int64 a83, __int64 a84, __int64 a85, __int64 a86, __int64 a87, __int64 a88, __int64 a89, __int64 a90, __int64 a91, __int64 a92, __int64 a93, __int64 a94, __int64 a95)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rdi;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p2F8;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p41;
    unsigned __int64 v_stack_p44;
    unsigned __int64 v_stack_p4C;
    unsigned int v_stack_p54;
    unsigned __int64 v_stack_p5C;
    unsigned int v_stack_p64;
    unsigned __int64 v_stack_p6C;
    unsigned int v_stack_p74;

    v_stack_p2F8 = v_rdi;
    if (condition_is_not_equal) { result = a1; }
    *(unsigned int *)(v_rbp - 68) = (unsigned int)(v_r13);
    *(unsigned __int64 *)(v_rbp - 80) = result;
    result = 14;
    if (condition_is_not_equal) { result = 22; }
    *(unsigned int *)(v_rbp - 72) = (unsigned int)(result);
    result = SepGetLearningModeObjectInformation(v_stack_p41, a2, a3, a4);
    *(unsigned __int64 *)(v_rbp - 96) = result;
    if (result == 0) goto loc_006F03B7;
    if (*(unsigned __int64 *)(result + 16) == 0) goto loc_006F03B7;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(result + 16)) + 2) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(result + 16) + 2))) {
        a1 = (unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(result + 16) + 2));
    }
    *(unsigned __int64 *)(v_rbp - 64) = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8);
    *(unsigned int *)(v_rbp - 56) = (unsigned int)(a1);
    *(unsigned int *)(v_rbp - 52) = (unsigned int)(v_r13);
    goto loc_006F03CE;
loc_006F03B7:
    *(unsigned __int64 *)(v_rbp - 64) = v_rip - 160953;
    *(unsigned __int64 *)(v_rbp - 56) = 2;
    if (result == 0) goto loc_006F0407;
loc_006F03CE:
    if (*(unsigned __int64 *)(result + 24) == 0) goto loc_006F0407;
    if ((*(unsigned __int64 *)(result + 32)) == v_r13) goto loc_006F03EC;
    if (*(unsigned __int64 *)(result + 48) == 0) goto loc_006F03EC;
    goto loc_006F040F;
loc_006F03EC:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(result + 24)) + 2) < (*(unsigned __int16 *)(*(unsigned __int64 *)(result + 24) + 2))) {
        a1 = *(unsigned __int16 *)(*(unsigned __int64 *)(result + 24)) + 2;
    }
    goto loc_006F040F;
loc_006F0407:
loc_006F040F:
    *(unsigned __int64 *)(v_rbp - 48) = v_rip - 160953;
    v_r10 = (unsigned int)((2) + 1);
    *(unsigned int *)(v_rbp - 36) = (unsigned int)(v_r13);
    *(unsigned int *)(v_rbp - 40) = 2;
    result = ((unsigned int)((unsigned int)(v_r10))) << (4);
    a4 = (v_rbp - 80) + (result);
    v_r10 = (unsigned int)((v_r10) + 1);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 848) == 0) goto loc_006F0457;
    goto loc_006F045F;
loc_006F0457:
loc_006F045F:
    *(unsigned __int64 *)(a4) = v_rip - 160953;
    *(unsigned int *)(a4 + 8) = 2;
    *(unsigned int *)(a4 + 12) = (unsigned int)((unsigned int)((unsigned int)(v_r13)));
    result = ((unsigned int)((unsigned int)(v_r10))) + ((unsigned int)((unsigned int)(v_r10)));
    *(unsigned __int64 *)(v_rbp + result * 8 - 80) = v_rip - 160953;
    *(unsigned __int64 *)(v_rbp + result * 8 - 72) = 2;
    a2 = (unsigned int)((v_r10 + 1) + 1);
    result = ((unsigned int)((unsigned int)(v_r10 + 1))) + ((unsigned int)((unsigned int)(v_r10 + 1)));
    *(unsigned __int64 *)(v_rbp + result * 8 - 80) = v_rbp + 536;
    *(unsigned __int64 *)(v_rbp + result * 8 - 72) = 4;
    a2 = (unsigned int)((a2) + 1);
    result = ((unsigned int)((unsigned int)(a2))) + ((unsigned int)((unsigned int)(a2)));
    *(unsigned __int64 *)(v_rbp + result * 8 - 80) = v_stack_p5C;
    *(unsigned __int64 *)(v_rbp + result * 8 - 72) = 4;
    a2 = (unsigned int)((a2) + 1);
    result = ((unsigned int)((unsigned int)(a2))) + ((unsigned int)((unsigned int)(a2)));
    *(unsigned __int64 *)(v_rbp + result * 8 - 80) = a12;
    *(unsigned __int64 *)(v_rbp + result * 8 - 72) = 4;
    result = ((unsigned int)((unsigned int)(a2))) << (4);
    a1 = (v_rbp - 80) + (result);
    *(unsigned __int64 *)(a1) = v_rbx + 120;
    *(unsigned __int64 *)(a1 + 8) = 4;
    result = ((unsigned int)((unsigned int)(a2 + 1))) << (4);
    a2 = (v_rbp - 80) + (result);
    result = *(unsigned __int64 *)(v_rbx + 1080) + 40;
    if (*(unsigned __int64 *)(v_rbx + 1080) == 0) {
        result = a10;
    }
    *(unsigned __int64 *)(a2) = result;
    *(unsigned __int64 *)(a2 + 8) = 4;
    *(unsigned int *)(v_rbp - 120) = 1;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 152)) + 1) * 4 + 12)), (unsigned int)(0x69536553ULL), a4);
    *(unsigned __int64 *)(v_rbp - 112) = result;
    if (result == 0) goto loc_006F05B4;
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbx + 152) + 8)));
    result = memcpy(result + 4, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 152)), *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 152)) + 1) * 4 + 8, a4);
    a1 = ((unsigned int)((unsigned int)(a2 + 1 + 1))) + ((unsigned int)((unsigned int)(a2 + 1 + 1)));
    v_rdi = (unsigned int)((a2 + 1 + 1) + 1);
    *(unsigned __int64 *)(v_rbp + a1 * 8 - 80) = v_rbp - 120;
    *(unsigned __int64 *)(v_rbp + a1 * 8 - 72) = 4;
    result = ((unsigned int)((unsigned int)(v_rdi))) + ((unsigned int)((unsigned int)(v_rdi)));
    *(unsigned int *)(v_rbp + result * 8 - 72) = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 152)) + 1) * 4 + 12);
    *(unsigned int *)(v_rbp + result * 8 - 68) = (unsigned int)(v_r15);
    goto loc_006F05C7;
loc_006F05B4:
    result = ((unsigned int)((unsigned int)(v_rdi))) + ((unsigned int)((unsigned int)(v_rdi)));
    *(unsigned __int64 *)(v_rbp + result * 8 - 72) = 4;
loc_006F05C7:
    *(unsigned __int64 *)(v_rbp + result * 8 - 80) = a10;
    result = ((unsigned int)((unsigned int)(v_rdi + 1))) << (4);
    a3 = (v_rbp - 80) + (result);
    *(unsigned __int64 *)(a3 + 8) = 4;
    if (*(unsigned __int64 *)(v_rbx + 784) == 0) goto loc_006F062B;
    *(unsigned __int64 *)(a3) = a13;
    result = ((unsigned int)((unsigned int)(v_rdi + 1 + 1))) << (4);
    a2 = (v_rbp - 80) + (result);
    v_r13 = (unsigned int)((v_rdi + 1 + 1) + 1);
    *(unsigned __int64 *)(a2) = *(unsigned __int64 *)(v_rbx + 784);
    *(unsigned int *)(a2 + 12) = (unsigned int)(v_r15);
    *(unsigned int *)(a2 + 8) = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbx + 784) + 1) * 4 + 8);
    goto loc_006F0633;
loc_006F062B:
    *(unsigned __int64 *)(a3) = a10;
loc_006F0633:
    v_stack_p64 = (unsigned int)(v_r13);
    if ((*(unsigned int *)(v_rbx + 800)) <= ((unsigned int)(v_r15))) goto loc_006F0750;
    v_rdi = 0;
loc_006F0655:
    v_rdi = (unsigned int)((v_rdi + *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 792)) + 1) * 4) + (12));
    v_r10 = ((unsigned int)(*(unsigned int *)(v_rbx + 800))) - (1);
    if (condition_is_not_equal) goto loc_006F0655;
    v_stack_p74 = (unsigned int)(v_rdi);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x69536553ULL), *(unsigned __int64 *)(v_rbx + 792) + 16);
    if (result == 0) goto loc_006F0713;
    v_stack_p54 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 800)));
    *(unsigned int *)(v_rbp - 116) = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 800))) == 0) goto loc_006F0717;
loc_006F06AA:
    v_rdi = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp - 116))))) + ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp - 116)))));
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbx + 792) + v_rdi * 8 + 8)));
    result = memcpy(result + 4, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 792) + v_rdi * 8), *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 792) + v_rdi * 8) + 1) * 4 + 8, *(unsigned __int64 *)(v_rbx + 792) + 16);
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp - 116))) + 1);
    if (((unsigned int)(v_r14)) < ((unsigned int)((unsigned int)(v_stack_p54)))) goto loc_006F06AA;
    goto loc_006F0717;
loc_006F0713:
loc_006F0717:
    result = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p64)))) + ((unsigned int)((unsigned int)((unsigned int)(v_stack_p64))));
    v_r13 = (unsigned int)(((unsigned int)(v_stack_p64)) + 1);
    *(unsigned __int64 *)(v_rbp + result * 8 - 80) = v_stack_p54;
    *(unsigned __int64 *)(v_rbp + result * 8 - 72) = 4;
    if ((unsigned int)((unsigned int)(v_stack_p54)) == 0) goto loc_006F076C;
    result = ((unsigned int)((unsigned int)(v_r13))) + ((unsigned int)((unsigned int)(v_r13)));
    *(unsigned __int64 *)(v_rbp + result * 8 - 80) = result;
    *(unsigned int *)(v_rbp + result * 8 - 72) = (unsigned int)((unsigned int)(v_stack_p74));
    *(unsigned int *)(v_rbp + result * 8 - 68) = 0;
    goto loc_006F0769;
loc_006F0750:
    result = ((unsigned int)((unsigned int)(v_r13))) + ((unsigned int)((unsigned int)(v_r13)));
    *(unsigned __int64 *)(v_rbp + result * 8 - 80) = a10;
    *(unsigned __int64 *)(v_rbp + result * 8 - 72) = 4;
loc_006F0769:
    v_r13 = (unsigned int)((v_r13) + 1);
loc_006F076C:
    result = ((unsigned int)((unsigned int)(v_r13))) << (4);
    a1 = (v_rbp - 80) + (result);
    *(unsigned __int64 *)(a1 + 8) = 4;
    if (v_r12 == 0) goto loc_006F07BE;
    *(unsigned __int64 *)(a1) = a13;
    result = ((unsigned int)((unsigned int)(v_r13 + 1))) << (4);
    a1 = (v_rbp - 80) + (result);
    a2 = (unsigned int)((v_r13 + 1) + 1);
    *(unsigned __int64 *)(a1) = v_r12;
    *(unsigned int *)(a1 + 8) = (unsigned int)(*(unsigned __int8 *)(v_r12 + 1) * 4 + 8);
    *(unsigned int *)(a1 + 12) = 0;
    goto loc_006F07C6;
loc_006F07BE:
    *(unsigned __int64 *)(a1) = a10;
loc_006F07C6:
    a2 = (unsigned int)((a2) + 1);
    result = ((unsigned int)((unsigned int)(a2))) + ((unsigned int)((unsigned int)(a2)));
    *(unsigned __int64 *)(v_rbp + result * 8 - 80) = *(unsigned __int64 *)(v_rbp - 104);
    *(unsigned __int64 *)(v_rbp + result * 8 - 72) = 1;
    a2 = (unsigned int)((a2) + 1);
    result = ((unsigned int)((unsigned int)(a2))) + ((unsigned int)((unsigned int)(a2)));
    *(unsigned __int64 *)(v_rbp + result * 8 - 80) = *(unsigned __int64 *)(v_rbp - 104) + 2;
    *(unsigned __int64 *)(v_rbp + result * 8 - 72) = 2;
    if (!sign_flag) goto loc_006F080D;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 104) + 4))) == 0) goto loc_006F0816;
    goto loc_006F0811;
loc_006F080D:
loc_006F0811:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 104) + 8) == 0) {
        a3 = *(unsigned __int64 *)(v_rip + 9343835);
    }
    result = ((unsigned int)((unsigned int)(a2))) << (4);
    a2 = (unsigned int)((a2) + 1);
    a1 = (v_rbp - 80) + (result);
    *(unsigned __int64 *)(a1) = a3;
    *(unsigned int *)(a1 + 8) = (unsigned int)(*(unsigned __int8 *)(a3 + 1) * 4 + 8);
    *(unsigned int *)(a1 + 12) = 0;
    if (!sign_flag) goto loc_006F0859;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 104) + 4))) == 0) goto loc_006F0862;
    goto loc_006F085D;
loc_006F0859:
loc_006F085D:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 104) + 8) == 0) {
        a3 = *(unsigned __int64 *)(v_rip + 9343759);
    }
    result = ((unsigned int)((unsigned int)(a2))) << (4);
    a1 = (v_rbp - 80) + (result);
    a2 = (unsigned int)((a2) + 1);
    *(unsigned __int64 *)(a1) = a3;
    *(unsigned int *)(a1 + 8) = (unsigned int)(*(unsigned __int8 *)(a3 + 1) * 4 + 8);
    *(unsigned int *)(a1 + 12) = 0;
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp - 104) + 2))) & (4)) == 0) goto loc_006F08AB;
    if (!sign_flag) goto loc_006F0919;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 104) + 16))) == 0) goto loc_006F08AB;
    goto loc_006F091D;
loc_006F08AB:
    result = ((unsigned int)((unsigned int)(a2))) << (4);
    v_r12 = (v_rbp - 80) + (result);
loc_006F08BB:
    *(unsigned __int64 *)(v_r12 + 8) = 1;
loc_006F08C4:
    *(unsigned __int64 *)(v_r12) = a8;
    result = ((unsigned int)((unsigned int)(a2 + 1))) + ((unsigned int)((unsigned int)(a2 + 1)));
    *(unsigned __int64 *)(v_rbp + result * 8 - 72) = 2;
    *(unsigned __int64 *)(v_rbp + result * 8 - 80) = v_stack_p44;
loc_006F08EA:
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp - 104) + 2))) & (16)) == 0) goto loc_006F0A1A;
    if (!sign_flag) goto loc_006F09A0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 104) + 12))) == 0) goto loc_006F0A1A;
    goto loc_006F09A4;
loc_006F0919:
loc_006F091D:
    result = ((unsigned int)((unsigned int)(a2))) << (4);
    v_r12 = (v_rbp - 80) + (result);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 104) + 32) == 0) goto loc_006F08BB;
    result = SepFlattenAcl(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 104) + 32), a15, v_stack_p6C, a9);
    *(unsigned __int64 *)(v_r12 + 8) = 1;
    if (sign_flag) goto loc_006F08C4;
    *(unsigned __int64 *)(v_r12) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 104) + 32);
    v_rdi = (unsigned int)((a2 + 1) + 1);
    result = ((unsigned int)((unsigned int)(a2 + 1))) + ((unsigned int)((unsigned int)(a2 + 1)));
    *(unsigned __int64 *)(v_rbp + result * 8 - 80) = a9;
    *(unsigned __int64 *)(v_rbp + result * 8 - 72) = 2;
    result = ((unsigned int)((unsigned int)(v_rdi))) << (4);
    a1 = (v_rbp - 80) + (result);
    *(unsigned __int64 *)(a1) = a15;
    *(unsigned int *)(a1 + 8) = (unsigned int)((unsigned int)(v_stack_p6C));
    *(unsigned int *)(a1 + 12) = 0;
    goto loc_006F08EA;
loc_006F09A0:
loc_006F09A4:
    result = ((unsigned int)(v_stack_p6C)) << (4);
    v_r14 = (v_rbp - 80) + (result);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 104) + 24) == 0) goto loc_006F0A28;
    result = SepFlattenAcl(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 104) + 24), v_rbp - 128, a14, v_stack_p4C);
    *(unsigned __int64 *)(v_r14 + 8) = 1;
    if (sign_flag) goto loc_006F0A30;
    *(unsigned __int64 *)(v_r14) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 104) + 24);
    v_rdi = (unsigned int)(((unsigned int)(v_stack_p6C) + 1) + 1);
    result = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p6C) + 1))) + ((unsigned int)((unsigned int)((unsigned int)(v_stack_p6C) + 1)));
    *(unsigned __int64 *)(v_rbp + result * 8 - 80) = v_stack_p4C;
    *(unsigned __int64 *)(v_rbp + result * 8 - 72) = 2;
    result = ((unsigned int)((unsigned int)(v_rdi))) << (4);
    a1 = (v_rbp - 80) + (result);
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(v_rbp - 128);
    *(unsigned int *)(a1 + 8) = (unsigned int)((unsigned int)(a14));
    *(unsigned int *)(a1 + 12) = 0;
    goto loc_006F0A54;
loc_006F0A1A:
    result = ((unsigned int)(a14)) << (4);
    v_r14 = (v_rbp - 80) + (result);
loc_006F0A28:
    *(unsigned __int64 *)(v_r14 + 8) = 1;
loc_006F0A30:
    *(unsigned __int64 *)(v_r14) = a8;
    result = ((unsigned int)((unsigned int)((unsigned int)(a14) + 1))) + ((unsigned int)((unsigned int)((unsigned int)(a14) + 1)));
    *(unsigned __int64 *)(v_rbp + result * 8 - 72) = 2;
    *(unsigned __int64 *)(v_rbp + result * 8 - 80) = v_stack_p44;
loc_006F0A54:
    a4 = 0;
    v_stack_p38 = v_rbp - 80;
    v_stack_p30 = (unsigned int)((unsigned int)(a14) + 1 + 1);
    a3 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = EtwWriteEx(*(unsigned __int64 *)(v_rip + 8449982), v_rip - 7137153, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_006F033D(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10, uint64_t Arg11, int64_t Arg12, int64_t Arg13, uint32_t Arg14, int64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, uint64_t Arg24, uint64_t Arg25, uint64_t Arg26, uint64_t Arg27, uint64_t Arg28, uint64_t Arg29, uint64_t Arg30, uint64_t Arg31, uint64_t Arg32, uint64_t Arg33, uint64_t Arg34, uint64_t Arg35, uint64_t Arg36, uint64_t Arg37, uint64_t Arg38, uint64_t Arg39, uint64_t Arg40, uint64_t Arg41, uint64_t Arg42, uint64_t Arg43, uint64_t Arg44, uint64_t Arg45, uint64_t Arg46, uint64_t Arg47, uint64_t Arg48, uint64_t Arg49, uint64_t Arg50, uint64_t Arg51, uint64_t Arg52, uint64_t Arg53, uint64_t Arg54, uint64_t Arg55, uint64_t Arg56, uint64_t Arg57, uint64_t Arg58, uint64_t Arg59, uint64_t Arg60, uint64_t Arg61, uint64_t Arg62, uint64_t Arg63, uint64_t Arg64, uint64_t Arg65, uint64_t Arg66, uint64_t Arg67, uint64_t Arg68, uint64_t Arg69, uint64_t Arg70, uint64_t Arg71, uint64_t Arg72, uint64_t Arg73, uint64_t Arg74, uint64_t Arg75, uint64_t Arg76, uint64_t Arg77, uint64_t Arg78, uint64_t Arg79, uint64_t Arg80, uint64_t Arg81, uint64_t Arg82, uint64_t Arg83, uint64_t Arg84, uint64_t Arg85, uint64_t Arg86, uint64_t Arg87, uint64_t Arg88, uint64_t Arg89, uint64_t Arg90, uint64_t Arg91, uint64_t Arg92, uint64_t Arg93, uint64_t Arg94, int64_t Arg95)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rdi;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p2F8;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p41;
    uint64_t v_stack_p44;
    uint64_t v_stack_p4C;
    uint32_t v_stack_p54;
    uint64_t v_stack_p5C;
    uint32_t v_stack_p64;
    uint64_t v_stack_p6C;
    uint32_t v_stack_p74;

    v_stack_p2F8 = local_rdi;
    if (condition_is_not_equal) { result = Arg1; }
    *(uint32_t *)(local_rbp - 0x44) = (uint32_t)(local_r13);
    *(uint64_t *)(local_rbp - 0x50) = result;
    result = 14;
    if (condition_is_not_equal) { result = 22; }
    *(uint32_t *)(local_rbp - 0x48) = (uint32_t)(result);
    result = SepGetLearningModeObjectInformation(v_stack_p41, Arg2, Arg3, Arg4);
    *(uint64_t *)(local_rbp - 0x60) = result;
    if (result == 0) goto loc_006F03B7;
    if (*(uint64_t *)(result + 0x10) == 0) goto loc_006F03B7;
    if ((*(uint16_t *)(*(uint64_t *)(result + 0x10)) + 2) >= (*(uint16_t *)(*(uint64_t *)(result + 0x10) + 0x2))) {
        Arg1 = (uint32_t)(*(uint16_t *)(*(uint64_t *)(result + 0x10) + 0x2));
    }
    *(uint64_t *)(local_rbp - 0x40) = *(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8);
    *(uint32_t *)(local_rbp - 0x38) = (uint32_t)(Arg1);
    *(uint32_t *)(local_rbp - 0x34) = (uint32_t)(local_r13);
    goto loc_006F03CE;
loc_006F03B7:
    *(uint64_t *)(local_rbp - 0x40) = v_rip - 160953;
    *(uint64_t *)(local_rbp - 0x38) = 2;
    if (result == 0) goto loc_006F0407;
loc_006F03CE:
    if (*(uint64_t *)(result + 0x18) == 0) goto loc_006F0407;
    if ((*(uint64_t *)(result + 0x20)) == local_r13) goto loc_006F03EC;
    if (*(uint64_t *)(result + 0x30) == 0) goto loc_006F03EC;
    goto loc_006F040F;
loc_006F03EC:
    if ((*(uint16_t *)(*(uint64_t *)(result + 0x18)) + 2) < (*(uint16_t *)(*(uint64_t *)(result + 0x18) + 0x2))) {
        Arg1 = *(uint16_t *)(*(uint64_t *)(result + 0x18)) + 2;
    }
    goto loc_006F040F;
loc_006F0407:
loc_006F040F:
    *(uint64_t *)(local_rbp - 0x30) = v_rip - 160953;
    local_r10 = (uint32_t)((2) + 1);
    *(uint32_t *)(local_rbp - 0x24) = (uint32_t)(local_r13);
    *(uint32_t *)(local_rbp - 0x28) = 2;
    result = ((uint32_t)((uint32_t)(local_r10))) << (4);
    Arg4 = (local_rbp - 80) + (result);
    local_r10 = (uint32_t)((local_r10) + 1);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x350) == 0) goto loc_006F0457;
    goto loc_006F045F;
loc_006F0457:
loc_006F045F:
    *(uint64_t *)(Arg4) = v_rip - 160953;
    *(uint32_t *)(Arg4 + 0x8) = 2;
    *(uint32_t *)(Arg4 + 0xC) = (uint32_t)((uint32_t)((uint32_t)(local_r13)));
    result = ((uint32_t)((uint32_t)(local_r10))) + ((uint32_t)((uint32_t)(local_r10)));
    *(uint64_t *)(local_rbp + result * 8 - 0x50) = v_rip - 160953;
    *(uint64_t *)(local_rbp + result * 8 - 0x48) = 2;
    Arg2 = (uint32_t)((local_r10 + 1) + 1);
    result = ((uint32_t)((uint32_t)(local_r10 + 1))) + ((uint32_t)((uint32_t)(local_r10 + 1)));
    *(uint64_t *)(local_rbp + result * 8 - 0x50) = local_rbp + 536;
    *(uint64_t *)(local_rbp + result * 8 - 0x48) = 4;
    Arg2 = (uint32_t)((Arg2) + 1);
    result = ((uint32_t)((uint32_t)(Arg2))) + ((uint32_t)((uint32_t)(Arg2)));
    *(uint64_t *)(local_rbp + result * 8 - 0x50) = v_stack_p5C;
    *(uint64_t *)(local_rbp + result * 8 - 0x48) = 4;
    Arg2 = (uint32_t)((Arg2) + 1);
    result = ((uint32_t)((uint32_t)(Arg2))) + ((uint32_t)((uint32_t)(Arg2)));
    *(uint64_t *)(local_rbp + result * 8 - 0x50) = Arg12;
    *(uint64_t *)(local_rbp + result * 8 - 0x48) = 4;
    result = ((uint32_t)((uint32_t)(Arg2))) << (4);
    Arg1 = (local_rbp - 80) + (result);
    *(uint64_t *)(Arg1) = local_rbx + 120;
    *(uint64_t *)(Arg1 + 0x8) = 4;
    result = ((uint32_t)((uint32_t)(Arg2 + 1))) << (4);
    Arg2 = (local_rbp - 80) + (result);
    result = *(uint64_t *)(local_rbx + 0x438) + 40;
    if (*(uint64_t *)(local_rbx + 0x438) == 0) {
        result = Arg10;
    }
    *(uint64_t *)(Arg2) = result;
    *(uint64_t *)(Arg2 + 0x8) = 4;
    *(uint32_t *)(local_rbp - 0x78) = 1;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x98)) + 0x1) * 4 + 12)), (uint32_t)(0x69536553ULL), Arg4);
    *(uint64_t *)(local_rbp - 0x70) = result;
    if (result == 0) goto loc_006F05B4;
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbx + 0x98) + 0x8)));
    result = memcpy(result + 4, *(uint64_t *)(*(uint64_t *)(local_rbx + 0x98)), *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x98)) + 0x1) * 4 + 8, Arg4);
    Arg1 = ((uint32_t)((uint32_t)(Arg2 + 1 + 1))) + ((uint32_t)((uint32_t)(Arg2 + 1 + 1)));
    local_rdi = (uint32_t)((Arg2 + 1 + 1) + 1);
    *(uint64_t *)(local_rbp + Arg1 * 8 - 0x50) = local_rbp - 120;
    *(uint64_t *)(local_rbp + Arg1 * 8 - 0x48) = 4;
    result = ((uint32_t)((uint32_t)(local_rdi))) + ((uint32_t)((uint32_t)(local_rdi)));
    *(uint32_t *)(local_rbp + result * 8 - 0x48) = (uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x98)) + 0x1) * 4 + 12);
    *(uint32_t *)(local_rbp + result * 8 - 0x44) = (uint32_t)(local_r15);
    goto loc_006F05C7;
loc_006F05B4:
    result = ((uint32_t)((uint32_t)(local_rdi))) + ((uint32_t)((uint32_t)(local_rdi)));
    *(uint64_t *)(local_rbp + result * 8 - 0x48) = 4;
loc_006F05C7:
    *(uint64_t *)(local_rbp + result * 8 - 0x50) = Arg10;
    result = ((uint32_t)((uint32_t)(local_rdi + 1))) << (4);
    Arg3 = (local_rbp - 80) + (result);
    *(uint64_t *)(Arg3 + 0x8) = 4;
    if (*(uint64_t *)(local_rbx + 0x310) == 0) goto loc_006F062B;
    *(uint64_t *)(Arg3) = Arg13;
    result = ((uint32_t)((uint32_t)(local_rdi + 1 + 1))) << (4);
    Arg2 = (local_rbp - 80) + (result);
    local_r13 = (uint32_t)((local_rdi + 1 + 1) + 1);
    *(uint64_t *)(Arg2) = *(uint64_t *)(local_rbx + 0x310);
    *(uint32_t *)(Arg2 + 0xC) = (uint32_t)(local_r15);
    *(uint32_t *)(Arg2 + 0x8) = (uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rbx + 0x310) + 0x1) * 4 + 8);
    goto loc_006F0633;
loc_006F062B:
    *(uint64_t *)(Arg3) = Arg10;
loc_006F0633:
    v_stack_p64 = (uint32_t)(local_r13);
    if ((*(uint32_t *)(local_rbx + 0x320)) <= ((uint32_t)(local_r15))) goto loc_006F0750;
    local_rdi = 0;
loc_006F0655:
    local_rdi = (uint32_t)((local_rdi + *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x318)) + 0x1) * 4) + (12));
    local_r10 = ((uint32_t)(*(uint32_t *)(local_rbx + 0x320))) - (1);
    if (condition_is_not_equal) goto loc_006F0655;
    v_stack_p74 = (uint32_t)(local_rdi);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x69536553ULL), *(uint64_t *)(local_rbx + 0x318) + 16);
    if (result == 0) goto loc_006F0713;
    v_stack_p54 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x320)));
    *(uint32_t *)(local_rbp - 0x74) = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x320))) == 0) goto loc_006F0717;
loc_006F06AA:
    local_rdi = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x74))))) + ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x74)))));
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbx + 0x318) + local_rdi * 8 + 0x8)));
    result = memcpy(result + 4, *(uint64_t *)(*(uint64_t *)(local_rbx + 0x318) + local_rdi * 8), *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x318) + local_rdi * 8) + 0x1) * 4 + 8, *(uint64_t *)(local_rbx + 0x318) + 16);
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp - 0x74))) + 1);
    if (((uint32_t)(local_r14)) < ((uint32_t)((uint32_t)(v_stack_p54)))) goto loc_006F06AA;
    goto loc_006F0717;
loc_006F0713:
loc_006F0717:
    result = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p64)))) + ((uint32_t)((uint32_t)((uint32_t)(v_stack_p64))));
    local_r13 = (uint32_t)(((uint32_t)(v_stack_p64)) + 1);
    *(uint64_t *)(local_rbp + result * 8 - 0x50) = v_stack_p54;
    *(uint64_t *)(local_rbp + result * 8 - 0x48) = 4;
    if ((uint32_t)((uint32_t)(v_stack_p54)) == 0) goto loc_006F076C;
    result = ((uint32_t)((uint32_t)(local_r13))) + ((uint32_t)((uint32_t)(local_r13)));
    *(uint64_t *)(local_rbp + result * 8 - 0x50) = result;
    *(uint32_t *)(local_rbp + result * 8 - 0x48) = (uint32_t)((uint32_t)(v_stack_p74));
    *(uint32_t *)(local_rbp + result * 8 - 0x44) = 0;
    goto loc_006F0769;
loc_006F0750:
    result = ((uint32_t)((uint32_t)(local_r13))) + ((uint32_t)((uint32_t)(local_r13)));
    *(uint64_t *)(local_rbp + result * 8 - 0x50) = Arg10;
    *(uint64_t *)(local_rbp + result * 8 - 0x48) = 4;
loc_006F0769:
    local_r13 = (uint32_t)((local_r13) + 1);
loc_006F076C:
    result = ((uint32_t)((uint32_t)(local_r13))) << (4);
    Arg1 = (local_rbp - 80) + (result);
    *(uint64_t *)(Arg1 + 0x8) = 4;
    if (local_r12 == 0) goto loc_006F07BE;
    *(uint64_t *)(Arg1) = Arg13;
    result = ((uint32_t)((uint32_t)(local_r13 + 1))) << (4);
    Arg1 = (local_rbp - 80) + (result);
    Arg2 = (uint32_t)((local_r13 + 1) + 1);
    *(uint64_t *)(Arg1) = local_r12;
    *(uint32_t *)(Arg1 + 0x8) = (uint32_t)(*(uint8_t *)(local_r12 + 0x1) * 4 + 8);
    *(uint32_t *)(Arg1 + 0xC) = 0;
    goto loc_006F07C6;
loc_006F07BE:
    *(uint64_t *)(Arg1) = Arg10;
loc_006F07C6:
    Arg2 = (uint32_t)((Arg2) + 1);
    result = ((uint32_t)((uint32_t)(Arg2))) + ((uint32_t)((uint32_t)(Arg2)));
    *(uint64_t *)(local_rbp + result * 8 - 0x50) = *(uint64_t *)(local_rbp - 0x68);
    *(uint64_t *)(local_rbp + result * 8 - 0x48) = 1;
    Arg2 = (uint32_t)((Arg2) + 1);
    result = ((uint32_t)((uint32_t)(Arg2))) + ((uint32_t)((uint32_t)(Arg2)));
    *(uint64_t *)(local_rbp + result * 8 - 0x50) = *(uint64_t *)(local_rbp - 0x68) + 2;
    *(uint64_t *)(local_rbp + result * 8 - 0x48) = 2;
    if (!sign_flag) goto loc_006F080D;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x68) + 0x4))) == 0) goto loc_006F0816;
    goto loc_006F0811;
loc_006F080D:
loc_006F0811:
    if (*(uint64_t *)(*(uint64_t *)(local_rbp - 0x68) + 0x8) == 0) {
        Arg3 = *(uint64_t *)(v_rip + 0x8E935B);
    }
    result = ((uint32_t)((uint32_t)(Arg2))) << (4);
    Arg2 = (uint32_t)((Arg2) + 1);
    Arg1 = (local_rbp - 80) + (result);
    *(uint64_t *)(Arg1) = Arg3;
    *(uint32_t *)(Arg1 + 0x8) = (uint32_t)(*(uint8_t *)(Arg3 + 0x1) * 4 + 8);
    *(uint32_t *)(Arg1 + 0xC) = 0;
    if (!sign_flag) goto loc_006F0859;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x68) + 0x4))) == 0) goto loc_006F0862;
    goto loc_006F085D;
loc_006F0859:
loc_006F085D:
    if (*(uint64_t *)(*(uint64_t *)(local_rbp - 0x68) + 0x8) == 0) {
        Arg3 = *(uint64_t *)(v_rip + 0x8E930F);
    }
    result = ((uint32_t)((uint32_t)(Arg2))) << (4);
    Arg1 = (local_rbp - 80) + (result);
    Arg2 = (uint32_t)((Arg2) + 1);
    *(uint64_t *)(Arg1) = Arg3;
    *(uint32_t *)(Arg1 + 0x8) = (uint32_t)(*(uint8_t *)(Arg3 + 0x1) * 4 + 8);
    *(uint32_t *)(Arg1 + 0xC) = 0;
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(local_rbp - 0x68) + 0x2))) & (4)) == 0) goto loc_006F08AB;
    if (!sign_flag) goto loc_006F0919;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x68) + 0x10))) == 0) goto loc_006F08AB;
    goto loc_006F091D;
loc_006F08AB:
    result = ((uint32_t)((uint32_t)(Arg2))) << (4);
    local_r12 = (local_rbp - 80) + (result);
loc_006F08BB:
    *(uint64_t *)(local_r12 + 0x8) = 1;
loc_006F08C4:
    *(uint64_t *)(local_r12) = Arg8;
    result = ((uint32_t)((uint32_t)(Arg2 + 1))) + ((uint32_t)((uint32_t)(Arg2 + 1)));
    *(uint64_t *)(local_rbp + result * 8 - 0x48) = 2;
    *(uint64_t *)(local_rbp + result * 8 - 0x50) = v_stack_p44;
loc_006F08EA:
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(local_rbp - 0x68) + 0x2))) & (16)) == 0) goto loc_006F0A1A;
    if (!sign_flag) goto loc_006F09A0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x68) + 0xC))) == 0) goto loc_006F0A1A;
    goto loc_006F09A4;
loc_006F0919:
loc_006F091D:
    result = ((uint32_t)((uint32_t)(Arg2))) << (4);
    local_r12 = (local_rbp - 80) + (result);
    if (*(uint64_t *)(*(uint64_t *)(local_rbp - 0x68) + 0x20) == 0) goto loc_006F08BB;
    result = SepFlattenAcl(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x68) + 0x20), Arg15, v_stack_p6C, Arg9);
    *(uint64_t *)(local_r12 + 0x8) = 1;
    if (sign_flag) goto loc_006F08C4;
    *(uint64_t *)(local_r12) = *(uint64_t *)(*(uint64_t *)(local_rbp - 0x68) + 0x20);
    local_rdi = (uint32_t)((Arg2 + 1) + 1);
    result = ((uint32_t)((uint32_t)(Arg2 + 1))) + ((uint32_t)((uint32_t)(Arg2 + 1)));
    *(uint64_t *)(local_rbp + result * 8 - 0x50) = Arg9;
    *(uint64_t *)(local_rbp + result * 8 - 0x48) = 2;
    result = ((uint32_t)((uint32_t)(local_rdi))) << (4);
    Arg1 = (local_rbp - 80) + (result);
    *(uint64_t *)(Arg1) = Arg15;
    *(uint32_t *)(Arg1 + 0x8) = (uint32_t)((uint32_t)(v_stack_p6C));
    *(uint32_t *)(Arg1 + 0xC) = 0;
    goto loc_006F08EA;
loc_006F09A0:
loc_006F09A4:
    result = ((uint32_t)(v_stack_p6C)) << (4);
    local_r14 = (local_rbp - 80) + (result);
    if (*(uint64_t *)(*(uint64_t *)(local_rbp - 0x68) + 0x18) == 0) goto loc_006F0A28;
    result = SepFlattenAcl(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x68) + 0x18), local_rbp - 128, Arg14, v_stack_p4C);
    *(uint64_t *)(local_r14 + 0x8) = 1;
    if (sign_flag) goto loc_006F0A30;
    *(uint64_t *)(local_r14) = *(uint64_t *)(*(uint64_t *)(local_rbp - 0x68) + 0x18);
    local_rdi = (uint32_t)(((uint32_t)(v_stack_p6C) + 1) + 1);
    result = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p6C) + 1))) + ((uint32_t)((uint32_t)((uint32_t)(v_stack_p6C) + 1)));
    *(uint64_t *)(local_rbp + result * 8 - 0x50) = v_stack_p4C;
    *(uint64_t *)(local_rbp + result * 8 - 0x48) = 2;
    result = ((uint32_t)((uint32_t)(local_rdi))) << (4);
    Arg1 = (local_rbp - 80) + (result);
    *(uint64_t *)(Arg1) = *(uint64_t *)(local_rbp - 0x80);
    *(uint32_t *)(Arg1 + 0x8) = (uint32_t)((uint32_t)(Arg14));
    *(uint32_t *)(Arg1 + 0xC) = 0;
    goto loc_006F0A54;
loc_006F0A1A:
    result = ((uint32_t)(Arg14)) << (4);
    local_r14 = (local_rbp - 80) + (result);
loc_006F0A28:
    *(uint64_t *)(local_r14 + 0x8) = 1;
loc_006F0A30:
    *(uint64_t *)(local_r14) = Arg8;
    result = ((uint32_t)((uint32_t)((uint32_t)(Arg14) + 1))) + ((uint32_t)((uint32_t)((uint32_t)(Arg14) + 1)));
    *(uint64_t *)(local_rbp + result * 8 - 0x48) = 2;
    *(uint64_t *)(local_rbp + result * 8 - 0x50) = v_stack_p44;
loc_006F0A54:
    Arg4 = 0;
    v_stack_p38 = local_rbp - 80;
    v_stack_p30 = (uint32_t)((uint32_t)(Arg14) + 1 + 1);
    Arg3 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = EtwWriteEx(*(uint64_t *)(v_rip + 0x80EFBE), v_rip - 7137153, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F033D&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
