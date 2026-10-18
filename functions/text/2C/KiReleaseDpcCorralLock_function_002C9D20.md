# KiReleaseDpcCorralLock

- RVA: `0x002C9D20`–`0x002C9D5A` (길이 `58` bytes)
- VA: `0x00000001402C9D20`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x002C9D3E` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x002C9D4A` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x002C9D4F` → [KeLeaveGuardedRegion](../2E/KeLeaveGuardedRegion_function_002E2C40.md) (function, `0x002E2C40`)

### Direct callers
- [KeGenericCallDpcEx](KeGenericCallDpcEx_function_002C99F4.md) at `0x002C9AC8`
- [KiGenericCallDpcInitiatorWorker](KiGenericCallDpcInitiatorWorker_function_002C9B60.md) at `0x002C9BB6`

### Static image references
- `0x002C9D28` → RVA `0x00F10F10` (`.data`; read/write)
- `0x002C9D37` → RVA `0x00F10F10` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002C9D20  48 83 EC 28                     sub rsp, 0x28
002C9D24  48 83 C8 FF                     or rax, 0xffffffffffffffff
002C9D28  F0 48 0F C1 05 DF 71 C4 00      lock xadd qword ptr [rip + 0xc471df], rax
002C9D31  24 06                           and al, 6
002C9D33  3C 02                           cmp al, 2
002C9D35  75 0C                           jne 0x1402c9d43
002C9D37  48 8D 0D D2 71 C4 00            lea rcx, [rip + 0xc471d2]
002C9D3E  E8 8D C0 F9 FF                  call 0x140265dd0
002C9D43  48 8D 0D C6 71 C4 00            lea rcx, [rip + 0xc471c6]
002C9D4A  E8 B1 78 01 00                  call 0x1402e1600
002C9D4F  E8 EC 8E 01 00                  call 0x1402e2c40
002C9D54  48 83 C4 28                     add rsp, 0x28
002C9D58  C3                              ret
002C9D59  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiReleaseDpcCorralLock(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = v_rip + 12874194;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_rip + 12874182, a2, a3, a4);
    result = KeLeaveGuardedRegion(v_rip + 12874182, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void KiReleaseDpcCorralLock(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) {
        a1 = v_rip + 12874194;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_rip + 12874182, a2, a3, a4);
    result = KeLeaveGuardedRegion(v_rip + 12874182, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C9D20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002C9D20[BB_002C9D20]
  bb_002C9D37[BB_002C9D37]
  bb_002C9D43[BB_002C9D43]
  bb_002C9D59[BB_002C9D59]
  bb_002C9D20 -->|branch| bb_002C9D43
  bb_002C9D20 -->|fallthrough| bb_002C9D37
  bb_002C9D37 -->|flow| bb_002C9D43
```
