# sub_00B222A0

- RVA: `0x00B222A0`–`0x00B2259B` (길이 `763` bytes)
- VA: `0x0000000140B222A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008B614`
- 디코드: `211`개 명령, `763/763` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B222B5` → [SeMaximumAuditMask](../../text/4A/SeMaximumAuditMask_function_004A8D2C.md) (function, `0x004A8D2C`)
- `0x00B222CB` → [SeMaximumAuditMaskFromGlobalSacl](../A8/SeMaximumAuditMaskFromGlobalSacl_function_00A832DC.md) (function, `0x00A832DC`)
- `0x00B2234E` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x00B2241E` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x00B2245F` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x00B224D2` → [SepIsSidEqual](../7A/SepIsSidEqual_function_007A3764.md) (function, `0x007A3764`)
- `0x00B22523` → [SepIsSidEqual](../7A/SepIsSidEqual_function_007A3764.md) (function, `0x007A3764`)
- `0x00B22586` → [SepIsAclEqual](../92/SepIsAclEqual_function_009207C8.md) (function, `0x009207C8`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00B222B5` → [SeMaximumAuditMask](../../text/4A/SeMaximumAuditMask_function_004A8D2C.md) (`PAGE` → `.text`)
  - `0x00B2234E` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (`PAGE` → `.text`)
  - `0x00B2241E` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (`PAGE` → `.text`)
  - `0x00B2245F` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **17**
  - `0x00B222DB` → [SeSecurityDescriptorChangedAuditAlarm + 0x129](../91/SeSecurityDescriptorChangedAuditAlarm_function_0091FC5C.md) (`tail-transfer`)
  - `0x00B222E4` → [SeSecurityDescriptorChangedAuditAlarm + 0x129](../91/SeSecurityDescriptorChangedAuditAlarm_function_0091FC5C.md) (`tail-transfer`)
  - `0x00B222F2` → [SeSecurityDescriptorChangedAuditAlarm + 0x129](../91/SeSecurityDescriptorChangedAuditAlarm_function_0091FC5C.md) (`tail-transfer`)
  - `0x00B222FA` → [SeSecurityDescriptorChangedAuditAlarm + 0x15E](../91/SeSecurityDescriptorChangedAuditAlarm_function_0091FC5C.md) (`tail-transfer`)
  - `0x00B22303` → [SeSecurityDescriptorChangedAuditAlarm + 0x15E](../91/SeSecurityDescriptorChangedAuditAlarm_function_0091FC5C.md) (`tail-transfer`)
  - `0x00B2230B` → [SeSecurityDescriptorChangedAuditAlarm + 0x184](../91/SeSecurityDescriptorChangedAuditAlarm_function_0091FC5C.md) (`tail-transfer`)
  - `0x00B22314` → [SeSecurityDescriptorChangedAuditAlarm + 0x184](../91/SeSecurityDescriptorChangedAuditAlarm_function_0091FC5C.md) (`tail-transfer`)
  - `0x00B22325` → [SeSecurityDescriptorChangedAuditAlarm + 0x325](../91/SeSecurityDescriptorChangedAuditAlarm_function_0091FC5C.md) (`tail-transfer`)
  - `0x00B2232F` → [SeSecurityDescriptorChangedAuditAlarm + 0x349](../91/SeSecurityDescriptorChangedAuditAlarm_function_0091FC5C.md) (`tail-transfer`)
  - `0x00B22385` → [SeSecurityDescriptorChangedAuditAlarm + 0x33F](../91/SeSecurityDescriptorChangedAuditAlarm_function_0091FC5C.md) (`tail-transfer`)
  - `0x00B223F6` → [SeSecurityDescriptorChangedAuditAlarm + 0x349](../91/SeSecurityDescriptorChangedAuditAlarm_function_0091FC5C.md) (`tail-transfer`)
  - `0x00B223FF` → [SeSecurityDescriptorChangedAuditAlarm + 0x349](../91/SeSecurityDescriptorChangedAuditAlarm_function_0091FC5C.md) (`tail-transfer`)
  - `0x00B2249E` → [SeSecurityDescriptorChangedAuditAlarm + 0x34D](../91/SeSecurityDescriptorChangedAuditAlarm_function_0091FC5C.md) (`tail-transfer`)
  - `0x00B224A5` → [SeSecurityDescriptorChangedAuditAlarm + 0x198](../91/SeSecurityDescriptorChangedAuditAlarm_function_0091FC5C.md) (`tail-transfer`)
  - `0x00B22536` → [SeSecurityDescriptorChangedAuditAlarm + 0x1A1](../91/SeSecurityDescriptorChangedAuditAlarm_function_0091FC5C.md) (`tail-transfer`)
  - `0x00B2258D` → [SeSecurityDescriptorChangedAuditAlarm + 0x1A1](../91/SeSecurityDescriptorChangedAuditAlarm_function_0091FC5C.md) (`tail-transfer`)
  - `0x00B22596` → [SeSecurityDescriptorChangedAuditAlarm + 0x1A1](../91/SeSecurityDescriptorChangedAuditAlarm_function_0091FC5C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B222A0  49 8B CB                        mov rcx, r11
00B222A3  EB 04                           jmp 0x140b222a9
00B222A5  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
00B222A9  4C 8B 45 8F                     mov r8, qword ptr [rbp - 0x71]
00B222AD  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
00B222B2  41 8B D6                        mov edx, r14d
00B222B5  E8 72 6A 98 FF                  call 0x1404a8d2c
00B222BA  4C 8B 45 8F                     mov r8, qword ptr [rbp - 0x71]
00B222BE  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
00B222C3  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00B222C8  41 8B D6                        mov edx, r14d
00B222CB  E8 0C 10 F6 FF                  call 0x140a832dc
00B222D0  45 33 DB                        xor r11d, r11d
00B222D3  F7 44 24 60 00 00 08 00         test dword ptr [rsp + 0x60], 0x80000
00B222DB  0F 84 A4 DA DF FF               je 0x14091fd85
00B222E1  45 84 FF                        test r15b, r15b
00B222E4  0F 84 9B DA DF FF               je 0x14091fd85
00B222EA  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
00B222ED  83 E0 10                        and eax, 0x10
00B222F0  0B F8                           or edi, eax
00B222F2  E9 8E DA DF FF                  jmp 0x14091fd85
00B222F7  4D 8B E3                        mov r12, r11
00B222FA  E9 BB DA DF FF                  jmp 0x14091fdba
00B222FF  4D 8B 66 18                     mov r12, qword ptr [r14 + 0x18]
00B22303  E9 B2 DA DF FF                  jmp 0x14091fdba
00B22308  49 8B D3                        mov rdx, r11
00B2230B  E9 D0 DA DF FF                  jmp 0x14091fde0
00B22310  49 8B 51 18                     mov rdx, qword ptr [r9 + 0x18]
00B22314  E9 C7 DA DF FF                  jmp 0x14091fde0
00B22319  83 E9 01                        sub ecx, 1
00B2231C  0F 84 D9 00 00 00               je 0x140b223fb
00B22322  83 F9 01                        cmp ecx, 1
00B22325  0F 85 56 DC DF FF               jne 0x14091ff81
00B2232B  40 F6 C7 40                     test dil, 0x40
00B2232F  0F 84 70 DC DF FF               je 0x14091ffa5
00B22335  4D 85 FF                        test r15, r15
00B22338  74 50                           je 0x140b2238a
00B2233A  41 0F B7 47 02                  movzx eax, word ptr [r15 + 2]
00B2233F  66 39 46 02                     cmp word ptr [rsi + 2], ax
00B22343  75 45                           jne 0x140b2238a
00B22345  44 8B C0                        mov r8d, eax
00B22348  49 8B D7                        mov rdx, r15
00B2234B  48 8B CE                        mov rcx, rsi
00B2234E  E8 1D 83 B9 FF                  call 0x1406ba670
00B22353  41 0F B7 4F 02                  movzx ecx, word ptr [r15 + 2]
00B22358  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00B2235D  48 3B C1                        cmp rax, rcx
00B22360  75 28                           jne 0x140b2238a
00B22362  44 0F B7 5D 6F                  movzx r11d, word ptr [rbp + 0x6f]
00B22367  49 03 CF                        add rcx, r15
00B2236A  B8 FF FF 00 00                  mov eax, 0xffff
00B2236F  66 44 03 D8                     add r11w, ax
00B22373  41 0F B7 C3                     movzx eax, r11w
00B22377  66 44 89 5D 6F                  mov word ptr [rbp + 0x6f], r11w
00B2237C  66 F7 D8                        neg ax
00B2237F  4D 1B FF                        sbb r15, r15
00B22382  4C 23 F9                        and r15, rcx
00B22385  E9 11 DC DF FF                  jmp 0x14091ff9b
00B2238A  83 CB 40                        or ebx, 0x40
00B2238D  83 E7 BF                        and edi, 0xffffffbf
00B22390  EB 06                           jmp 0x140b22398
00B22392  83 CB 10                        or ebx, 0x10
00B22395  83 E7 EF                        and edi, 0xffffffef
00B22398  44 0F B7 4D 5F                  movzx r9d, word ptr [rbp + 0x5f]
00B2239D  EB 23                           jmp 0x140b223c2
00B2239F  44 0F B7 4D 5F                  movzx r9d, word ptr [rbp + 0x5f]
00B223A4  49 03 CD                        add rcx, r13
00B223A7  B8 FF FF 00 00                  mov eax, 0xffff
00B223AC  66 44 03 C8                     add r9w, ax
00B223B0  41 0F B7 C1                     movzx eax, r9w
00B223B4  66 44 89 4D 5F                  mov word ptr [rbp + 0x5f], r9w
00B223B9  66 F7 D8                        neg ax
00B223BC  4D 1B ED                        sbb r13, r13
00B223BF  4C 23 E9                        and r13, rcx
00B223C2  44 0F B7 55 47                  movzx r10d, word ptr [rbp + 0x47]
00B223C7  EB 28                           jmp 0x140b223f1
00B223C9  44 0F B7 55 47                  movzx r10d, word ptr [rbp + 0x47]
00B223CE  49 03 CE                        add rcx, r14
00B223D1  44 0F B7 4D 5F                  movzx r9d, word ptr [rbp + 0x5f]
00B223D6  B8 FF FF 00 00                  mov eax, 0xffff
00B223DB  66 44 03 D0                     add r10w, ax
00B223DF  41 0F B7 C2                     movzx eax, r10w
00B223E3  66 44 89 55 47                  mov word ptr [rbp + 0x47], r10w
00B223E8  66 F7 D8                        neg ax
00B223EB  4D 1B F6                        sbb r14, r14
00B223EE  4C 23 F1                        and r14, rcx
00B223F1  44 0F B7 5D 6F                  movzx r11d, word ptr [rbp + 0x6f]
00B223F6  E9 AA DB DF FF                  jmp 0x14091ffa5
00B223FB  40 F6 C7 20                     test dil, 0x20
00B223FF  0F 84 A0 DB DF FF               je 0x14091ffa5
00B22405  4D 85 F6                        test r14, r14
00B22408  74 28                           je 0x140b22432
00B2240A  41 0F B7 46 02                  movzx eax, word ptr [r14 + 2]
00B2240F  66 39 46 02                     cmp word ptr [rsi + 2], ax
00B22413  75 1D                           jne 0x140b22432
00B22415  44 8B C0                        mov r8d, eax
00B22418  49 8B D6                        mov rdx, r14
00B2241B  48 8B CE                        mov rcx, rsi
00B2241E  E8 4D 82 B9 FF                  call 0x1406ba670
00B22423  41 0F B7 4E 02                  movzx ecx, word ptr [r14 + 2]
00B22428  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00B2242D  48 3B C1                        cmp rax, rcx
00B22430  74 97                           je 0x140b223c9
00B22432  83 CB 20                        or ebx, 0x20
00B22435  83 E7 DF                        and edi, 0xffffffdf
00B22438  E9 5B FF FF FF                  jmp 0x140b22398
00B2243D  4D 85 E4                        test r12, r12
00B22440  0F 84 4C FF FF FF               je 0x140b22392
00B22446  41 0F B7 44 24 02               movzx eax, word ptr [r12 + 2]
00B2244C  66 39 46 02                     cmp word ptr [rsi + 2], ax
00B22450  0F 85 3C FF FF FF               jne 0x140b22392
00B22456  44 8B C0                        mov r8d, eax
00B22459  49 8B D4                        mov rdx, r12
00B2245C  48 8B CE                        mov rcx, rsi
00B2245F  E8 0C 82 B9 FF                  call 0x1406ba670
00B22464  41 0F B7 4C 24 02               movzx ecx, word ptr [r12 + 2]
00B2246A  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00B2246F  48 3B C1                        cmp rax, rcx
00B22472  0F 85 1A FF FF FF               jne 0x140b22392
00B22478  8B 54 24 50                     mov edx, dword ptr [rsp + 0x50]
00B2247C  49 03 CC                        add rcx, r12
00B2247F  44 0F B7 4D 5F                  movzx r9d, word ptr [rbp + 0x5f]
00B22484  FF CA                           dec edx
00B22486  44 0F B7 55 47                  movzx r10d, word ptr [rbp + 0x47]
00B2248B  8B C2                           mov eax, edx
00B2248D  44 0F B7 5D 6F                  movzx r11d, word ptr [rbp + 0x6f]
00B22492  F7 D8                           neg eax
00B22494  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
00B22498  4D 1B E4                        sbb r12, r12
00B2249B  4C 23 E1                        and r12, rcx
00B2249E  E9 06 DB DF FF                  jmp 0x14091ffa9
00B224A3  0B DF                           or ebx, edi
00B224A5  E9 4A D9 DF FF                  jmp 0x14091fdf4
00B224AA  49 8D 14 07                     lea rdx, [r15 + rax]
00B224AE  EB 04                           jmp 0x140b224b4
00B224B0  49 8B 57 08                     mov rdx, qword ptr [r15 + 8]
00B224B4  66 45 39 5E 02                  cmp word ptr [r14 + 2], r11w
00B224B9  7D 13                           jge 0x140b224ce
00B224BB  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
00B224BF  85 C0                           test eax, eax
00B224C1  75 05                           jne 0x140b224c8
00B224C3  49 8B CB                        mov rcx, r11
00B224C6  EB 0A                           jmp 0x140b224d2
00B224C8  49 8D 0C 06                     lea rcx, [r14 + rax]
00B224CC  EB 04                           jmp 0x140b224d2
00B224CE  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
00B224D2  E8 8D 12 C8 FF                  call 0x1407a3764
00B224D7  45 33 DB                        xor r11d, r11d
00B224DA  84 C0                           test al, al
00B224DC  75 03                           jne 0x140b224e1
00B224DE  83 CB 01                        or ebx, 1
00B224E1  F6 45 7F 02                     test byte ptr [rbp + 0x7f], 2
00B224E5  74 4B                           je 0x140b22532
00B224E7  66 45 39 5F 02                  cmp word ptr [r15 + 2], r11w
00B224EC  7D 13                           jge 0x140b22501
00B224EE  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
00B224F2  85 C0                           test eax, eax
00B224F4  75 05                           jne 0x140b224fb
00B224F6  49 8B D3                        mov rdx, r11
00B224F9  EB 0A                           jmp 0x140b22505
00B224FB  49 8D 14 07                     lea rdx, [r15 + rax]
00B224FF  EB 04                           jmp 0x140b22505
00B22501  49 8B 57 10                     mov rdx, qword ptr [r15 + 0x10]
00B22505  66 45 39 5E 02                  cmp word ptr [r14 + 2], r11w
00B2250A  7D 13                           jge 0x140b2251f
00B2250C  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
00B22510  85 C0                           test eax, eax
00B22512  75 05                           jne 0x140b22519
00B22514  49 8B CB                        mov rcx, r11
00B22517  EB 0A                           jmp 0x140b22523
00B22519  49 8D 0C 06                     lea rcx, [r14 + rax]
00B2251D  EB 04                           jmp 0x140b22523
00B2251F  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
00B22523  E8 3C 12 C8 FF                  call 0x1407a3764
00B22528  45 33 DB                        xor r11d, r11d
00B2252B  84 C0                           test al, al
00B2252D  75 03                           jne 0x140b22532
00B2252F  83 CB 02                        or ebx, 2
00B22532  0F BA E7 12                     bt edi, 0x12
00B22536  0F 83 C1 D8 DF FF               jae 0x14091fdfd
00B2253C  41 0F B7 47 02                  movzx eax, word ptr [r15 + 2]
00B22541  A8 04                           test al, 4
00B22543  74 13                           je 0x140b22558
00B22545  66 85 C0                        test ax, ax
00B22548  79 13                           jns 0x140b2255d
00B2254A  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
00B2254E  85 C0                           test eax, eax
00B22550  74 06                           je 0x140b22558
00B22552  49 8D 14 07                     lea rdx, [r15 + rax]
00B22556  EB 09                           jmp 0x140b22561
00B22558  49 8B D3                        mov rdx, r11
00B2255B  EB 04                           jmp 0x140b22561
00B2255D  49 8B 57 20                     mov rdx, qword ptr [r15 + 0x20]
00B22561  41 0F B7 46 02                  movzx eax, word ptr [r14 + 2]
00B22566  A8 04                           test al, 4
00B22568  74 13                           je 0x140b2257d
00B2256A  66 85 C0                        test ax, ax
00B2256D  79 13                           jns 0x140b22582
00B2256F  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
00B22573  85 C0                           test eax, eax
00B22575  74 06                           je 0x140b2257d
00B22577  49 8D 0C 06                     lea rcx, [r14 + rax]
00B2257B  EB 09                           jmp 0x140b22586
00B2257D  49 8B CB                        mov rcx, r11
00B22580  EB 04                           jmp 0x140b22586
00B22582  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
00B22586  E8 3D E2 DF FF                  call 0x1409207c8
00B2258B  84 C0                           test al, al
00B2258D  0F 85 6A D8 DF FF               jne 0x14091fdfd
00B22593  83 CB 04                        or ebx, 4
00B22596  E9 62 D8 DF FF                  jmp 0x14091fdfd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B222A0(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, unsigned int a12, __int64 a13)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_rdi;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;

    goto loc_00B222A9;
loc_00B222A9:
    result = SeMaximumAuditMask(v_r11, (unsigned int)((unsigned int)(v_r14)), *(unsigned __int64 *)(v_rbp - 113), a12);
    result = SeMaximumAuditMaskFromGlobalSacl(a13, (unsigned int)((unsigned int)(v_r14)), *(unsigned __int64 *)(v_rbp - 113), a12);
    v_r11 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp + 127))) & (16));
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(result)));
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B222A0(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint32_t Arg12, int64_t Arg13)
{
    int64_t result;
    int64_t local_r11;
    int64_t local_rdi;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;

    goto loc_00B222A9;
loc_00B222A9:
    result = SeMaximumAuditMask(local_r11, (uint32_t)((uint32_t)(local_r14)), *(uint64_t *)(local_rbp - 0x71), Arg12);
    result = SeMaximumAuditMaskFromGlobalSacl(Arg13, (uint32_t)((uint32_t)(local_r14)), *(uint64_t *)(local_rbp - 0x71), Arg12);
    local_r11 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp + 0x7F))) & (16));
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(result)));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B222A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
