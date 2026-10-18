# MiFreeVirtualMemory

- RVA: `0x00880268`–`0x00880796` (길이 `1,326` bytes)
- VA: `0x0000000140880268`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007C4CC`
- 디코드: `310`개 명령, `1,326/1,326` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008803FB` → [MiDecommitRegion](MiDecommitRegion_function_008807A0.md) (function, `0x008807A0`)
- `0x0088040A` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (function, `0x00316E60`)
- `0x0088048C` → [MiFreeVadRange](../../text/2A/MiFreeVadRange_function_002A77AC.md) (function, `0x002A77AC`)
- `0x008804F2` → [MiDeleteEmptyPageTables](../../text/2A/MiDeleteEmptyPageTables_function_002A5220.md) (function, `0x002A5220`)
- `0x00880518` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (function, `0x00316E60`)
- `0x0088053F` → [UNLOCK_ADDRESS_SPACE](../../text/2A/UNLOCK_ADDRESS_SPACE_function_002A4844.md) (function, `0x002A4844`)
- `0x00880588` → [PerfInfoLogVirtualFree](PerfInfoLogVirtualFree_function_00880B98.md) (function, `0x00880B98`)
- `0x008805AF` → [MiGetVadPageSize](../../text/42/MiGetVadPageSize_function_0042F0E0.md) (function, `0x0042F0E0`)
- `0x00880600` → [MiDecommitEnclavePages](MiDecommitEnclavePages_function_00880C28.md) (function, `0x00880C28`)
- `0x00880631` → [MiLocateLockedVadEvent](../../text/2A/MiLocateLockedVadEvent_function_002A7A0C.md) (function, `0x002A7A0C`)
- `0x008806AC` → [MiCheckSecuredVad](MiCheckSecuredVad_function_00881FB4.md) (function, `0x00881FB4`)

### Direct callers
- [MmCommitDecommitSecuredMemory](../7F/MmCommitDecommitSecuredMemory_function_007FE904.md) at `0x007FEA00`
- [sub_0087FFB4](../87/Unknown_function_0087FFB4.md) at `0x00880076`

