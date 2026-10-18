# DifExEnterCriticalRegionAndAcquireSharedWaitForExclusiveWrapper

- RVA: `0x0061FFD0`–`0x00620131` (길이 `353` bytes)
- VA: `0x000000014061FFD0`
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
- `0x0061FFFF` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00620027` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00620055` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062007C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00620095` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062009D` → [ExEnterCriticalRegionAndAcquireSharedWaitForExclusive](../3D/ExEnterCriticalRegionAndAcquireSharedWaitForExclusive_function_003D43B0.md) (function, `0x003D43B0`)
- `0x006200CB` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006200F2` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062010B` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00620039` → RVA `0x00F048B8` (`.data`; read)
- `0x00620042` → RVA `0x00F04980` (`.data`; read)
- `0x0062004E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0061FFD0  4C 8B DC                        mov r11, rsp
0061FFD3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0061FFD7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0061FFDB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0061FFDF  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
0061FFE3  41 56                           push r14
0061FFE5  48 83 EC 40                     sub rsp, 0x40
0061FFE9  33 C0                           xor eax, eax
0061FFEB  0F 57 C0                        xorps xmm0, xmm0
0061FFEE  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0061FFF3  48 8B E9                        mov rbp, rcx
0061FFF6  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0061FFFA  B9 94 01 00 00                  mov ecx, 0x194
0061FFFF  E8 30 5A E7 FF                  call 0x140495a34
00620004  48 8B F0                        mov rsi, rax
00620007  48 85 C0                        test rax, rax
0062000A  0F 84 8A 00 00 00               je 0x14062009a
00620010  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00620013  A8 18                           test al, 0x18
00620015  74 0C                           je 0x140620023
00620017  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0062001C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00620021  EB 0E                           jmp 0x140620031
00620023  A8 04                           test al, 4
00620025  74 0A                           je 0x140620031
00620027  E8 DC 3B EB FF                  call 0x1404d3c08
0062002C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00620031  40 32 FF                        xor dil, dil
00620034  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00620039  40 38 3D 78 48 8E 00            cmp byte ptr [rip + 0x8e4878], dil
00620040  75 0C                           jne 0x14062004e
00620042  F7 05 34 49 8E 00 00 08 00 00   test dword ptr [rip + 0x8e4934], 0x800
0062004C  74 13                           je 0x140620061
0062004E  48 8D 0D 2B 3E 8E 00            lea rcx, [rip + 0x8e3e2b]
00620055  E8 C6 65 BF FF                  call 0x140216620
0062005A  40 8A F8                        mov dil, al
0062005D  84 C0                           test al, al
0062005F  74 39                           je 0x14062009a
00620061  4C 8D 76 20                     lea r14, [rsi + 0x20]
00620065  49 8B 1E                        mov rbx, qword ptr [r14]
00620068  EB 1A                           jmp 0x140620084
0062006A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062006E  48 85 C0                        test rax, rax
00620071  74 0E                           je 0x140620081
00620073  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00620077  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062007C  E8 4F AA 09 00                  call 0x1406baad0
00620081  48 8B 1B                        mov rbx, qword ptr [rbx]
00620084  49 3B DE                        cmp rbx, r14
00620087  75 E1                           jne 0x14062006a
00620089  40 84 FF                        test dil, dil
0062008C  74 0C                           je 0x14062009a
0062008E  48 8D 0D EB 3D 8E 00            lea rcx, [rip + 0x8e3deb]
00620095  E8 E6 9D D2 FF                  call 0x140349e80
0062009A  48 8B CD                        mov rcx, rbp
0062009D  E8 0E 43 DB FF                  call 0x1403d43b0
006200A2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
006200A7  48 85 F6                        test rsi, rsi
006200AA  74 64                           je 0x140620110
006200AC  40 32 FF                        xor dil, dil
006200AF  40 38 3D 02 48 8E 00            cmp byte ptr [rip + 0x8e4802], dil
006200B6  75 0C                           jne 0x1406200c4
006200B8  F7 05 BE 48 8E 00 00 08 00 00   test dword ptr [rip + 0x8e48be], 0x800
006200C2  74 13                           je 0x1406200d7
006200C4  48 8D 0D B5 3D 8E 00            lea rcx, [rip + 0x8e3db5]
006200CB  E8 50 65 BF FF                  call 0x140216620
006200D0  40 8A F8                        mov dil, al
006200D3  84 C0                           test al, al
006200D5  74 39                           je 0x140620110
006200D7  48 83 C6 30                     add rsi, 0x30
006200DB  48 8B 1E                        mov rbx, qword ptr [rsi]
006200DE  EB 1A                           jmp 0x1406200fa
006200E0  48 8D 43 F0                     lea rax, [rbx - 0x10]
006200E4  48 85 C0                        test rax, rax
006200E7  74 0E                           je 0x1406200f7
006200E9  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006200ED  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006200F2  E8 D9 A9 09 00                  call 0x1406baad0
006200F7  48 8B 1B                        mov rbx, qword ptr [rbx]
006200FA  48 3B DE                        cmp rbx, rsi
006200FD  75 E1                           jne 0x1406200e0
006200FF  40 84 FF                        test dil, dil
00620102  74 0C                           je 0x140620110
00620104  48 8D 0D 75 3D 8E 00            lea rcx, [rip + 0x8e3d75]
0062010B  E8 70 9D D2 FF                  call 0x140349e80
00620110  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00620115  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0062011A  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0062011F  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00620124  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00620129  48 83 C4 40                     add rsp, 0x40
0062012D  41 5E                           pop r14
0062012F  C3                              ret
00620130  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExEnterCriticalRegionAndAcquireSharedWaitForExclusiveWrapper(__int64 a1)
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
    result = DifGetAPIThunkContextById(404, a2, a3, a4);
    if (result == 0) goto loc_0062009A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00620023;
    v_stack_m28 = v_stack_p0;
    goto loc_00620031;
