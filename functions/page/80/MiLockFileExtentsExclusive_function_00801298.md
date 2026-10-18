# MiLockFileExtentsExclusive

- RVA: `0x00801298`–`0x008012F5` (길이 `93` bytes)
- VA: `0x0000000140801298`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `23`개 명령, `93/93` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x008012BB` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008012E0` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [MiInsertCopyExtents](../../text/68/MiInsertCopyExtents_function_00681440.md) at `0x00681469`
- [MiMergeCopyExtents](../../text/68/MiMergeCopyExtents_function_00681844.md) at `0x006819BC`
- [MiDeleteFileExtentList](MiDeleteFileExtentList_function_00800F6C.md) at `0x00800F7E`

### Static image references
- `0x008012A7` → RVA `0x00E2D898` (`.data`; read)
- `0x008012C0` → RVA `0x00E2D898` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x008012BB` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008012E0` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00801298  40 53                           push rbx
0080129A  48 83 EC 20                     sub rsp, 0x20
0080129E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008012A7  48 8D 0D EA C5 62 00            lea rcx, [rip + 0x62c5ea]
008012AE  45 33 C0                        xor r8d, r8d
008012B1  33 D2                           xor edx, edx
008012B3  66 FF 88 E6 01 00 00            dec word ptr [rax + 0x1e6]
008012BA  90                              nop
008012BB  E8 70 EF A0 FF                  call 0x140210230
008012C0  F0 48 0F BA 2D CE C5 62 00 00   lock bts qword ptr [rip + 0x62c5ce], 0
008012CA  48 8B D8                        mov rbx, rax
008012CD  73 16                           jae 0x1408012e5
008012CF  4C 8D 05 C2 C5 62 00            lea r8, [rip + 0x62c5c2]
008012D6  48 8B D0                        mov rdx, rax
008012D9  48 8D 0D B8 C5 62 00            lea rcx, [rip + 0x62c5b8]
008012E0  E8 AB E9 A0 FF                  call 0x14020fc90
008012E5  48 85 DB                        test rbx, rbx
008012E8  74 04                           je 0x1408012ee
008012EA  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
008012EE  48 83 C4 20                     add rsp, 0x20
008012F2  5B                              pop rbx
008012F3  C3                              ret
008012F4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLockFileExtentsExclusive(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 6473194, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 6473154;
        a2 = result;
        a1 = v_rip + 6473144;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiLockFileExtentsExclusive(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 6473194, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 6473154;
        Arg2 = result;
        Arg1 = v_rip + 6473144;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00801298&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00801298[BB_00801298]
  bb_008012CF[BB_008012CF]
  bb_008012E5[BB_008012E5]
  bb_008012EA[BB_008012EA]
  bb_008012EE[BB_008012EE]
  bb_008012F4[BB_008012F4]
  bb_00801298 -->|branch| bb_008012E5
  bb_00801298 -->|fallthrough| bb_008012CF
  bb_008012CF -->|flow| bb_008012E5
  bb_008012E5 -->|branch| bb_008012EE
  bb_008012E5 -->|fallthrough| bb_008012EA
  bb_008012EA -->|flow| bb_008012EE
```