### Static image references
- `0x0088041D` → RVA `0x00FC6B04` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x0088040A` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (`PAGE` → `.text`)
  - `0x0088048C` → [MiFreeVadRange](../../text/2A/MiFreeVadRange_function_002A77AC.md) (`PAGE` → `.text`)
  - `0x008804F2` → [MiDeleteEmptyPageTables](../../text/2A/MiDeleteEmptyPageTables_function_002A5220.md) (`PAGE` → `.text`)
  - `0x00880518` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (`PAGE` → `.text`)
  - `0x0088053F` → [UNLOCK_ADDRESS_SPACE](../../text/2A/UNLOCK_ADDRESS_SPACE_function_002A4844.md) (`PAGE` → `.text`)
  - `0x008805AF` → [MiGetVadPageSize](../../text/42/MiGetVadPageSize_function_0042F0E0.md) (`PAGE` → `.text`)
  - `0x00880631` → [MiLocateLockedVadEvent](../../text/2A/MiLocateLockedVadEvent_function_002A7A0C.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00880268  48 8B C4                        mov rax, rsp
0088026B  48 89 48 08                     mov qword ptr [rax + 8], rcx
0088026F  53                              push rbx
00880270  55                              push rbp
00880271  56                              push rsi
00880272  57                              push rdi
00880273  41 54                           push r12
00880275  41 55                           push r13
00880277  41 56                           push r14
00880279  41 57                           push r15
0088027B  48 83 EC 48                     sub rsp, 0x48
0088027F  4D 8B 38                        mov r15, qword ptr [r8]
00880282  48 8B FA                        mov rdi, rdx
00880285  49 8B 31                        mov rsi, qword ptr [r9]
00880288  4D 8B E9                        mov r13, r9
0088028B  83 A4 24 A8 00 00 00 00         and dword ptr [rsp + 0xa8], 0
00880293  4D 8B E0                        mov r12, r8
00880296  8B 94 24 B8 00 00 00            mov edx, dword ptr [rsp + 0xb8]
0088029D  4C 8B D1                        mov r10, rcx
008802A0  49 C1 EF 0C                     shr r15, 0xc
008802A4  48 C1 EE 0C                     shr rsi, 0xc
008802A8  81 E2 00 80 00 00               and edx, 0x8000
008802AE  C6 40 10 00                     mov byte ptr [rax + 0x10], 0
008802B2  89 94 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], edx
008802B9  49 B8 FD FF FF FF 07 00 00 00   movabs r8, 0x7fffffffd
008802C3  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
008802C6  0F B6 6F 20                     movzx ebp, byte ptr [rdi + 0x20]
008802CA  44 0F B6 77 21                  movzx r14d, byte ptr [rdi + 0x21]
008802CF  48 C1 E5 20                     shl rbp, 0x20
008802D3  48 0B E8                        or rbp, rax
008802D6  49 C1 E6 20                     shl r14, 0x20
008802DA  8B 47 1C                        mov eax, dword ptr [rdi + 0x1c]
008802DD  4C 0B F0                        or r14, rax
008802E0  48 83 BC 24 B0 00 00 00 00      cmp qword ptr [rsp + 0xb0], 0
008802E9  0F 84 C3 01 00 00               je 0x1408804b2
008802EF  4C 3B FD                        cmp r15, rbp
008802F2  0F 82 04 02 00 00               jb 0x1408804fc
008802F8  4D 3B FE                        cmp r15, r14
008802FB  0F 87 FB 01 00 00               ja 0x1408804fc
00880301  48 3B F5                        cmp rsi, rbp
00880304  0F 82 F2 01 00 00               jb 0x1408804fc
0088030A  49 3B F6                        cmp rsi, r14
0088030D  0F 87 E9 01 00 00               ja 0x1408804fc
00880313  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
00880316  8B C8                           mov ecx, eax
00880318  81 E1 00 00 20 00               and ecx, 0x200000
0088031E  F7 84 24 B8 00 00 00 00 00 01 00  test dword ptr [rsp + 0xb8], 0x10000
00880329  0F 85 DB 03 00 00               jne 0x14088070a
0088032F  85 C9                           test ecx, ecx
00880331  0F 84 55 04 00 00               je 0x14088078c
00880337  24 70                           and al, 0x70
00880339  3C 10                           cmp al, 0x10
0088033B  0F 84 4B 04 00 00               je 0x14088078c
00880341  44 8B 8C 24 C0 00 00 00         mov r9d, dword ptr [rsp + 0xc0]
00880349  41 0F BA E1 1A                  bt r9d, 0x1a
0088034E  0F 82 D5 02 00 00               jb 0x140880629
00880354  41 0F BA E1 1E                  bt r9d, 0x1e
00880359  0F 82 A4 01 00 00               jb 0x140880503
0088035F  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
00880362  A8 08                           test al, 8
00880364  0F 85 F8 02 00 00               jne 0x140880662
0088036A  85 D2                           test edx, edx
0088036C  0F 85 CF 00 00 00               jne 0x140880441
00880372  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
00880375  25 00 00 20 0C                  and eax, 0xc200000
0088037A  3D 00 00 20 08                  cmp eax, 0x8200000
0088037F  0F 84 54 02 00 00               je 0x1408805d9
00880385  8B 4F 30                        mov ecx, dword ptr [rdi + 0x30]
00880388  8B C1                           mov eax, ecx
0088038A  83 E0 70                        and eax, 0x70
0088038D  3C 30                           cmp al, 0x30
0088038F  0F 84 3A 02 00 00               je 0x1408805cf
00880395  0F BA E1 15                     bt ecx, 0x15
00880399  73 1C                           jae 0x1408803b7
0088039B  0F BA E1 17                     bt ecx, 0x17
0088039F  0F 82 ED 01 00 00               jb 0x140880592
008803A5  8B C1                           mov eax, ecx
008803A7  25 00 00 18 00                  and eax, 0x180000
008803AC  3D 00 00 10 00                  cmp eax, 0x100000
008803B1  0F 83 DB 01 00 00               jae 0x140880592
008803B7  8B 4F 34                        mov ecx, dword ptr [rdi + 0x34]
008803BA  48 B8 FD FF FF FF 07 00 00 00   movabs rax, 0x7fffffffd
008803C4  0F B6 57 22                     movzx edx, byte ptr [rdi + 0x22]
008803C8  48 C1 E2 20                     shl rdx, 0x20
008803CC  48 0B D1                        or rdx, rcx
008803CF  48 3B D0                        cmp rdx, rax
008803D2  0F 84 F7 01 00 00               je 0x1408805cf
008803D8  48 83 BC 24 B0 00 00 00 00      cmp qword ptr [rsp + 0xb0], 0
008803E1  0F 84 5F 01 00 00               je 0x140880546
008803E7  4D 8B 45 00                     mov r8, qword ptr [r13]
008803EB  48 8B CF                        mov rcx, rdi
008803EE  49 8B 14 24                     mov rdx, qword ptr [r12]
008803F2  49 8B F0                        mov rsi, r8
008803F5  48 2B F2                        sub rsi, rdx
008803F8  48 FF C6                        inc rsi
008803FB  E8 A0 03 00 00                  call 0x1408807a0
00880400  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00880407  48 8B CF                        mov rcx, rdi
0088040A  E8 51 6A A9 FF                  call 0x140316e60
0088040F  83 BC 24 A8 00 00 00 00         cmp dword ptr [rsp + 0xa8], 0
00880417  0F 85 CA 00 00 00               jne 0x1408804e7
0088041D  F7 05 DD 66 74 00 00 80 00 00   test dword ptr [rip + 0x7466dd], 0x8000
00880427  0F 85 44 01 00 00               jne 0x140880571
0088042D  33 C0                           xor eax, eax
0088042F  48 83 C4 48                     add rsp, 0x48
00880433  41 5F                           pop r15
00880435  41 5E                           pop r14
00880437  41 5D                           pop r13
00880439  41 5C                           pop r12
0088043B  5F                              pop rdi
0088043C  5E                              pop rsi
0088043D  5D                              pop rbp
0088043E  5B                              pop rbx
0088043F  C3                              ret
00880440  CC                              int3
00880441  F6 84 24 C8 00 00 00 01         test byte ptr [rsp + 0xc8], 1
00880449  74 11                           je 0x14088045c
0088044B  41 F7 82 FC 05 00 00 00 01 00 00  test dword ptr [r10 + 0x5fc], 0x100
00880456  0F 85 02 03 00 00               jne 0x14088075e
0088045C  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
00880464  48 8D 94 24 98 00 00 00         lea rdx, [rsp + 0x98]
0088046C  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00880471  41 8B C1                        mov eax, r9d
00880474  C1 E8 1A                        shr eax, 0x1a
00880477  4C 8B CE                        mov r9, rsi
0088047A  83 E0 01                        and eax, 1
0088047D  4D 8B C7                        mov r8, r15
00880480  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00880484  48 8B CF                        mov rcx, rdi
00880487  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
0088048C  E8 1B 73 A2 FF                  call 0x1402a77ac
00880491  8B D8                           mov ebx, eax
00880493  85 C0                           test eax, eax
00880495  79 96                           jns 0x14088042d
00880497  3D 2D 02 00 C0                  cmp eax, 0xc000022d
0088049C  75 77                           jne 0x140880515
0088049E  4C 8B 94 24 90 00 00 00         mov r10, qword ptr [rsp + 0x90]
008804A6  8B 94 24 A0 00 00 00            mov edx, dword ptr [rsp + 0xa0]
008804AD  E9 07 FE FF FF                  jmp 0x1408802b9
008804B2  49 8B C6                        mov rax, r14
008804B5  49 8B F6                        mov rsi, r14
008804B8  48 C1 E0 0C                     shl rax, 0xc
008804BC  48 0D FF 0F 00 00               or rax, 0xfff
008804C2  49 89 45 00                     mov qword ptr [r13], rax
008804C6  85 D2                           test edx, edx
008804C8  0F 84 21 FE FF FF               je 0x1408802ef
008804CE  4C 3B FD                        cmp r15, rbp
008804D1  0F 85 48 01 00 00               jne 0x14088061f
008804D7  48 8B C5                        mov rax, rbp
008804DA  48 C1 E0 0C                     shl rax, 0xc
008804DE  49 89 04 24                     mov qword ptr [r12], rax
008804E2  E9 11 FE FF FF                  jmp 0x1408802f8
008804E7  49 8B 55 00                     mov rdx, qword ptr [r13]
008804EB  45 33 C0                        xor r8d, r8d
008804EE  49 8B 0C 24                     mov rcx, qword ptr [r12]
008804F2  E8 29 4D A2 FF                  call 0x1402a5220
008804F7  E9 21 FF FF FF                  jmp 0x14088041d
008804FC  BB 1A 00 00 C0                  mov ebx, 0xc000001a
00880501  EB 12                           jmp 0x140880515
00880503  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
00880506  0F BA E0 15                     bt eax, 0x15
0088050A  0F 82 5D 02 00 00               jb 0x14088076d
00880510  BB 18 00 00 C0                  mov ebx, 0xc0000018
00880515  48 8B CF                        mov rcx, rdi
00880518  E8 43 69 A9 FF                  call 0x140316e60
0088051D  80 BC 24 98 00 00 00 00         cmp byte ptr [rsp + 0x98], 0
00880525  75 07                           jne 0x14088052e
00880527  8B C3                           mov eax, ebx
00880529  E9 01 FF FF FF                  jmp 0x14088042f
0088052E  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00880537  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
0088053F  E8 00 43 A2 FF                  call 0x1402a4844
00880544  EB E1                           jmp 0x140880527
00880546  4C 3B FD                        cmp r15, rbp
00880549  0F 85 D0 00 00 00               jne 0x14088061f
0088054F  0F B6 4F 21                     movzx ecx, byte ptr [rdi + 0x21]
00880553  8B 47 1C                        mov eax, dword ptr [rdi + 0x1c]
00880556  48 C1 E1 20                     shl rcx, 0x20
0088055A  48 0B C8                        or rcx, rax
0088055D  48 C1 E1 0C                     shl rcx, 0xc
00880561  48 81 C9 FF 0F 00 00            or rcx, 0xfff
00880568  49 89 4D 00                     mov qword ptr [r13], rcx
0088056C  E9 76 FE FF FF                  jmp 0x1408803e7
00880571  44 8B 8C 24 B8 00 00 00         mov r9d, dword ptr [rsp + 0xb8]
00880579  48 8B D6                        mov rdx, rsi
0088057C  4C 8B 84 24 90 00 00 00         mov r8, qword ptr [rsp + 0x90]
00880584  49 8B 0C 24                     mov rcx, qword ptr [r12]
00880588  E8 0B 06 00 00                  call 0x140880b98
0088058D  E9 9B FE FF FF                  jmp 0x14088042d
00880592  B8 00 00 A0 00                  mov eax, 0xa00000
00880597  23 C8                           and ecx, eax
00880599  3B C8                           cmp ecx, eax
0088059B  75 32                           jne 0x1408805cf
0088059D  48 83 BC 24 B0 00 00 00 00      cmp qword ptr [rsp + 0xb0], 0
008805A6  0F 84 0B FE FF FF               je 0x1408803b7
008805AC  48 8B CF                        mov rcx, rdi
008805AF  E8 2C EB BA FF                  call 0x14042f0e0
008805B4  49 8B 4D 00                     mov rcx, qword ptr [r13]
008805B8  48 FF C1                        inc rcx
008805BB  48 C1 E0 0C                     shl rax, 0xc
008805BF  49 0B 0C 24                     or rcx, qword ptr [r12]
008805C3  48 FF C8                        dec rax
008805C6  48 85 C1                        test rcx, rax
008805C9  0F 84 E8 FD FF FF               je 0x1408803b7
008805CF  BB A0 00 00 C0                  mov ebx, 0xc00000a0
008805D4  E9 3C FF FF FF                  jmp 0x140880515
008805D9  48 83 BC 24 B0 00 00 00 00      cmp qword ptr [rsp + 0xb0], 0
008805E2  74 EB                           je 0x1408805cf
008805E4  4D 8B 04 24                     mov r8, qword ptr [r12]
008805E8  48 8B D7                        mov rdx, rdi
008805EB  49 8B 75 00                     mov rsi, qword ptr [r13]
008805EF  49 8B CA                        mov rcx, r10
008805F2  49 2B F0                        sub rsi, r8
008805F5  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
008805FA  48 FF C6                        inc rsi
008805FD  4C 8B CE                        mov r9, rsi
00880600  E8 23 06 00 00                  call 0x140880c28
00880605  8B D8                           mov ebx, eax
00880607  3D 16 00 00 C0                  cmp eax, 0xc0000016
0088060C  0F 84 73 FD FF FF               je 0x140880385
00880612  85 C0                           test eax, eax
00880614  0F 88 FB FE FF FF               js 0x140880515
0088061A  E9 E8 FD FF FF                  jmp 0x140880407
0088061F  BB 9F 00 00 C0                  mov ebx, 0xc000009f
00880624  E9 EC FE FF FF                  jmp 0x140880515
00880629  BA 80 00 00 00                  mov edx, 0x80
0088062E  48 8B CF                        mov rcx, rdi
00880631  E8 D6 73 A2 FF                  call 0x1402a7a0c
00880636  48 85 C0                        test rax, rax
00880639  0F 84 98 00 00 00               je 0x1408806d7
0088063F  8B 4F 34                        mov ecx, dword ptr [rdi + 0x34]
00880642  0F B6 57 22                     movzx edx, byte ptr [rdi + 0x22]
00880646  48 C1 E2 20                     shl rdx, 0x20
0088064A  48 0B D1                        or rdx, rcx
0088064D  49 3B D0                        cmp rdx, r8
00880650  0F 84 9D 00 00 00               je 0x1408806f3
00880656  8B 94 24 A0 00 00 00            mov edx, dword ptr [rsp + 0xa0]
0088065D  E9 F2 FC FF FF                  jmp 0x140880354
00880662  41 0F BA E1 1E                  bt r9d, 0x1e
00880667  0F 82 FD FC FF FF               jb 0x14088036a
0088066D  85 D2                           test edx, edx
0088066F  0F 85 AE 00 00 00               jne 0x140880723
00880675  49 8B 14 24                     mov rdx, qword ptr [r12]
00880679  4C 8B C6                        mov r8, rsi
0088067C  4D 2B C7                        sub r8, r15
0088067F  4C 8B 9C 24 E0 00 00 00         mov r11, qword ptr [rsp + 0xe0]
00880687  48 8B C7                        mov rax, rdi
0088068A  44 8A 94 24 D0 00 00 00         mov r10b, byte ptr [rsp + 0xd0]
00880692  49 FF C0                        inc r8
00880695  4C 89 5C 24 28                  mov qword ptr [rsp + 0x28], r11
0088069A  48 8B C8                        mov rcx, rax
0088069D  49 C1 E0 0C                     shl r8, 0xc
008806A1  41 B9 55 00 00 00               mov r9d, 0x55
008806A7  44 88 54 24 20                  mov byte ptr [rsp + 0x20], r10b
008806AC  E8 03 19 00 00                  call 0x140881fb4
008806B1  8B D8                           mov ebx, eax
008806B3  85 C0                           test eax, eax
008806B5  0F 88 5A FE FF FF               js 0x140880515
008806BB  4C 8B 94 24 90 00 00 00         mov r10, qword ptr [rsp + 0x90]
008806C3  44 8B 8C 24 C0 00 00 00         mov r9d, dword ptr [rsp + 0xc0]
008806CB  8B 94 24 A0 00 00 00            mov edx, dword ptr [rsp + 0xa0]
008806D2  E9 93 FC FF FF                  jmp 0x14088036a
008806D7  8B 57 34                        mov edx, dword ptr [rdi + 0x34]
008806DA  0F B6 4F 22                     movzx ecx, byte ptr [rdi + 0x22]
008806DE  48 C1 E1 20                     shl rcx, 0x20
008806E2  48 0B CA                        or rcx, rdx
008806E5  49 3B C8                        cmp rcx, r8
008806E8  0F 84 51 FF FF FF               je 0x14088063f
008806EE  E9 1D FE FF FF                  jmp 0x140880510
008806F3  49 3B F6                        cmp rsi, r14
008806F6  0F 85 5A FF FF FF               jne 0x140880656
008806FC  4C 3B FD                        cmp r15, rbp
008806FF  0F 85 51 FF FF FF               jne 0x140880656
00880705  E9 06 FE FF FF                  jmp 0x140880510
0088070A  85 C9                           test ecx, ecx
0088070C  75 7E                           jne 0x14088078c
0088070E  A8 70                           test al, 0x70
00880710  75 7A                           jne 0x14088078c
00880712  4C 3B FD                        cmp r15, rbp
00880715  0F 85 26 FC FF FF               jne 0x140880341
0088071B  49 3B F6                        cmp rsi, r14
0088071E  E9 18 FC FF FF                  jmp 0x14088033b
00880723  41 8B 82 F4 01 00 00            mov eax, dword ptr [r10 + 0x1f4]
0088072A  A8 20                           test al, 0x20
0088072C  0F 85 0F FD FF FF               jne 0x140880441
00880732  8B 47 1C                        mov eax, dword ptr [rdi + 0x1c]
00880735  48 8B D5                        mov rdx, rbp
00880738  44 0F B6 47 21                  movzx r8d, byte ptr [rdi + 0x21]
0088073D  0F B6 4F 20                     movzx ecx, byte ptr [rdi + 0x20]
00880741  49 C1 E0 20                     shl r8, 0x20
00880745  4C 0B C0                        or r8, rax
00880748  48 C1 E1 20                     shl rcx, 0x20
0088074C  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
0088074F  48 0B C8                        or rcx, rax
00880752  48 C1 E2 0C                     shl rdx, 0xc
00880756  4C 2B C1                        sub r8, rcx
00880759  E9 21 FF FF FF                  jmp 0x14088067f
0088075E  49 3B F6                        cmp rsi, r14
00880761  74 1F                           je 0x140880782
00880763  BB 0A 01 00 C0                  mov ebx, 0xc000010a
00880768  E9 A8 FD FF FF                  jmp 0x140880515
0088076D  25 00 00 00 14                  and eax, 0x14000000
00880772  3D 00 00 00 10                  cmp eax, 0x10000000
00880777  0F 85 93 FD FF FF               jne 0x140880510
0088077D  E9 DD FB FF FF                  jmp 0x14088035f
00880782  4C 3B FD                        cmp r15, rbp
00880785  75 DC                           jne 0x140880763
00880787  E9 D0 FC FF FF                  jmp 0x14088045c
0088078C  BB 1B 00 00 C0                  mov ebx, 0xc000001b
00880791  E9 7F FD FF FF                  jmp 0x140880515
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFreeVirtualMemory(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, unsigned int a7, unsigned __int8 a8, unsigned __int8 a9, __int64 a10, __int64 a11)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned int v_stack_pA0;

    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (72);
    v_r15 = (*(unsigned __int64 *)(a3)) >> (12);
    v_rsi = (*(unsigned __int64 *)(a4)) >> (12);
    a2 = (unsigned int)(((unsigned int)(a6)) & (0x8000ULL));
    *(unsigned __int8 *)(v_rsp + 16) = 0;
    v_stack_p18 = (unsigned int)(a2);
loc_008802B9:
    v_rbp = (*(unsigned __int8 *)(a2 + 32)) << (32);
    v_rbp = (v_rbp) | ((unsigned int)(*(unsigned int *)(a2 + 24)));
    v_r14 = (*(unsigned __int8 *)(a2 + 33)) << (32);
    v_r14 = (v_r14) | ((unsigned int)(*(unsigned int *)(a2 + 28)));
    if (a5 == 0) goto loc_008804B2;
loc_008802EF:
    if (v_r15 < v_rbp) goto loc_008804FC;
loc_008802F8:
    if (v_r15 > v_r14) goto loc_008804FC;
    if (v_rsi < v_rbp) goto loc_008804FC;
    if (v_rsi > v_r14) goto loc_008804FC;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 48))))) & (0x200000ULL));
    if (((a6) & (0x10000ULL)) != 0) goto loc_0088070A;
    if ((unsigned int)(a1) == 0) goto loc_0088078C;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a2 + 48))) & (112));
loc_0088033B:
    if (((unsigned __int8)(result)) == 16) goto loc_0088078C;
loc_00880341:
    if (((unsigned __int8)(result)) < 16) goto loc_00880629;
loc_00880354:
    if (((unsigned __int8)(result)) < 16) goto loc_00880503;
loc_0088035F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 48)))) & (8)) != 0) goto loc_00880662;
loc_0088036A:
    if ((unsigned int)(a2) != 0) goto loc_00880441;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 48))) & (0xC200000ULL));
    if (((unsigned int)(result)) == 0x8200000ULL) goto loc_008805D9;
loc_00880385:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 48))))) & (112));
    if (((unsigned __int8)(result)) == 48) goto loc_008805CF;
    if (((unsigned __int8)(result)) >= 48) goto loc_008803B7;
    if (((unsigned __int8)(result)) < 48) goto loc_00880592;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 48))))) & (0x180000ULL));
    if (((unsigned int)(result)) >= 0x100000ULL) goto loc_00880592;
loc_008803B7:
    a2 = (*(unsigned __int8 *)(a2 + 34)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(a2 + 52)));
    if (a2 == result) goto loc_008805CF;
    if (a5 == 0) goto loc_00880546;
loc_008803E7:
    v_rsi = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(a3));
    v_rsi = (v_rsi) + 1;
    result = MiDecommitRegion(a2, *(unsigned __int64 *)(a3), *(unsigned __int64 *)(a4), (unsigned int)(a7));
    v_stack_p20 = (unsigned int)(result);
loc_00880407:
    result = MiUnlockAndDereferenceVad(a2, *(unsigned __int64 *)(a3), *(unsigned __int64 *)(a4), (unsigned int)(a7));
    if (v_stack_p20 != 0) goto loc_008804E7;
loc_0088041D:
    if (((*(unsigned int *)(v_rip + 7628509)) & (0x8000ULL)) != 0) goto loc_00880571;
loc_0088042D:
    result = 0;
loc_0088042F:
    v_rsp = (v_rsp) + (72);
    return result;
loc_00880441:
    if (((a8) & (1)) == 0) goto loc_0088045C;
    if (((*(unsigned int *)(a1 + 1532)) & (256)) != 0) goto loc_0088075E;
loc_0088045C:
    v_stack_p30 = a10;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a7)))) >> (26));
    result = (unsigned int)((result) & (1));
    v_stack_p28 = (unsigned int)(result);
    v_stack_p20 = a1;
    result = MiFreeVadRange(a2, v_stack_p98, v_r15, v_rsi);
    if (!sign_flag) goto loc_0088042D;
    if (((unsigned int)(result)) != 0xC000022DULL) goto loc_00880515;
    goto loc_008802B9;
loc_008804B2:
    result = (v_r14) << (12);
    result = (result) | (0xFFFULL);
    *(unsigned __int64 *)(a4) = result;
    if ((unsigned int)((unsigned int)(v_stack_pA0)) == 0) goto loc_008802EF;
    if (v_r15 != v_rbp) goto loc_0088061F;
    result = (v_rbp) << (12);
    *(unsigned __int64 *)(a3) = result;
    goto loc_008802F8;
loc_008804E7:
    a3 = 0;
    result = MiDeleteEmptyPageTables(*(unsigned __int64 *)(a3), *(unsigned __int64 *)(a4), a3, v_rsi);
    goto loc_0088041D;
loc_008804FC:
    goto loc_00880515;
loc_00880503:
    if (condition_is_below) goto loc_0088076D;
loc_00880510:
loc_00880515:
    result = MiUnlockAndDereferenceVad(a2, *(unsigned __int64 *)(a4), a3, v_rsi);
    if (v_stack_p98 != 0) goto loc_0088052E;
loc_00880527:
    goto loc_0088042F;
loc_0088052E:
    result = UNLOCK_ADDRESS_SPACE(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_p90, a3, v_rsi);
    goto loc_00880527;
loc_00880546:
    if (v_r15 != v_rbp) goto loc_0088061F;
    a1 = (*(unsigned __int8 *)(a2 + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(a2 + 28)));
    a1 = (a1) << (12);
    a1 = (a1) | (0xFFFULL);
    *(unsigned __int64 *)(a4) = a1;
    goto loc_008803E7;
loc_00880571:
    result = PerfInfoLogVirtualFree(*(unsigned __int64 *)(a3), v_r14, v_stack_p90, (unsigned int)(a6));
    goto loc_0088042D;
loc_00880592:
    a1 = (unsigned int)((*(unsigned __int64 *)(a3)) & ((unsigned int)((unsigned int)(0xA00000ULL))));
    if (((unsigned int)(a1)) != ((unsigned int)((unsigned int)(0xA00000ULL)))) goto loc_008805CF;
    if (a5 == 0) goto loc_008803B7;
    result = MiGetVadPageSize(a2, v_r14, v_stack_p90, (unsigned int)(a6));
    a1 = (*(unsigned __int64 *)(a4)) + 1;
    result = (result) << (12);
    a1 = (a1) | (*(unsigned __int64 *)(a3));
    result = (result) - 1;
    if (((a1) & (result)) == 0) goto loc_008803B7;
loc_008805CF:
    goto loc_00880515;
loc_008805D9:
    if (a5 == 0) goto loc_008805CF;
    v_rsi = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(a3));
    v_stack_p20 = (unsigned int)((unsigned int)(a6));
    v_rsi = (v_rsi) + 1;
    result = MiDecommitEnclavePages(v_stack_p90, a2, *(unsigned __int64 *)(a3), v_rsi);
    if (((unsigned int)(result)) == 0xC0000016ULL) goto loc_00880385;
    if (sign_flag) goto loc_00880515;
    goto loc_00880407;
loc_0088061F:
    goto loc_00880515;
loc_00880629:
    result = MiLocateLockedVadEvent(a2, 128, *(unsigned __int64 *)(a3), v_rsi);
    if (result == 0) goto loc_008806D7;
loc_0088063F:
    a2 = (*(unsigned __int8 *)(a2 + 34)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(a2 + 52)));
    if (a2 == (*(unsigned __int64 *)(a3))) goto loc_008806F3;
loc_00880656:
    goto loc_00880354;
loc_00880662:
    if (a2 < (*(unsigned __int64 *)(a3))) goto loc_0088036A;
    if ((unsigned int)((unsigned int)(v_stack_pA0)) != 0) goto loc_00880723;
    a3 = (v_rsi) - (v_r15);
loc_0088067F:
    a3 = (a3) + 1;
    v_stack_p28 = a11;
    a3 = (a3) << (12);
    v_stack_p20 = a9;
    result = MiCheckSecuredVad(a2, *(unsigned __int64 *)(a3), a3, 85);
    if (sign_flag) goto loc_00880515;
    goto loc_0088036A;
loc_008806D7:
    a1 = (*(unsigned __int8 *)(a2 + 34)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(a2 + 52)));
    if (a1 == a3) goto loc_0088063F;
    goto loc_00880510;
loc_008806F3:
    if (v_rsi != v_r14) goto loc_00880656;
    if (v_r15 != v_rbp) goto loc_00880656;
    goto loc_00880510;
loc_0088070A:
    if ((unsigned int)(a1) != 0) goto loc_0088078C;
    if ((((unsigned __int8)(result)) & (112)) != 0) goto loc_0088078C;
    if (v_r15 != v_rbp) goto loc_00880341;
    goto loc_0088033B;
loc_00880723:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p90 + 500)))) & (32)) != 0) goto loc_00880441;
    a3 = (*(unsigned __int8 *)(a2 + 33)) << (32);
    a3 = (a3) | ((unsigned int)(*(unsigned int *)(a2 + 28)));
    a1 = (*(unsigned __int8 *)(a2 + 32)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(a2 + 24)));
    a2 = (v_rbp) << (12);
    a3 = (a3) - (a1);
    goto loc_0088067F;
loc_0088075E:
    if (v_rsi == v_r14) goto loc_00880782;
loc_00880763:
    goto loc_00880515;
loc_0088076D:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 24))) & (0x14000000ULL));
    if (((unsigned int)(result)) != 0x10000000ULL) goto loc_00880510;
    goto loc_0088035F;
loc_00880782:
    if (v_r15 != v_rbp) goto loc_00880763;
    goto loc_0088045C;
loc_0088078C:
    goto loc_00880515;
}
```

