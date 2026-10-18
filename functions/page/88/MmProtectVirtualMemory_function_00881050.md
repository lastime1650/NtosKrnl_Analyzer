# MmProtectVirtualMemory

- RVA: `0x00881050`–`0x00881A3F` (길이 `2,543` bytes)
- VA: `0x0000000140881050`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007C57C`
- 디코드: `545`개 명령, `2,543/2,543` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00881126` → [MiMakeProtectionMask](../../text/32/MiMakeProtectionMask_function_00329480.md) (function, `0x00329480`)
- `0x008811AE` → [MiObtainReferencedVadEx](../../text/31/MiObtainReferencedVadEx_function_00316690.md) (function, `0x00316690`)
- `0x0088130C` → [MiVadMapsLargeImage](../../text/2A/MiVadMapsLargeImage_function_002A70F0.md) (function, `0x002A70F0`)
- `0x0088131F` → [MiIsRangeFullyCommitted](MiIsRangeFullyCommitted_function_00881E24.md) (function, `0x00881E24`)
- `0x0088135A` → [MiSetProtectionOnSection](../../text/2C/MiSetProtectionOnSection_function_002C3770.md) (function, `0x002C3770`)
- `0x0088136A` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (function, `0x00316E60`)
- `0x008813DB` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (function, `0x00316E60`)
- `0x00881413` → [MiGetVadPageSize](../../text/42/MiGetVadPageSize_function_0042F0E0.md) (function, `0x0042F0E0`)
- `0x00881488` → [MiProtectPrivateMemory](../../text/2C/MiProtectPrivateMemory_function_002C45B0.md) (function, `0x002C45B0`)
- `0x008814DC` → [MiAllowProtectionChange](../../text/44/MiAllowProtectionChange_function_00448834.md) (function, `0x00448834`)
- `0x00881543` → [MiCheckSecuredVad](MiCheckSecuredVad_function_00881FB4.md) (function, `0x00881FB4`)
- `0x008815D8` → [HalAdjustResourceList](../../text/48/HalAdjustResourceList_function_0048FDC0.md) (function, `0x0048FDC0`)
- `0x008816EF` → [MiCommitVadMetadataBits](../8D/MiCommitVadMetadataBits_function_008D1A00.md) (function, `0x008D1A00`)
- `0x0088172E` → [DefaultAddProfileSource](../../text/4E/DefaultAddProfileSource_function_004E1110.md) (function, `0x004E1110`)
- `0x0088178C` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (function, `0x00316E60`)
- `0x008817F7` → [MiCheckSecuredVad](MiCheckSecuredVad_function_00881FB4.md) (function, `0x00881FB4`)
- `0x0088183E` → [MiProtectAweRegion](../../text/4C/MiProtectAweRegion_function_004CE62C.md) (function, `0x004CE62C`)
- `0x00881852` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (function, `0x00316E60`)
- `0x008818CE` → [MiMakeProtectionMask](../../text/32/MiMakeProtectionMask_function_00329480.md) (function, `0x00329480`)
- `0x00881961` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (function, `0x00316E60`)

### Direct callers
- [KiTpWriteUmMemory](../../text/5C/KiTpWriteUmMemory_function_005CACB8.md) at `0x005CAD14`
- [KiTpWriteUmMemory](../../text/5C/KiTpWriteUmMemory_function_005CACB8.md) at `0x005CAD67`
- [sub_006F88AE](../../text/6F/Unknown_function_006F88AE.md) at `0x006F89DC`
- [NtProtectVirtualMemory](NtProtectVirtualMemory_function_00880CA0.md) at `0x00880E71`
- [MiAllocateVirtualMemory](MiAllocateVirtualMemory_function_00883B40.md) at `0x0088418D`

