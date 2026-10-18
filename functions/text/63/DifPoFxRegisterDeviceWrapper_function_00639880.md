# DifPoFxRegisterDeviceWrapper

- RVA: `0x00639880`–`0x006399F7` (길이 `375` bytes)
- VA: `0x0000000140639880`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9A64`
- 디코드: `108`개 명령, `375/375` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006398BE` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006398E4` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00639918` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063993E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00639957` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00639965` → [PoFxRegisterDevice](../../page/75/PoFxRegisterDevice_function_00758940.md) (function, `0x00758940`)
- `0x00639991` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006399B7` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006399D0` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006398F4` → RVA `0x00F048B8` (`.data`; read)
- `0x00639905` → RVA `0x00F04980` (`.data`; read)
- `0x00639911` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00639965` → [PoFxRegisterDevice](../../page/75/PoFxRegisterDevice_function_00758940.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00639880  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00639885  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0063988A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0063988F  55                              push rbp
00639890  41 54                           push r12
00639892  41 55                           push r13
00639894  41 56                           push r14
00639896  41 57                           push r15
00639898  48 8B EC                        mov rbp, rsp
0063989B  48 83 EC 50                     sub rsp, 0x50
0063989F  0F 57 C0                        xorps xmm0, xmm0
006398A2  33 C0                           xor eax, eax
006398A4  4C 8B E9                        mov r13, rcx
006398A7  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
006398AB  B9 BA 00 00 00                  mov ecx, 0xba
006398B0  4D 8B F8                        mov r15, r8
006398B3  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
006398B7  4C 8B E2                        mov r12, rdx
006398BA  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
006398BE  E8 71 C1 E5 FF                  call 0x140495a34
006398C3  48 8B F0                        mov rsi, rax
006398C6  48 85 C0                        test rax, rax
006398C9  0F 84 8D 00 00 00               je 0x14063995c
006398CF  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006398D2  A8 18                           test al, 0x18
006398D4  74 0A                           je 0x1406398e0
006398D6  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
006398DA  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
006398DE  EB 0D                           jmp 0x1406398ed
006398E0  A8 04                           test al, 4
006398E2  74 09                           je 0x1406398ed
006398E4  E8 1F A3 E9 FF                  call 0x1404d3c08
006398E9  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
006398ED  45 32 F6                        xor r14b, r14b
006398F0  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
006398F4  44 38 35 BD AF 8C 00            cmp byte ptr [rip + 0x8cafbd], r14b
006398FB  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
006398FF  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
00639903  75 0C                           jne 0x140639911
00639905  F7 05 71 B0 8C 00 00 08 00 00   test dword ptr [rip + 0x8cb071], 0x800
0063990F  74 13                           je 0x140639924
00639911  48 8D 0D 68 A5 8C 00            lea rcx, [rip + 0x8ca568]
00639918  E8 03 CD BD FF                  call 0x140216620
0063991D  44 8A F0                        mov r14b, al
00639920  84 C0                           test al, al
00639922  74 38                           je 0x14063995c
00639924  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00639928  48 8B 1F                        mov rbx, qword ptr [rdi]
0063992B  EB 19                           jmp 0x140639946
0063992D  48 8D 43 F0                     lea rax, [rbx - 0x10]
00639931  48 85 C0                        test rax, rax
00639934  74 0D                           je 0x140639943
00639936  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063993A  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063993E  E8 8D 11 08 00                  call 0x1406baad0
00639943  48 8B 1B                        mov rbx, qword ptr [rbx]
00639946  48 3B DF                        cmp rbx, rdi
00639949  75 E2                           jne 0x14063992d
0063994B  45 84 F6                        test r14b, r14b
0063994E  74 0C                           je 0x14063995c
00639950  48 8D 0D 29 A5 8C 00            lea rcx, [rip + 0x8ca529]
00639957  E8 24 05 D1 FF                  call 0x140349e80
0063995C  4D 8B C7                        mov r8, r15
0063995F  49 8B D4                        mov rdx, r12
00639962  49 8B CD                        mov rcx, r13
00639965  E8 D6 EF 11 00                  call 0x140758940
0063996A  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0063996D  48 85 F6                        test rsi, rsi
00639970  74 63                           je 0x1406399d5
00639972  40 32 FF                        xor dil, dil
00639975  40 38 3D 3C AF 8C 00            cmp byte ptr [rip + 0x8caf3c], dil
0063997C  75 0C                           jne 0x14063998a
0063997E  F7 05 F8 AF 8C 00 00 08 00 00   test dword ptr [rip + 0x8caff8], 0x800
00639988  74 13                           je 0x14063999d
0063998A  48 8D 0D EF A4 8C 00            lea rcx, [rip + 0x8ca4ef]
00639991  E8 8A CC BD FF                  call 0x140216620
00639996  40 8A F8                        mov dil, al
00639999  84 C0                           test al, al
0063999B  74 38                           je 0x1406399d5
0063999D  48 83 C6 30                     add rsi, 0x30
006399A1  48 8B 1E                        mov rbx, qword ptr [rsi]
006399A4  EB 19                           jmp 0x1406399bf
006399A6  48 8D 43 F0                     lea rax, [rbx - 0x10]
006399AA  48 85 C0                        test rax, rax
006399AD  74 0D                           je 0x1406399bc
006399AF  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006399B3  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006399B7  E8 14 11 08 00                  call 0x1406baad0
006399BC  48 8B 1B                        mov rbx, qword ptr [rbx]
006399BF  48 3B DE                        cmp rbx, rsi
006399C2  75 E2                           jne 0x1406399a6
006399C4  40 84 FF                        test dil, dil
006399C7  74 0C                           je 0x1406399d5
006399C9  48 8D 0D B0 A4 8C 00            lea rcx, [rip + 0x8ca4b0]
006399D0  E8 AB 04 D1 FF                  call 0x140349e80
006399D5  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
006399D8  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
006399DD  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
006399E1  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
006399E5  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
006399E9  49 8B E3                        mov rsp, r11
006399EC  41 5F                           pop r15
006399EE  41 5E                           pop r14
006399F0  41 5D                           pop r13
006399F2  41 5C                           pop r12
006399F4  5D                              pop rbp
006399F5  C3                              ret
006399F6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifPoFxRegisterDeviceWrapper(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(186, a2, a3, a4);
    if (result == 0) goto loc_0063995C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006398E0;
    v_stack_m58 = v_stack_p0;
    goto loc_006398ED;
loc_006398E0:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9220029)) != 0) goto loc_00639911;
    if (((*(unsigned int *)(v_rip + 9220209)) & (0x800ULL)) == 0) goto loc_00639924;
