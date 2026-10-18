# PpmEventEnterPlatformIdleState

- RVA: `0x005DA864`–`0x005DA8D4` (길이 `112` bytes)
- VA: `0x00000001405DA864`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AD25C`
- 디코드: `23`개 명령, `112/112` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x005DA8BC` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x005DA8C9` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PpmEnterCoordinatedIdle](../2D/PpmEnterCoordinatedIdle_function_002D19B0.md) at `0x002D19EA`

### Static image references
- `0x005DA86C` → RVA `0x00E0A740` (`.data`; read)
- `0x005DA87B` → RVA `0x00FC6B08` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005DA864  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
005DA868  48 83 EC 58                     sub rsp, 0x58
005DA86C  48 8B 05 CD FE 82 00            mov rax, qword ptr [rip + 0x82fecd]
005DA873  48 33 C4                        xor rax, rsp
005DA876  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
005DA87B  F7 05 83 C2 9E 00 00 80 00 00   test dword ptr [rip + 0x9ec283], 0x8000
005DA885  74 3A                           je 0x1405da8c1
005DA887  83 64 24 3C 00                  and dword ptr [rsp + 0x3c], 0
005DA88C  48 8D 44 24 60                  lea rax, [rsp + 0x60]
005DA891  41 B9 3B 12 00 00               mov r9d, 0x123b
005DA897  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
005DA89C  BA 01 00 00 00                  mov edx, 1
005DA8A1  C7 44 24 38 04 00 00 00         mov dword ptr [rsp + 0x38], 4
005DA8A9  41 B8 00 80 00 40               mov r8d, 0x40008000
005DA8AF  C7 44 24 20 02 06 00 00         mov dword ptr [rsp + 0x20], 0x602
005DA8B7  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
005DA8BC  E8 8F AA C5 FF                  call 0x140235350
005DA8C1  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
005DA8C6  48 33 CC                        xor rcx, rsp
005DA8C9  E8 72 1D 0D 00                  call 0x1406ac640
005DA8CE  48 83 C4 58                     add rsp, 0x58
005DA8D2  C3                              ret
005DA8D3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmEventEnterPlatformIdleState(int a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m38;
    unsigned int v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (88);
    result = (*(unsigned __int64 *)(v_rip + 8584909)) ^ (v_rsp);
    v_stack_m18 = result;
    if (((*(unsigned int *)(v_rip + 10404483)) & (0x8000ULL)) != 0) {
        result = v_stack_p8;
        a4 = 0x123BULL;
        v_stack_m28 = result;
        a2 = 1;
        v_stack_m20 = 4;
        a3 = 0x40008000ULL;
        v_stack_m38 = 0x602ULL;
        a1 = v_stack_m28;
        result = EtwTraceKernelEvent(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmEventEnterPlatformIdleState(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m38;
    uint32_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (88);
    result = (*(uint64_t *)(v_rip + 0x82FECD)) ^ (local_rsp);
    v_stack_m18 = result;
    if (((*(uint32_t *)(v_rip + 0x9EC283)) & (0x8000ULL)) != 0) {
        result = v_stack_p8;
        a4 = 0x123BULL;
        v_stack_m28 = result;
        a2 = 1;
        v_stack_m20 = 4;
        a3 = 0x40008000ULL;
        v_stack_m38 = 0x602ULL;
        Arg1 = v_stack_m28;
        result = EtwTraceKernelEvent(Arg1, a2, a3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005DA864&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005DA864[BB_005DA864]
  bb_005DA887[BB_005DA887]
  bb_005DA8C1[BB_005DA8C1]
  bb_005DA8D3[BB_005DA8D3]
  bb_005DA864 -->|branch| bb_005DA8C1
  bb_005DA864 -->|fallthrough| bb_005DA887
  bb_005DA887 -->|flow| bb_005DA8C1
```