### Static image references
- `0x008812D9` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x00881126` → [MiMakeProtectionMask](../../text/32/MiMakeProtectionMask_function_00329480.md) (`PAGE` → `.text`)
  - `0x008811AE` → [MiObtainReferencedVadEx](../../text/31/MiObtainReferencedVadEx_function_00316690.md) (`PAGE` → `.text`)
  - `0x0088130C` → [MiVadMapsLargeImage](../../text/2A/MiVadMapsLargeImage_function_002A70F0.md) (`PAGE` → `.text`)
  - `0x0088135A` → [MiSetProtectionOnSection](../../text/2C/MiSetProtectionOnSection_function_002C3770.md) (`PAGE` → `.text`)
  - `0x0088136A` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (`PAGE` → `.text`)
  - `0x008813DB` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (`PAGE` → `.text`)
  - `0x00881413` → [MiGetVadPageSize](../../text/42/MiGetVadPageSize_function_0042F0E0.md) (`PAGE` → `.text`)
  - `0x00881488` → [MiProtectPrivateMemory](../../text/2C/MiProtectPrivateMemory_function_002C45B0.md) (`PAGE` → `.text`)
  - `0x008814DC` → [MiAllowProtectionChange](../../text/44/MiAllowProtectionChange_function_00448834.md) (`PAGE` → `.text`)
  - `0x008815D8` → [HalAdjustResourceList](../../text/48/HalAdjustResourceList_function_0048FDC0.md) (`PAGE` → `.text`)
  - `0x0088172E` → [DefaultAddProfileSource](../../text/4E/DefaultAddProfileSource_function_004E1110.md) (`PAGE` → `.text`)
  - `0x0088178C` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (`PAGE` → `.text`)
  - `0x0088183E` → [MiProtectAweRegion](../../text/4C/MiProtectAweRegion_function_004CE62C.md) (`PAGE` → `.text`)
  - `0x00881852` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (`PAGE` → `.text`)
  - `0x008818CE` → [MiMakeProtectionMask](../../text/32/MiMakeProtectionMask_function_00329480.md) (`PAGE` → `.text`)
  - `0x00881961` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0088124C` → [sub_00B18CEA](../B1/Unknown_function_00B18CEA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00881050  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00881055  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0088105A  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0088105F  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00881064  53                              push rbx
00881065  56                              push rsi
00881066  57                              push rdi
00881067  41 54                           push r12
00881069  41 55                           push r13
0088106B  41 56                           push r14
0088106D  41 57                           push r15
0088106F  48 81 EC F0 00 00 00            sub rsp, 0xf0
00881076  4C 8B DA                        mov r11, rdx
00881079  8B 9C 24 50 01 00 00            mov ebx, dword ptr [rsp + 0x150]
00881080  44 8B D3                        mov r10d, ebx
00881083  33 F6                           xor esi, esi
00881085  89 74 24 60                     mov dword ptr [rsp + 0x60], esi
00881089  89 74 24 70                     mov dword ptr [rsp + 0x70], esi
0088108D  48 8B 8C 24 58 01 00 00         mov rcx, qword ptr [rsp + 0x158]
00881095  C7 01 01 00 00 00               mov dword ptr [rcx], 1
0088109B  89 74 24 74                     mov dword ptr [rsp + 0x74], esi
0088109F  89 74 24 68                     mov dword ptr [rsp + 0x68], esi
008810A3  C6 44 24 64 01                  mov byte ptr [rsp + 0x64], 1
008810A8  4D 8B 00                        mov r8, qword ptr [r8]
008810AB  4C 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], r8
008810B3  4C 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r8
008810BB  4D 8B 09                        mov r9, qword ptr [r9]
008810BE  4C 89 8C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r9
008810C6  4C 89 8C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r9
008810CE  8B D3                           mov edx, ebx
008810D0  81 E2 00 F8 07 00               and edx, 0x7f800
008810D6  89 54 24 6C                     mov dword ptr [rsp + 0x6c], edx
008810DA  0F 85 4E 06 00 00               jne 0x14088172e
008810E0  8B CB                           mov ecx, ebx
008810E2  C1 E9 1F                        shr ecx, 0x1f
008810E5  89 8C 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], ecx
008810EC  89 8C 24 90 00 00 00            mov dword ptr [rsp + 0x90], ecx
008810F3  44 8B FB                        mov r15d, ebx
008810F6  41 81 E7 00 00 00 B0            and r15d, 0xb0000000
008810FD  44 89 BC 24 A4 00 00 00         mov dword ptr [rsp + 0xa4], r15d
00881105  81 E3 FF 07 F8 4F               and ebx, 0x4ff807ff
0088110B  89 9C 24 50 01 00 00            mov dword ptr [rsp + 0x150], ebx
00881112  0F BA E3 1E                     bt ebx, 0x1e
00881116  0F 82 45 04 00 00               jb 0x140881561
0088111C  85 DB                           test ebx, ebx
0088111E  0F 84 2A 06 00 00               je 0x14088174e
00881124  8B CB                           mov ecx, ebx
00881126  E8 55 83 AA FF                  call 0x140329480
0088112B  44 8B E8                        mov r13d, eax
0088112E  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
00881135  83 F8 FF                        cmp eax, -1
00881138  0F 84 9C 08 00 00               je 0x1408819da
0088113E  4D 8D 70 FF                     lea r14, [r8 - 1]
00881142  4D 03 F1                        add r14, r9
00881145  49 81 CE FF 0F 00 00            or r14, 0xfff
0088114C  4C 89 B4 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r14
00881154  4D 8B E0                        mov r12, r8
00881157  49 81 E4 00 F0 FF FF            and r12, 0xfffffffffffff000
0088115E  4C 89 A4 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r12
00881166  48 89 B4 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rsi
0088116E  48 8B C6                        mov rax, rsi
00881171  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00881176  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0088117E  41 8B C5                        mov eax, r13d
00881181  83 E0 F8                        and eax, 0xfffffff8
00881184  83 F8 10                        cmp eax, 0x10
00881187  0F 84 63 04 00 00               je 0x1408815f0
0088118D  48 89 B4 24 90 00 00 00         mov qword ptr [rsp + 0x90], rsi
00881195  49 8B C6                        mov rax, r14
00881198  48 C1 E8 0C                     shr rax, 0xc
0088119C  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
008811A4  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
008811A9  33 D2                           xor edx, edx
008811AB  49 8B CC                        mov rcx, r12
008811AE  E8 DD 54 A9 FF                  call 0x140316690
008811B3  48 8B F8                        mov rdi, rax
008811B6  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
008811BE  48 85 C0                        test rax, rax
008811C1  0F 84 F3 01 00 00               je 0x1408813ba
008811C7  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
008811CF  0F B6 48 21                     movzx ecx, byte ptr [rax + 0x21]
008811D3  48 C1 E1 20                     shl rcx, 0x20
008811D7  8B 40 1C                        mov eax, dword ptr [rax + 0x1c]
008811DA  48 0B C8                        or rcx, rax
008811DD  48 39 8C 24 C0 00 00 00         cmp qword ptr [rsp + 0xc0], rcx
008811E5  0F 87 9A 03 00 00               ja 0x140881585
008811EB  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
008811EE  25 00 00 20 04                  and eax, 0x4200000
008811F3  3D 00 00 20 04                  cmp eax, 0x4200000
008811F8  0F 84 70 05 00 00               je 0x14088176e
008811FE  83 7C 24 6C 00                  cmp dword ptr [rsp + 0x6c], 0
00881203  0F 85 DB 07 00 00               jne 0x1408819e4
00881209  45 32 C0                        xor r8b, r8b
0088120C  44 88 84 24 50 01 00 00         mov byte ptr [rsp + 0x150], r8b
00881214  41 F6 C5 02                     test r13b, 2
00881218  0F 85 9E 02 00 00               jne 0x1408814bc
0088121E  8B 57 30                        mov edx, dword ptr [rdi + 0x30]
00881221  0F BA E2 15                     bt edx, 0x15
00881225  0F 82 BB 01 00 00               jb 0x1408813e6
0088122B  8B C2                           mov eax, edx
0088122D  83 E0 70                        and eax, 0x70
00881230  3C 50                           cmp al, 0x50
00881232  0F 84 C6 01 00 00               je 0x1408813fe
00881238  4C 8B 94 24 98 00 00 00         mov r10, qword ptr [rsp + 0x98]
00881240  8B C2                           mov eax, edx
00881242  25 00 00 20 04                  and eax, 0x4200000
00881247  3D 00 00 20 00                  cmp eax, 0x200000
0088124C  0F 84 98 7A 29 00               je 0x140b18cea
00881252  41 F7 C7 FF FF FF 5F            test r15d, 0x5fffffff
00881259  0F 85 8F 07 00 00               jne 0x1408819ee
0088125F  85 DB                           test ebx, ebx
00881261  0F 84 91 07 00 00               je 0x1408819f8
00881267  8B C2                           mov eax, edx
00881269  83 E0 70                        and eax, 0x70
0088126C  83 F8 30                        cmp eax, 0x30
0088126F  0F 84 B1 05 00 00               je 0x140881826
00881275  83 F8 10                        cmp eax, 0x10
00881278  0F 84 8E 07 00 00               je 0x140881a0c
0088127E  44 8B BC 24 8C 00 00 00         mov r15d, dword ptr [rsp + 0x8c]
00881286  45 85 FF                        test r15d, r15d
00881289  0F 85 00 03 00 00               jne 0x14088158f
0088128F  F6 C2 08                        test dl, 8
00881292  0F 85 78 02 00 00               jne 0x140881510
00881298  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
0088129D  8B 4F 30                        mov ecx, dword ptr [rdi + 0x30]
008812A0  0F BA E1 15                     bt ecx, 0x15
008812A4  0F 82 94 01 00 00               jb 0x14088143e
008812AA  F7 C3 00 06 00 00               test ebx, 0x600
008812B0  0F 85 F1 02 00 00               jne 0x1408815a7
008812B6  8B C1                           mov eax, ecx
008812B8  24 70                           and al, 0x70
008812BA  3C 20                           cmp al, 0x20
008812BC  75 14                           jne 0x1408812d2
008812BE  F6 C3 04                        test bl, 4
008812C1  74 06                           je 0x1408812c9
008812C3  83 E3 FB                        and ebx, 0xfffffffb
008812C6  83 CB 08                        or ebx, 8
008812C9  F6 C3 40                        test bl, 0x40
008812CC  0F 85 DE 01 00 00               jne 0x1408814b0
008812D2  48 C1 E9 07                     shr rcx, 7
008812D6  83 E1 07                        and ecx, 7
008812D9  48 8D 35 20 ED 77 FF            lea rsi, [rip - 0x8812e0]
008812E0  8B 8C 8E 10 47 01 00            mov ecx, dword ptr [rsi + rcx*4 + 0x14710]
008812E7  81 C9 00 07 00 00               or ecx, 0x700
008812ED  8B C1                           mov eax, ecx
008812EF  0B C3                           or eax, ebx
008812F1  3B C1                           cmp eax, ecx
008812F3  0F 85 1D 07 00 00               jne 0x140881a16
008812F9  48 8B 47 48                     mov rax, qword ptr [rdi + 0x48]
008812FD  48 8B 08                        mov rcx, qword ptr [rax]
00881300  8B 41 38                        mov eax, dword ptr [rcx + 0x38]
00881303  24 A0                           and al, 0xa0
00881305  3C 80                           cmp al, 0x80
00881307  74 23                           je 0x14088132c
00881309  48 8B CF                        mov rcx, rdi
0088130C  E8 DF 5D A2 FF                  call 0x1402a70f0
00881311  85 C0                           test eax, eax
00881313  0F 85 6A 04 00 00               jne 0x140881783
00881319  4D 8B C6                        mov r8, r14
0088131C  49 8B D4                        mov rdx, r12
0088131F  E8 00 0B 00 00                  call 0x140881e24
00881324  85 C0                           test eax, eax
00881326  0F 84 5E 05 00 00               je 0x14088188a
0088132C  48 8D 44 24 74                  lea rax, [rsp + 0x74]
00881331  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00881336  48 8D 44 24 70                  lea rax, [rsp + 0x70]
0088133B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00881340  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00881345  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00881349  4D 8B CE                        mov r9, r14
0088134C  4D 8B C4                        mov r8, r12
0088134F  48 8B D7                        mov rdx, rdi
00881352  48 8B 8C 24 38 01 00 00         mov rcx, qword ptr [rsp + 0x138]
0088135A  E8 11 24 A4 FF                  call 0x1402c3770
0088135F  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00881363  85 C0                           test eax, eax
00881365  78 67                           js 0x1408813ce
00881367  48 8B CF                        mov rcx, rdi
0088136A  E8 F1 5A A9 FF                  call 0x140316e60
0088136F  4D 2B F4                        sub r14, r12
00881372  49 FF C6                        inc r14
00881375  48 8B 84 24 48 01 00 00         mov rax, qword ptr [rsp + 0x148]
0088137D  4C 89 30                        mov qword ptr [rax], r14
00881380  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
00881388  4C 89 20                        mov qword ptr [rax], r12
0088138B  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
0088138F  48 8B 8C 24 58 01 00 00         mov rcx, qword ptr [rsp + 0x158]
00881397  89 01                           mov dword ptr [rcx], eax
00881399  8B 44 24 74                     mov eax, dword ptr [rsp + 0x74]
0088139D  F7 D8                           neg eax
0088139F  1B C0                           sbb eax, eax
008813A1  25 17 00 00 40                  and eax, 0x40000017
008813A6  48 81 C4 F0 00 00 00            add rsp, 0xf0
008813AD  41 5F                           pop r15
008813AF  41 5E                           pop r14
008813B1  41 5D                           pop r13
008813B3  41 5C                           pop r12
008813B5  5F                              pop rdi
008813B6  5E                              pop rsi
008813B7  5B                              pop rbx
008813B8  C3                              ret
008813B9  CC                              int3
008813BA  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
008813BE  3D A0 00 00 C0                  cmp eax, 0xc00000a0
008813C3  75 09                           jne 0x1408813ce
008813C5  B8 18 00 00 C0                  mov eax, 0xc0000018
008813CA  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
008813CE  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
008813D6  48 85 C9                        test rcx, rcx
008813D9  74 CB                           je 0x1408813a6
008813DB  E8 80 5A A9 FF                  call 0x140316e60
008813E0  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
008813E4  EB C0                           jmp 0x1408813a6
008813E6  0F BA E2 17                     bt edx, 0x17
008813EA  72 12                           jb 0x1408813fe
008813EC  8B C2                           mov eax, edx
008813EE  25 00 00 18 00                  and eax, 0x180000
008813F3  3D 00 00 10 00                  cmp eax, 0x100000
008813F8  0F 82 2D FE FF FF               jb 0x14088122b
008813FE  8B C2                           mov eax, edx
00881400  25 00 00 A0 00                  and eax, 0xa00000
00881405  3D 00 00 A0 00                  cmp eax, 0xa00000
0088140A  0F 85 3F 05 00 00               jne 0x14088194f
00881410  48 8B CF                        mov rcx, rdi
00881413  E8 C8 DC BA FF                  call 0x14042f0e0
00881418  48 C1 E0 0C                     shl rax, 0xc
0088141C  49 8D 4E 01                     lea rcx, [r14 + 1]
00881420  4C 8B 94 24 98 00 00 00         mov r10, qword ptr [rsp + 0x98]
00881428  49 0B CA                        or rcx, r10
0088142B  48 FF C8                        dec rax
0088142E  48 85 C8                        test rax, rcx
00881431  0F 84 09 FE FF FF               je 0x140881240
00881437  B8 18 00 00 C0                  mov eax, 0xc0000018
0088143C  EB 8C                           jmp 0x1408813ca
0088143E  F6 C3 88                        test bl, 0x88
00881441  0F 85 60 01 00 00               jne 0x1408815a7
00881447  45 85 FF                        test r15d, r15d
0088144A  0F 85 57 01 00 00               jne 0x1408815a7
00881450  8B C1                           mov eax, ecx
00881452  24 70                           and al, 0x70
00881454  3C 40                           cmp al, 0x40
00881456  0F 84 38 04 00 00               je 0x140881894
0088145C  48 8D 44 24 74                  lea rax, [rsp + 0x74]
00881461  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00881466  48 8D 44 24 70                  lea rax, [rsp + 0x70]
0088146B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00881470  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
00881474  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00881478  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0088147C  45 8B CD                        mov r9d, r13d
0088147F  4D 8B C6                        mov r8, r14
00881482  49 8B D4                        mov rdx, r12
00881485  48 8B CF                        mov rcx, rdi
00881488  E8 23 31 A4 FF                  call 0x1402c45b0
0088148D  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00881491  85 C0                           test eax, eax
00881493  0F 88 35 FF FF FF               js 0x1408813ce
00881499  48 85 F6                        test rsi, rsi
0088149C  0F 84 C5 FE FF FF               je 0x140881367
008814A2  49 3B F6                        cmp rsi, r14
008814A5  0F 83 BC FE FF FF               jae 0x140881367
008814AB  E9 2B 04 00 00                  jmp 0x1408818db
008814B0  83 E3 BF                        and ebx, 0xffffffbf
008814B3  0F BA EB 07                     bts ebx, 7
008814B7  E9 16 FE FF FF                  jmp 0x1408812d2
008814BC  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
008814C1  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
008814C6  45 8B CD                        mov r9d, r13d
008814C9  4C 8B C7                        mov r8, rdi
008814CC  48 8B 94 24 30 01 00 00         mov rdx, qword ptr [rsp + 0x130]
008814D4  48 8B 8C 24 38 01 00 00         mov rcx, qword ptr [rsp + 0x138]
008814DC  E8 53 73 BC FF                  call 0x140448834
008814E1  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
008814E5  85 C0                           test eax, eax
008814E7  0F 88 E1 FE FF FF               js 0x1408813ce
008814ED  44 8B 47 30                     mov r8d, dword ptr [rdi + 0x30]
008814F1  41 0F BA E0 08                  bt r8d, 8
008814F6  0F 83 B5 00 00 00               jae 0x1408815b1
008814FC  8B 54 24 68                     mov edx, dword ptr [rsp + 0x68]
00881500  85 D2                           test edx, edx
00881502  0F 85 BF 01 00 00               jne 0x1408816c7
00881508  45 32 C0                        xor r8b, r8b
0088150B  E9 0E FD FF FF                  jmp 0x14088121e
00881510  45 84 C0                        test r8b, r8b
00881513  0F 85 7F FD FF FF               jne 0x140881298
00881519  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00881522  0F B6 88 32 02 00 00            movzx ecx, byte ptr [rax + 0x232]
00881529  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
0088152E  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
00881532  45 8B CD                        mov r9d, r13d
00881535  4C 8B 84 24 A8 00 00 00         mov r8, qword ptr [rsp + 0xa8]
0088153D  49 8B D2                        mov rdx, r10
00881540  48 8B CF                        mov rcx, rdi
00881543  E8 6C 0A 00 00                  call 0x140881fb4
00881548  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
0088154C  85 C0                           test eax, eax
0088154E  0F 88 7A FE FF FF               js 0x1408813ce
00881554  48 8B B4 24 80 00 00 00         mov rsi, qword ptr [rsp + 0x80]
0088155C  E9 3C FD FF FF                  jmp 0x14088129d
00881561  41 F6 C2 F0                     test r10b, 0xf0
00881565  0F 84 D9 01 00 00               je 0x140881744
0088156B  40 88 74 24 64                  mov byte ptr [rsp + 0x64], sil
00881570  41 8B DA                        mov ebx, r10d
00881573  81 E3 FF 07 F8 0F               and ebx, 0xff807ff
00881579  89 9C 24 50 01 00 00            mov dword ptr [rsp + 0x150], ebx
00881580  E9 97 FB FF FF                  jmp 0x14088111c
00881585  B8 18 00 00 C0                  mov eax, 0xc0000018
0088158A  E9 3B FE FF FF                  jmp 0x1408813ca
0088158F  0F BA E2 15                     bt edx, 0x15
00881593  72 12                           jb 0x1408815a7
00881595  48 8B 47 48                     mov rax, qword ptr [rdi + 0x48]
00881599  48 8B 08                        mov rcx, qword ptr [rax]
0088159C  8B 41 38                        mov eax, dword ptr [rcx + 0x38]
0088159F  A8 20                           test al, 0x20
008815A1  0F 84 E8 FC FF FF               je 0x14088128f
008815A7  B8 F2 00 00 C0                  mov eax, 0xc00000f2
008815AC  E9 19 FE FF FF                  jmp 0x1408813ca
008815B1  80 7C 24 64 00                  cmp byte ptr [rsp + 0x64], 0
008815B6  0F 84 40 FF FF FF               je 0x1408814fc
008815BC  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
008815C4  48 8B 80 10 04 00 00            mov rax, qword ptr [rax + 0x410]
008815CB  8B CE                           mov ecx, esi
008815CD  48 83 B8 A8 04 00 00 00         cmp qword ptr [rax + 0x4a8], 0
008815D5  0F 95 C1                        setne cl
008815D8  E8 E3 E7 C0 FF                  call 0x14048fdc0
008815DD  8B D1                           mov edx, ecx
008815DF  83 CA 04                        or edx, 4
008815E2  85 C0                           test eax, eax
008815E4  0F 44 D1                        cmove edx, ecx
008815E7  89 54 24 68                     mov dword ptr [rsp + 0x68], edx
008815EB  E9 10 FF FF FF                  jmp 0x140881500
008815F0  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008815F9  80 B8 4A 02 00 00 01            cmp byte ptr [rax + 0x24a], 1
00881600  0F 84 1E 01 00 00               je 0x140881724
00881606  49 39 B3 10 03 00 00            cmp qword ptr [r11 + 0x310], rsi
0088160D  0F 85 FB 00 00 00               jne 0x14088170e
00881613  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0088161C  48 8B 90 F0 00 00 00            mov rdx, qword ptr [rax + 0xf0]
00881623  48 89 94 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdx
0088162B  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
00881630  48 8B 4A 10                     mov rcx, qword ptr [rdx + 0x10]
00881634  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
0088163C  EB 70                           jmp 0x1408816ae
0088163E  33 F6                           xor esi, esi
00881640  8B 9C 24 50 01 00 00            mov ebx, dword ptr [rsp + 0x150]
00881647  4C 8B A4 24 C8 00 00 00         mov r12, qword ptr [rsp + 0xc8]
0088164F  4C 8B B4 24 D0 00 00 00         mov r14, qword ptr [rsp + 0xd0]
00881657  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
0088165F  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
00881667  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
0088166F  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
00881677  44 8B AC 24 88 00 00 00         mov r13d, dword ptr [rsp + 0x88]
0088167F  89 74 24 68                     mov dword ptr [rsp + 0x68], esi
00881683  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00881688  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
00881690  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
00881698  44 8B BC 24 A4 00 00 00         mov r15d, dword ptr [rsp + 0xa4]
008816A0  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
008816A7  89 84 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], eax
008816AE  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
008816B5  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
008816BD  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
008816C2  E9 C6 FA FF FF                  jmp 0x14088118d
008816C7  41 F6 C0 08                     test r8b, 8
008816CB  0F 85 F7 00 00 00               jne 0x1408817c8
008816D1  4C 89 A4 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r12
008816D9  4C 89 B4 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r14
008816E1  44 8B C2                        mov r8d, edx
008816E4  48 8D 94 24 D8 00 00 00         lea rdx, [rsp + 0xd8]
008816EC  48 8B CF                        mov rcx, rdi
008816EF  E8 0C 03 05 00                  call 0x1408d1a00
008816F4  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
008816F8  85 C0                           test eax, eax
008816FA  0F 88 CE FC FF FF               js 0x1408813ce
00881700  44 0F B6 84 24 50 01 00 00      movzx r8d, byte ptr [rsp + 0x150]
00881709  E9 10 FB FF FF                  jmp 0x14088121e
0088170E  41 0F B7 83 EC 06 00 00         movzx eax, word ptr [r11 + 0x6ec]
00881716  B9 4C 01 00 00                  mov ecx, 0x14c
0088171B  66 3B C1                        cmp ax, cx
0088171E  0F 85 96 02 00 00               jne 0x1408819ba
00881724  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
0088172C  EB 8F                           jmp 0x1408816bd
0088172E  E8 DD F9 C5 FF                  call 0x1404e1110
00881733  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00881737  85 C0                           test eax, eax
00881739  0F 89 A1 F9 FF FF               jns 0x1408810e0
0088173F  E9 62 FC FF FF                  jmp 0x1408813a6
00881744  B8 F2 00 00 C0                  mov eax, 0xc00000f2
00881749  E9 58 FC FF FF                  jmp 0x1408813a6
0088174E  41 81 FF 00 00 00 10            cmp r15d, 0x10000000
00881755  0F 85 72 02 00 00               jne 0x1408819cd
0088175B  41 BD 18 00 00 00               mov r13d, 0x18
00881761  44 89 AC 24 88 00 00 00         mov dword ptr [rsp + 0x88], r13d
00881769  E9 D0 F9 FF FF                  jmp 0x14088113e
0088176E  83 7C 24 6C 00                  cmp dword ptr [rsp + 0x6c], 0
00881773  0F 85 90 FA FF FF               jne 0x140881209
00881779  B8 45 00 00 C0                  mov eax, 0xc0000045
0088177E  E9 47 FC FF FF                  jmp 0x1408813ca
00881783  83 FB 08                        cmp ebx, 8
00881786  0F 85 18 02 00 00               jne 0x1408819a4
0088178C  E8 CF 56 A9 FF                  call 0x140316e60
00881791  4D 2B F4                        sub r14, r12
00881794  49 FF C6                        inc r14
00881797  48 8B 84 24 48 01 00 00         mov rax, qword ptr [rsp + 0x148]
0088179F  4C 89 30                        mov qword ptr [rax], r14
008817A2  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
008817AA  4C 89 20                        mov qword ptr [rax], r12
008817AD  41 8B C5                        mov eax, r13d
008817B0  8B 84 86 30 46 01 00            mov eax, dword ptr [rsi + rax*4 + 0x14630]
008817B7  48 8B 8C 24 58 01 00 00         mov rcx, qword ptr [rsp + 0x158]
008817BF  89 01                           mov dword ptr [rcx], eax
008817C1  33 C0                           xor eax, eax
008817C3  E9 DE FB FF FF                  jmp 0x1408813a6
008817C8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008817D1  0F B6 88 32 02 00 00            movzx ecx, byte ptr [rax + 0x232]
008817D8  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008817DD  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
008817E1  45 8B CD                        mov r9d, r13d
008817E4  4C 8B 84 24 A8 00 00 00         mov r8, qword ptr [rsp + 0xa8]
008817EC  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
008817F4  48 8B CF                        mov rcx, rdi
008817F7  E8 B8 07 00 00                  call 0x140881fb4
008817FC  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00881800  85 C0                           test eax, eax
00881802  0F 88 C6 FB FF FF               js 0x1408813ce
00881808  C6 84 24 50 01 00 00 01         mov byte ptr [rsp + 0x150], 1
00881810  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
00881818  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
0088181D  8B 54 24 68                     mov edx, dword ptr [rsp + 0x68]
00881821  E9 AB FE FF FF                  jmp 0x1408816d1
00881826  48 8D 44 24 70                  lea rax, [rsp + 0x70]
0088182B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00881830  44 8B 4C 24 6C                  mov r9d, dword ptr [rsp + 0x6c]
00881835  45 8B C5                        mov r8d, r13d
00881838  49 8B D6                        mov rdx, r14
0088183B  49 8B CC                        mov rcx, r12
0088183E  E8 E9 CD C4 FF                  call 0x1404ce62c
00881843  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00881847  85 C0                           test eax, eax
00881849  0F 88 B3 01 00 00               js 0x140881a02
0088184F  48 8B CF                        mov rcx, rdi
00881852  E8 09 56 A9 FF                  call 0x140316e60
00881857  4D 2B F4                        sub r14, r12
0088185A  49 FF C6                        inc r14
0088185D  48 8B 84 24 48 01 00 00         mov rax, qword ptr [rsp + 0x148]
00881865  4C 89 30                        mov qword ptr [rax], r14
00881868  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
00881870  4C 89 20                        mov qword ptr [rax], r12
00881873  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
00881877  48 8B 8C 24 58 01 00 00         mov rcx, qword ptr [rsp + 0x158]
0088187F  89 01                           mov dword ptr [rcx], eax
00881881  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
00881885  E9 1C FB FF FF                  jmp 0x1408813a6
0088188A  B8 2D 00 00 C0                  mov eax, 0xc000002d
0088188F  E9 36 FB FF FF                  jmp 0x1408813ca
00881894  F7 C3 F9 F9 FF FF               test ebx, 0xfffff9f9
0088189A  0F 85 80 01 00 00               jne 0x140881a20
008818A0  81 E3 FF F9 FF FF               and ebx, 0xfffff9ff
008818A6  8B D1                           mov edx, ecx
008818A8  81 E2 00 0C 00 00               and edx, 0xc00
008818AE  F7 C1 80 03 00 00               test ecx, 0x380
008818B4  0F 95 C1                        setne cl
008818B7  81 FA 00 0C 00 00               cmp edx, 0xc00
008818BD  0F 94 C0                        sete al
008818C0  84 C8                           test al, cl
008818C2  0F 84 62 01 00 00               je 0x140881a2a
008818C8  0F BA EB 0A                     bts ebx, 0xa
008818CC  8B CB                           mov ecx, ebx
008818CE  E8 AD 7B AA FF                  call 0x140329480
008818D3  44 8B E8                        mov r13d, eax
008818D6  E9 81 FB FF FF                  jmp 0x14088145c
008818DB  0F B6 4F 20                     movzx ecx, byte ptr [rdi + 0x20]
008818DF  48 C1 E1 20                     shl rcx, 0x20
008818E3  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
008818E6  48 0B C8                        or rcx, rax
008818E9  48 C1 EE 0C                     shr rsi, 0xc
008818ED  48 3B F1                        cmp rsi, rcx
008818F0  0F 82 71 FA FF FF               jb 0x140881367
008818F6  0F B6 4F 21                     movzx ecx, byte ptr [rdi + 0x21]
008818FA  48 C1 E1 20                     shl rcx, 0x20
008818FE  8B 47 1C                        mov eax, dword ptr [rdi + 0x1c]
00881901  48 0B C8                        or rcx, rax
00881904  48 3B F1                        cmp rsi, rcx
00881907  0F 87 5A FA FF FF               ja 0x140881367
0088190D  49 8D 56 01                     lea rdx, [r14 + 1]
00881911  48 8B C2                        mov rax, rdx
00881914  48 C1 E8 0C                     shr rax, 0xc
00881918  48 3B C1                        cmp rax, rcx
0088191B  0F 87 46 FA FF FF               ja 0x140881367
00881921  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
00881929  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
0088192D  E9 35 FA FF FF                  jmp 0x140881367
00881932  48 8B BC 24 B8 00 00 00         mov rdi, qword ptr [rsp + 0xb8]
0088193A  4C 8B A4 24 C8 00 00 00         mov r12, qword ptr [rsp + 0xc8]
00881942  4C 8B B4 24 D0 00 00 00         mov r14, qword ptr [rsp + 0xd0]
0088194A  E9 18 FA FF FF                  jmp 0x140881367
0088194F  C1 EA 07                        shr edx, 7
00881952  83 E2 1F                        and edx, 0x1f
00881955  44 3B EA                        cmp r13d, edx
00881958  0F 85 67 FA FF FF               jne 0x1408813c5
0088195E  48 8B CF                        mov rcx, rdi
00881961  E8 FA 54 A9 FF                  call 0x140316e60
00881966  4D 2B F4                        sub r14, r12
00881969  49 FF C6                        inc r14
0088196C  48 8B 84 24 48 01 00 00         mov rax, qword ptr [rsp + 0x148]
00881974  4C 89 30                        mov qword ptr [rax], r14
00881977  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
0088197F  4C 89 20                        mov qword ptr [rax], r12
00881982  41 8B C5                        mov eax, r13d
00881985  48 8D 35 74 E6 77 FF            lea rsi, [rip - 0x88198c]
0088198C  8B 84 86 30 46 01 00            mov eax, dword ptr [rsi + rax*4 + 0x14630]
00881993  48 8B 8C 24 58 01 00 00         mov rcx, qword ptr [rsp + 0x158]
0088199B  89 01                           mov dword ptr [rcx], eax
0088199D  33 C0                           xor eax, eax
0088199F  E9 02 FA FF FF                  jmp 0x1408813a6
008819A4  81 FB 80 00 00 00               cmp ebx, 0x80
008819AA  0F 84 DC FD FF FF               je 0x14088178c
008819B0  B8 4E 00 00 C0                  mov eax, 0xc000004e
008819B5  E9 10 FA FF FF                  jmp 0x1408813ca
008819BA  B9 C4 01 00 00                  mov ecx, 0x1c4
008819BF  66 3B C1                        cmp ax, cx
008819C2  0F 84 5C FD FF FF               je 0x140881724
008819C8  E9 46 FC FF FF                  jmp 0x140881613
008819CD  41 81 FF 00 00 00 80            cmp r15d, 0x80000000
008819D4  0F 84 81 FD FF FF               je 0x14088175b
008819DA  B8 45 00 00 C0                  mov eax, 0xc0000045
008819DF  E9 C2 F9 FF FF                  jmp 0x1408813a6
008819E4  B8 45 00 00 C0                  mov eax, 0xc0000045
008819E9  E9 DC F9 FF FF                  jmp 0x1408813ca
008819EE  B8 45 00 00 C0                  mov eax, 0xc0000045
008819F3  E9 D2 F9 FF FF                  jmp 0x1408813ca
008819F8  B8 45 00 00 C0                  mov eax, 0xc0000045
008819FD  E9 C8 F9 FF FF                  jmp 0x1408813ca
00881A02  B8 18 00 00 C0                  mov eax, 0xc0000018
00881A07  E9 BE F9 FF FF                  jmp 0x1408813ca
00881A0C  B8 18 00 00 C0                  mov eax, 0xc0000018
00881A11  E9 B4 F9 FF FF                  jmp 0x1408813ca
00881A16  B8 4E 00 00 C0                  mov eax, 0xc000004e
00881A1B  E9 AA F9 FF FF                  jmp 0x1408813ca
00881A20  B8 45 00 00 C0                  mov eax, 0xc0000045
00881A25  E9 A0 F9 FF FF                  jmp 0x1408813ca
00881A2A  81 FA 00 04 00 00               cmp edx, 0x400
00881A30  0F 85 96 FE FF FF               jne 0x1408818cc
00881A36  0F BA EB 09                     bts ebx, 9
00881A3A  E9 8D FE FF FF                  jmp 0x1408818cc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmProtectVirtualMemory(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int8 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m84;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned __int8 v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p130;
    unsigned __int64 v_stack_p138;
    unsigned __int64 v_stack_p140;
    unsigned __int64 v_stack_p148;
    unsigned int v_stack_p150;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p60;
    unsigned __int8 v_stack_p64;
    unsigned int v_stack_p68;
    unsigned int v_stack_p6C;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p74;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p80;
    unsigned int v_stack_p88;
    unsigned int v_stack_p8C;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned int v_stack_pA4;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE0;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (240);
    v_rsi = 0;
    v_stack_mC8 = 0;
    v_stack_mB8 = 0;
    *(unsigned int *)(a6) = 1;
    v_stack_mB4 = 0;
    v_stack_mC0 = 0;
    v_stack_mC4 = 1;
    v_stack_m90 = *(unsigned __int64 *)(a3);
    v_stack_m70 = *(unsigned __int64 *)(a3);
    v_stack_m80 = *(unsigned __int64 *)(a4);
    v_stack_m68 = *(unsigned __int64 *)(a4);
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (0x7F800ULL));
    v_stack_mBC = (unsigned int)(a2);
    if (condition_is_not_equal) goto loc_0088172E;