loc_00639911:
    result = ExAcquireRundownProtection(v_rip + 9217384, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063995C;
loc_00639924:
    goto loc_00639946;
loc_0063992D:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00639946:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063992D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9217321;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = PoFxRegisterDevice(a1, a2, a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_006399D5;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9219900)) != 0) goto loc_0063998A;
    if (((*(unsigned int *)(v_rip + 9220088)) & (0x800ULL)) == 0) goto loc_0063999D;
loc_0063998A:
    result = ExAcquireRundownProtection(v_rip + 9217263, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006399D5;
loc_0063999D:
    v_rsi = (result) + (48);
    goto loc_006399BF;
loc_006399A6:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006399BF:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006399A6;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9217200;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifPoFxRegisterDeviceWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(186, Arg2, Arg3, a4);
    if (result == 0) goto loc_0063995C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006398E0;
    v_stack_m58 = v_stack_p0;
    goto loc_006398ED;
loc_006398E0:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8CAFBD)) != 0) goto loc_00639911;
    if (((*(uint32_t *)(v_rip + 0x8CB071)) & (0x800ULL)) == 0) goto loc_00639924;
loc_00639911:
    result = ExAcquireRundownProtection(v_rip + 9217384, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063995C;
loc_00639924:
    goto loc_00639946;
loc_0063992D:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_00639946:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063992D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9217321;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = PoFxRegisterDevice(Arg1, Arg2, Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_006399D5;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CAF3C)) != 0) goto loc_0063998A;
    if (((*(uint32_t *)(v_rip + 0x8CAFF8)) & (0x800ULL)) == 0) goto loc_0063999D;
