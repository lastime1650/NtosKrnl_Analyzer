# RtlpCreateFunctionOverrideFixupInfo

- RVA: `0x009433D8`–`0x009439B5` (길이 `1,501` bytes)
- VA: `0x00000001409433D8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00090570`
- 디코드: `379`개 명령, `1,501/1,501` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0094344F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0094352C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009436EC` → [RtlpParseFunctionOverrideRelocations](RtlpParseFunctionOverrideRelocations_function_00943A68.md) (function, `0x00943A68`)
- `0x00943771` → [RtlpAllocateFunctionOverrideInfo](RtlpAllocateFunctionOverrideInfo_function_009442CC.md) (function, `0x009442CC`)
- `0x009437FA` → [gsl::details::terminate](../../text/4F/gsl_details_terminate_function_004F9AA0.md) (function, `0x004F9AA0`)
- `0x00943803` → [RtlpSortAndValidateRelocations](RtlpSortAndValidateRelocations_function_009439BC.md) (function, `0x009439BC`)
- `0x009438BE` → [RtlpParseFunctionOverrideRelocations](RtlpParseFunctionOverrideRelocations_function_00943A68.md) (function, `0x00943A68`)
- `0x0094390F` → [RtlpParseBinaryDecisionDiagram](RtlpParseBinaryDecisionDiagram_function_00943F94.md) (function, `0x00943F94`)
- `0x009439AB` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)

### Direct callers
- [RtlCreateFunctionOverrideFixupInfo](RtlCreateFunctionOverrideFixupInfo_function_00943034.md) at `0x0094316D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0094344F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0094352C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009437FA` → [gsl::details::terminate](../../text/4F/gsl_details_terminate_function_004F9AA0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009433D8  48 8B C4                        mov rax, rsp
009433DB  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
009433DF  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
009433E3  89 50 10                        mov dword ptr [rax + 0x10], edx
009433E6  55                              push rbp
009433E7  53                              push rbx
009433E8  56                              push rsi
009433E9  57                              push rdi
009433EA  41 54                           push r12
009433EC  41 55                           push r13
009433EE  41 56                           push r14
009433F0  41 57                           push r15
009433F2  48 8D 68 B8                     lea rbp, [rax - 0x48]
009433F6  48 81 EC 08 01 00 00            sub rsp, 0x108
009433FD  0F 10 09                        movups xmm1, xmmword ptr [rcx]
00943400  45 33 ED                        xor r13d, r13d
00943403  44 8B D2                        mov r10d, edx
00943406  0F 29 70 A8                     movaps xmmword ptr [rax - 0x58], xmm6
0094340A  0F 57 C0                        xorps xmm0, xmm0
0094340D  33 C0                           xor eax, eax
0094340F  41 C1 EA 0C                     shr r10d, 0xc
00943413  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00943417  66 48 0F 7E C9                  movq rcx, xmm1
0094341C  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00943420  8B FA                           mov edi, edx
00943422  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
00943426  0F 29 4C 24 40                  movaps xmmword ptr [rsp + 0x40], xmm1
0094342B  4C 89 6D 80                     mov qword ptr [rbp - 0x80], r13
0094342F  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
00943433  4C 21 28                        and qword ptr [rax], r13
00943436  48 83 F9 04                     cmp rcx, 4
0094343A  73 3F                           jae 0x14094347b
0094343C  BF 7B 00 00 C0                  mov edi, 0xc000007b
00943441  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
00943445  48 85 C0                        test rax, rax
00943448  74 0A                           je 0x140943454
0094344A  33 D2                           xor edx, edx
0094344C  48 8B C8                        mov rcx, rax
0094344F  E8 1C F4 23 00                  call 0x140b82870
00943454  85 FF                           test edi, edi
00943456  0F 88 43 05 00 00               js 0x14094399f
0094345C  0F 28 B4 24 F0 00 00 00         movaps xmm6, xmmword ptr [rsp + 0xf0]
00943464  8B C7                           mov eax, edi
00943466  48 81 C4 08 01 00 00            add rsp, 0x108
0094346D  41 5F                           pop r15
0094346F  41 5E                           pop r14
00943471  41 5D                           pop r13
00943473  41 5C                           pop r12
00943475  5F                              pop rdi
00943476  5E                              pop rsi
00943477  5B                              pop rbx
00943478  5D                              pop rbp
00943479  C3                              ret
0094347A  CC                              int3
0094347B  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00943480  48 83 C1 FC                     add rcx, -4
00943484  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00943489  48 8D 42 04                     lea rax, [rdx + 4]
0094348D  48 83 F9 FF                     cmp rcx, -1
00943491  0F 84 63 03 00 00               je 0x1409437fa
00943497  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0094349C  0F 28 44 24 40                  movaps xmm0, xmmword ptr [rsp + 0x40]
009434A1  66 0F 7F 44 24 40               movdqa xmmword ptr [rsp + 0x40], xmm0
009434A7  48 85 D2                        test rdx, rdx
009434AA  74 90                           je 0x14094343c
009434AC  8B 02                           mov eax, dword ptr [rdx]
009434AE  85 C0                           test eax, eax
009434B0  74 8A                           je 0x14094343c
009434B2  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009434B7  8B F0                           mov esi, eax
009434B9  48 3B C1                        cmp rax, rcx
009434BC  0F 83 7A FF FF FF               jae 0x14094343c
009434C2  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
009434C7  48 8B D1                        mov rdx, rcx
009434CA  48 2B D6                        sub rdx, rsi
009434CD  49 03 C7                        add rax, r15
009434D0  48 89 55 B0                     mov qword ptr [rbp - 0x50], rdx
009434D4  48 83 FA FF                     cmp rdx, -1
009434D8  0F 84 1C 03 00 00               je 0x1409437fa
009434DE  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
009434E2  48 3B F1                        cmp rsi, rcx
009434E5  0F 87 0F 03 00 00               ja 0x1409437fa
009434EB  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
009434F0  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
009434F5  4D 85 FF                        test r15, r15
009434F8  0F 84 FC 02 00 00               je 0x1409437fa
009434FE  0F 28 74 24 40                  movaps xmm6, xmmword ptr [rsp + 0x40]
00943503  66 0F 7F 74 24 40               movdqa xmmword ptr [rsp + 0x40], xmm6
00943509  48 85 D2                        test rdx, rdx
0094350C  0F 84 2A FF FF FF               je 0x14094343c
00943512  4B 8D 1C 12                     lea rbx, [r10 + r10]
00943516  45 8B E2                        mov r12d, r10d
00943519  48 8D 14 9D 00 00 00 00         lea rdx, [rbx*4]
00943521  B9 00 01 00 00                  mov ecx, 0x100
00943526  41 B8 52 74 46 6F               mov r8d, 0x6f467452
0094352C  E8 BF EB 23 00                  call 0x140b820f0
00943531  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00943535  48 8B C8                        mov rcx, rax
00943538  48 85 C0                        test rax, rax
0094353B  0F 84 1B 04 00 00               je 0x14094395c
00943541  4C 3B E3                        cmp r12, rbx
00943544  0F 87 B0 02 00 00               ja 0x1409437fa
0094354A  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0094354F  48 8B C3                        mov rax, rbx
00943552  49 2B C4                        sub rax, r12
00943555  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
0094355A  48 3B D8                        cmp rbx, rax
0094355D  0F 82 97 02 00 00               jb 0x1409437fa
00943563  0F 10 44 24 50                  movups xmm0, xmmword ptr [rsp + 0x50]
00943568  48 8D 04 81                     lea rax, [rcx + rax*4]
0094356C  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
00943571  33 C9                           xor ecx, ecx
00943573  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00943578  21 4D C0                        and dword ptr [rbp - 0x40], ecx
0094357B  89 4D 50                        mov dword ptr [rbp + 0x50], ecx
0094357E  F3 0F 7F 45 C8                  movdqu xmmword ptr [rbp - 0x38], xmm0
00943583  48 83 FE 10                     cmp rsi, 0x10
00943587  0F 82 91 02 00 00               jb 0x14094381e
0094358D  48 8D 4E F0                     lea rcx, [rsi - 0x10]
00943591  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
00943596  49 8D 47 10                     lea rax, [r15 + 0x10]
0094359A  48 83 F9 FF                     cmp rcx, -1
0094359E  0F 84 56 02 00 00               je 0x1409437fa
009435A4  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
009435A9  4D 8B F7                        mov r14, r15
009435AC  0F 28 44 24 50                  movaps xmm0, xmmword ptr [rsp + 0x50]
009435B1  41 8B CD                        mov ecx, r13d
009435B4  66 0F 7F 44 24 40               movdqa xmmword ptr [rsp + 0x40], xmm0
009435BA  4D 85 F6                        test r14, r14
009435BD  0F 84 79 01 00 00               je 0x14094373c
009435C3  44 8B 5D 60                     mov r11d, dword ptr [rbp + 0x60]
009435C7  4D 8D 4E 04                     lea r9, [r14 + 4]
009435CB  49 8B D6                        mov rdx, r14
009435CE  49 3B D1                        cmp rdx, r9
009435D1  74 21                           je 0x1409435f4
009435D3  44 8B 02                        mov r8d, dword ptr [rdx]
009435D6  8B CF                           mov ecx, edi
009435D8  48 83 E9 04                     sub rcx, 4
009435DC  4C 3B C1                        cmp r8, rcx
009435DF  0F 83 57 FE FF FF               jae 0x14094343c
009435E5  45 3B C3                        cmp r8d, r11d
009435E8  0F 82 4E FE FF FF               jb 0x14094343c
009435EE  48 83 C2 04                     add rdx, 4
009435F2  EB DA                           jmp 0x1409435ce
009435F4  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
009435F8  85 C0                           test eax, eax
009435FA  0F 84 3C FE FF FF               je 0x14094343c
00943600  A8 03                           test al, 3
00943602  0F 85 34 FE FF FF               jne 0x14094343c
00943608  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0094360D  8B C8                           mov ecx, eax
0094360F  48 3B C3                        cmp rax, rbx
00943612  0F 87 24 FE FF FF               ja 0x14094343c
00943618  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
0094361D  4D 85 C0                        test r8, r8
00943620  0F 84 D4 01 00 00               je 0x1409437fa
00943626  F6 C1 03                        test cl, 3
00943629  0F 85 CB 01 00 00               jne 0x1409437fa
0094362F  8B D0                           mov edx, eax
00943631  48 C1 EA 02                     shr rdx, 2
00943635  4D 85 C0                        test r8, r8
00943638  0F 84 28 03 00 00               je 0x140943966
0094363E  48 3B D9                        cmp rbx, rcx
00943641  0F 82 B3 01 00 00               jb 0x1409437fa
00943647  49 03 C0                        add rax, r8
0094364A  48 2B D9                        sub rbx, rcx
0094364D  48 83 FB FF                     cmp rbx, -1
00943651  0F 84 A3 01 00 00               je 0x1409437fa
00943657  4D 8D 14 90                     lea r10, [r8 + rdx*4]
0094365B  4D 3B C2                        cmp r8, r10
0094365E  74 21                           je 0x140943681
00943660  45 8B 08                        mov r9d, dword ptr [r8]
00943663  8B D7                           mov edx, edi
00943665  48 83 EA 04                     sub rdx, 4
00943669  4C 3B CA                        cmp r9, rdx
0094366C  0F 83 CA FD FF FF               jae 0x14094343c
00943672  45 3B CB                        cmp r9d, r11d
00943675  0F 82 C1 FD FF FF               jb 0x14094343c
0094367B  49 83 C0 04                     add r8, 4
0094367F  EB DA                           jmp 0x14094365b
00943681  41 8B 4E 0C                     mov ecx, dword ptr [r14 + 0xc]
00943685  85 C9                           test ecx, ecx
00943687  0F 84 AF FD FF FF               je 0x14094343c
0094368D  F6 C1 03                        test cl, 3
00943690  0F 85 A6 FD FF FF               jne 0x14094343c
00943696  48 3B CB                        cmp rcx, rbx
00943699  0F 87 9D FD FF FF               ja 0x14094343c
0094369F  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
009436A3  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
009436A7  48 85 C0                        test rax, rax
009436AA  0F 84 4A 01 00 00               je 0x1409437fa
009436B0  48 2B D9                        sub rbx, rcx
009436B3  4C 8D 34 01                     lea r14, [rcx + rax]
009436B7  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
009436BC  48 83 FB FF                     cmp rbx, -1
009436C0  0F 84 34 01 00 00               je 0x1409437fa
009436C6  0F 28 4D A0                     movaps xmm1, xmmword ptr [rbp - 0x60]
009436CA  4C 8D 4D C0                     lea r9, [rbp - 0x40]
009436CE  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
009436D3  48 8D 55 90                     lea rdx, [rbp - 0x70]
009436D7  0F 28 44 24 50                  movaps xmm0, xmmword ptr [rsp + 0x50]
009436DC  45 8B C3                        mov r8d, r11d
009436DF  8B CF                           mov ecx, edi
009436E1  66 0F 7F 44 24 40               movdqa xmmword ptr [rsp + 0x40], xmm0
009436E7  66 0F 7F 4D 90                  movdqa xmmword ptr [rbp - 0x70], xmm1
009436EC  E8 77 03 00 00                  call 0x140943a68
009436F1  8B F8                           mov edi, eax
009436F3  85 C0                           test eax, eax
009436F5  0F 88 46 FD FF FF               js 0x140943441
009436FB  48 83 FB 10                     cmp rbx, 0x10
009436FF  0F 82 21 01 00 00               jb 0x140943826
00943705  48 8D 4B F0                     lea rcx, [rbx - 0x10]
00943709  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
0094370E  49 8D 46 10                     lea rax, [r14 + 0x10]
00943712  48 83 F9 FF                     cmp rcx, -1
00943716  0F 84 DE 00 00 00               je 0x1409437fa
0094371C  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00943721  0F 28 44 24 60                  movaps xmm0, xmmword ptr [rsp + 0x60]
00943726  66 0F 7F 44 24 40               movdqa xmmword ptr [rsp + 0x40], xmm0
0094372C  8B 4D 50                        mov ecx, dword ptr [rbp + 0x50]
0094372F  8B 7D 58                        mov edi, dword ptr [rbp + 0x58]
00943732  FF C1                           inc ecx
00943734  89 4D 50                        mov dword ptr [rbp + 0x50], ecx
00943737  E9 7E FE FF FF                  jmp 0x1409435ba
0094373C  49 83 FC FF                     cmp r12, -1
00943740  0F 84 B4 00 00 00               je 0x1409437fa
00943746  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
0094374A  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
0094374F  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00943754  48 85 C0                        test rax, rax
00943757  0F 84 17 02 00 00               je 0x140943974
0094375D  0F 28 44 24 60                  movaps xmm0, xmmword ptr [rsp + 0x60]
00943762  4C 8D 45 80                     lea r8, [rbp - 0x80]
00943766  8B D1                           mov edx, ecx
00943768  66 0F 7F 45 90                  movdqa xmmword ptr [rbp - 0x70], xmm0
0094376D  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00943771  E8 56 0B 00 00                  call 0x1409442cc
00943776  4C 8B 6D 80                     mov r13, qword ptr [rbp - 0x80]
0094377A  8B F8                           mov edi, eax
0094377C  85 C0                           test eax, eax
0094377E  0F 88 BD FC FF FF               js 0x140943441
00943784  0F 10 44 24 70                  movups xmm0, xmmword ptr [rsp + 0x70]
00943789  83 65 E0 00                     and dword ptr [rbp - 0x20], 0
0094378D  C7 45 C0 01 00 00 00            mov dword ptr [rbp - 0x40], 1
00943794  4C 89 6D D8                     mov qword ptr [rbp - 0x28], r13
00943798  66 0F 7F 74 24 40               movdqa xmmword ptr [rsp + 0x40], xmm6
0094379E  F3 0F 7F 45 C8                  movdqu xmmword ptr [rbp - 0x38], xmm0
009437A3  48 83 FE 10                     cmp rsi, 0x10
009437A7  0F 82 81 00 00 00               jb 0x14094382e
009437AD  48 8D 4E F0                     lea rcx, [rsi - 0x10]
009437B1  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
009437B6  49 8D 47 10                     lea rax, [r15 + 0x10]
009437BA  48 83 F9 FF                     cmp rcx, -1
009437BE  74 3A                           je 0x1409437fa
009437C0  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
009437C5  0F 28 44 24 70                  movaps xmm0, xmmword ptr [rsp + 0x70]
009437CA  66 0F 7F 44 24 40               movdqa xmmword ptr [rsp + 0x40], xmm0
009437D0  4C 8B 65 78                     mov r12, qword ptr [rbp + 0x78]
009437D4  0F 28 75 B0                     movaps xmm6, xmmword ptr [rbp - 0x50]
009437D8  4D 85 FF                        test r15, r15
009437DB  74 23                           je 0x140943800
009437DD  41 8B 4F 08                     mov ecx, dword ptr [r15 + 8]
009437E1  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
009437E6  45 8B 47 0C                     mov r8d, dword ptr [r15 + 0xc]
009437EA  48 3B F1                        cmp rsi, rcx
009437ED  72 0B                           jb 0x1409437fa
009437EF  48 8B C6                        mov rax, rsi
009437F2  48 2B C1                        sub rax, rcx
009437F5  49 3B C0                        cmp rax, r8
009437F8  73 39                           jae 0x140943833
009437FA  E8 A1 62 BB FF                  call 0x1404f9aa0
009437FF  CC                              int3
00943800  49 8B CD                        mov rcx, r13
00943803  E8 B4 01 00 00                  call 0x1409439bc
00943808  8B F8                           mov edi, eax
0094380A  85 C0                           test eax, eax
0094380C  0F 88 2F FC FF FF               js 0x140943441
00943812  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
00943816  4C 89 28                        mov qword ptr [rax], r13
00943819  E9 23 FC FF FF                  jmp 0x140943441
0094381E  45 33 F6                        xor r14d, r14d
00943821  E9 94 FD FF FF                  jmp 0x1409435ba
00943826  45 33 F6                        xor r14d, r14d
00943829  E9 FE FE FF FF                  jmp 0x14094372c
0094382E  45 33 FF                        xor r15d, r15d
00943831  EB 9D                           jmp 0x1409437d0
00943833  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00943838  4C 89 44 24 70                  mov qword ptr [rsp + 0x70], r8
0094383D  48 8D 04 0A                     lea rax, [rdx + rcx]
00943841  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00943846  48 3B CE                        cmp rcx, rsi
00943849  77 AF                           ja 0x1409437fa
0094384B  48 85 D2                        test rdx, rdx
0094384E  0F 84 2E 01 00 00               je 0x140943982
00943854  F6 C1 03                        test cl, 3
00943857  75 A1                           jne 0x1409437fa
00943859  48 8B C1                        mov rax, rcx
0094385C  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
00943861  48 C1 E8 02                     shr rax, 2
00943865  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0094386A  48 85 D2                        test rdx, rdx
0094386D  0F 84 1D 01 00 00               je 0x140943990
00943873  42 8D 04 01                     lea eax, [rcx + r8]
00943877  8B C8                           mov ecx, eax
00943879  48 3B F1                        cmp rsi, rcx
0094387C  0F 82 78 FF FF FF               jb 0x1409437fa
00943882  48 2B F1                        sub rsi, rcx
00943885  48 8D 1C 02                     lea rbx, [rdx + rax]
00943889  48 89 75 B0                     mov qword ptr [rbp - 0x50], rsi
0094388D  48 83 FE FF                     cmp rsi, -1
00943891  0F 84 63 FF FF FF               je 0x1409437fa
00943897  0F 28 4C 24 70                  movaps xmm1, xmmword ptr [rsp + 0x70]
0094389C  4C 8D 4D C0                     lea r9, [rbp - 0x40]
009438A0  44 8B 45 60                     mov r8d, dword ptr [rbp + 0x60]
009438A4  48 8D 55 90                     lea rdx, [rbp - 0x70]
009438A8  8B 4D 58                        mov ecx, dword ptr [rbp + 0x58]
009438AB  48 89 5D B8                     mov qword ptr [rbp - 0x48], rbx
009438AF  0F 28 45 B0                     movaps xmm0, xmmword ptr [rbp - 0x50]
009438B3  66 0F 7F 44 24 40               movdqa xmmword ptr [rsp + 0x40], xmm0
009438B9  66 0F 7F 4D 90                  movdqa xmmword ptr [rbp - 0x70], xmm1
009438BE  E8 A5 01 00 00                  call 0x140943a68
009438C3  8B F8                           mov edi, eax
009438C5  85 C0                           test eax, eax
009438C7  0F 88 74 FB FF FF               js 0x140943441
009438CD  41 8B 07                        mov eax, dword ptr [r15]
009438D0  48 8D 55 90                     lea rdx, [rbp - 0x70]
009438D4  0F 28 44 24 60                  movaps xmm0, xmmword ptr [rsp + 0x60]
009438D9  44 8B 75 E0                     mov r14d, dword ptr [rbp - 0x20]
009438DD  4C 8B 4D 68                     mov r9, qword ptr [rbp + 0x68]
009438E1  41 8B CE                        mov ecx, r14d
009438E4  48 C1 E1 04                     shl rcx, 4
009438E8  48 83 C1 28                     add rcx, 0x28
009438EC  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
009438F1  49 03 CD                        add rcx, r13
009438F4  66 0F 7F 45 90                  movdqa xmmword ptr [rbp - 0x70], xmm0
009438F9  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
009438FE  66 0F 7F 74 24 50               movdqa xmmword ptr [rsp + 0x50], xmm6
00943904  89 01                           mov dword ptr [rcx], eax
00943906  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0094390B  45 8B 47 04                     mov r8d, dword ptr [r15 + 4]
0094390F  E8 80 06 00 00                  call 0x140943f94
00943914  8B F8                           mov edi, eax
00943916  85 C0                           test eax, eax
00943918  0F 88 23 FB FF FF               js 0x140943441
0094391E  48 83 FE 10                     cmp rsi, 0x10
00943922  72 33                           jb 0x140943957
00943924  48 8D 4E F0                     lea rcx, [rsi - 0x10]
00943928  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
0094392C  48 8D 43 10                     lea rax, [rbx + 0x10]
00943930  48 83 F9 FF                     cmp rcx, -1
00943934  0F 84 C0 FE FF FF               je 0x1409437fa
0094393A  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
0094393E  4C 8B FB                        mov r15, rbx
00943941  0F 28 45 A0                     movaps xmm0, xmmword ptr [rbp - 0x60]
00943945  66 0F 7F 44 24 40               movdqa xmmword ptr [rsp + 0x40], xmm0
0094394B  41 FF C6                        inc r14d
0094394E  44 89 75 E0                     mov dword ptr [rbp - 0x20], r14d
00943952  E9 81 FE FF FF                  jmp 0x1409437d8
00943957  45 33 FF                        xor r15d, r15d
0094395A  EB EF                           jmp 0x14094394b
0094395C  BF 17 00 00 C0                  mov edi, 0xc0000017
00943961  E9 F6 FA FF FF                  jmp 0x14094345c
00943966  48 85 D2                        test rdx, rdx
00943969  0F 85 8B FE FF FF               jne 0x1409437fa
0094396F  E9 CA FC FF FF                  jmp 0x14094363e
00943974  4D 85 E4                        test r12, r12
00943977  0F 85 7D FE FF FF               jne 0x1409437fa
0094397D  E9 DB FD FF FF                  jmp 0x14094375d
00943982  48 85 C9                        test rcx, rcx
00943985  0F 85 6F FE FF FF               jne 0x1409437fa
0094398B  E9 C4 FE FF FF                  jmp 0x140943854
00943990  48 83 F9 04                     cmp rcx, 4
00943994  0F 83 60 FE FF FF               jae 0x1409437fa
0094399A  E9 D4 FE FF FF                  jmp 0x140943873
0094399F  4D 85 ED                        test r13, r13
009439A2  0F 84 B4 FA FF FF               je 0x14094345c
009439A8  49 8B CD                        mov rcx, r13
009439AB  E8 54 EA F8 FF                  call 0x1408d2404
009439B0  E9 A7 FA FF FF                  jmp 0x14094345c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpCreateFunctionOverrideFixupInfo(__int64 a1, int a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (264);
    v_r13 = 0;
    *(unsigned __int64 *)(v_rsp - 88) = v_xmm6;
    result = 0;
    v_r10 = (unsigned int)(((unsigned int)(a2)) >> (12));
    *(unsigned __int64 *)(v_rsp - 72 - 64) = 0;
    *(unsigned __int64 *)(v_rsp - 72 - 120) = 0;
    v_stack_m108 = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 72 - 128) = 0;
    *(unsigned __int64 *)(v_rsp - 72 - 40) = v_xmm0;
    if (a1 >= 4) goto loc_0094347B;
loc_0094343C:
loc_00943441:
    result = *(unsigned __int64 *)(v_rsp - 72 - 120);
    if (*(unsigned __int64 *)(v_rsp - 72 - 120) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rsp - 72 - 120);
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (sign_flag) goto loc_0094399F;
loc_0094345C:
    v_rsp = (v_rsp) + (264);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000007BULL)));
loc_0094347B:
    a1 = (a1) + (-4);
    v_stack_p40 = a1;
    if (a1 == -1) goto loc_009437FA;
    v_stack_p48 = v_stack_p48 + 4;
    v_stack_p40 = v_xmm0;
    if (v_stack_p48 == 0) goto loc_0094343C;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48))) == 0) goto loc_0094343C;
    if (((unsigned int)(*(unsigned int *)(v_stack_p48))) >= v_stack_p40) goto loc_0094343C;
    a2 = (v_stack_p40) - ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48)))));
    result = ((unsigned int)(*(unsigned int *)(v_stack_p48))) + (v_stack_p48);
    *(unsigned __int64 *)(v_rsp - 72 - 80) = a2;
    if (a2 == -1) goto loc_009437FA;
    *(unsigned __int64 *)(v_rsp - 72 - 72) = result;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48))))) > v_stack_p40) goto loc_009437FA;
    v_stack_p40 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48))));
    v_stack_p48 = v_stack_p48;
    if (v_stack_p48 == 0) goto loc_009437FA;
    v_stack_p40 = v_xmm6;
    if (a2 == 0) goto loc_0094343C;
    result = ExAllocatePool2(256, v_r10 + v_r10 * 1 * 4, (unsigned int)(0x6F467452ULL), a4);
    *(unsigned __int64 *)(v_rsp - 72 - 120) = result;
    if (result == 0) goto loc_0094395C;
    if (((unsigned int)((unsigned int)(v_r10))) > (v_r10 + v_r10 * 1)) goto loc_009437FA;
    v_stack_p58 = result;
    result = (v_r10 + v_r10 * 1) - ((unsigned int)((unsigned int)(v_r10)));
    v_stack_p50 = (unsigned int)((unsigned int)(v_r10));
    if ((v_r10 + v_r10 * 1) < result) goto loc_009437FA;
    v_stack_p70 = (unsigned int)((unsigned int)(v_r10));
    a1 = 0;
    v_stack_p78 = result + result * 4;
    *(unsigned int *)(v_rsp - 72 + 80) = 0;
    *(unsigned __int64 *)(v_rsp - 72 - 56) = v_xmm0;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48))))) < 16) goto loc_0094381E;
    v_stack_p50 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48)))) - 16;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48)))) - 16) == -1) goto loc_009437FA;
    v_stack_p58 = v_stack_p48 + 16;
    v_stack_p40 = v_xmm0;
loc_009435BA:
    if (v_stack_p48 == 0) goto loc_0094373C;
loc_009435CE:
    if (v_stack_p48 == (v_stack_p48 + 4)) goto loc_009435F4;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(0xC000007BULL)))) - (4);
    if (((unsigned int)(*(unsigned int *)(v_stack_p48))) >= a1) goto loc_0094343C;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 72 + 96))))) goto loc_0094343C;
    a2 = (v_stack_p48) + (4);
    goto loc_009435CE;
loc_009435F4:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48 + 8))) == 0) goto loc_0094343C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p48 + 8)))) & (3)) != 0) goto loc_0094343C;
    if (((unsigned int)(*(unsigned int *)(v_stack_p48 + 8))) > v_stack_p40) goto loc_0094343C;
    if (v_stack_p48 == 0) goto loc_009437FA;
    if ((((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48 + 8)))))) & (3)) != 0) goto loc_009437FA;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48 + 8))))) >> (2);
    if (v_stack_p48 == 0) goto loc_00943966;
loc_0094363E:
    if (v_stack_p40 < ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48 + 8)))))) goto loc_009437FA;
    result = ((unsigned int)(*(unsigned int *)(v_stack_p48 + 8))) + (v_stack_p48);
    v_rbx = (v_stack_p40) - ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48 + 8)))));
    if (v_rbx == -1) goto loc_009437FA;
loc_0094365B:
    if (v_stack_p48 == (v_stack_p48 + a2 * 4)) goto loc_00943681;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(0xC000007BULL)))) - (4);
    if (((unsigned int)(*(unsigned int *)(v_stack_p48))) >= a2) goto loc_0094343C;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 72 + 96))))) goto loc_0094343C;
    a3 = (v_stack_p48) + (4);
    goto loc_0094365B;
loc_00943681:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48 + 12))) == 0) goto loc_0094343C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p48 + 12)))) & (3)) != 0) goto loc_0094343C;
    if (((unsigned int)(*(unsigned int *)(v_stack_p48 + 12))) > v_rbx) goto loc_0094343C;
    *(unsigned __int64 *)(v_rsp - 72 - 96) = (unsigned int)(*(unsigned int *)(v_stack_p48 + 12));
    *(unsigned __int64 *)(v_rsp - 72 - 88) = result;
    if (result == 0) goto loc_009437FA;
    v_rbx = (v_rbx) - ((unsigned int)(*(unsigned int *)(v_stack_p48 + 12)));
    v_stack_p50 = v_rbx;
    if (v_rbx == -1) goto loc_009437FA;
    v_stack_p58 = (unsigned int)(*(unsigned int *)(v_stack_p48 + 12)) + result * 1;
    v_stack_p40 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 72 - 112) = v_xmm1;
    result = RtlpParseFunctionOverrideRelocations((unsigned int)((unsigned int)((unsigned int)(0xC000007BULL))), v_rsp - 72 - 112, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 72 + 96)))), v_rsp - 72 - 64);
    if (sign_flag) goto loc_00943441;
    if (v_rbx < 16) goto loc_00943826;
    v_stack_p60 = v_rbx - 16;
    if ((v_rbx - 16) == -1) goto loc_009437FA;
    v_stack_p68 = (unsigned int)(*(unsigned int *)(v_stack_p48 + 12)) + result * 1 + 16;
    v_stack_p40 = v_xmm0;
loc_0094372C:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 72 + 80))) + 1);
    *(unsigned int *)(v_rsp - 72 + 80) = (unsigned int)(a1);
    goto loc_009435BA;
loc_0094373C:
    if (((unsigned int)((unsigned int)(v_r10))) == -1) goto loc_009437FA;
    v_stack_p60 = (unsigned int)((unsigned int)(v_r10));
    v_stack_p68 = *(unsigned __int64 *)(v_rsp - 72 - 120);
    if (*(unsigned __int64 *)(v_rsp - 72 - 120) == 0) goto loc_00943974;
loc_0094375D:
    *(unsigned __int64 *)(v_rsp - 72 - 112) = v_xmm0;
    result = RtlpAllocateFunctionOverrideInfo(v_rsp - 72 - 112, (unsigned int)((unsigned int)(a1)), v_rsp - 72 - 128, v_rsp - 72 - 64);
    if (sign_flag) goto loc_00943441;
    *(unsigned int *)(v_rsp - 72 - 64) = 1;
    *(unsigned __int64 *)(v_rsp - 72 - 40) = *(unsigned __int64 *)(v_rsp - 72 - 128);
    v_stack_p40 = v_xmm6;
    *(unsigned __int64 *)(v_rsp - 72 - 56) = v_xmm0;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48))))) < 16) goto loc_0094382E;
    v_stack_p70 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48)))) - 16;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48)))) - 16) == -1) goto loc_009437FA;
    v_stack_p78 = v_stack_p48 + 16;
    v_stack_p40 = v_xmm0;
loc_009437D0:
loc_009437D8:
    if (v_stack_p48 == 0) goto loc_00943800;
    if (v_stack_p40 < ((unsigned int)(*(unsigned int *)(v_stack_p48 + 8)))) goto loc_009437FA;
    result = (v_stack_p40) - ((unsigned int)(*(unsigned int *)(v_stack_p48 + 8)));
    if (result >= ((unsigned int)(*(unsigned int *)(v_stack_p48 + 12)))) goto loc_00943833;
loc_009437FA:
    result = gsl__details__terminate((unsigned int)(*(unsigned int *)(v_stack_p48 + 8)), (unsigned int)((unsigned int)(a1)), (unsigned int)(*(unsigned int *)(v_stack_p48 + 12)), v_rsp - 72 - 64);
loc_00943800:
    result = RtlpSortAndValidateRelocations(*(unsigned __int64 *)(v_rsp - 72 - 128), (unsigned int)((unsigned int)(a1)), (unsigned int)(*(unsigned int *)(v_stack_p48 + 12)), v_rsp - 72 - 64);
    if (sign_flag) goto loc_00943441;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 72 + 112)) = *(unsigned __int64 *)(v_rsp - 72 - 128);
    goto loc_00943441;
loc_0094381E:
    v_r14 = 0;
    goto loc_009435BA;
loc_00943826:
    v_r14 = 0;
    goto loc_0094372C;
loc_0094382E:
    v_r15 = 0;
    goto loc_009437D0;
loc_00943833:
    v_stack_p70 = (unsigned int)(*(unsigned int *)(v_stack_p48 + 12));
    v_stack_p78 = v_stack_p48 + *(unsigned __int64 *)(v_rsp - 72 - 128) * 1;
    if ((*(unsigned __int64 *)(v_rsp - 72 - 128)) > v_stack_p40) goto loc_009437FA;
    if (v_stack_p48 == 0) goto loc_00943982;
loc_00943854:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rsp - 72 - 128))) & (3)) != 0) goto loc_009437FA;
    v_stack_p68 = v_stack_p48;
    result = (*(unsigned __int64 *)(v_rsp - 72 - 128)) >> (2);
    v_stack_p60 = result;
    if (v_stack_p48 == 0) goto loc_00943990;
loc_00943873:
    if (v_stack_p40 < ((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 72 - 128) + (unsigned int)(*(unsigned int *)(v_stack_p48 + 12)) * 1)))) goto loc_009437FA;
    v_rsi = (v_stack_p40) - ((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 72 - 128) + (unsigned int)(*(unsigned int *)(v_stack_p48 + 12)) * 1)));
    *(unsigned __int64 *)(v_rsp - 72 - 80) = v_rsi;
    if (v_rsi == -1) goto loc_009437FA;
    *(unsigned __int64 *)(v_rsp - 72 - 72) = v_stack_p48 + *(unsigned __int64 *)(v_rsp - 72 - 128) + (unsigned int)(*(unsigned int *)(v_stack_p48 + 12)) * 1 * 1;
    v_stack_p40 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 72 - 112) = v_xmm1;
    result = RtlpParseFunctionOverrideRelocations((unsigned int)(*(unsigned int *)(v_rsp - 72 + 88)), v_rsp - 72 - 112, (unsigned int)(*(unsigned int *)(v_rsp - 72 + 96)), v_rsp - 72 - 64);
    if (sign_flag) goto loc_00943441;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 72 - 32))))) << (4);
    a1 = (a1) + (40);
    v_stack_p28 = *(unsigned __int64 *)(v_rsp - 72 + 120);
    a1 = (a1) + (*(unsigned __int64 *)(v_rsp - 72 - 128));
    *(unsigned __int64 *)(v_rsp - 72 - 112) = v_xmm0;
    v_stack_p20 = a1;
    v_stack_p50 = v_xmm6;
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15)));
    result = RtlpParseBinaryDecisionDiagram(v_stack_p50, v_rsp - 72 - 112, (unsigned int)(*(unsigned int *)(v_r15 + 4)), *(unsigned __int64 *)(v_rsp - 72 + 104));
    if (sign_flag) goto loc_00943441;
    if (v_rsi < 16) goto loc_00943957;
    *(unsigned __int64 *)(v_rsp - 72 - 96) = v_rsi - 16;
    if ((v_rsi - 16) == -1) goto loc_009437FA;
    *(unsigned __int64 *)(v_rsp - 72 - 88) = v_stack_p48 + *(unsigned __int64 *)(v_rsp - 72 - 128) + (unsigned int)(*(unsigned int *)(v_stack_p48 + 12)) * 1 * 1 + 16;
    v_stack_p40 = v_xmm0;
loc_0094394B:
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 72 - 32))) + 1);
    *(unsigned int *)(v_rsp - 72 - 32) = (unsigned int)(v_r14);
    goto loc_009437D8;
loc_00943957:
    v_r15 = 0;
    goto loc_0094394B;
loc_0094395C:
    goto loc_0094345C;
loc_00943966:
    if (v_rsp - 72 - 112 != 0) goto loc_009437FA;
    goto loc_0094363E;
loc_00943974:
    if (*(unsigned __int64 *)(v_rsp - 72 + 120) != 0) goto loc_009437FA;
    goto loc_0094375D;
loc_00943982:
    if (v_rsi - 16 != 0) goto loc_009437FA;
    goto loc_00943854;
loc_00943990:
    if ((v_rsi - 16) >= 4) goto loc_009437FA;
    goto loc_00943873;
loc_0094399F:
    if (*(unsigned __int64 *)(v_rsp - 72 - 128) == 0) goto loc_0094345C;
    result = PdcCloseEvent(*(unsigned __int64 *)(v_rsp - 72 - 128), v_rsp - 72 - 112, (unsigned int)(*(unsigned int *)(v_r15 + 4)), *(unsigned __int64 *)(v_rsp - 72 + 104));
    goto loc_0094345C;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpCreateFunctionOverrideFixupInfo(void *Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m58;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (264);
    local_r13 = 0;
    *(uint64_t *)(local_rsp - 0x58) = v_xmm6;
    result = 0;
    local_r10 = (uint32_t)(((uint32_t)(Arg2)) >> (12));
    *(uint64_t *)(local_rsp - 0x48 - 0x40) = 0;
    *(uint64_t *)(local_rsp - 0x48 - 0x78) = 0;
    v_stack_m108 = v_xmm1;
    *(uint64_t *)(local_rsp - 0x48 - 0x80) = 0;
    *(uint64_t *)(local_rsp - 0x48 - 0x28) = v_xmm0;
    if (Arg1 >= 4) goto loc_0094347B;
loc_0094343C:
loc_00943441:
    result = *(uint64_t *)(local_rsp - 0x48 - 0x78);
    if (*(uint64_t *)(local_rsp - 0x48 - 0x78) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_rsp - 0x48 - 0x78);
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if (sign_flag) goto loc_0094399F;
loc_0094345C:
    local_rsp = (local_rsp) + (264);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000007BULL)));
loc_0094347B:
    Arg1 = (Arg1) + (-4);
    v_stack_p40 = Arg1;
    if (Arg1 == -1) goto loc_009437FA;
    v_stack_p48 = v_stack_p48 + 4;
    v_stack_p40 = v_xmm0;
    if (v_stack_p48 == 0) goto loc_0094343C;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48))) == 0) goto loc_0094343C;
    if (((uint32_t)(*(uint32_t *)(v_stack_p48))) >= v_stack_p40) goto loc_0094343C;
    Arg2 = (v_stack_p40) - ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48)))));
    result = ((uint32_t)(*(uint32_t *)(v_stack_p48))) + (v_stack_p48);
    *(uint64_t *)(local_rsp - 0x48 - 0x50) = Arg2;
    if (Arg2 == -1) goto loc_009437FA;
    *(uint64_t *)(local_rsp - 0x48 - 0x48) = result;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48))))) > v_stack_p40) goto loc_009437FA;
    v_stack_p40 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48))));
    v_stack_p48 = v_stack_p48;
    if (v_stack_p48 == 0) goto loc_009437FA;
    v_stack_p40 = v_xmm6;
    if (Arg2 == 0) goto loc_0094343C;
    result = ExAllocatePool2(256, local_r10 + local_r10 * 1 * 4, (uint32_t)(0x6F467452ULL), Arg4);
    *(uint64_t *)(local_rsp - 0x48 - 0x78) = result;
    if (result == 0) goto loc_0094395C;
    if (((uint32_t)((uint32_t)(local_r10))) > (local_r10 + local_r10 * 1)) goto loc_009437FA;
    v_stack_p58 = result;
    result = (local_r10 + local_r10 * 1) - ((uint32_t)((uint32_t)(local_r10)));
    v_stack_p50 = (uint32_t)((uint32_t)(local_r10));
    if ((local_r10 + local_r10 * 1) < result) goto loc_009437FA;
    v_stack_p70 = (uint32_t)((uint32_t)(local_r10));
    Arg1 = 0;
    v_stack_p78 = result + result * 4;
    *(uint32_t *)(local_rsp - 0x48 + 0x50) = 0;
    *(uint64_t *)(local_rsp - 0x48 - 0x38) = v_xmm0;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48))))) < 16) goto loc_0094381E;
    v_stack_p50 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48)))) - 16;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48)))) - 16) == -1) goto loc_009437FA;
    v_stack_p58 = v_stack_p48 + 16;
    v_stack_p40 = v_xmm0;
loc_009435BA:
    if (v_stack_p48 == 0) goto loc_0094373C;
loc_009435CE:
    if (v_stack_p48 == (v_stack_p48 + 4)) goto loc_009435F4;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(0xC000007BULL)))) - (4);
    if (((uint32_t)(*(uint32_t *)(v_stack_p48))) >= Arg1) goto loc_0094343C;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x48 + 0x60))))) goto loc_0094343C;
    Arg2 = (v_stack_p48) + (4);
    goto loc_009435CE;
loc_009435F4:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48 + 0x8))) == 0) goto loc_0094343C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p48 + 0x8)))) & (3)) != 0) goto loc_0094343C;
    if (((uint32_t)(*(uint32_t *)(v_stack_p48 + 0x8))) > v_stack_p40) goto loc_0094343C;
    if (v_stack_p48 == 0) goto loc_009437FA;
    if ((((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48 + 0x8)))))) & (3)) != 0) goto loc_009437FA;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48 + 0x8))))) >> (2);
    if (v_stack_p48 == 0) goto loc_00943966;
loc_0094363E:
    if (v_stack_p40 < ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48 + 0x8)))))) goto loc_009437FA;
    result = ((uint32_t)(*(uint32_t *)(v_stack_p48 + 0x8))) + (v_stack_p48);
    local_rbx = (v_stack_p40) - ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48 + 0x8)))));
    if (local_rbx == -1) goto loc_009437FA;
loc_0094365B:
    if (v_stack_p48 == (v_stack_p48 + Arg2 * 4)) goto loc_00943681;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(0xC000007BULL)))) - (4);
    if (((uint32_t)(*(uint32_t *)(v_stack_p48))) >= Arg2) goto loc_0094343C;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x48 + 0x60))))) goto loc_0094343C;
    Arg3 = (v_stack_p48) + (4);
    goto loc_0094365B;
loc_00943681:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48 + 0xC))) == 0) goto loc_0094343C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p48 + 0xC)))) & (3)) != 0) goto loc_0094343C;
    if (((uint32_t)(*(uint32_t *)(v_stack_p48 + 0xC))) > local_rbx) goto loc_0094343C;
    *(uint64_t *)(local_rsp - 0x48 - 0x60) = (uint32_t)(*(uint32_t *)(v_stack_p48 + 0xC));
    *(uint64_t *)(local_rsp - 0x48 - 0x58) = result;
    if (result == 0) goto loc_009437FA;
    local_rbx = (local_rbx) - ((uint32_t)(*(uint32_t *)(v_stack_p48 + 0xC)));
    v_stack_p50 = local_rbx;
    if (local_rbx == -1) goto loc_009437FA;
    v_stack_p58 = (uint32_t)(*(uint32_t *)(v_stack_p48 + 0xC)) + result * 1;
    v_stack_p40 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x48 - 0x70) = v_xmm1;
    result = RtlpParseFunctionOverrideRelocations((uint32_t)((uint32_t)((uint32_t)(0xC000007BULL))), local_rsp - 72 - 112, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x48 + 0x60)))), local_rsp - 72 - 64);
    if (sign_flag) goto loc_00943441;
    if (local_rbx < 16) goto loc_00943826;
    v_stack_p60 = local_rbx - 16;
    if ((local_rbx - 16) == -1) goto loc_009437FA;
    v_stack_p68 = (uint32_t)(*(uint32_t *)(v_stack_p48 + 0xC)) + result * 1 + 16;
    v_stack_p40 = v_xmm0;
loc_0094372C:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x48 + 0x50))) + 1);
    *(uint32_t *)(local_rsp - 0x48 + 0x50) = (uint32_t)(Arg1);
    goto loc_009435BA;
loc_0094373C:
    if (((uint32_t)((uint32_t)(local_r10))) == -1) goto loc_009437FA;
    v_stack_p60 = (uint32_t)((uint32_t)(local_r10));
    v_stack_p68 = *(uint64_t *)(local_rsp - 0x48 - 0x78);
    if (*(uint64_t *)(local_rsp - 0x48 - 0x78) == 0) goto loc_00943974;
loc_0094375D:
    *(uint64_t *)(local_rsp - 0x48 - 0x70) = v_xmm0;
    result = RtlpAllocateFunctionOverrideInfo(local_rsp - 72 - 112, (uint32_t)((uint32_t)(Arg1)), local_rsp - 72 - 128, local_rsp - 72 - 64);
    if (sign_flag) goto loc_00943441;
    *(uint32_t *)(local_rsp - 0x48 - 0x40) = 1;
    *(uint64_t *)(local_rsp - 0x48 - 0x28) = *(uint64_t *)(local_rsp - 0x48 - 0x80);
    v_stack_p40 = v_xmm6;
    *(uint64_t *)(local_rsp - 0x48 - 0x38) = v_xmm0;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48))))) < 16) goto loc_0094382E;
    v_stack_p70 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48)))) - 16;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48)))) - 16) == -1) goto loc_009437FA;
    v_stack_p78 = v_stack_p48 + 16;
    v_stack_p40 = v_xmm0;
loc_009437D0:
loc_009437D8:
    if (v_stack_p48 == 0) goto loc_00943800;
    if (v_stack_p40 < ((uint32_t)(*(uint32_t *)(v_stack_p48 + 0x8)))) goto loc_009437FA;
    result = (v_stack_p40) - ((uint32_t)(*(uint32_t *)(v_stack_p48 + 0x8)));
    if (result >= ((uint32_t)(*(uint32_t *)(v_stack_p48 + 0xC)))) goto loc_00943833;
loc_009437FA:
    result = gsl__details__terminate((uint32_t)(*(uint32_t *)(v_stack_p48 + 0x8)), (uint32_t)((uint32_t)(Arg1)), (uint32_t)(*(uint32_t *)(v_stack_p48 + 0xC)), local_rsp - 72 - 64);
loc_00943800:
    result = RtlpSortAndValidateRelocations(*(uint64_t *)(local_rsp - 0x48 - 0x80), (uint32_t)((uint32_t)(Arg1)), (uint32_t)(*(uint32_t *)(v_stack_p48 + 0xC)), local_rsp - 72 - 64);
    if (sign_flag) goto loc_00943441;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x48 + 0x70)) = *(uint64_t *)(local_rsp - 0x48 - 0x80);
    goto loc_00943441;
loc_0094381E:
    local_r14 = 0;
    goto loc_009435BA;
loc_00943826:
    local_r14 = 0;
    goto loc_0094372C;
loc_0094382E:
    local_r15 = 0;
    goto loc_009437D0;
loc_00943833:
    v_stack_p70 = (uint32_t)(*(uint32_t *)(v_stack_p48 + 0xC));
    v_stack_p78 = v_stack_p48 + *(uint64_t *)(local_rsp - 0x48 - 0x80) * 1;
    if ((*(uint64_t *)(local_rsp - 0x48 - 0x80)) > v_stack_p40) goto loc_009437FA;
    if (v_stack_p48 == 0) goto loc_00943982;
loc_00943854:
    if ((((uint8_t)(*(uint64_t *)(local_rsp - 0x48 - 0x80))) & (3)) != 0) goto loc_009437FA;
    v_stack_p68 = v_stack_p48;
    result = (*(uint64_t *)(local_rsp - 0x48 - 0x80)) >> (2);
    v_stack_p60 = result;
    if (v_stack_p48 == 0) goto loc_00943990;
loc_00943873:
    if (v_stack_p40 < ((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x48 - 0x80) + (uint32_t)(*(uint32_t *)(v_stack_p48 + 0xC)) * 1)))) goto loc_009437FA;
    local_rsi = (v_stack_p40) - ((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x48 - 0x80) + (uint32_t)(*(uint32_t *)(v_stack_p48 + 0xC)) * 1)));
    *(uint64_t *)(local_rsp - 0x48 - 0x50) = local_rsi;
    if (local_rsi == -1) goto loc_009437FA;
    *(uint64_t *)(local_rsp - 0x48 - 0x48) = v_stack_p48 + *(uint64_t *)(local_rsp - 0x48 - 0x80) + (uint32_t)(*(uint32_t *)(v_stack_p48 + 0xC)) * 1 * 1;
    v_stack_p40 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x48 - 0x70) = v_xmm1;
    result = RtlpParseFunctionOverrideRelocations((uint32_t)(*(uint32_t *)(local_rsp - 0x48 + 0x58)), local_rsp - 72 - 112, (uint32_t)(*(uint32_t *)(local_rsp - 0x48 + 0x60)), local_rsp - 72 - 64);
    if (sign_flag) goto loc_00943441;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x48 - 0x20))))) << (4);
    Arg1 = (Arg1) + (40);
    v_stack_p28 = *(uint64_t *)(local_rsp - 0x48 + 0x78);
    Arg1 = (Arg1) + (*(uint64_t *)(local_rsp - 0x48 - 0x80));
    *(uint64_t *)(local_rsp - 0x48 - 0x70) = v_xmm0;
    v_stack_p20 = Arg1;
    v_stack_p50 = v_xmm6;
    *(uint32_t *)(arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15)));
    result = RtlpParseBinaryDecisionDiagram(v_stack_p50, local_rsp - 72 - 112, (uint32_t)(*(uint32_t *)(local_r15 + 0x4)), *(uint64_t *)(local_rsp - 0x48 + 0x68));
    if (sign_flag) goto loc_00943441;
    if (local_rsi < 16) goto loc_00943957;
    *(uint64_t *)(local_rsp - 0x48 - 0x60) = local_rsi - 16;
    if ((local_rsi - 16) == -1) goto loc_009437FA;
    *(uint64_t *)(local_rsp - 0x48 - 0x58) = v_stack_p48 + *(uint64_t *)(local_rsp - 0x48 - 0x80) + (uint32_t)(*(uint32_t *)(v_stack_p48 + 0xC)) * 1 * 1 + 16;
    v_stack_p40 = v_xmm0;
loc_0094394B:
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x48 - 0x20))) + 1);
    *(uint32_t *)(local_rsp - 0x48 - 0x20) = (uint32_t)(local_r14);
    goto loc_009437D8;
loc_00943957:
    local_r15 = 0;
    goto loc_0094394B;
loc_0094395C:
    goto loc_0094345C;
loc_00943966:
    if (local_rsp - 72 - 112 != 0) goto loc_009437FA;
    goto loc_0094363E;
loc_00943974:
    if (*(uint64_t *)(local_rsp - 0x48 + 0x78) != 0) goto loc_009437FA;
    goto loc_0094375D;
loc_00943982:
    if (local_rsi - 16 != 0) goto loc_009437FA;
    goto loc_00943854;
loc_00943990:
    if ((local_rsi - 16) >= 4) goto loc_009437FA;
    goto loc_00943873;
loc_0094399F:
    if (*(uint64_t *)(local_rsp - 0x48 - 0x80) == 0) goto loc_0094345C;
    result = PdcCloseEvent(*(uint64_t *)(local_rsp - 0x48 - 0x80), local_rsp - 72 - 112, (uint32_t)(*(uint32_t *)(local_r15 + 0x4)), *(uint64_t *)(local_rsp - 0x48 + 0x68));
    goto loc_0094345C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009433D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