loc_008810E0:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) >> (31));
    v_stack_m9C = (unsigned int)(a1);
    v_stack_m98 = (unsigned int)(a1);
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (0xB0000000ULL));
    v_stack_m84 = (unsigned int)(v_r15);
    v_rbx = (unsigned int)(((unsigned int)(a5)) & (0x4FF807FFULL));
    v_stack_p28 = (unsigned int)(v_rbx);
    if (condition_is_below) goto loc_00881561;
loc_0088111C:
    if ((unsigned int)(v_rbx) == 0) goto loc_0088174E;
    result = MiMakeProtectionMask((unsigned int)((unsigned int)(v_rbx)), a2, *(unsigned __int64 *)(a3), *(unsigned __int64 *)(a4));
    v_stack_mA0 = (unsigned int)(result);
    if (((unsigned int)(result)) == -1) goto loc_008819DA;
loc_0088113E:
    v_r14 = (*(unsigned __int64 *)(a3) - 1) + (*(unsigned __int64 *)(a4));
    v_r14 = (v_r14) | (0xFFFULL);
    v_stack_m58 = v_r14;
    v_r12 = (*(unsigned __int64 *)(a3)) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m60 = v_r12;
    v_stack_m78 = 0;
    v_stack_mB0 = 0;
    v_stack_mA8 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) & (0xFFFFFFF8ULL));
    if (((unsigned int)(result)) == 16) goto loc_008815F0;
