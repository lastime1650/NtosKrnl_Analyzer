# PopDeviceIdleCompletion

- RVA: `0x005D1580`–`0x005D15D0` (길이 `80` bytes)
- VA: `0x00000001405D1580`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `21`개 명령, `80/80` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x005D158D` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x005D15AE` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x005D15C4` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005D1586` → RVA `0x00F0CBA0` (`.data`; read)
- `0x005D1592` → RVA `0x00E676A0` (`.data`; read/write)
- `0x005D159D` → RVA `0x00E67698` (`.data`; read)
- `0x005D15B3` → RVA `0x00E67698` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D1580  40 53                           push rbx
005D1582  48 83 EC 20                     sub rsp, 0x20
005D1586  48 8D 0D 13 B6 93 00            lea rcx, [rip + 0x93b613]
005D158D  E8 DE 6E C3 FF                  call 0x140208470
005D1592  83 05 07 61 89 00 FF            add dword ptr [rip + 0x896107], -1
005D1599  8A D8                           mov bl, al
005D159B  75 1E                           jne 0x1405d15bb
005D159D  48 8B 0D F4 60 89 00            mov rcx, qword ptr [rip + 0x8960f4]
005D15A4  48 85 C9                        test rcx, rcx
005D15A7  74 12                           je 0x1405d15bb
005D15A9  45 33 C0                        xor r8d, r8d
005D15AC  33 D2                           xor edx, edx
005D15AE  E8 5D DD D6 FF                  call 0x14033f310
005D15B3  48 83 25 DD 60 89 00 00         and qword ptr [rip + 0x8960dd], 0
005D15BB  8A D3                           mov dl, bl
005D15BD  48 8D 0D DC B5 93 00            lea rcx, [rip + 0x93b5dc]
005D15C4  E8 D7 15 DC FF                  call 0x140392ba0
005D15C9  48 83 C4 20                     add rsp, 0x20
005D15CD  5B                              pop rbx
005D15CE  C3                              ret
005D15CF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDeviceIdleCompletion(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 9680403, a2, a3, a4);
    if (condition_is_not_equal) goto loc_005D15BB;
    if (*(unsigned __int64 *)(v_rip + 9003252) != 0) {
        a3 = 0;
        a2 = 0;
        result = KeSetEvent(*(unsigned __int64 *)(v_rip + 9003252), a2, a3, a4);
    }
    result = KeReleaseSpinLock(v_rip + 9680348, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDeviceIdleCompletion(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 9680403, Arg2, Arg3, a4);
    if (condition_is_not_equal) goto loc_005D15BB;
    if (*(uint64_t *)(v_rip + 0x8960F4) != 0) {
        Arg3 = 0;
        Arg2 = 0;
        result = KeSetEvent(*(uint64_t *)(v_rip + 0x8960F4), Arg2, Arg3, a4);
    }
    result = KeReleaseSpinLock(v_rip + 9680348, (uint8_t)((uint8_t)(result)), Arg3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D1580&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D1580[BB_005D1580]
  bb_005D159D[BB_005D159D]
  bb_005D15A9[BB_005D15A9]
  bb_005D15BB[BB_005D15BB]
  bb_005D15CF[BB_005D15CF]
  bb_005D1580 -->|branch| bb_005D15BB
  bb_005D1580 -->|fallthrough| bb_005D159D
  bb_005D159D -->|branch| bb_005D15BB
  bb_005D159D -->|fallthrough| bb_005D15A9
  bb_005D15A9 -->|flow| bb_005D15BB
```
