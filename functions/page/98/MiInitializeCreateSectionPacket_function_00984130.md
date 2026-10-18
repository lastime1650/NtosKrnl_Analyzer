# MiInitializeCreateSectionPacket

- RVA: `0x00984130`–`0x009844F5` (길이 `965` bytes)
- VA: `0x0000000140984130`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00097AE8`
- 디코드: `224`개 명령, `965/965` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00984277` → [MiMakeProtectionMask](../../text/32/MiMakeProtectionMask_function_00329480.md) (function, `0x00329480`)
- `0x009842D5` → [Feature_TrustedLaunchHosts__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_TrustedLaunchHosts__private_IsEnabledDeviceUsageNoInline_function_004F4150.md) (function, `0x004F4150`)
- `0x009843B0` → [PsReferencePartitionByHandle](../90/PsReferencePartitionByHandle_function_0090337C.md) (function, `0x0090337C`)
- `0x009843E8` → [PsDereferencePartition](../../text/34/PsDereferencePartition_function_00342E70.md) (function, `0x00342E70`)
- `0x009844DE` → [MiHugePagesSupported](../../text/4A/MiHugePagesSupported_function_004A0650.md) (function, `0x004A0650`)

### Direct callers
- [MmCreateSectionEx](MmCreateSectionEx_function_009839CC.md) at `0x00983B15`
- [MmCreateCacheManagerSection](MmCreateCacheManagerSection_function_00983CB8.md) at `0x00983D45`
- [MiCreateSection](MiCreateSection_function_00983EC0.md) at `0x00983F86`