loc_0088118D:
    v_stack_m98 = 0;
    result = (v_r14) >> (12);
    v_stack_m68 = result;
    a2 = 0;
    result = MiObtainReferencedVadEx(v_r12, a2, v_stack_mC8, *(unsigned __int64 *)(a4));
    v_stack_m70 = result;
    if (result == 0) goto loc_008813BA;
    v_stack_m98 = result;
    a1 = (*(unsigned __int8 *)(result + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(result + 28)));
    if (v_stack_m68 > a1) goto loc_00881585;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) & (0x4200000ULL));
    if (((unsigned int)(result)) == 0x4200000ULL) goto loc_0088176E;
    if (v_stack_mBC != 0) goto loc_008819E4;
loc_00881209:
    a3 = 0;
    v_stack_p28 = 0;
    if ((((unsigned __int8)((unsigned int)((unsigned int)(result)))) & (2)) != 0) goto loc_008814BC;
loc_0088121E:
    if (condition_is_below) goto loc_008813E6;
loc_0088122B:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 48))))) & (112));
    if (((unsigned __int8)(result)) == 80) goto loc_008813FE;
loc_00881240:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 48))))) & (0x4200000ULL));
    if ((((unsigned int)(v_r15)) & (0x5FFFFFFFULL)) != 0) goto loc_008819EE;
    if ((unsigned int)(v_rbx) == 0) goto loc_008819F8;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 48))))) & (112));
    if (((unsigned int)(result)) == 48) goto loc_00881826;
    if (((unsigned int)(result)) == 16) goto loc_00881A0C;
    if ((unsigned int)((unsigned int)(v_stack_m9C)) != 0) goto loc_0088158F;