loc_00620023:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9324664)) != 0) goto loc_0062004E;
    if (((*(unsigned int *)(v_rip + 9324852)) & (0x800ULL)) == 0) goto loc_00620061;
loc_0062004E:
    result = ExAcquireRundownProtection(v_rip + 9322027, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062009A;
loc_00620061:
    goto loc_00620084;
loc_0062006A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00620084:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062006A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9321963;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExEnterCriticalRegionAndAcquireSharedWaitForExclusive(a1, a2, a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_00620110;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9324546)) != 0) goto loc_006200C4;
    if (((*(unsigned int *)(v_rip + 9324734)) & (0x800ULL)) == 0) goto loc_006200D7;
loc_006200C4:
    result = ExAcquireRundownProtection(v_rip + 9321909, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00620110;
loc_006200D7:
    v_rsi = (result) + (48);
    goto loc_006200FA;
loc_006200E0:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006200FA:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006200E0;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9321845;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifExEnterCriticalRegionAndAcquireSharedWaitForExclusiveWrapper(int64_t Arg1)
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
    result = DifGetAPIThunkContextById(404, a2, a3, a4);
    if (result == 0) goto loc_0062009A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00620023;
    v_stack_m28 = v_stack_p0;
    goto loc_00620031;
loc_00620023:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E4878)) != 0) goto loc_0062004E;
    if (((*(uint32_t *)(v_rip + 0x8E4934)) & (0x800ULL)) == 0) goto loc_00620061;
loc_0062004E:
    result = ExAcquireRundownProtection(v_rip + 9322027, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062009A;
loc_00620061:
    goto loc_00620084;
loc_0062006A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00620084:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062006A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9321963;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExEnterCriticalRegionAndAcquireSharedWaitForExclusive(Arg1, a2, a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_00620110;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E4802)) != 0) goto loc_006200C4;
    if (((*(uint32_t *)(v_rip + 0x8E48BE)) & (0x800ULL)) == 0) goto loc_006200D7;