### Static image references
- `0x00984314` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x00984354` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x009843C2` → RVA `0x00E38D00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00984277` → [MiMakeProtectionMask](../../text/32/MiMakeProtectionMask_function_00329480.md) (`PAGE` → `.text`)
  - `0x009842D5` → [Feature_TrustedLaunchHosts__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_TrustedLaunchHosts__private_IsEnabledDeviceUsageNoInline_function_004F4150.md) (`PAGE` → `.text`)
  - `0x009843E8` → [PsDereferencePartition](../../text/34/PsDereferencePartition_function_00342E70.md) (`PAGE` → `.text`)
  - `0x009844DE` → [MiHugePagesSupported](../../text/4A/MiHugePagesSupported_function_004A0650.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x00984381` → [sub_00B2AB3A](../B2/Unknown_function_00B2AB3A.md) (`tail-transfer`)
  - `0x0098445F` → [sub_00B2AB3A + 0xD](../B2/Unknown_function_00B2AB3A.md) (`tail-transfer`)
  - `0x00984471` → [sub_00B2AB3A + 0x1D](../B2/Unknown_function_00B2AB3A.md) (`tail-transfer`)
  - `0x00984480` → [sub_00B2AB3A + 0x11](../B2/Unknown_function_00B2AB3A.md) (`tail-transfer`)
  - `0x0098448A` → [sub_00B2AB3A + 0x11](../B2/Unknown_function_00B2AB3A.md) (`tail-transfer`)
  - `0x009844E5` → [sub_00B2AB3A + 0x28](../B2/Unknown_function_00B2AB3A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00984130  48 8B C4                        mov rax, rsp
00984133  48 89 58 08                     mov qword ptr [rax + 8], rbx
00984137  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
0098413B  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
0098413F  4C 89 60 20                     mov qword ptr [rax + 0x20], r12
00984143  41 55                           push r13
00984145  48 83 EC 40                     sub rsp, 0x40
00984149  8B 7C 24 70                     mov edi, dword ptr [rsp + 0x70]
0098414D  48 8B D9                        mov rbx, rcx
00984150  40 F6 C7 7F                     test dil, 0x7f
00984154  0F 85 95 02 00 00               jne 0x1409843ef
0098415A  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
00984162  8B 74 24 78                     mov esi, dword ptr [rsp + 0x78]
00984166  48 89 51 08                     mov qword ptr [rcx + 8], rdx
0098416A  0F B6 94 24 88 00 00 00         movzx edx, byte ptr [rsp + 0x88]
00984172  4C 89 81 98 00 00 00            mov qword ptr [rcx + 0x98], r8
00984179  44 8A 84 24 A0 00 00 00         mov r8b, byte ptr [rsp + 0xa0]
00984181  48 89 81 A0 00 00 00            mov qword ptr [rcx + 0xa0], rax
00984188  8B 84 24 A8 00 00 00            mov eax, dword ptr [rsp + 0xa8]
0098418F  89 81 A8 00 00 00               mov dword ptr [rcx + 0xa8], eax
00984195  89 79 14                        mov dword ptr [rcx + 0x14], edi
00984198  44 89 49 1C                     mov dword ptr [rcx + 0x1c], r9d
0098419C  44 88 41 48                     mov byte ptr [rcx + 0x48], r8b
009841A0  88 51 18                        mov byte ptr [rcx + 0x18], dl
009841A3  40 F6 C6 01                     test sil, 1
009841A7  0F 85 4C 02 00 00               jne 0x1409843f9
009841AD  40 F6 C6 02                     test sil, 2
009841B1  0F 85 B3 01 00 00               jne 0x14098436a
009841B7  41 BC 00 00 00 11               mov r12d, 0x11000000
009841BD  41 BD 00 00 00 01               mov r13d, 0x1000000
009841C3  40 F6 C6 10                     test sil, 0x10
009841C7  0F 85 35 02 00 00               jne 0x140984402
009841CD  40 F6 C6 40                     test sil, 0x40
009841D1  0F 85 5F 02 00 00               jne 0x140984436
009841D7  8B 83 8C 00 00 00               mov eax, dword ptr [rbx + 0x8c]
009841DD  41 BA FF FF EF FF               mov r10d, 0xffefffff
009841E3  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
009841EB  8B C8                           mov ecx, eax
009841ED  41 33 C9                        xor ecx, r9d
009841F0  48 89 53 30                     mov qword ptr [rbx + 0x30], rdx
009841F4  81 E1 FF 0F 00 00               and ecx, 0xfff
009841FA  41 B9 00 00 10 01               mov r9d, 0x1100000
00984200  33 C8                           xor ecx, eax
00984202  8B C7                           mov eax, edi
00984204  41 23 C1                        and eax, r9d
00984207  89 8B 8C 00 00 00               mov dword ptr [rbx + 0x8c], ecx
0098420D  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00984215  48 89 4B 28                     mov qword ptr [rbx + 0x28], rcx
00984219  41 3B C1                        cmp eax, r9d
0098421C  0F 84 1D 02 00 00               je 0x14098443f
00984222  0F BA E7 14                     bt edi, 0x14
00984226  0F 82 1F 02 00 00               jb 0x14098444b
0098422C  0F BA E7 19                     bt edi, 0x19
00984230  0F 82 40 02 00 00               jb 0x140984476
00984236  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0098423C  0F BA E7 12                     bt edi, 0x12
00984240  0F 82 4B 01 00 00               jb 0x140984391
00984246  41 85 FD                        test r13d, edi
00984249  75 63                           jne 0x1409842ae
0098424B  0F BA E7 1C                     bt edi, 0x1c
0098424F  0F 82 75 02 00 00               jb 0x1409844ca
00984255  0F BA E7 1E                     bt edi, 0x1e
00984259  0F 82 75 02 00 00               jb 0x1409844d4
0098425F  4C 8B 84 24 B0 00 00 00         mov r8, qword ptr [rsp + 0xb0]
00984267  0F BA E7 11                     bt edi, 0x11
0098426B  0F 82 6D 02 00 00               jb 0x1409844de
00984271  8B 4B 1C                        mov ecx, dword ptr [rbx + 0x1c]
00984274  89 7B 10                        mov dword ptr [rbx + 0x10], edi
00984277  E8 04 52 9A FF                  call 0x140329480
0098427C  89 43 20                        mov dword ptr [rbx + 0x20], eax
0098427F  83 F8 FF                        cmp eax, -1
00984282  75 21                           jne 0x1409842a5
00984284  B8 45 00 00 C0                  mov eax, 0xc0000045
00984289  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0098428E  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00984293  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00984298  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
0098429D  48 83 C4 40                     add rsp, 0x40
009842A1  41 5D                           pop r13
009842A3  C3                              ret
009842A4  CC                              int3
009842A5  4D 85 C0                        test r8, r8
009842A8  75 57                           jne 0x140984301
009842AA  33 C0                           xor eax, eax
009842AC  EB DB                           jmp 0x140984289
009842AE  40 F6 C6 08                     test sil, 8
009842B2  0F 85 D7 01 00 00               jne 0x14098448f
009842B8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009842C1  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
009842C8  F6 81 70 01 00 00 01            test byte ptr [rcx + 0x170], 1
009842CF  0F 85 C3 01 00 00               jne 0x140984498
009842D5  E8 76 FE B6 FF                  call 0x1404f4150
009842DA  85 C0                           test eax, eax
009842DC  74 0A                           je 0x1409842e8
009842DE  40 F6 C6 20                     test sil, 0x20
009842E2  0F 85 BB 01 00 00               jne 0x1409844a3
009842E8  8B C7                           mov eax, edi
009842EA  41 23 C4                        and eax, r12d
009842ED  41 3B C4                        cmp eax, r12d
009842F0  75 50                           jne 0x140984342
009842F2  83 7B 1C 02                     cmp dword ptr [rbx + 0x1c], 2
009842F6  75 8C                           jne 0x140984284
009842F8  0F BA F7 1C                     btr edi, 0x1c
009842FC  E9 5E FF FF FF                  jmp 0x14098425f
00984301  41 8A 00                        mov al, byte ptr [r8]
00984304  88 83 C0 00 00 00               mov byte ptr [rbx + 0xc0], al
0098430A  41 8B 40 04                     mov eax, dword ptr [r8 + 4]
0098430E  89 83 C4 00 00 00               mov dword ptr [rbx + 0xc4], eax
00984314  0F B7 05 E5 0C 64 00            movzx eax, word ptr [rip + 0x640ce5]
0098431B  41 8B 48 08                     mov ecx, dword ptr [r8 + 8]
0098431F  3B C8                           cmp ecx, eax
00984321  0F 87 C8 00 00 00               ja 0x1409843ef
00984327  89 8B AC 00 00 00               mov dword ptr [rbx + 0xac], ecx
0098432D  41 8B 40 14                     mov eax, dword ptr [r8 + 0x14]
00984331  A8 01                           test al, 1
00984333  0F 84 71 FF FF FF               je 0x1409842aa
00984339  0F BA 2B 19                     bts dword ptr [rbx], 0x19
0098433D  E9 68 FF FF FF                  jmp 0x1409842aa
00984342  8B 0B                           mov ecx, dword ptr [rbx]
00984344  8B C1                           mov eax, ecx
00984346  0F BA E8 09                     bts eax, 9
0098434A  89 03                           mov dword ptr [rbx], eax
0098434C  A8 20                           test al, 0x20
0098434E  0F 85 58 01 00 00               jne 0x1409844ac
00984354  48 F7 05 29 27 64 00 00 00 08 00  test qword ptr [rip + 0x642729], 0x80000
0098435F  0F 84 FA FE FF FF               je 0x14098425f
00984365  E9 53 01 00 00                  jmp 0x1409844bd
0098436A  8B 09                           mov ecx, dword ptr [rcx]
0098436C  8B C1                           mov eax, ecx
0098436E  83 C8 01                        or eax, 1
00984371  89 03                           mov dword ptr [rbx], eax
00984373  40 F6 C6 04                     test sil, 4
00984377  0F 84 3A FE FF FF               je 0x1409841b7
0098437D  0F BA E1 19                     bt ecx, 0x19
00984381  0F 83 B3 67 1A 00               jae 0x140b2ab3a
00984387  B8 11 09 00 C0                  mov eax, 0xc0000911
0098438C  E9 F8 FE FF FF                  jmp 0x140984289
00984391  48 85 C9                        test rcx, rcx
00984394  74 59                           je 0x1409843ef
00984396  48 85 D2                        test rdx, rdx
00984399  75 54                           jne 0x1409843ef
0098439B  48 8D 44 24 30                  lea rax, [rsp + 0x30]
009843A0  BA 02 00 00 00                  mov edx, 2
009843A5  41 B9 4D 4D 43 70               mov r9d, 0x70434d4d
009843AB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009843B0  E8 C7 EF F7 FF                  call 0x14090337c
009843B5  85 C0                           test eax, eax
009843B7  0F 88 CC FE FF FF               js 0x140984289
009843BD  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
009843C2  48 8D 05 37 49 4B 00            lea rax, [rip + 0x4b4937]
009843C9  48 39 01                        cmp qword ptr [rcx], rax
009843CC  74 15                           je 0x1409843e3
009843CE  48 89 8B B0 00 00 00            mov qword ptr [rbx + 0xb0], rcx
009843D5  48 83 63 28 00                  and qword ptr [rbx + 0x28], 0
009843DA  0F BA F7 12                     btr edi, 0x12
009843DE  E9 63 FE FF FF                  jmp 0x140984246
009843E3  BA 4D 4D 43 70                  mov edx, 0x70434d4d
009843E8  E8 83 EA 9B FF                  call 0x140342e70
009843ED  EB E6                           jmp 0x1409843d5
009843EF  B8 0D 00 00 C0                  mov eax, 0xc000000d
009843F4  E9 90 FE FF FF                  jmp 0x140984289
009843F9  0F BA 29 0A                     bts dword ptr [rcx], 0xa
009843FD  E9 AB FD FF FF                  jmp 0x1409841ad
00984402  45 84 C0                        test r8b, r8b
00984405  75 E8                           jne 0x1409843ef
00984407  F7 C7 00 00 10 02               test edi, 0x2100000
0098440D  75 E0                           jne 0x1409843ef
0098440F  8B C7                           mov eax, edi
00984411  41 23 C4                        and eax, r12d
00984414  41 3B C4                        cmp eax, r12d
00984417  74 D6                           je 0x1409843ef
00984419  41 85 FD                        test r13d, edi
0098441C  74 D1                           je 0x1409843ef
0098441E  80 FA 0E                        cmp dl, 0xe
00984421  77 CC                           ja 0x1409843ef
00984423  B9 D0 51 00 00                  mov ecx, 0x51d0
00984428  0F A3 D1                        bt ecx, edx
0098442B  73 C2                           jae 0x1409843ef
0098442D  0F BA 2B 1A                     bts dword ptr [rbx], 0x1a
00984431  E9 97 FD FF FF                  jmp 0x1409841cd
00984436  0F BA 2B 1C                     bts dword ptr [rbx], 0x1c
0098443A  E9 98 FD FF FF                  jmp 0x1409841d7
0098443F  0F BA 2B 08                     bts dword ptr [rbx], 8
00984443  41 23 FA                        and edi, r10d
00984446  E9 D7 FD FF FF                  jmp 0x140984222
0098444B  0F BA E7 15                     bt edi, 0x15
0098444F  72 9E                           jb 0x1409843ef
00984451  8B 03                           mov eax, dword ptr [rbx]
00984453  41 23 FA                        and edi, r10d
00984456  83 C8 20                        or eax, 0x20
00984459  89 03                           mov dword ptr [rbx], eax
0098445B  0F BA E7 16                     bt edi, 0x16
0098445F  0F 83 E2 66 1A 00               jae 0x140b2ab47
00984465  0F BA F7 16                     btr edi, 0x16
00984469  0F BA E8 07                     bts eax, 7
0098446D  89 03                           mov dword ptr [rbx], eax
0098446F  B0 0C                           mov al, 0xc
00984471  E9 E1 66 1A 00                  jmp 0x140b2ab57
00984476  83 0B 10                        or dword ptr [rbx], 0x10
00984479  8B C7                           mov eax, edi
0098447B  25 00 00 40 00                  and eax, 0x400000
00984480  0F 84 C5 66 1A 00               je 0x140b2ab4b
00984486  0F BA F7 16                     btr edi, 0x16
0098448A  E9 BC 66 1A 00                  jmp 0x140b2ab4b
0098448F  0F BA 2B 12                     bts dword ptr [rbx], 0x12
00984493  E9 20 FE FF FF                  jmp 0x1409842b8
00984498  81 0B 00 00 24 00               or dword ptr [rbx], 0x240000
0098449E  E9 32 FE FF FF                  jmp 0x1409842d5
009844A3  0F BA 2B 1B                     bts dword ptr [rbx], 0x1b
009844A7  E9 3C FE FF FF                  jmp 0x1409842e8
009844AC  48 F7 05 D1 25 64 00 00 80 00 00  test qword ptr [rip + 0x6425d1], 0x8000
009844B7  0F 84 97 FE FF FF               je 0x140984354
009844BD  81 C9 00 02 04 00               or ecx, 0x40200
009844C3  89 0B                           mov dword ptr [rbx], ecx
009844C5  E9 95 FD FF FF                  jmp 0x14098425f
009844CA  0F BA 6B 1C 09                  bts dword ptr [rbx + 0x1c], 9
009844CF  E9 8B FD FF FF                  jmp 0x14098425f
009844D4  0F BA 6B 1C 0A                  bts dword ptr [rbx + 0x1c], 0xa
009844D9  E9 81 FD FF FF                  jmp 0x14098425f
009844DE  E8 6D C1 B1 FF                  call 0x1404a0650
009844E3  85 C0                           test eax, eax
009844E5  0F 85 77 66 1A 00               jne 0x140b2ab62
009844EB  B8 BB 00 00 C0                  mov eax, 0xc00000bb
009844F0  E9 94 FD FF FF                  jmp 0x140984289
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInitializeCreateSectionPacket(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5, unsigned int a6, __int64 a7, unsigned __int8 a8, __int64 a9, __int64 a10, unsigned __int8 a11, unsigned int a12, __int64 a13)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 32) = v_r12;
    v_rsp = (v_rsp) - (64);
    if ((((unsigned __int8)((unsigned int)(a5))) & (127)) != 0) goto loc_009843EF;
    *(unsigned __int64 *)(a1 + 8) = a2;
    *(unsigned __int64 *)(a1 + 152) = a3;
    *(unsigned __int64 *)(a1 + 160) = a7;
    *(unsigned int *)(a1 + 168) = (unsigned int)((unsigned int)(a12));
    *(unsigned int *)(a1 + 20) = (unsigned int)((unsigned int)(a5));
    *(unsigned int *)(a1 + 28) = a4;
    *(unsigned __int8 *)(a1 + 72) = a11;
    *(unsigned __int8 *)(a1 + 24) = a8;
    if ((((unsigned __int8)((unsigned int)(a6))) & (1)) != 0) goto loc_009843F9;
loc_009841AD:
    if ((((unsigned __int8)((unsigned int)(a6))) & (2)) != 0) goto loc_0098436A;
loc_009841B7:
    if ((((unsigned __int8)((unsigned int)(a6))) & (16)) != 0) goto loc_00984402;
loc_009841CD:
    if ((((unsigned __int8)((unsigned int)(a6))) & (64)) != 0) goto loc_00984436;
loc_009841D7:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 140))))) ^ (a4));
    *(unsigned __int64 *)(a1 + 48) = a10;
    a1 = (unsigned int)((a1) & (0xFFFULL));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 140)))));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & ((unsigned int)((unsigned int)(0x1100000ULL))));
    *(unsigned int *)(a1 + 140) = (unsigned int)(a1);
    *(unsigned __int64 *)(a1 + 40) = a9;
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x1100000ULL)))) goto loc_0098443F;
loc_00984222:
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(0x1100000ULL)))) goto loc_0098444B;
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(0x1100000ULL)))) goto loc_00984476;
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(0x1100000ULL)))) goto loc_00984391;
loc_00984246:
    if ((((unsigned int)((unsigned int)(0x1000000ULL))) & ((unsigned int)((unsigned int)(a5)))) != 0) goto loc_009842AE;
    if (condition_is_below) goto loc_009844CA;
    if (condition_is_below) goto loc_009844D4;
loc_0098425F:
    if (condition_is_below) goto loc_009844DE;
    *(unsigned int *)(a1 + 16) = (unsigned int)((unsigned int)(a5));
    result = MiMakeProtectionMask((unsigned int)(*(unsigned int *)(a1 + 28)), a10, a13, (unsigned int)(0x1100000ULL));
    *(unsigned int *)(a1 + 32) = (unsigned int)(result);
    if (((unsigned int)(result)) != -1) goto loc_009842A5;
loc_00984284:
loc_00984289:
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(0xC0000045ULL);
loc_009842A5:
    if (a13 != 0) goto loc_00984301;
loc_009842AA:
    result = 0;
    goto loc_00984289;
loc_009842AE:
    if ((((unsigned __int8)(v_stack_p10)) & (8)) != 0) goto loc_0098448F;
loc_009842B8:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 368)) & (1)) != 0) goto loc_00984498;
loc_009842D5:
    result = Feature_TrustedLaunchHosts__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a10, a13, (unsigned int)(0x1100000ULL));
    if ((unsigned int)(result) == 0) goto loc_009842E8;
    if ((((unsigned __int8)(v_stack_p10)) & (32)) != 0) goto loc_009844A3;
loc_009842E8:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p18))) & ((unsigned int)(v_stack_p20)));
    if (((unsigned int)(result)) != ((unsigned int)(v_stack_p20))) goto loc_00984342;
    if ((*(unsigned int *)(v_stack_p8 + 28)) != 2) goto loc_00984284;
    goto loc_0098425F;
loc_00984301:
    *(unsigned __int8 *)(v_stack_p8 + 192) = (unsigned __int8)(*(unsigned __int8 *)(a13));
    *(unsigned int *)(v_stack_p8 + 196) = (unsigned int)((unsigned int)(*(unsigned int *)(a13 + 4)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a13 + 8)))) > ((unsigned int)(*(unsigned __int16 *)(v_rip + 6556901)))) goto loc_009843EF;
    *(unsigned int *)(v_stack_p8 + 172) = (unsigned int)((unsigned int)(*(unsigned int *)(a13 + 8)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a13 + 20)))) & (1)) == 0) goto loc_009842AA;
    goto loc_009842AA;
loc_00984342:
    *(unsigned int *)(v_stack_p8) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8)))));
    if ((((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8)))))) & (32)) != 0) goto loc_009844AC;
loc_00984354:
    if (((*(unsigned __int64 *)(v_rip + 6563625)) & (0x80000ULL)) == 0) goto loc_0098425F;
    goto loc_009844BD;
loc_0098436A:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_p8))))))) | (1));
    *(unsigned int *)(v_stack_p8) = (unsigned int)(result);
    if ((((unsigned __int8)(v_stack_p10)) & (4)) == 0) goto loc_009841B7;
    goto loc_00984289;
loc_00984391:
    if ((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_p8)))) == 0) goto loc_009843EF;
    if (a10 != 0) goto loc_009843EF;
    v_stack_p20 = v_stack_p30;
    result = PsReferencePartitionByHandle((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_p8)))), 2, a13, (unsigned int)(0x70434D4DULL));
    if (sign_flag) goto loc_00984289;
    if ((*(unsigned __int64 *)(v_stack_p30)) == (v_rip + 4933943)) goto loc_009843E3;
    *(unsigned __int64 *)(v_stack_p8 + 176) = v_stack_p30;
loc_009843D5:
    goto loc_00984246;
loc_009843E3:
    result = PsDereferencePartition(v_stack_p30, (unsigned int)(0x70434D4DULL), a13, (unsigned int)(0x70434D4DULL));
    goto loc_009843D5;
loc_009843EF:
    goto loc_00984289;
loc_009843F9:
    goto loc_009841AD;
loc_00984402:
    if ((unsigned __int8)(a13) != 0) goto loc_009843EF;
    if ((((unsigned int)(v_stack_p18)) & (0x2100000ULL)) != 0) goto loc_009843EF;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p18))) & ((unsigned int)(v_stack_p20)));
    if (((unsigned int)(result)) == ((unsigned int)(v_stack_p20))) goto loc_009843EF;
    if ((((unsigned int)((unsigned int)(0x1000000ULL))) & ((unsigned int)(v_stack_p18))) == 0) goto loc_009843EF;
    if (((unsigned __int8)((unsigned int)(0x70434D4DULL))) > 14) goto loc_009843EF;
    if (((unsigned __int8)((unsigned int)(0x70434D4DULL))) >= 14) goto loc_009843EF;
    goto loc_009841CD;
loc_00984436:
    goto loc_009841D7;
loc_0098443F:
    v_rdi = (unsigned int)((v_stack_p18) & ((unsigned int)((unsigned int)(0xFFEFFFFFULL))));
    goto loc_00984222;
loc_0098444B:
    if (condition_is_below) goto loc_009843EF;
    v_rdi = (unsigned int)((v_rdi) & ((unsigned int)((unsigned int)(0xFFEFFFFFULL))));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8))) | (32));
    *(unsigned int *)(v_stack_p8) = (unsigned int)(result);
    *(unsigned int *)(v_stack_p8) = (unsigned int)(result);
loc_00984476:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (0x400000ULL));
loc_0098448F:
    goto loc_009842B8;
loc_00984498:
    goto loc_009842D5;
loc_009844A3:
    goto loc_009842E8;
loc_009844AC:
    if (((*(unsigned __int64 *)(v_rip + 6563281)) & (0x8000ULL)) == 0) goto loc_00984354;
loc_009844BD:
    a1 = (unsigned int)(((unsigned int)(0x51D0ULL)) | (0x40200ULL));
    *(unsigned int *)(v_stack_p8) = (unsigned int)(a1);
    goto loc_0098425F;
loc_009844CA:
    goto loc_0098425F;
loc_009844D4:
    goto loc_0098425F;
loc_009844DE:
    result = MiHugePagesSupported(a1, (unsigned int)(0x70434D4DULL), a13, (unsigned int)(0x70434D4DULL));
    goto loc_00984289;
}
```

## 5. (Beta) C Style

```c
int64_t MiInitializeCreateSectionPacket(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5, uint32_t Arg6, int64_t Arg7, uint8_t Arg8, int64_t Arg9, int64_t Arg10, uint8_t Arg11, uint32_t Arg12, int64_t Arg13)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint64_t *)(local_rsp + 0x20) = local_r12;
    local_rsp = (local_rsp) - (64);
    if ((((uint8_t)((uint32_t)(Arg5))) & (127)) != 0) goto loc_009843EF;
    *(uint64_t *)(arg1 + 0x8) = Arg2;
    *(uint64_t *)(arg1 + 0x98) = Arg3;
    *(uint64_t *)(arg1 + 0xA0) = Arg7;
    *(uint32_t *)(arg1 + 0xA8) = (uint32_t)((uint32_t)(Arg12));
    *(uint32_t *)(arg1 + 0x14) = (uint32_t)((uint32_t)(Arg5));
    *(uint32_t *)(arg1 + 0x1C) = Arg4;
    *(uint8_t *)(arg1 + 0x48) = Arg11;
    *(uint8_t *)(arg1 + 0x18) = Arg8;
    if ((((uint8_t)((uint32_t)(Arg6))) & (1)) != 0) goto loc_009843F9;
loc_009841AD:
    if ((((uint8_t)((uint32_t)(Arg6))) & (2)) != 0) goto loc_0098436A;
loc_009841B7:
    if ((((uint8_t)((uint32_t)(Arg6))) & (16)) != 0) goto loc_00984402;
loc_009841CD:
    if ((((uint8_t)((uint32_t)(Arg6))) & (64)) != 0) goto loc_00984436;
loc_009841D7:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8C))))) ^ (Arg4));
    *(uint64_t *)(arg1 + 0x30) = Arg10;
    Arg1 = (uint32_t)((Arg1) & (0xFFFULL));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8C)))));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & ((uint32_t)((uint32_t)(0x1100000ULL))));
    *(uint32_t *)(arg1 + 0x8C) = (uint32_t)(Arg1);
    *(uint64_t *)(arg1 + 0x28) = Arg9;
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x1100000ULL)))) goto loc_0098443F;
loc_00984222:
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(0x1100000ULL)))) goto loc_0098444B;
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(0x1100000ULL)))) goto loc_00984476;
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(0x1100000ULL)))) goto loc_00984391;
loc_00984246:
    if ((((uint32_t)((uint32_t)(0x1000000ULL))) & ((uint32_t)((uint32_t)(Arg5)))) != 0) goto loc_009842AE;
    if (condition_is_below) goto loc_009844CA;
    if (condition_is_below) goto loc_009844D4;
loc_0098425F:
    if (condition_is_below) goto loc_009844DE;
    *(uint32_t *)(arg1 + 0x10) = (uint32_t)((uint32_t)(Arg5));
    result = MiMakeProtectionMask((uint32_t)(*(uint32_t *)(arg1 + 0x1C)), Arg10, Arg13, (uint32_t)(0x1100000ULL));
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)(result);
    if (((uint32_t)(result)) != -1) goto loc_009842A5;
loc_00984284:
loc_00984289:
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(0xC0000045ULL);
loc_009842A5:
    if (Arg13 != 0) goto loc_00984301;
loc_009842AA:
    result = 0;
    goto loc_00984289;
loc_009842AE:
    if ((((uint8_t)(v_stack_p10)) & (8)) != 0) goto loc_0098448F;
loc_009842B8:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x170)) & (1)) != 0) goto loc_00984498;
loc_009842D5:
    result = Feature_TrustedLaunchHosts__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg10, Arg13, (uint32_t)(0x1100000ULL));
    if ((uint32_t)(result) == 0) goto loc_009842E8;
    if ((((uint8_t)(v_stack_p10)) & (32)) != 0) goto loc_009844A3;
loc_009842E8:
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p18))) & ((uint32_t)(v_stack_p20)));
    if (((uint32_t)(result)) != ((uint32_t)(v_stack_p20))) goto loc_00984342;
    if ((*(uint32_t *)(v_stack_p8 + 0x1C)) != 2) goto loc_00984284;
    goto loc_0098425F;
loc_00984301:
    *(uint8_t *)(v_stack_p8 + 0xC0) = (uint8_t)(*(uint8_t *)(Arg13));
    *(uint32_t *)(v_stack_p8 + 0xC4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg13 + 0x4)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg13 + 0x8)))) > ((uint32_t)(*(uint16_t *)(v_rip + 0x640CE5)))) goto loc_009843EF;
    *(uint32_t *)(v_stack_p8 + 0xAC) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg13 + 0x8)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg13 + 0x14)))) & (1)) == 0) goto loc_009842AA;
    goto loc_009842AA;
loc_00984342:
    *(uint32_t *)(v_stack_p8) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8)))));
    if ((((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8)))))) & (32)) != 0) goto loc_009844AC;
loc_00984354:
    if (((*(uint64_t *)(v_rip + 0x642729)) & (0x80000ULL)) == 0) goto loc_0098425F;
    goto loc_009844BD;
loc_0098436A:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_p8))))))) | (1));
    *(uint32_t *)(v_stack_p8) = (uint32_t)(result);
    if ((((uint8_t)(v_stack_p10)) & (4)) == 0) goto loc_009841B7;
    goto loc_00984289;
loc_00984391:
    if ((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_p8)))) == 0) goto loc_009843EF;
    if (Arg10 != 0) goto loc_009843EF;
    v_stack_p20 = v_stack_p30;
    result = PsReferencePartitionByHandle((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_p8)))), 2, Arg13, (uint32_t)(0x70434D4DULL));
    if (sign_flag) goto loc_00984289;
    if ((*(uint64_t *)(v_stack_p30)) == (v_rip + 4933943)) goto loc_009843E3;
    *(uint64_t *)(v_stack_p8 + 0xB0) = v_stack_p30;
loc_009843D5:
    goto loc_00984246;
loc_009843E3:
    result = PsDereferencePartition(v_stack_p30, (uint32_t)(0x70434D4DULL), Arg13, (uint32_t)(0x70434D4DULL));
    goto loc_009843D5;
loc_009843EF:
    goto loc_00984289;
loc_009843F9:
    goto loc_009841AD;
loc_00984402:
    if ((uint8_t)(Arg13) != 0) goto loc_009843EF;
    if ((((uint32_t)(v_stack_p18)) & (0x2100000ULL)) != 0) goto loc_009843EF;
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p18))) & ((uint32_t)(v_stack_p20)));
    if (((uint32_t)(result)) == ((uint32_t)(v_stack_p20))) goto loc_009843EF;
    if ((((uint32_t)((uint32_t)(0x1000000ULL))) & ((uint32_t)(v_stack_p18))) == 0) goto loc_009843EF;
    if (((uint8_t)((uint32_t)(0x70434D4DULL))) > 14) goto loc_009843EF;
    if (((uint8_t)((uint32_t)(0x70434D4DULL))) >= 14) goto loc_009843EF;
    goto loc_009841CD;
loc_00984436:
    goto loc_009841D7;
loc_0098443F:
    local_rdi = (uint32_t)((v_stack_p18) & ((uint32_t)((uint32_t)(0xFFEFFFFFULL))));
    goto loc_00984222;
loc_0098444B:
    if (condition_is_below) goto loc_009843EF;
    local_rdi = (uint32_t)((local_rdi) & ((uint32_t)((uint32_t)(0xFFEFFFFFULL))));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8))) | (32));
    *(uint32_t *)(v_stack_p8) = (uint32_t)(result);
    *(uint32_t *)(v_stack_p8) = (uint32_t)(result);
loc_00984476:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (0x400000ULL));
loc_0098448F:
    goto loc_009842B8;
loc_00984498:
    goto loc_009842D5;
loc_009844A3:
    goto loc_009842E8;
loc_009844AC:
    if (((*(uint64_t *)(v_rip + 0x6425D1)) & (0x8000ULL)) == 0) goto loc_00984354;
loc_009844BD:
    Arg1 = (uint32_t)(((uint32_t)(0x51D0ULL)) | (0x40200ULL));
    *(uint32_t *)(v_stack_p8) = (uint32_t)(Arg1);
    goto loc_0098425F;
loc_009844CA:
    goto loc_0098425F;
loc_009844D4:
    goto loc_0098425F;
loc_009844DE:
    result = MiHugePagesSupported(Arg1, (uint32_t)(0x70434D4DULL), Arg13, (uint32_t)(0x70434D4DULL));
    goto loc_00984289;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `32` | `W` |
| `Arg1` | `+ 0x14` | `32` | `W` |
| `Arg1` | `+ 0x18` | `8` | `W` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R/W` |
| `Arg1` | `+ 0x1C` | `32` | `W` |
| `Arg1` | `+ 0x20` | `32` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R/W` |
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x48` | `8` | `W` |
| `Arg1` | `+ 0x8C` | `32` | `R` |
| `Arg1` | `+ 0x8C` | `32` | `W` |
| `Arg1` | `+ 0x98` | `64` | `W` |
| `Arg1` | `+ 0xA0` | `64` | `W` |
| `Arg1` | `+ 0xA8` | `32` | `W` |
| `Arg1` | `+ 0xAC` | `32` | `W` |
| `Arg1` | `+ 0xB0` | `64` | `W` |
| `Arg1` | `+ 0xC0` | `8` | `W` |
| `Arg1` | `+ 0xC4` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00984130&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