loc_0088128F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 48)))) & (8)) != 0) goto loc_00881510;
loc_00881298:
loc_0088129D:
    if (condition_is_below) goto loc_0088143E;
    if ((((unsigned int)(v_rbx)) & (0x600ULL)) != 0) goto loc_008815A7;
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 48))))) & (112));
    if (((unsigned __int8)(result)) != 32) goto loc_008812D2;
    if ((((unsigned __int8)(v_rbx)) & (4)) != 0) {
        v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFBULL));
        v_rbx = (unsigned int)((v_rbx) | (8));
    }
    if ((((unsigned __int8)(v_rbx)) & (64)) != 0) goto loc_008814B0;
loc_008812D2:
    a1 = ((unsigned int)(*(unsigned int *)(result + 48))) >> (7);
    a1 = (unsigned int)((a1) & (7));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip - 8917728 + a1 * 4 + 83728))) | (0x700ULL));
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) | ((unsigned int)(v_rbx)));
    if (((unsigned int)(result)) != ((unsigned int)(a1))) goto loc_00881A16;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)) + 56))) & (160));
    if (((unsigned __int8)(result)) == 128) goto loc_0088132C;
    result = MiVadMapsLargeImage(result, (unsigned int)(*(unsigned int *)(result + 48)), a3, *(unsigned __int64 *)(a4));
    if ((unsigned int)(result) != 0) goto loc_00881783;
    result = MiIsRangeFullyCommitted(result, v_r12, v_r14, *(unsigned __int64 *)(a4));
    if ((unsigned int)(result) == 0) goto loc_0088188A;
loc_0088132C:
    v_stack_mF0 = v_stack_mB4;
    v_stack_mF8 = v_stack_mB8;
    v_stack_m100 = (unsigned int)((unsigned int)(v_stack_m9C));
    v_stack_m108 = (unsigned int)(v_rbx);
    result = MiSetProtectionOnSection(v_stack_p10, result, v_r12, v_r14);
    v_stack_mC8 = (unsigned int)(result);
    if (sign_flag) goto loc_008813CE;
loc_00881367:
    result = MiUnlockAndDereferenceVad(result, result, v_r12, v_r14);
    v_r14 = (v_r14) - (v_r12);
    v_r14 = (v_r14) + 1;
    *(unsigned __int64 *)(v_stack_p20) = v_r14;
    *(unsigned __int64 *)(v_stack_p18) = v_r12;
    *(unsigned int *)(a6) = (unsigned int)((unsigned int)(v_stack_mB8));
    result = (unsigned int)(-((unsigned int)(v_stack_mB4)));
    result = (unsigned int)((result) & (0x40000017ULL));
loc_008813A6:
    v_rsp = (v_rsp) + (240);
    return result;
loc_008813BA:
    if (((unsigned int)((unsigned int)(v_stack_p60))) != 0xC00000A0ULL) goto loc_008813CE;
loc_008813C5:
loc_008813CA:
    v_stack_p60 = (unsigned int)((unsigned int)(0xC0000018ULL));
loc_008813CE:
    if (v_stack_p90 == 0) goto loc_008813A6;
    result = MiUnlockAndDereferenceVad(v_stack_p90, result, v_r12, v_r14);
    goto loc_008813A6;