loc_006200C4:
    result = ExAcquireRundownProtection(v_rip + 9321909, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00620110;
loc_006200D7:
    local_rsi = (result) + (48);
    goto loc_006200FA;
loc_006200E0:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006200FA:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006200E0;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9321845;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0061FFD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0061FFD0[BB_0061FFD0]
  bb_00620010[BB_00620010]
  bb_00620017[BB_00620017]
  bb_00620023[BB_00620023]
  bb_00620027[BB_00620027]
  bb_00620031[BB_00620031]
  bb_00620042[BB_00620042]
  bb_0062004E[BB_0062004E]
  bb_00620061[BB_00620061]
  bb_0062006A[BB_0062006A]
  bb_00620073[BB_00620073]
  bb_00620081[BB_00620081]
  bb_00620084[BB_00620084]
  bb_00620089[BB_00620089]
  bb_0062008E[BB_0062008E]
  bb_0062009A[BB_0062009A]
  bb_006200AC[BB_006200AC]
  bb_006200B8[BB_006200B8]
  bb_006200C4[BB_006200C4]
  bb_006200D7[BB_006200D7]
  bb_006200E0[BB_006200E0]
  bb_006200E9[BB_006200E9]
  bb_006200F7[BB_006200F7]
  bb_006200FA[BB_006200FA]
  bb_006200FF[BB_006200FF]
  bb_00620104[BB_00620104]
  bb_00620110[BB_00620110]
  bb_00620130[BB_00620130]
  bb_0061FFD0 -->|branch| bb_0062009A
  bb_0061FFD0 -->|fallthrough| bb_00620010
  bb_00620010 -->|branch| bb_00620023
  bb_00620010 -->|fallthrough| bb_00620017
  bb_00620017 -->|branch| bb_00620031
  bb_00620023 -->|branch| bb_00620031
  bb_00620023 -->|fallthrough| bb_00620027
  bb_00620027 -->|flow| bb_00620031
  bb_00620031 -->|branch| bb_0062004E
  bb_00620031 -->|fallthrough| bb_00620042
  bb_00620042 -->|branch| bb_00620061
  bb_00620042 -->|fallthrough| bb_0062004E
  bb_0062004E -->|branch| bb_0062009A
  bb_0062004E -->|fallthrough| bb_00620061
  bb_00620061 -->|branch| bb_00620084
  bb_0062006A -->|branch| bb_00620081
  bb_0062006A -->|fallthrough| bb_00620073
  bb_00620073 -->|flow| bb_00620081
  bb_00620081 -->|flow| bb_00620084
  bb_00620084 -->|branch| bb_0062006A
  bb_00620084 -->|fallthrough| bb_00620089
  bb_00620089 -->|branch| bb_0062009A
  bb_00620089 -->|fallthrough| bb_0062008E
  bb_0062008E -->|flow| bb_0062009A
  bb_0062009A -->|branch| bb_00620110
  bb_0062009A -->|fallthrough| bb_006200AC
  bb_006200AC -->|branch| bb_006200C4
  bb_006200AC -->|fallthrough| bb_006200B8
  bb_006200B8 -->|branch| bb_006200D7
  bb_006200B8 -->|fallthrough| bb_006200C4
  bb_006200C4 -->|branch| bb_00620110
  bb_006200C4 -->|fallthrough| bb_006200D7
  bb_006200D7 -->|branch| bb_006200FA
  bb_006200E0 -->|branch| bb_006200F7
  bb_006200E0 -->|fallthrough| bb_006200E9
  bb_006200E9 -->|flow| bb_006200F7
  bb_006200F7 -->|flow| bb_006200FA
  bb_006200FA -->|branch| bb_006200E0
  bb_006200FA -->|fallthrough| bb_006200FF
  bb_006200FF -->|branch| bb_00620110
  bb_006200FF -->|fallthrough| bb_00620104
  bb_00620104 -->|flow| bb_00620110
```
