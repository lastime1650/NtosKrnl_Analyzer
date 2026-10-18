# DifExEnterCriticalRegionAndAcquireResourceSharedWrapper

- RVA: `0x0061FE60`–`0x0061FFC1` (길이 `353` bytes)
- VA: `0x000000014061FE60`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `353/353` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0061FE8F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0061FEB7` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0061FEE5` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061FF0C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061FF25` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0061FF2D` → [ExEnterCriticalRegionAndAcquireResourceShared](../21/ExEnterCriticalRegionAndAcquireResourceShared_function_002134E0.md) (function, `0x002134E0`)
- `0x0061FF5B` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061FF82` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061FF9B` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0061FEC9` → RVA `0x00F048B8` (`.data`; read)
- `0x0061FED2` → RVA `0x00F04980` (`.data`; read)
- `0x0061FEDE` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0061FE60  4C 8B DC                        mov r11, rsp
0061FE63  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0061FE67  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0061FE6B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0061FE6F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
0061FE73  41 56                           push r14
0061FE75  48 83 EC 40                     sub rsp, 0x40
0061FE79  33 C0                           xor eax, eax
0061FE7B  0F 57 C0                        xorps xmm0, xmm0
0061FE7E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0061FE83  48 8B E9                        mov rbp, rcx
0061FE86  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0061FE8A  B9 95 01 00 00                  mov ecx, 0x195
0061FE8F  E8 A0 5B E7 FF                  call 0x140495a34
0061FE94  48 8B F0                        mov rsi, rax
0061FE97  48 85 C0                        test rax, rax
0061FE9A  0F 84 8A 00 00 00               je 0x14061ff2a
0061FEA0  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0061FEA3  A8 18                           test al, 0x18
0061FEA5  74 0C                           je 0x14061feb3
0061FEA7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0061FEAC  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0061FEB1  EB 0E                           jmp 0x14061fec1
0061FEB3  A8 04                           test al, 4
0061FEB5  74 0A                           je 0x14061fec1
0061FEB7  E8 4C 3D EB FF                  call 0x1404d3c08
0061FEBC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0061FEC1  40 32 FF                        xor dil, dil
0061FEC4  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0061FEC9  40 38 3D E8 49 8E 00            cmp byte ptr [rip + 0x8e49e8], dil
0061FED0  75 0C                           jne 0x14061fede
0061FED2  F7 05 A4 4A 8E 00 00 08 00 00   test dword ptr [rip + 0x8e4aa4], 0x800
0061FEDC  74 13                           je 0x14061fef1
0061FEDE  48 8D 0D 9B 3F 8E 00            lea rcx, [rip + 0x8e3f9b]
0061FEE5  E8 36 67 BF FF                  call 0x140216620
0061FEEA  40 8A F8                        mov dil, al
0061FEED  84 C0                           test al, al
0061FEEF  74 39                           je 0x14061ff2a
0061FEF1  4C 8D 76 20                     lea r14, [rsi + 0x20]
0061FEF5  49 8B 1E                        mov rbx, qword ptr [r14]
0061FEF8  EB 1A                           jmp 0x14061ff14
0061FEFA  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061FEFE  48 85 C0                        test rax, rax
0061FF01  74 0E                           je 0x14061ff11
0061FF03  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061FF07  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0061FF0C  E8 BF AB 09 00                  call 0x1406baad0
0061FF11  48 8B 1B                        mov rbx, qword ptr [rbx]
0061FF14  49 3B DE                        cmp rbx, r14
0061FF17  75 E1                           jne 0x14061fefa
0061FF19  40 84 FF                        test dil, dil
0061FF1C  74 0C                           je 0x14061ff2a
0061FF1E  48 8D 0D 5B 3F 8E 00            lea rcx, [rip + 0x8e3f5b]
0061FF25  E8 56 9F D2 FF                  call 0x140349e80
0061FF2A  48 8B CD                        mov rcx, rbp
0061FF2D  E8 AE 35 BF FF                  call 0x1402134e0
0061FF32  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0061FF37  48 85 F6                        test rsi, rsi
0061FF3A  74 64                           je 0x14061ffa0
0061FF3C  40 32 FF                        xor dil, dil
0061FF3F  40 38 3D 72 49 8E 00            cmp byte ptr [rip + 0x8e4972], dil
0061FF46  75 0C                           jne 0x14061ff54
0061FF48  F7 05 2E 4A 8E 00 00 08 00 00   test dword ptr [rip + 0x8e4a2e], 0x800
0061FF52  74 13                           je 0x14061ff67
0061FF54  48 8D 0D 25 3F 8E 00            lea rcx, [rip + 0x8e3f25]
0061FF5B  E8 C0 66 BF FF                  call 0x140216620
0061FF60  40 8A F8                        mov dil, al
0061FF63  84 C0                           test al, al
0061FF65  74 39                           je 0x14061ffa0
0061FF67  48 83 C6 30                     add rsi, 0x30
0061FF6B  48 8B 1E                        mov rbx, qword ptr [rsi]
0061FF6E  EB 1A                           jmp 0x14061ff8a
0061FF70  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061FF74  48 85 C0                        test rax, rax
0061FF77  74 0E                           je 0x14061ff87
0061FF79  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061FF7D  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0061FF82  E8 49 AB 09 00                  call 0x1406baad0
0061FF87  48 8B 1B                        mov rbx, qword ptr [rbx]
0061FF8A  48 3B DE                        cmp rbx, rsi
0061FF8D  75 E1                           jne 0x14061ff70
0061FF8F  40 84 FF                        test dil, dil
0061FF92  74 0C                           je 0x14061ffa0
0061FF94  48 8D 0D E5 3E 8E 00            lea rcx, [rip + 0x8e3ee5]
0061FF9B  E8 E0 9E D2 FF                  call 0x140349e80
0061FFA0  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0061FFA5  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0061FFAA  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0061FFAF  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0061FFB4  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0061FFB9  48 83 C4 40                     add rsp, 0x40
0061FFBD  41 5E                           pop r14
0061FFBF  C3                              ret
0061FFC0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExEnterCriticalRegionAndAcquireResourceSharedWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    result = DifGetAPIThunkContextById(405, a2, a3, a4);
    if (result == 0) goto loc_0061FF2A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0061FEB3;
    v_stack_m28 = v_stack_p0;
    goto loc_0061FEC1;
loc_0061FEB3:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9325032)) != 0) goto loc_0061FEDE;
    if (((*(unsigned int *)(v_rip + 9325220)) & (0x800ULL)) == 0) goto loc_0061FEF1;
loc_0061FEDE:
    result = ExAcquireRundownProtection(v_rip + 9322395, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061FF2A;
loc_0061FEF1:
    goto loc_0061FF14;
loc_0061FEFA:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061FF14:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0061FEFA;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9322331;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExEnterCriticalRegionAndAcquireResourceShared(a1, a2, a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_0061FFA0;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9324914)) != 0) goto loc_0061FF54;
    if (((*(unsigned int *)(v_rip + 9325102)) & (0x800ULL)) == 0) goto loc_0061FF67;
loc_0061FF54:
    result = ExAcquireRundownProtection(v_rip + 9322277, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061FFA0;
loc_0061FF67:
    v_rsi = (result) + (48);
    goto loc_0061FF8A;
loc_0061FF70:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061FF8A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0061FF70;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9322213;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifExEnterCriticalRegionAndAcquireResourceSharedWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x18) = 0;
    result = DifGetAPIThunkContextById(405, a2, a3, a4);
    if (result == 0) goto loc_0061FF2A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0061FEB3;
    v_stack_m28 = v_stack_p0;
    goto loc_0061FEC1;
loc_0061FEB3:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E49E8)) != 0) goto loc_0061FEDE;
    if (((*(uint32_t *)(v_rip + 0x8E4AA4)) & (0x800ULL)) == 0) goto loc_0061FEF1;
loc_0061FEDE:
    result = ExAcquireRundownProtection(v_rip + 9322395, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061FF2A;
loc_0061FEF1:
    goto loc_0061FF14;
loc_0061FEFA:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0061FF14:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0061FEFA;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9322331;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExEnterCriticalRegionAndAcquireResourceShared(Arg1, a2, a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_0061FFA0;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E4972)) != 0) goto loc_0061FF54;
    if (((*(uint32_t *)(v_rip + 0x8E4A2E)) & (0x800ULL)) == 0) goto loc_0061FF67;
loc_0061FF54:
    result = ExAcquireRundownProtection(v_rip + 9322277, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061FFA0;
loc_0061FF67:
    local_rsi = (result) + (48);
    goto loc_0061FF8A;
loc_0061FF70:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0061FF8A:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0061FF70;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9322213;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0061FE60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0061FE60[BB_0061FE60]
  bb_0061FEA0[BB_0061FEA0]
  bb_0061FEA7[BB_0061FEA7]
  bb_0061FEB3[BB_0061FEB3]
  bb_0061FEB7[BB_0061FEB7]
  bb_0061FEC1[BB_0061FEC1]
  bb_0061FED2[BB_0061FED2]
  bb_0061FEDE[BB_0061FEDE]
  bb_0061FEF1[BB_0061FEF1]
  bb_0061FEFA[BB_0061FEFA]
  bb_0061FF03[BB_0061FF03]
  bb_0061FF11[BB_0061FF11]
  bb_0061FF14[BB_0061FF14]
  bb_0061FF19[BB_0061FF19]
  bb_0061FF1E[BB_0061FF1E]
  bb_0061FF2A[BB_0061FF2A]
  bb_0061FF3C[BB_0061FF3C]
  bb_0061FF48[BB_0061FF48]
  bb_0061FF54[BB_0061FF54]
  bb_0061FF67[BB_0061FF67]
  bb_0061FF70[BB_0061FF70]
  bb_0061FF79[BB_0061FF79]
  bb_0061FF87[BB_0061FF87]
  bb_0061FF8A[BB_0061FF8A]
  bb_0061FF8F[BB_0061FF8F]
  bb_0061FF94[BB_0061FF94]
  bb_0061FFA0[BB_0061FFA0]
  bb_0061FFC0[BB_0061FFC0]
  bb_0061FE60 -->|branch| bb_0061FF2A
  bb_0061FE60 -->|fallthrough| bb_0061FEA0
  bb_0061FEA0 -->|branch| bb_0061FEB3
  bb_0061FEA0 -->|fallthrough| bb_0061FEA7
  bb_0061FEA7 -->|branch| bb_0061FEC1
  bb_0061FEB3 -->|branch| bb_0061FEC1
  bb_0061FEB3 -->|fallthrough| bb_0061FEB7
  bb_0061FEB7 -->|flow| bb_0061FEC1
  bb_0061FEC1 -->|branch| bb_0061FEDE
  bb_0061FEC1 -->|fallthrough| bb_0061FED2
  bb_0061FED2 -->|branch| bb_0061FEF1
  bb_0061FED2 -->|fallthrough| bb_0061FEDE
  bb_0061FEDE -->|branch| bb_0061FF2A
  bb_0061FEDE -->|fallthrough| bb_0061FEF1
  bb_0061FEF1 -->|branch| bb_0061FF14
  bb_0061FEFA -->|branch| bb_0061FF11
  bb_0061FEFA -->|fallthrough| bb_0061FF03
  bb_0061FF03 -->|flow| bb_0061FF11
  bb_0061FF11 -->|flow| bb_0061FF14
  bb_0061FF14 -->|branch| bb_0061FEFA
  bb_0061FF14 -->|fallthrough| bb_0061FF19
  bb_0061FF19 -->|branch| bb_0061FF2A
  bb_0061FF19 -->|fallthrough| bb_0061FF1E
  bb_0061FF1E -->|flow| bb_0061FF2A
  bb_0061FF2A -->|branch| bb_0061FFA0
  bb_0061FF2A -->|fallthrough| bb_0061FF3C
  bb_0061FF3C -->|branch| bb_0061FF54
  bb_0061FF3C -->|fallthrough| bb_0061FF48
  bb_0061FF48 -->|branch| bb_0061FF67
  bb_0061FF48 -->|fallthrough| bb_0061FF54
  bb_0061FF54 -->|branch| bb_0061FFA0
  bb_0061FF54 -->|fallthrough| bb_0061FF67
  bb_0061FF67 -->|branch| bb_0061FF8A
  bb_0061FF70 -->|branch| bb_0061FF87
  bb_0061FF70 -->|fallthrough| bb_0061FF79
  bb_0061FF79 -->|flow| bb_0061FF87
  bb_0061FF87 -->|flow| bb_0061FF8A
  bb_0061FF8A -->|branch| bb_0061FF70
  bb_0061FF8A -->|fallthrough| bb_0061FF8F
  bb_0061FF8F -->|branch| bb_0061FFA0
  bb_0061FF8F -->|fallthrough| bb_0061FF94
  bb_0061FF94 -->|flow| bb_0061FFA0
```