loc_008813E6:
    if (condition_is_below) goto loc_008813FE;
    result = (unsigned int)(((unsigned int)((unsigned int)(result))) & (0x180000ULL));
    if (((unsigned int)(result)) < 0x100000ULL) goto loc_0088122B;
loc_008813FE:
    result = (unsigned int)(((unsigned int)((unsigned int)(result))) & (0xA00000ULL));
    if (((unsigned int)(result)) != 0xA00000ULL) goto loc_0088194F;
    result = MiGetVadPageSize(result, result, v_r12, v_r14);
    result = (result) << (12);
    a1 = (v_r14 + 1) | (v_stack_p98);
    result = (result) - 1;
    if (((result) & (a1)) == 0) goto loc_00881240;
    goto loc_008813CA;
loc_0088143E:
    if ((((unsigned __int8)(v_rbx)) & (136)) != 0) goto loc_008815A7;
    if ((unsigned int)((unsigned int)(v_stack_m9C)) != 0) goto loc_008815A7;
    result = (unsigned __int8)(((unsigned int)((unsigned int)(a1))) & (112));
    if (((unsigned __int8)(result)) == 64) goto loc_00881894;
loc_0088145C:
    v_stack_p38 = v_stack_p74;
    v_stack_p30 = v_stack_p70;
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_p6C));
    v_stack_p20 = (unsigned int)(v_rbx);
    result = MiProtectPrivateMemory(result, v_r12, v_r14, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    v_stack_p60 = (unsigned int)(result);
    if (sign_flag) goto loc_008813CE;
    if (v_rip - 8917728 == 0) goto loc_00881367;
    if ((v_rip - 8917728) >= v_r14) goto loc_00881367;
    goto loc_008818DB;
loc_008814B0:
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFBFULL));
    goto loc_008812D2;
loc_008814BC:
    v_stack_p28 = v_r14;
    v_stack_p20 = v_r12;
    result = MiAllowProtectionChange(v_stack_p138, v_stack_p130, result, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    v_stack_p60 = (unsigned int)(result);
    if (sign_flag) goto loc_008813CE;
    if (condition_is_above_or_equal) goto loc_008815B1;
loc_008814FC:
loc_00881500:
    if ((unsigned int)((unsigned int)(v_stack_p68)) != 0) goto loc_008816C7;
    a3 = 0;
    goto loc_0088121E;
loc_00881510:
    if (0 != 0) goto loc_00881298;
    v_stack_p28 = v_rip - 8917728;
    v_stack_p20 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    result = MiCheckSecuredVad(result, v_stack_p98, v_stack_pA8, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    v_stack_p60 = (unsigned int)(result);
    if (sign_flag) goto loc_008813CE;
    goto loc_0088129D;
loc_00881561:
    if ((((unsigned __int8)(v_stack_p98)) & (240)) == 0) goto loc_00881744;
    v_stack_p64 = (unsigned __int8)(v_stack_p80);
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p98))) & (0xFF807FFULL));
    v_stack_p150 = (unsigned int)(v_rbx);
    goto loc_0088111C;
loc_00881585:
    goto loc_008813CA;
loc_0088158F:
    if (condition_is_below) goto loc_008815A7;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)) + 56)))) & (32)) == 0) goto loc_0088128F;
loc_008815A7:
    goto loc_008813CA;
loc_008815B1:
    if (v_stack_p64 == 0) goto loc_008814FC;
    a1 = ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p138 + 1040) + 1192)) != 0) ? 1 : 0;
    result = HalAdjustResourceList(a1, v_stack_p98, v_stack_pA8, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (4));
    if ((unsigned int)(result) == 0) { a2 = (unsigned int)(a1); }
    v_stack_p68 = (unsigned int)(a2);
    goto loc_00881500;
loc_008815F0:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 586)) == 1) goto loc_00881724;
    if ((*(unsigned __int64 *)(a2 + 784)) != v_stack_p80) goto loc_0088170E;
loc_00881613:
    v_stack_pB0 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240);
    v_stack_p78 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240);
    v_stack_p80 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240) + 16);
    goto loc_008816AE;
loc_008816AE:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240) + 16)) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_p80 = a1;
loc_008816BD:
    v_stack_p78 = a1;
    goto loc_0088118D;
loc_008816C7:
    if ((((unsigned __int8)(v_stack_pA8)) & (8)) != 0) goto loc_008817C8;
loc_008816D1:
    v_stack_pD8 = v_r12;
    v_stack_pE0 = v_r14;
    result = MiCommitVadMetadataBits(result, v_stack_pD8, (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    v_stack_p60 = (unsigned int)(result);
    if (sign_flag) goto loc_008813CE;
    goto loc_0088121E;
loc_0088170E:
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 1772))) != 332) goto loc_008819BA;
loc_00881724:
    goto loc_008816BD;
loc_0088172E:
    result = DefaultAddProfileSource(v_stack_p80, v_stack_pD8, a5, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    v_stack_p60 = (unsigned int)(result);
    if (!sign_flag) goto loc_008810E0;
    goto loc_008813A6;
loc_00881744:
    goto loc_008813A6;
loc_0088174E:
    if (((unsigned int)((unsigned int)(v_stack_m9C))) != 0x10000000ULL) goto loc_008819CD;
loc_0088175B:
    v_stack_p88 = 24;
    goto loc_0088113E;
loc_0088176E:
    if (v_stack_p6C != 0) goto loc_00881209;
    goto loc_008813CA;
loc_00881783:
    if (((unsigned int)(v_rbx)) != 8) goto loc_008819A4;
loc_0088178C:
    result = MiUnlockAndDereferenceVad(v_stack_p80, v_stack_pD8, a5, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    v_r14 = (v_r14) - (v_r12);
    v_r14 = (v_r14) + 1;
    *(unsigned __int64 *)(v_stack_p148) = v_r14;
    *(unsigned __int64 *)(v_stack_p140) = v_r12;
    *(unsigned int *)(a6) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p80 + 24 * 4 + 83504)));
    result = 0;
    goto loc_008813A6;
loc_008817C8:
    v_stack_p28 = v_stack_p80;
    v_stack_p20 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    result = MiCheckSecuredVad(0, v_stack_p98, v_stack_pA8, 24);
    v_stack_p60 = (unsigned int)(result);
    if (sign_flag) goto loc_008813CE;
    v_stack_p150 = 1;
    v_stack_p78 = v_stack_p80;
    goto loc_008816D1;
loc_00881826:
    v_stack_p20 = v_stack_p70;
    result = MiProtectAweRegion(v_r12, v_r14, 24, (unsigned int)(v_stack_p6C));
    v_stack_p60 = (unsigned int)(result);
    if (sign_flag) goto loc_00881A02;
    result = MiUnlockAndDereferenceVad(result, v_r14, 24, (unsigned int)(v_stack_p6C));
    v_r14 = (v_r14) - (v_r12);
    v_r14 = (v_r14) + 1;
    *(unsigned __int64 *)(v_stack_p148) = v_r14;
    *(unsigned __int64 *)(v_stack_p140) = v_r12;
    *(unsigned int *)(a6) = (unsigned int)((unsigned int)(v_stack_p70));
    goto loc_008813A6;
loc_0088188A:
    goto loc_008813CA;
loc_00881894:
    if ((((unsigned int)(v_rbx)) & (0xFFFFF9F9ULL)) != 0) goto loc_00881A20;
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFF9FFULL));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a6))) & (0xC00ULL));
    a1 = ((((unsigned int)(a6)) & (896)) != 0) ? 1 : 0;
    result = (((unsigned int)(a2)) == 0xC00ULL) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00881A2A;
loc_008818CC:
    result = MiMakeProtectionMask((unsigned int)((unsigned int)(v_rbx)), a2, 24, (unsigned int)(v_stack_p6C));
    goto loc_0088145C;
loc_008818DB:
    a1 = (*(unsigned __int8 *)(result + 32)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(result + 24)));
    v_rsi = (v_stack_p80) >> (12);
    if (v_rsi < a1) goto loc_00881367;
    a1 = (*(unsigned __int8 *)(result + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(result + 28)));
    if (v_rsi > a1) goto loc_00881367;
    result = (v_r14 + 1) >> (12);
    if (result > a1) goto loc_00881367;
    *(unsigned __int64 *)(v_stack_pB0 + 16) = v_r14 + 1;
    goto loc_00881367;
loc_0088194F:
    a2 = (unsigned int)((v_r14 + 1) >> (7));
    a2 = (unsigned int)((a2) & (31));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)(a2))) goto loc_008813C5;
    result = MiUnlockAndDereferenceVad(result, a2, 24, (unsigned int)(v_stack_p6C));
    v_r14 = (v_r14) - (v_r12);
    v_r14 = (v_r14) + 1;
    *(unsigned __int64 *)(v_stack_p148) = v_r14;
    *(unsigned __int64 *)(v_stack_p140) = v_r12;
    *(unsigned int *)(a6) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 8919436 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))) * 4 + 83504)));
    result = 0;
    goto loc_008813A6;
loc_008819A4:
    if (((unsigned int)(v_rbx)) == 128) goto loc_0088178C;
    goto loc_008813CA;
loc_008819BA:
    if (((unsigned __int16)((unsigned int)(0xC000004EULL))) == 452) goto loc_00881724;
    goto loc_00881613;
loc_008819CD:
    if (((unsigned int)((unsigned int)(v_stack_m9C))) == 0x80000000ULL) goto loc_0088175B;