## 5. (Beta) C Style

```c
int64_t MiFreeVirtualMemory(int64_t Arg1, void *Arg2, void *Arg3, void *Arg4, int64_t Arg5, uint32_t Arg6, uint32_t Arg7, uint8_t Arg8, uint8_t Arg9, int64_t Arg10, int64_t Arg11)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint32_t v_stack_pA0;

    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (72);
    local_r15 = (*(uint64_t *)(arg3)) >> (12);
    local_rsi = (*(uint64_t *)(arg4)) >> (12);
    Arg2 = (uint32_t)(((uint32_t)(Arg6)) & (0x8000ULL));
    *(uint8_t *)(local_rsp + 0x10) = 0;
    v_stack_p18 = (uint32_t)(Arg2);
loc_008802B9:
    local_rbp = (*(uint8_t *)(arg2 + 0x20)) << (32);
    local_rbp = (local_rbp) | ((uint32_t)(*(uint32_t *)(arg2 + 0x18)));
    local_r14 = (*(uint8_t *)(arg2 + 0x21)) << (32);
    local_r14 = (local_r14) | ((uint32_t)(*(uint32_t *)(arg2 + 0x1C)));
    if (Arg5 == 0) goto loc_008804B2;
loc_008802EF:
    if (local_r15 < local_rbp) goto loc_008804FC;
loc_008802F8:
    if (local_r15 > local_r14) goto loc_008804FC;
    if (local_rsi < local_rbp) goto loc_008804FC;
    if (local_rsi > local_r14) goto loc_008804FC;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x30))))) & (0x200000ULL));
    if (((Arg6) & (0x10000ULL)) != 0) goto loc_0088070A;
    if ((uint32_t)(Arg1) == 0) goto loc_0088078C;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x30))) & (112));
loc_0088033B:
    if (((uint8_t)(result)) == 16) goto loc_0088078C;
loc_00880341:
    if (((uint8_t)(result)) < 16) goto loc_00880629;
loc_00880354:
    if (((uint8_t)(result)) < 16) goto loc_00880503;
loc_0088035F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x30)))) & (8)) != 0) goto loc_00880662;
loc_0088036A:
    if ((uint32_t)(Arg2) != 0) goto loc_00880441;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x30))) & (0xC200000ULL));
    if (((uint32_t)(result)) == 0x8200000ULL) goto loc_008805D9;
loc_00880385:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x30))))) & (112));
    if (((uint8_t)(result)) == 48) goto loc_008805CF;
    if (((uint8_t)(result)) >= 48) goto loc_008803B7;
    if (((uint8_t)(result)) < 48) goto loc_00880592;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x30))))) & (0x180000ULL));
    if (((uint32_t)(result)) >= 0x100000ULL) goto loc_00880592;
loc_008803B7:
    Arg2 = (*(uint8_t *)(arg2 + 0x22)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(arg2 + 0x34)));
    if (Arg2 == result) goto loc_008805CF;
    if (Arg5 == 0) goto loc_00880546;
loc_008803E7:
    local_rsi = (*(uint64_t *)(arg4)) - (*(uint64_t *)(arg3));
    local_rsi = (local_rsi) + 1;
    result = MiDecommitRegion(Arg2, *(uint64_t *)(arg3), *(uint64_t *)(arg4), (uint32_t)(Arg7));
    v_stack_p20 = (uint32_t)(result);
loc_00880407:
    result = MiUnlockAndDereferenceVad(Arg2, *(uint64_t *)(arg3), *(uint64_t *)(arg4), (uint32_t)(Arg7));
    if (v_stack_p20 != 0) goto loc_008804E7;
loc_0088041D:
    if (((*(uint32_t *)(v_rip + 0x7466DD)) & (0x8000ULL)) != 0) goto loc_00880571;
loc_0088042D:
    result = 0;
loc_0088042F:
    local_rsp = (local_rsp) + (72);
    return result;
loc_00880441:
    if (((Arg8) & (1)) == 0) goto loc_0088045C;
    if (((*(uint32_t *)(Arg1 + 0x5FC)) & (256)) != 0) goto loc_0088075E;
loc_0088045C:
    v_stack_p30 = Arg10;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg7)))) >> (26));
    result = (uint32_t)((result) & (1));
    v_stack_p28 = (uint32_t)(result);
    v_stack_p20 = Arg1;
    result = MiFreeVadRange(Arg2, v_stack_p98, local_r15, local_rsi);
    if (!sign_flag) goto loc_0088042D;
    if (((uint32_t)(result)) != 0xC000022DULL) goto loc_00880515;
    goto loc_008802B9;
loc_008804B2:
    result = (local_r14) << (12);
    result = (result) | (0xFFFULL);
    *(uint64_t *)(arg4) = result;
    if ((uint32_t)((uint32_t)(v_stack_pA0)) == 0) goto loc_008802EF;
    if (local_r15 != local_rbp) goto loc_0088061F;
    result = (local_rbp) << (12);
    *(uint64_t *)(arg3) = result;
    goto loc_008802F8;
loc_008804E7:
    Arg3 = 0;
    result = MiDeleteEmptyPageTables(*(uint64_t *)(arg3), *(uint64_t *)(arg4), Arg3, local_rsi);
    goto loc_0088041D;
loc_008804FC:
    goto loc_00880515;
loc_00880503:
    if (condition_is_below) goto loc_0088076D;
loc_00880510:
loc_00880515:
    result = MiUnlockAndDereferenceVad(Arg2, *(uint64_t *)(arg4), Arg3, local_rsi);
    if (v_stack_p98 != 0) goto loc_0088052E;
loc_00880527:
    goto loc_0088042F;
loc_0088052E:
    result = UNLOCK_ADDRESS_SPACE(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_p90, Arg3, local_rsi);
    goto loc_00880527;
loc_00880546:
    if (local_r15 != local_rbp) goto loc_0088061F;
    Arg1 = (*(uint8_t *)(arg2 + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(arg2 + 0x1C)));
    Arg1 = (Arg1) << (12);
    Arg1 = (Arg1) | (0xFFFULL);
    *(uint64_t *)(arg4) = Arg1;
    goto loc_008803E7;
loc_00880571:
    result = PerfInfoLogVirtualFree(*(uint64_t *)(arg3), local_r14, v_stack_p90, (uint32_t)(Arg6));
    goto loc_0088042D;
loc_00880592:
    Arg1 = (uint32_t)((*(uint64_t *)(arg3)) & ((uint32_t)((uint32_t)(0xA00000ULL))));
    if (((uint32_t)(Arg1)) != ((uint32_t)((uint32_t)(0xA00000ULL)))) goto loc_008805CF;
    if (Arg5 == 0) goto loc_008803B7;
    result = MiGetVadPageSize(Arg2, local_r14, v_stack_p90, (uint32_t)(Arg6));
    Arg1 = (*(uint64_t *)(arg4)) + 1;
    result = (result) << (12);
    Arg1 = (Arg1) | (*(uint64_t *)(arg3));
    result = (result) - 1;
    if (((Arg1) & (result)) == 0) goto loc_008803B7;
loc_008805CF:
    goto loc_00880515;
loc_008805D9:
    if (Arg5 == 0) goto loc_008805CF;
    local_rsi = (*(uint64_t *)(arg4)) - (*(uint64_t *)(arg3));
    v_stack_p20 = (uint32_t)((uint32_t)(Arg6));
    local_rsi = (local_rsi) + 1;
    result = MiDecommitEnclavePages(v_stack_p90, Arg2, *(uint64_t *)(arg3), local_rsi);
    if (((uint32_t)(result)) == 0xC0000016ULL) goto loc_00880385;
    if (sign_flag) goto loc_00880515;
    goto loc_00880407;
loc_0088061F:
    goto loc_00880515;
loc_00880629:
    result = MiLocateLockedVadEvent(Arg2, 128, *(uint64_t *)(arg3), local_rsi);
    if (result == 0) goto loc_008806D7;
loc_0088063F:
    Arg2 = (*(uint8_t *)(arg2 + 0x22)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(arg2 + 0x34)));
    if (Arg2 == (*(uint64_t *)(arg3))) goto loc_008806F3;
loc_00880656:
    goto loc_00880354;
loc_00880662:
    if (Arg2 < (*(uint64_t *)(arg3))) goto loc_0088036A;
    if ((uint32_t)((uint32_t)(v_stack_pA0)) != 0) goto loc_00880723;
    Arg3 = (local_rsi) - (local_r15);
loc_0088067F:
    Arg3 = (Arg3) + 1;
    v_stack_p28 = Arg11;
    Arg3 = (Arg3) << (12);
    v_stack_p20 = Arg9;
    result = MiCheckSecuredVad(Arg2, *(uint64_t *)(arg3), Arg3, 85);
    if (sign_flag) goto loc_00880515;
    goto loc_0088036A;
loc_008806D7:
    Arg1 = (*(uint8_t *)(arg2 + 0x22)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(arg2 + 0x34)));
    if (Arg1 == Arg3) goto loc_0088063F;
    goto loc_00880510;
loc_008806F3:
    if (local_rsi != local_r14) goto loc_00880656;
    if (local_r15 != local_rbp) goto loc_00880656;
    goto loc_00880510;
loc_0088070A:
    if ((uint32_t)(Arg1) != 0) goto loc_0088078C;
    if ((((uint8_t)(result)) & (112)) != 0) goto loc_0088078C;
    if (local_r15 != local_rbp) goto loc_00880341;
    goto loc_0088033B;
loc_00880723:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p90 + 0x1F4)))) & (32)) != 0) goto loc_00880441;
    Arg3 = (*(uint8_t *)(arg2 + 0x21)) << (32);
    Arg3 = (Arg3) | ((uint32_t)(*(uint32_t *)(arg2 + 0x1C)));
    Arg1 = (*(uint8_t *)(arg2 + 0x20)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(arg2 + 0x18)));
    Arg2 = (local_rbp) << (12);
    Arg3 = (Arg3) - (Arg1);
    goto loc_0088067F;
loc_0088075E:
    if (local_rsi == local_r14) goto loc_00880782;
loc_00880763:
    goto loc_00880515;
loc_0088076D:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x18))) & (0x14000000ULL));
    if (((uint32_t)(result)) != 0x10000000ULL) goto loc_00880510;
    goto loc_0088035F;
loc_00880782:
    if (local_r15 != local_rbp) goto loc_00880763;
    goto loc_0088045C;
loc_0088078C:
    goto loc_00880515;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x18` | `32` | `R` |
| `Arg2` | `+ 0x1C` | `32` | `R` |
| `Arg2` | `+ 0x20` | `8` | `R` |
| `Arg2` | `+ 0x21` | `8` | `R` |
| `Arg2` | `+ 0x22` | `8` | `R` |
| `Arg2` | `+ 0x30` | `32` | `R` |
| `Arg2` | `+ 0x34` | `32` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00880268&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