loc_0063998A:
    result = ExAcquireRundownProtection(v_rip + 9217263, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_006399D5;
loc_0063999D:
    local_rsi = (result) + (48);
    goto loc_006399BF;
loc_006399A6:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_006399BF:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006399A6;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9217200;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00639880&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00639880[BB_00639880]
  bb_006398CF[BB_006398CF]
  bb_006398D6[BB_006398D6]
  bb_006398E0[BB_006398E0]
  bb_006398E4[BB_006398E4]
  bb_006398ED[BB_006398ED]
  bb_00639905[BB_00639905]
  bb_00639911[BB_00639911]
  bb_00639924[BB_00639924]
  bb_0063992D[BB_0063992D]
  bb_00639936[BB_00639936]
  bb_00639943[BB_00639943]
  bb_00639946[BB_00639946]
  bb_0063994B[BB_0063994B]
  bb_00639950[BB_00639950]
  bb_0063995C[BB_0063995C]
  bb_00639972[BB_00639972]
  bb_0063997E[BB_0063997E]
  bb_0063998A[BB_0063998A]
  bb_0063999D[BB_0063999D]
  bb_006399A6[BB_006399A6]
  bb_006399AF[BB_006399AF]
  bb_006399BC[BB_006399BC]
  bb_006399BF[BB_006399BF]
  bb_006399C4[BB_006399C4]
  bb_006399C9[BB_006399C9]
  bb_006399D5[BB_006399D5]
  bb_006399F6[BB_006399F6]
  bb_00639880 -->|branch| bb_0063995C
  bb_00639880 -->|fallthrough| bb_006398CF
  bb_006398CF -->|branch| bb_006398E0
  bb_006398CF -->|fallthrough| bb_006398D6
  bb_006398D6 -->|branch| bb_006398ED
  bb_006398E0 -->|branch| bb_006398ED
  bb_006398E0 -->|fallthrough| bb_006398E4
  bb_006398E4 -->|flow| bb_006398ED
  bb_006398ED -->|branch| bb_00639911
  bb_006398ED -->|fallthrough| bb_00639905
  bb_00639905 -->|branch| bb_00639924
  bb_00639905 -->|fallthrough| bb_00639911
  bb_00639911 -->|branch| bb_0063995C
  bb_00639911 -->|fallthrough| bb_00639924
  bb_00639924 -->|branch| bb_00639946
  bb_0063992D -->|branch| bb_00639943
  bb_0063992D -->|fallthrough| bb_00639936
  bb_00639936 -->|flow| bb_00639943
  bb_00639943 -->|flow| bb_00639946
  bb_00639946 -->|branch| bb_0063992D
  bb_00639946 -->|fallthrough| bb_0063994B
  bb_0063994B -->|branch| bb_0063995C
  bb_0063994B -->|fallthrough| bb_00639950
  bb_00639950 -->|flow| bb_0063995C
  bb_0063995C -->|branch| bb_006399D5
  bb_0063995C -->|fallthrough| bb_00639972
  bb_00639972 -->|branch| bb_0063998A
  bb_00639972 -->|fallthrough| bb_0063997E
  bb_0063997E -->|branch| bb_0063999D
  bb_0063997E -->|fallthrough| bb_0063998A
  bb_0063998A -->|branch| bb_006399D5
  bb_0063998A -->|fallthrough| bb_0063999D
  bb_0063999D -->|branch| bb_006399BF
  bb_006399A6 -->|branch| bb_006399BC
  bb_006399A6 -->|fallthrough| bb_006399AF
  bb_006399AF -->|flow| bb_006399BC
  bb_006399BC -->|flow| bb_006399BF
  bb_006399BF -->|branch| bb_006399A6
  bb_006399BF -->|fallthrough| bb_006399C4
  bb_006399C4 -->|branch| bb_006399D5
  bb_006399C4 -->|fallthrough| bb_006399C9
  bb_006399C9 -->|flow| bb_006399D5
```