loc_008819DA:
    goto loc_008813A6;
loc_008819E4:
    goto loc_008813CA;
loc_008819EE:
    goto loc_008813CA;
loc_008819F8:
    goto loc_008813CA;
loc_00881A02:
    goto loc_008813CA;
loc_00881A0C:
    goto loc_008813CA;
loc_00881A16:
    goto loc_008813CA;
loc_00881A20:
    goto loc_008813CA;
loc_00881A2A:
    if (((unsigned int)(a2)) != 0x400ULL) goto loc_008818CC;
    goto loc_008818CC;
}
```

## 5. (Beta) C Style

```c
int64_t MmProtectVirtualMemory(int64_t Arg1, int64_t Arg2, void *Arg3, void *Arg4, uint8_t Arg5, void *Arg6)
{
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint32_t v_stack_m108;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m84;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint8_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p130;
    uint64_t v_stack_p138;
    uint64_t v_stack_p140;
    uint64_t v_stack_p148;
    uint32_t v_stack_p150;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p60;
    uint8_t v_stack_p64;
    uint32_t v_stack_p68;
    uint32_t v_stack_p6C;
    uint64_t v_stack_p70;
    uint64_t v_stack_p74;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;
    uint64_t v_stack_p80;
    uint32_t v_stack_p88;
    uint32_t v_stack_p8C;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint32_t v_stack_pA4;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE0;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (240);
    local_rsi = 0;
    v_stack_mC8 = 0;
    v_stack_mB8 = 0;
    *(uint32_t *)(arg6) = 1;
    v_stack_mB4 = 0;
    v_stack_mC0 = 0;
    v_stack_mC4 = 1;
    v_stack_m90 = *(uint64_t *)(arg3);
    v_stack_m70 = *(uint64_t *)(arg3);
    v_stack_m80 = *(uint64_t *)(arg4);
    v_stack_m68 = *(uint64_t *)(arg4);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (0x7F800ULL));
    v_stack_mBC = (uint32_t)(Arg2);
    if (condition_is_not_equal) goto loc_0088172E;
loc_008810E0:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) >> (31));
    v_stack_m9C = (uint32_t)(Arg1);
    v_stack_m98 = (uint32_t)(Arg1);
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (0xB0000000ULL));
    v_stack_m84 = (uint32_t)(local_r15);
    local_rbx = (uint32_t)(((uint32_t)(Arg5)) & (0x4FF807FFULL));
    v_stack_p28 = (uint32_t)(local_rbx);
    if (condition_is_below) goto loc_00881561;
loc_0088111C:
    if ((uint32_t)(local_rbx) == 0) goto loc_0088174E;
    result = MiMakeProtectionMask((uint32_t)((uint32_t)(local_rbx)), Arg2, *(uint64_t *)(arg3), *(uint64_t *)(arg4));
    v_stack_mA0 = (uint32_t)(result);
    if (((uint32_t)(result)) == -1) goto loc_008819DA;
loc_0088113E:
    local_r14 = (*(uint64_t *)(arg3) - 1) + (*(uint64_t *)(arg4));
    local_r14 = (local_r14) | (0xFFFULL);
    v_stack_m58 = local_r14;
    local_r12 = (*(uint64_t *)(arg3)) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m60 = local_r12;
    v_stack_m78 = 0;
    v_stack_mB0 = 0;
    v_stack_mA8 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) & (0xFFFFFFF8ULL));
    if (((uint32_t)(result)) == 16) goto loc_008815F0;
loc_0088118D:
    v_stack_m98 = 0;
    result = (local_r14) >> (12);
    v_stack_m68 = result;
    Arg2 = 0;
    result = MiObtainReferencedVadEx(local_r12, Arg2, v_stack_mC8, *(uint64_t *)(arg4));
    v_stack_m70 = result;
    if (result == 0) goto loc_008813BA;
    v_stack_m98 = result;
    Arg1 = (*(uint8_t *)(result + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(result + 0x1C)));
    if (v_stack_m68 > Arg1) goto loc_00881585;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & (0x4200000ULL));
    if (((uint32_t)(result)) == 0x4200000ULL) goto loc_0088176E;
    if (v_stack_mBC != 0) goto loc_008819E4;
loc_00881209:
    Arg3 = 0;
    v_stack_p28 = 0;
    if ((((uint8_t)((uint32_t)((uint32_t)(result)))) & (2)) != 0) goto loc_008814BC;
loc_0088121E:
    if (condition_is_below) goto loc_008813E6;
loc_0088122B:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30))))) & (112));
    if (((uint8_t)(result)) == 80) goto loc_008813FE;
loc_00881240:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30))))) & (0x4200000ULL));
    if ((((uint32_t)(local_r15)) & (0x5FFFFFFFULL)) != 0) goto loc_008819EE;
    if ((uint32_t)(local_rbx) == 0) goto loc_008819F8;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30))))) & (112));
    if (((uint32_t)(result)) == 48) goto loc_00881826;
    if (((uint32_t)(result)) == 16) goto loc_00881A0C;
    if ((uint32_t)((uint32_t)(v_stack_m9C)) != 0) goto loc_0088158F;
loc_0088128F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x30)))) & (8)) != 0) goto loc_00881510;
loc_00881298:
loc_0088129D:
    if (condition_is_below) goto loc_0088143E;
    if ((((uint32_t)(local_rbx)) & (0x600ULL)) != 0) goto loc_008815A7;
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30))))) & (112));
    if (((uint8_t)(result)) != 32) goto loc_008812D2;
    if ((((uint8_t)(local_rbx)) & (4)) != 0) {
        local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFBULL));
        local_rbx = (uint32_t)((local_rbx) | (8));
    }
    if ((((uint8_t)(local_rbx)) & (64)) != 0) goto loc_008814B0;
loc_008812D2:
    Arg1 = ((uint32_t)(*(uint32_t *)(result + 0x30))) >> (7);
    Arg1 = (uint32_t)((Arg1) & (7));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip - 0x8812E0 + Arg1 * 4 + 0x14710))) | (0x700ULL));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | ((uint32_t)(local_rbx)));
    if (((uint32_t)(result)) != ((uint32_t)(Arg1))) goto loc_00881A16;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x48)) + 0x38))) & (160));
    if (((uint8_t)(result)) == 128) goto loc_0088132C;
    result = MiVadMapsLargeImage(result, (uint32_t)(*(uint32_t *)(result + 0x30)), Arg3, *(uint64_t *)(arg4));
    if ((uint32_t)(result) != 0) goto loc_00881783;
    result = MiIsRangeFullyCommitted(result, local_r12, local_r14, *(uint64_t *)(arg4));
    if ((uint32_t)(result) == 0) goto loc_0088188A;
loc_0088132C:
    v_stack_mF0 = v_stack_mB4;
    v_stack_mF8 = v_stack_mB8;
    v_stack_m100 = (uint32_t)((uint32_t)(v_stack_m9C));
    v_stack_m108 = (uint32_t)(local_rbx);
    result = MiSetProtectionOnSection(v_stack_p10, result, local_r12, local_r14);
    v_stack_mC8 = (uint32_t)(result);
    if (sign_flag) goto loc_008813CE;
loc_00881367:
    result = MiUnlockAndDereferenceVad(result, result, local_r12, local_r14);
    local_r14 = (local_r14) - (local_r12);
    local_r14 = (local_r14) + 1;
    *(uint64_t *)(v_stack_p20) = local_r14;
    *(uint64_t *)(v_stack_p18) = local_r12;
    *(uint32_t *)(arg6) = (uint32_t)((uint32_t)(v_stack_mB8));
    result = (uint32_t)(-((uint32_t)(v_stack_mB4)));
    result = (uint32_t)((result) & (0x40000017ULL));
loc_008813A6:
    local_rsp = (local_rsp) + (240);
    return result;
loc_008813BA:
    if (((uint32_t)((uint32_t)(v_stack_p60))) != 0xC00000A0ULL) goto loc_008813CE;
loc_008813C5:
loc_008813CA:
    v_stack_p60 = (uint32_t)((uint32_t)(0xC0000018ULL));
loc_008813CE:
    if (v_stack_p90 == 0) goto loc_008813A6;
    result = MiUnlockAndDereferenceVad(v_stack_p90, result, local_r12, local_r14);
    goto loc_008813A6;
loc_008813E6:
    if (condition_is_below) goto loc_008813FE;
    result = (uint32_t)(((uint32_t)((uint32_t)(result))) & (0x180000ULL));
    if (((uint32_t)(result)) < 0x100000ULL) goto loc_0088122B;
loc_008813FE:
    result = (uint32_t)(((uint32_t)((uint32_t)(result))) & (0xA00000ULL));
    if (((uint32_t)(result)) != 0xA00000ULL) goto loc_0088194F;
    result = MiGetVadPageSize(result, result, local_r12, local_r14);
    result = (result) << (12);
    Arg1 = (local_r14 + 1) | (v_stack_p98);
    result = (result) - 1;
    if (((result) & (Arg1)) == 0) goto loc_00881240;
    goto loc_008813CA;
loc_0088143E:
    if ((((uint8_t)(local_rbx)) & (136)) != 0) goto loc_008815A7;
    if ((uint32_t)((uint32_t)(v_stack_m9C)) != 0) goto loc_008815A7;
    result = (uint8_t)(((uint32_t)((uint32_t)(Arg1))) & (112));
    if (((uint8_t)(result)) == 64) goto loc_00881894;
