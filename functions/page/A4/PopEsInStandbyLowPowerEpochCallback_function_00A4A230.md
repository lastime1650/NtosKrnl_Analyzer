# PopEsInStandbyLowPowerEpochCallback

- RVA: `0x00A4A230`–`0x00A4A259` (길이 `41` bytes)
- VA: `0x0000000140A4A230`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A4A23B` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x00A4A240` → [PopEsInStandbyEvaluate](PopEsInStandbyEvaluate_function_00A4A260.md) (function, `0x00A4A260`)
- `0x00A4A24C` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00A4A234` → RVA `0x00F08440` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A4A23B` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x00A4A24C` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A4A230  48 83 EC 28                     sub rsp, 0x28
00A4A234  48 8D 0D 05 E2 4B 00            lea rcx, [rip + 0x4be205]
00A4A23B  E8 04 69 9E FF                  call 0x140430b44
00A4A240  E8 1B 00 00 00                  call 0x140a4a260
00A4A245  48 8D 0D F4 E1 4B 00            lea rcx, [rip + 0x4be1f4]
00A4A24C  E8 6B 59 89 FF                  call 0x1402dfbbc
00A4A251  33 C0                           xor eax, eax
00A4A253  48 83 C4 28                     add rsp, 0x28
00A4A257  C3                              ret
00A4A258  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopEsInStandbyLowPowerEpochCallback(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PopAcquireRwLockExclusive(v_rip + 4973061, a2, a3, a4);
    result = PopEsInStandbyEvaluate(v_rip + 4973061, a2, a3, a4);
    result = PopReleaseRwLock(v_rip + 4973044, a2, a3, a4);
    result = 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PopEsInStandbyLowPowerEpochCallback(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PopAcquireRwLockExclusive(v_rip + 4973061, a2, a3, a4);
    result = PopEsInStandbyEvaluate(v_rip + 4973061, a2, a3, a4);
    result = PopReleaseRwLock(v_rip + 4973044, a2, a3, a4);
    result = 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A4A230&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A4A230[BB_00A4A230]
  bb_00A4A258[BB_00A4A258]
```
