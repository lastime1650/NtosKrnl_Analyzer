# PopDiagTraceAbnormalReset

- RVA: `0x005D5D84`–`0x005D5E1C` (길이 `152` bytes)
- VA: `0x00000001405D5D84`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00073440`
- 디코드: `32`개 명령, `152/152` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x005D5DB2` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x005D5E04` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x005D5E11` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PoInitSystem](../../init/C7/PoInitSystem_function_00C72358.md) at `0x00C72FD9`

### Static image references
- `0x005D5D8C` → RVA `0x00E0A740` (`.data`; read)
- `0x005D5D9B` → RVA `0x00E67858` (`.data`; read)
- `0x005D5DA4` → RVA `0x00F0B408` (`.data`; read)
- `0x005D5DAB` → RVA `0x00020FB8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D5D84  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
005D5D88  48 83 EC 68                     sub rsp, 0x68
005D5D8C  48 8B 05 AD 49 83 00            mov rax, qword ptr [rip + 0x8349ad]
005D5D93  48 33 C4                        xor rax, rsp
005D5D96  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
005D5D9B  80 3D B6 1A 89 00 00            cmp byte ptr [rip + 0x891ab6], 0
005D5DA2  74 65                           je 0x1405d5e09
005D5DA4  48 8B 0D 5D 56 93 00            mov rcx, qword ptr [rip + 0x93565d]
005D5DAB  48 8D 15 06 B2 A4 FF            lea rdx, [rip - 0x5b4dfa]
005D5DB2  E8 99 C6 DB FF                  call 0x140392450
005D5DB7  84 C0                           test al, al
005D5DB9  74 4E                           je 0x1405d5e09
005D5DBB  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
005D5DC0  48 8D 44 24 70                  lea rax, [rsp + 0x70]
005D5DC5  48 8B 0D 3C 56 93 00            mov rcx, qword ptr [rip + 0x93563c]
005D5DCC  48 8D 15 E5 B1 A4 FF            lea rdx, [rip - 0x5b4e1b]
005D5DD3  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
005D5DD8  45 33 C9                        xor r9d, r9d
005D5DDB  48 8D 44 24 40                  lea rax, [rsp + 0x40]
005D5DE0  C7 44 24 48 04 00 00 00         mov dword ptr [rsp + 0x48], 4
005D5DE8  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005D5DED  45 33 C0                        xor r8d, r8d
005D5DF0  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
005D5DF8  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005D5DFE  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005D5E04  E8 C7 92 C8 FF                  call 0x14025f0d0
005D5E09  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
005D5E0E  48 33 CC                        xor rcx, rsp
005D5E11  E8 2A 68 0D 00                  call 0x1406ac640
005D5E16  48 83 C4 68                     add rsp, 0x68
005D5E1A  C3                              ret
005D5E1B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceAbnormalReset(int a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (104);
    result = (*(unsigned __int64 *)(v_rip + 8604077)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 8985270)) == 0) goto loc_005D5E09;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 9655901), v_rip - 5983738, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a1 = *(unsigned __int64 *)(v_rip + 9655868);
        a2 = v_rip - 5983771;
        v_stack_m28 = result;
        a4 = 0;
        result = v_stack_m28;
        v_stack_m20 = 4;
        v_stack_m30 = result;
        a3 = 0;
        v_stack_m38 = 1;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (104);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceAbnormalReset(int32_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (104);
    result = (*(uint64_t *)(v_rip + 0x8349AD)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0x891AB6)) == 0) goto loc_005D5E09;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x93565D), v_rip - 5983738, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg1 = *(uint64_t *)(v_rip + 0x93563C);
        Arg2 = v_rip - 5983771;
        v_stack_m28 = result;
        Arg4 = 0;
        result = v_stack_m28;
        v_stack_m20 = 4;
        v_stack_m30 = result;
        Arg3 = 0;
        v_stack_m38 = 1;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (104);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D5D84&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D5D84[BB_005D5D84]
  bb_005D5DA4[BB_005D5DA4]
  bb_005D5DBB[BB_005D5DBB]
  bb_005D5E09[BB_005D5E09]
  bb_005D5E1B[BB_005D5E1B]
  bb_005D5D84 -->|branch| bb_005D5E09
  bb_005D5D84 -->|fallthrough| bb_005D5DA4
  bb_005D5DA4 -->|branch| bb_005D5E09
  bb_005D5DA4 -->|fallthrough| bb_005D5DBB
  bb_005D5DBB -->|flow| bb_005D5E09
```