loc_0088145C:
    v_stack_p38 = v_stack_p74;
    v_stack_p30 = v_stack_p70;
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_p6C));
    v_stack_p20 = (uint32_t)(local_rbx);
    result = MiProtectPrivateMemory(result, local_r12, local_r14, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    v_stack_p60 = (uint32_t)(result);
    if (sign_flag) goto loc_008813CE;
    if (v_rip - 8917728 == 0) goto loc_00881367;
    if ((v_rip - 8917728) >= local_r14) goto loc_00881367;
    goto loc_008818DB;
loc_008814B0:
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFBFULL));
    goto loc_008812D2;
loc_008814BC:
    v_stack_p28 = local_r14;
    v_stack_p20 = local_r12;
    result = MiAllowProtectionChange(v_stack_p138, v_stack_p130, result, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    v_stack_p60 = (uint32_t)(result);
    if (sign_flag) goto loc_008813CE;
    if (condition_is_above_or_equal) goto loc_008815B1;
loc_008814FC:
loc_00881500:
    if ((uint32_t)((uint32_t)(v_stack_p68)) != 0) goto loc_008816C7;
    Arg3 = 0;
    goto loc_0088121E;
loc_00881510:
    if (0 != 0) goto loc_00881298;
    v_stack_p28 = v_rip - 8917728;
    v_stack_p20 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    result = MiCheckSecuredVad(result, v_stack_p98, v_stack_pA8, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    v_stack_p60 = (uint32_t)(result);
    if (sign_flag) goto loc_008813CE;
    goto loc_0088129D;
loc_00881561:
    if ((((uint8_t)(v_stack_p98)) & (240)) == 0) goto loc_00881744;
    v_stack_p64 = (uint8_t)(v_stack_p80);
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p98))) & (0xFF807FFULL));
    v_stack_p150 = (uint32_t)(local_rbx);
    goto loc_0088111C;
loc_00881585:
    goto loc_008813CA;
loc_0088158F:
    if (condition_is_below) goto loc_008815A7;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x48)) + 0x38)))) & (32)) == 0) goto loc_0088128F;
loc_008815A7:
    goto loc_008813CA;
loc_008815B1:
    if (v_stack_p64 == 0) goto loc_008814FC;
    Arg1 = ((*(uint64_t *)(*(uint64_t *)(v_stack_p138 + 0x410) + 0x4A8)) != 0) ? 1 : 0;
    result = HalAdjustResourceList(Arg1, v_stack_p98, v_stack_pA8, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (4));
    if ((uint32_t)(result) == 0) { Arg2 = (uint32_t)(Arg1); }
    v_stack_p68 = (uint32_t)(Arg2);
    goto loc_00881500;
loc_008815F0:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24A)) == 1) goto loc_00881724;
    if ((*(uint64_t *)(Arg2 + 0x310)) != v_stack_p80) goto loc_0088170E;
loc_00881613:
    v_stack_pB0 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0);
    v_stack_p78 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0);
    v_stack_p80 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0) + 0x10);
    goto loc_008816AE;
loc_008816AE:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0) + 0x10)) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_p80 = Arg1;
loc_008816BD:
    v_stack_p78 = Arg1;
    goto loc_0088118D;
loc_008816C7:
    if ((((uint8_t)(v_stack_pA8)) & (8)) != 0) goto loc_008817C8;
loc_008816D1:
    v_stack_pD8 = local_r12;
    v_stack_pE0 = local_r14;
    result = MiCommitVadMetadataBits(result, v_stack_pD8, (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    v_stack_p60 = (uint32_t)(result);
    if (sign_flag) goto loc_008813CE;
    goto loc_0088121E;
loc_0088170E:
    if (((uint16_t)(*(uint16_t *)(Arg2 + 0x6EC))) != 332) goto loc_008819BA;
loc_00881724:
    goto loc_008816BD;
loc_0088172E:
    result = DefaultAddProfileSource(v_stack_p80, v_stack_pD8, Arg5, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    v_stack_p60 = (uint32_t)(result);
    if (!sign_flag) goto loc_008810E0;
    goto loc_008813A6;
loc_00881744:
    goto loc_008813A6;
loc_0088174E:
    if (((uint32_t)((uint32_t)(v_stack_m9C))) != 0x10000000ULL) goto loc_008819CD;
loc_0088175B:
    v_stack_p88 = 24;
    goto loc_0088113E;
loc_0088176E:
    if (v_stack_p6C != 0) goto loc_00881209;
    goto loc_008813CA;
loc_00881783:
    if (((uint32_t)(local_rbx)) != 8) goto loc_008819A4;
loc_0088178C:
    result = MiUnlockAndDereferenceVad(v_stack_p80, v_stack_pD8, Arg5, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    local_r14 = (local_r14) - (local_r12);
    local_r14 = (local_r14) + 1;
    *(uint64_t *)(v_stack_p148) = local_r14;
    *(uint64_t *)(v_stack_p140) = local_r12;
    *(uint32_t *)(arg6) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p80 + 0x18 * 4 + 0x14630)));
    result = 0;
    goto loc_008813A6;
loc_008817C8:
    v_stack_p28 = v_stack_p80;
    v_stack_p20 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    result = MiCheckSecuredVad(0, v_stack_p98, v_stack_pA8, 24);
    v_stack_p60 = (uint32_t)(result);
    if (sign_flag) goto loc_008813CE;
    v_stack_p150 = 1;
    v_stack_p78 = v_stack_p80;
    goto loc_008816D1;
loc_00881826:
    v_stack_p20 = v_stack_p70;
    result = MiProtectAweRegion(local_r12, local_r14, 24, (uint32_t)(v_stack_p6C));
    v_stack_p60 = (uint32_t)(result);
    if (sign_flag) goto loc_00881A02;
    result = MiUnlockAndDereferenceVad(result, local_r14, 24, (uint32_t)(v_stack_p6C));
    local_r14 = (local_r14) - (local_r12);
    local_r14 = (local_r14) + 1;
    *(uint64_t *)(v_stack_p148) = local_r14;
    *(uint64_t *)(v_stack_p140) = local_r12;
    *(uint32_t *)(arg6) = (uint32_t)((uint32_t)(v_stack_p70));
    goto loc_008813A6;
loc_0088188A:
    goto loc_008813CA;
loc_00881894:
    if ((((uint32_t)(local_rbx)) & (0xFFFFF9F9ULL)) != 0) goto loc_00881A20;
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFF9FFULL));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg6))) & (0xC00ULL));
    Arg1 = ((((uint32_t)(Arg6)) & (896)) != 0) ? 1 : 0;
    result = (((uint32_t)(Arg2)) == 0xC00ULL) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00881A2A;
loc_008818CC:
    result = MiMakeProtectionMask((uint32_t)((uint32_t)(local_rbx)), Arg2, 24, (uint32_t)(v_stack_p6C));
    goto loc_0088145C;
loc_008818DB:
    Arg1 = (*(uint8_t *)(result + 0x20)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(result + 0x18)));
    local_rsi = (v_stack_p80) >> (12);
    if (local_rsi < Arg1) goto loc_00881367;
    Arg1 = (*(uint8_t *)(result + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(result + 0x1C)));
    if (local_rsi > Arg1) goto loc_00881367;
    result = (local_r14 + 1) >> (12);
    if (result > Arg1) goto loc_00881367;
    *(uint64_t *)(v_stack_pB0 + 0x10) = local_r14 + 1;
    goto loc_00881367;
loc_0088194F:
    Arg2 = (uint32_t)((local_r14 + 1) >> (7));
    Arg2 = (uint32_t)((Arg2) & (31));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)(Arg2))) goto loc_008813C5;
    result = MiUnlockAndDereferenceVad(result, Arg2, 24, (uint32_t)(v_stack_p6C));
    local_r14 = (local_r14) - (local_r12);
    local_r14 = (local_r14) + 1;
    *(uint64_t *)(v_stack_p148) = local_r14;
    *(uint64_t *)(v_stack_p140) = local_r12;
    *(uint32_t *)(arg6) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x88198C + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))) * 4 + 0x14630)));
    result = 0;
    goto loc_008813A6;
loc_008819A4:
    if (((uint32_t)(local_rbx)) == 128) goto loc_0088178C;
    goto loc_008813CA;
loc_008819BA:
    if (((uint16_t)((uint32_t)(0xC000004EULL))) == 452) goto loc_00881724;
    goto loc_00881613;
loc_008819CD:
    if (((uint32_t)((uint32_t)(v_stack_m9C))) == 0x80000000ULL) goto loc_0088175B;
loc_008819DA:
    goto loc_008813A6;
loc_008819E4:
    goto loc_008813CA;
loc_008819EE:
    goto loc_008813CA;
loc_008819F8:
    goto loc_008813CA;
loc_00881A02:
    goto loc_008813CA;
loc_00881A0C:
    goto loc_008813CA;
loc_00881A16:
    goto loc_008813CA;
loc_00881A20:
    goto loc_008813CA;
loc_00881A2A:
    if (((uint32_t)(Arg2)) != 0x400ULL) goto loc_008818CC;
    goto loc_008818CC;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg6` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00881050&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
